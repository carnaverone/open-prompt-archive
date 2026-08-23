#!/usr/bin/env python3
"""Validate one source-partitioned Open Prompt Archive publication directory.

This validator is intentionally independent from source importers. It verifies
that the material a maintainer is about to publish still satisfies the current
repository schemas, source registry, manifest and byte-level integrity claims.
"""

from __future__ import annotations

import argparse
import hashlib
import json
import sys
from pathlib import Path
from typing import Any

try:
    import yaml
    from jsonschema import Draft202012Validator, FormatChecker
except ImportError as exc:  # pragma: no cover - explicit operator error path
    raise SystemExit(
        "Missing curation dependencies. Install with: "
        "python -m pip install -r scripts/requirements.txt"
    ) from exc


class ValidationFailure(RuntimeError):
    """Raised when a publication invariant is violated."""


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Verify a staged or committed Open Prompt Archive source publication."
    )
    parser.add_argument(
        "source_dir",
        type=Path,
        help="Directory containing manifest.yaml and its declared dataset resources.",
    )
    parser.add_argument(
        "--require-published",
        action="store_true",
        help="Fail unless manifest publication.status is exactly 'published'.",
    )
    return parser.parse_args()


def repo_root() -> Path:
    return Path(__file__).resolve().parents[1]


def load_json(path: Path) -> Any:
    try:
        return json.loads(path.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError) as exc:
        raise ValidationFailure(f"Cannot read valid JSON from {path}: {exc}") from exc


def load_yaml(path: Path) -> Any:
    try:
        return yaml.safe_load(path.read_text(encoding="utf-8"))
    except (OSError, yaml.YAMLError) as exc:
        raise ValidationFailure(f"Cannot read valid YAML from {path}: {exc}") from exc


def sha256_file(path: Path) -> tuple[str, int]:
    digest = hashlib.sha256()
    size = 0
    try:
        with path.open("rb") as handle:
            while True:
                chunk = handle.read(1024 * 1024)
                if not chunk:
                    break
                digest.update(chunk)
                size += len(chunk)
    except OSError as exc:
        raise ValidationFailure(f"Cannot read resource {path}: {exc}") from exc
    return digest.hexdigest(), size


def validator_for(schema: dict[str, Any]) -> Draft202012Validator:
    return Draft202012Validator(schema, format_checker=FormatChecker())


def validate_instance(
    instance: Any,
    validator: Draft202012Validator,
    label: str,
) -> None:
    errors = sorted(validator.iter_errors(instance), key=lambda err: list(err.path))
    if not errors:
        return
    first = errors[0]
    location = ".".join(str(part) for part in first.path) or "<root>"
    raise ValidationFailure(
        f"{label} schema validation failed at {location}: {first.message}"
    )


def approved_source(registry: dict[str, Any], source_id: str) -> dict[str, Any]:
    sources = registry.get("sources")
    if not isinstance(sources, list):
        raise ValidationFailure("sources/sources.yaml does not contain a valid sources list.")

    matches = [item for item in sources if item.get("source_id") == source_id]
    if len(matches) != 1:
        raise ValidationFailure(
            f"Expected exactly one registry entry for {source_id!r}, found {len(matches)}."
        )
    source = matches[0]
    if source.get("status") != "approved":
        raise ValidationFailure(
            f"Source {source_id!r} is currently {source.get('status')!r}, not 'approved'."
        )
    license_data = source.get("license") or {}
    if license_data.get("scope_verified") is not True:
        raise ValidationFailure(
            f"Source {source_id!r} is approved but license.scope_verified is not true."
        )
    return source


def resolve_resource(source_dir: Path, source_id: str, resource: dict[str, Any]) -> Path:
    name = resource["name"]
    if Path(name).name != name or name in {".", ".."}:
        raise ValidationFailure(f"Unsafe resource name in manifest: {name!r}")

    expected_location = f"data/sources/{source_id}/{name}"
    if resource["location"] != expected_location:
        raise ValidationFailure(
            f"Resource {name!r} location must be {expected_location!r}, "
            f"got {resource['location']!r}."
        )
    path = (source_dir / name).resolve()
    try:
        path.relative_to(source_dir.resolve())
    except ValueError as exc:
        raise ValidationFailure(f"Resource escapes source directory: {name!r}") from exc
    return path


def validate_jsonl_resource(
    *,
    path: Path,
    resource: dict[str, Any],
    source_id: str,
    effective_spdx: str,
    prompt_validator: Draft202012Validator,
    seen_ids: set[str],
) -> int:
    count = 0
    try:
        with path.open("r", encoding="utf-8", newline="") as handle:
            for line_number, line in enumerate(handle, start=1):
                if not line.strip():
                    raise ValidationFailure(
                        f"Blank JSONL line in {path} at line {line_number}."
                    )
                try:
                    record = json.loads(line)
                except json.JSONDecodeError as exc:
                    raise ValidationFailure(
                        f"Invalid JSON in {path} at line {line_number}: {exc}"
                    ) from exc

                validate_instance(
                    record,
                    prompt_validator,
                    f"{path.name}:{line_number}",
                )
                if record["source"]["source_id"] != source_id:
                    raise ValidationFailure(
                        f"{path.name}:{line_number} references source_id "
                        f"{record['source']['source_id']!r}, expected {source_id!r}."
                    )
                if record["license"]["spdx"] != effective_spdx:
                    raise ValidationFailure(
                        f"{path.name}:{line_number} license {record['license']['spdx']!r} "
                        f"does not match manifest effective license {effective_spdx!r}."
                    )
                rid = record["id"]
                if rid in seen_ids:
                    raise ValidationFailure(f"Duplicate canonical record id: {rid}")
                seen_ids.add(rid)
                count += 1
    except OSError as exc:
        raise ValidationFailure(f"Cannot read JSONL resource {path}: {exc}") from exc

    if count != resource["record_count"]:
        raise ValidationFailure(
            f"Record count mismatch for {path.name}: manifest={resource['record_count']}, "
            f"actual={count}."
        )
    return count


def main() -> int:
    args = parse_args()
    root = repo_root()
    source_dir = args.source_dir.resolve()
    if not source_dir.is_dir():
        raise ValidationFailure(f"Source directory does not exist: {source_dir}")

    manifest_path = source_dir / "manifest.yaml"
    manifest = load_yaml(manifest_path)
    if not isinstance(manifest, dict):
        raise ValidationFailure("manifest.yaml must contain a YAML mapping.")

    manifest_schema = load_json(root / "schema" / "manifest.schema.json")
    prompt_schema = load_json(root / "schema" / "prompt.schema.json")
    manifest_validator = validator_for(manifest_schema)
    prompt_validator = validator_for(prompt_schema)
    validate_instance(manifest, manifest_validator, "manifest")

    source_id = manifest["source_id"]
    registry = load_yaml(root / "sources" / "sources.yaml")
    if not isinstance(registry, dict):
        raise ValidationFailure("sources/sources.yaml must contain a YAML mapping.")
    source = approved_source(registry, source_id)

    if manifest["source_revision"] != source.get("reviewed_revision"):
        raise ValidationFailure(
            f"Manifest source revision {manifest['source_revision']!r} does not match "
            f"currently reviewed revision {source.get('reviewed_revision')!r}."
        )

    effective_spdx = manifest["effective_license"]["spdx"]
    source_spdx = (source.get("license") or {}).get("spdx")
    if effective_spdx != source_spdx:
        raise ValidationFailure(
            f"Manifest license {effective_spdx!r} does not match registry license "
            f"{source_spdx!r}."
        )

    if args.require_published and manifest["publication"]["status"] != "published":
        raise ValidationFailure(
            "--require-published was supplied but manifest status is not 'published'."
        )

    resources = manifest["resources"]
    declared_names: set[str] = set()
    seen_ids: set[str] = set()
    total_records = 0

    for resource in resources:
        name = resource["name"]
        if name in declared_names:
            raise ValidationFailure(f"Manifest declares resource more than once: {name}")
        declared_names.add(name)

        path = resolve_resource(source_dir, source_id, resource)
        if not path.is_file():
            raise ValidationFailure(f"Declared resource is missing: {path}")

        actual_sha256, actual_bytes = sha256_file(path)
        if actual_bytes != resource["bytes"]:
            raise ValidationFailure(
                f"Byte count mismatch for {name}: manifest={resource['bytes']}, "
                f"actual={actual_bytes}."
            )
        if actual_sha256.lower() != resource["sha256"].lower():
            raise ValidationFailure(
                f"SHA-256 mismatch for {name}: manifest={resource['sha256']}, "
                f"actual={actual_sha256}."
            )

        if resource["format"] == "jsonl":
            total_records += validate_jsonl_resource(
                path=path,
                resource=resource,
                source_id=source_id,
                effective_spdx=effective_spdx,
                prompt_validator=prompt_validator,
                seen_ids=seen_ids,
            )
        else:
            raise ValidationFailure(
                f"Canonical publication validator does not yet support resource format "
                f"{resource['format']!r}; refusing an unchecked publication."
            )

    undeclared_jsonl = sorted(
        path.name
        for path in source_dir.glob("part-*.jsonl")
        if path.name not in declared_names
    )
    if undeclared_jsonl:
        raise ValidationFailure(
            "Source directory contains undeclared canonical JSONL shard(s): "
            + ", ".join(undeclared_jsonl)
        )

    totals = manifest["totals"]
    if total_records != totals["record_count"]:
        raise ValidationFailure(
            f"Manifest total record_count={totals['record_count']} but resources contain "
            f"{total_records}."
        )
    if totals.get("resource_count") is not None and totals["resource_count"] != len(resources):
        raise ValidationFailure(
            f"Manifest resource_count={totals['resource_count']} but resources contains "
            f"{len(resources)} entries."
        )

    result = {
        "source_id": source_id,
        "source_revision": manifest["source_revision"],
        "publication_status": manifest["publication"]["status"],
        "resources": len(resources),
        "records": total_records,
        "unique_ids": len(seen_ids),
        "status": "PASS",
    }
    print(json.dumps(result, sort_keys=True))
    return 0


if __name__ == "__main__":
    try:
        raise SystemExit(main())
    except ValidationFailure as exc:
        print(f"ERROR: {exc}", file=sys.stderr)
        raise SystemExit(2)
