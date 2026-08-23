#!/usr/bin/env python3
"""Deterministic importer for the approved prompts.chat source.

This tool never downloads upstream content. It accepts a local copy of the
reviewed prompts.csv, verifies the exact Git blob identity pinned by
data/sources/prompts-chat/source.lock.json, then produces a staged or
publication-ready source snapshot.
"""

from __future__ import annotations

import argparse
import csv
import hashlib
import io
import json
import re
import shutil
import sys
import tempfile
from collections import Counter
from datetime import date
from pathlib import Path
from typing import Any, Iterable

try:
    import yaml
    from jsonschema import Draft202012Validator, FormatChecker
except ImportError as exc:  # pragma: no cover - explicit operator error path
    raise SystemExit(
        "Missing curation dependencies. Install with: "
        "python -m pip install -r scripts/requirements.txt"
    ) from exc


EXPECTED_COLUMNS = ["act", "prompt", "for_devs", "type", "contributor"]
SOURCE_ID = "prompts-chat"
NORMALIZATION_VERSION = "prompts-chat-v1"
DEFAULT_SHARD_BYTES = 8 * 1024 * 1024

PRIVATE_KEY_RE = re.compile(
    r"-----BEGIN (?:RSA |EC |DSA |OPENSSH )?PRIVATE KEY-----", re.IGNORECASE
)
TOKEN_PATTERNS: tuple[tuple[str, re.Pattern[str]], ...] = (
    ("github-token-like", re.compile(r"\bgh[pousr]_[A-Za-z0-9]{30,}\b")),
    ("aws-access-key-like", re.compile(r"\b(?:AKIA|ASIA)[0-9A-Z]{16}\b")),
    (
        "openai-key-like",
        re.compile(r"\bsk-(?:proj-)?[A-Za-z0-9_-]{20,}\b"),
    ),
    ("slack-token-like", re.compile(r"\bxox[baprs]-[A-Za-z0-9-]{20,}\b")),
    (
        "jwt-like",
        re.compile(
            r"\beyJ[A-Za-z0-9_-]{8,}\.[A-Za-z0-9_-]{8,}\.[A-Za-z0-9_-]{8,}\b"
        ),
    ),
)
EMAIL_RE = re.compile(
    r"(?<![A-Za-z0-9._%+-])[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}(?![A-Za-z0-9.-])"
)
MISUSE_RE = re.compile(
    r"\b(?:phishing|credential\s+(?:theft|steal(?:ing)?|harvest(?:ing)?)|"
    r"ransomware|keylogger|infostealer|password\s+stealer|malware\s+distribution|"
    r"spam\s+campaign)\b",
    re.IGNORECASE,
)


class ImportFailure(RuntimeError):
    """Raised when deterministic import invariants are not satisfied."""


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Build a verified Open Prompt Archive snapshot from pinned prompts.chat CSV."
    )
    parser.add_argument("--input", required=True, type=Path, help="Local prompts.csv path.")
    parser.add_argument(
        "--output-dir",
        required=True,
        type=Path,
        help="New output directory. It must not already exist.",
    )
    parser.add_argument(
        "--retrieved-at",
        required=True,
        help="Acquisition/import date in ISO YYYY-MM-DD form.",
    )
    parser.add_argument(
        "--review-decisions",
        type=Path,
        default=None,
        help="Optional JSON decisions for content-policy review candidates.",
    )
    parser.add_argument(
        "--publication-status",
        choices=("staging", "published"),
        default="staging",
    )
    parser.add_argument("--dataset-version", default=None)
    parser.add_argument("--published-at", default=None)
    parser.add_argument("--release-tag", default=None)
    parser.add_argument("--release-url", default=None)
    parser.add_argument(
        "--max-shard-bytes",
        type=int,
        default=DEFAULT_SHARD_BYTES,
        help="Maximum target JSONL shard size; default 8 MiB.",
    )
    return parser.parse_args()


def validate_iso_date(value: str, label: str) -> str:
    try:
        parsed = date.fromisoformat(value)
    except ValueError as exc:
        raise ImportFailure(f"{label} must be YYYY-MM-DD, got {value!r}") from exc
    if parsed.isoformat() != value:
        raise ImportFailure(f"{label} must be canonical YYYY-MM-DD, got {value!r}")
    return value


def load_json(path: Path) -> Any:
    try:
        return json.loads(path.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError) as exc:
        raise ImportFailure(f"Cannot read valid JSON from {path}: {exc}") from exc


def repo_root() -> Path:
    return Path(__file__).resolve().parents[2]


def git_blob_sha1(data: bytes) -> str:
    header = f"blob {len(data)}\0".encode("ascii")
    return hashlib.sha1(header + data).hexdigest()


def sha256_hex(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()


def load_and_verify_source(input_path: Path, lock: dict[str, Any]) -> tuple[bytes, str]:
    try:
        data = input_path.read_bytes()
    except OSError as exc:
        raise ImportFailure(f"Cannot read input file {input_path}: {exc}") from exc

    expected_bytes = lock["bytes"]
    expected_blob = lock["git_blob_sha1"]

    if len(data) != expected_bytes:
        raise ImportFailure(
            f"Input byte size mismatch: expected {expected_bytes}, got {len(data)}."
        )

    actual_blob = git_blob_sha1(data)
    if actual_blob != expected_blob:
        raise ImportFailure(
            "Input Git blob mismatch: "
            f"expected {expected_blob}, got {actual_blob}. Refusing unpinned content."
        )

    return data, sha256_hex(data)


def decode_csv(data: bytes) -> csv.DictReader:
    try:
        text = data.decode("utf-8")
    except UnicodeDecodeError as exc:
        raise ImportFailure("Pinned prompts.csv is not valid UTF-8.") from exc

    reader = csv.DictReader(io.StringIO(text, newline=""))
    if reader.fieldnames != EXPECTED_COLUMNS:
        raise ImportFailure(
            f"Unexpected CSV header: expected {EXPECTED_COLUMNS!r}, got {reader.fieldnames!r}"
        )
    return reader


def canonical_row_payload(row: dict[str, str]) -> bytes:
    payload = [
        "prompts-chat-id-v1",
        row["act"],
        row["prompt"],
        row["for_devs"],
        row["type"],
        row["contributor"],
    ]
    return json.dumps(
        payload, ensure_ascii=False, separators=(",", ":")
    ).encode("utf-8")


def record_id(row: dict[str, str]) -> str:
    return f"{SOURCE_ID}-{sha256_hex(canonical_row_payload(row))}"


def review_reasons(prompt: str) -> list[str]:
    reasons: list[str] = []
    if PRIVATE_KEY_RE.search(prompt):
        reasons.append("private-key-block-like")
    for label, pattern in TOKEN_PATTERNS:
        if pattern.search(prompt):
            reasons.append(label)
    if EMAIL_RE.search(prompt):
        reasons.append("email-address-like")
    if MISUSE_RE.search(prompt):
        reasons.append("potential-abuse-purpose")
    return reasons


def normalize_decision(value: Any, rid: str) -> tuple[str, str | None]:
    if isinstance(value, str):
        decision, reason = value, None
    elif isinstance(value, dict):
        decision = value.get("decision")
        reason = value.get("reason")
        if reason is not None and not isinstance(reason, str):
            raise ImportFailure(f"Review reason for {rid} must be a string or null.")
    else:
        raise ImportFailure(
            f"Review decision for {rid} must be 'include'/'exclude' or an object."
        )

    if decision not in {"include", "exclude"}:
        raise ImportFailure(
            f"Review decision for {rid} must be 'include' or 'exclude', got {decision!r}."
        )
    return decision, reason


def load_decisions(path: Path | None) -> dict[str, tuple[str, str | None]]:
    if path is None:
        return {}
    raw = load_json(path)
    if not isinstance(raw, dict):
        raise ImportFailure("Review decisions file must contain one JSON object.")
    return {rid: normalize_decision(value, rid) for rid, value in raw.items()}


def build_record(
    row: dict[str, str],
    rid: str,
    row_number: int,
    retrieved_at: str,
    lock: dict[str, Any],
) -> dict[str, Any]:
    title = row["act"] if row["act"] else None
    author = row["contributor"] if row["contributor"] else None
    prompt_bytes = row["prompt"].encode("utf-8")

    return {
        "id": rid,
        "title": title,
        "prompt": row["prompt"],
        "type": "llm",
        "models": [],
        "tags": [],
        "language": None,
        "source": {
            "source_id": SOURCE_ID,
            "name": "prompts.chat prompt corpus",
            "url": lock["file_url"],
            "repository": lock["repository"],
            "author": author,
            "upstream_id": f"csv-row:{row_number}",
            "revision": lock["revision"],
        },
        "license": {
            "spdx": lock["license"]["spdx"],
            "url": lock["license"]["evidence_url"],
            "attribution_required": False,
            "attribution": None,
            "scope_verified": True,
        },
        "provenance": {
            "retrieved_at": retrieved_at,
            "sha256": sha256_hex(prompt_bytes),
            "verified": True,
            "modified": False,
            "transformation": (
                "RFC-compatible CSV decoding and deterministic JSON serialization only; "
                "prompt text was not rewritten."
            ),
        },
        "media": [],
    }


def validate_instance(instance: Any, schema: dict[str, Any], label: str) -> None:
    validator = Draft202012Validator(schema, format_checker=FormatChecker())
    errors = sorted(validator.iter_errors(instance), key=lambda err: list(err.path))
    if errors:
        first = errors[0]
        location = ".".join(str(part) for part in first.path) or "<root>"
        raise ImportFailure(f"{label} schema validation failed at {location}: {first.message}")


def encode_jsonl(record: dict[str, Any]) -> bytes:
    return (
        json.dumps(
            record,
            ensure_ascii=False,
            sort_keys=True,
            separators=(",", ":"),
        )
        + "\n"
    ).encode("utf-8")


def shard_records(
    records: Iterable[dict[str, Any]], max_bytes: int
) -> list[tuple[str, bytes, int]]:
    if max_bytes <= 0:
        raise ImportFailure("--max-shard-bytes must be greater than zero.")

    shards: list[tuple[str, bytes, int]] = []
    buffer = bytearray()
    count = 0
    shard_index = 0

    def flush() -> None:
        nonlocal buffer, count, shard_index
        if not buffer:
            return
        name = f"part-{shard_index:05d}.jsonl"
        shards.append((name, bytes(buffer), count))
        shard_index += 1
        buffer = bytearray()
        count = 0

    for record in records:
        line = encode_jsonl(record)
        if buffer and len(buffer) + len(line) > max_bytes:
            flush()
        buffer.extend(line)
        count += 1
        if len(buffer) >= max_bytes:
            flush()

    flush()
    return shards


def write_json(path: Path, payload: Any) -> None:
    path.write_text(
        json.dumps(payload, ensure_ascii=False, indent=2, sort_keys=True) + "\n",
        encoding="utf-8",
    )


def write_jsonl(path: Path, rows: Iterable[dict[str, Any]]) -> None:
    with path.open("wb") as handle:
        for row in rows:
            handle.write(encode_jsonl(row))


def build_manifest(
    *,
    lock: dict[str, Any],
    retrieved_at: str,
    publication_status: str,
    dataset_version: str | None,
    published_at: str | None,
    release_tag: str | None,
    release_url: str | None,
    upstream_sha256: str,
    shards: list[tuple[str, bytes, int]],
    counters: Counter[str],
) -> dict[str, Any]:
    resources = [
        {
            "name": name,
            "location": f"data/sources/prompts-chat/{name}",
            "format": "jsonl",
            "compression": None,
            "record_count": count,
            "sha256": sha256_hex(payload),
            "bytes": len(payload),
        }
        for name, payload, count in shards
    ]

    policy_removed = counters["review_excluded"] + counters["review_pending"]
    malformed_removed = counters["empty_prompt"] + counters["malformed_row"]

    manifest: dict[str, Any] = {
        "schema_version": 1,
        "source_id": SOURCE_ID,
        "source_revision": lock["revision"],
        "retrieved_at": retrieved_at,
        "review_file": "sources/reviews/prompts-chat.md",
        "effective_license": {
            "spdx": lock["license"]["spdx"],
            "evidence_url": lock["license"]["evidence_url"],
        },
        "approved_scope": (
            "Prompt text/data explicitly covered by the upstream CC0 declaration, "
            "using pinned prompts.csv; software, book content, branding, and media excluded."
        ),
        "record_schema": "schema/prompt.schema.json",
        "normalization": {
            "version": NORMALIZATION_VERSION,
            "semantic_prompt_changes": False,
            "notes": (
                "Stable IDs use SHA-256 over an exact JSON-array canonicalization of the "
                "five decoded upstream CSV fields. Prompt text is not rewritten."
            ),
        },
        "filters": [
            {
                "name": "empty-or-malformed",
                "description": "Exclude rows that cannot produce a valid non-empty canonical prompt record.",
                "records_removed": malformed_removed,
            },
            {
                "name": "exact-row-deduplication",
                "description": "Collapse byte-equivalent decoded source rows sharing the same deterministic content ID.",
                "records_removed": counters["duplicate_row"],
            },
            {
                "name": "content-policy-review",
                "description": (
                    "Hold heuristic credential/personal-data/abuse candidates out of canonical "
                    "shards until an explicit include/exclude decision exists."
                ),
                "records_removed": policy_removed,
            },
        ],
        "excluded_fields": ["for_devs", "type"],
        "publication": {
            "status": publication_status,
            "dataset_version": dataset_version,
            "release_tag": release_tag,
            "release_url": release_url,
            "published_at": published_at,
        },
        "resources": resources,
        "totals": {
            "record_count": sum(item["record_count"] for item in resources),
            "resource_count": len(resources),
        },
        "notes": (
            f"Acquisition lock: {lock['path']} bytes={lock['bytes']}, "
            f"git_blob_sha1={lock['git_blob_sha1']}, upstream_sha256={upstream_sha256}. "
            f"Pending content-review records: {counters['review_pending']}."
        ),
    }
    return manifest


def ensure_publication_args(args: argparse.Namespace, pending: int) -> None:
    if args.publication_status == "staging":
        if any(
            value is not None
            for value in (
                args.dataset_version,
                args.published_at,
                args.release_tag,
                args.release_url,
            )
        ):
            raise ImportFailure(
                "Release metadata must not be supplied while --publication-status=staging."
            )
        return

    if pending:
        raise ImportFailure(
            f"Cannot build a published manifest with {pending} unresolved review candidate(s)."
        )
    if not args.dataset_version:
        raise ImportFailure("--dataset-version is required for published output.")
    if not args.published_at:
        raise ImportFailure("--published-at is required for published output.")
    validate_iso_date(args.published_at, "--published-at")


def main() -> int:
    args = parse_args()
    retrieved_at = validate_iso_date(args.retrieved_at, "--retrieved-at")

    root = repo_root()
    lock_path = root / "data" / "sources" / SOURCE_ID / "source.lock.json"
    prompt_schema_path = root / "schema" / "prompt.schema.json"
    manifest_schema_path = root / "schema" / "manifest.schema.json"

    lock = load_json(lock_path)
    if lock.get("source_id") != SOURCE_ID:
        raise ImportFailure(f"Unexpected source lock identity in {lock_path}.")

    data, upstream_sha256 = load_and_verify_source(args.input, lock)
    prompt_schema = load_json(prompt_schema_path)
    manifest_schema = load_json(manifest_schema_path)
    decisions = load_decisions(args.review_decisions)

    reader = decode_csv(data)
    counters: Counter[str] = Counter()
    records_by_id: dict[str, dict[str, Any]] = {}
    flagged_ids: set[str] = set()
    review_queue: list[dict[str, Any]] = []
    decision_log: list[dict[str, Any]] = []

    for row_number, raw_row in enumerate(reader, start=1):
        counters["csv_rows"] += 1

        if None in raw_row or any(raw_row.get(column) is None for column in EXPECTED_COLUMNS):
            counters["malformed_row"] += 1
            continue

        row = {column: raw_row[column] for column in EXPECTED_COLUMNS}
        if not row["prompt"].strip():
            counters["empty_prompt"] += 1
            continue

        rid = record_id(row)
        if rid in records_by_id or rid in flagged_ids:
            counters["duplicate_row"] += 1
            continue

        record = build_record(row, rid, row_number, retrieved_at, lock)
        validate_instance(record, prompt_schema, f"record {rid}")

        reasons = review_reasons(row["act"] + "\n" + row["prompt"])
        if not reasons:
            records_by_id[rid] = record
            continue

        flagged_ids.add(rid)
        counters["review_flagged"] += 1
        review_queue.append(
            {
                "id": rid,
                "source_row": row_number,
                "title": record["title"],
                "prompt": row["prompt"],
                "author": record["source"]["author"],
                "reasons": reasons,
            }
        )

        if rid not in decisions:
            counters["review_pending"] += 1
            continue

        decision, reason = decisions[rid]
        decision_log.append(
            {
                "id": rid,
                "decision": decision,
                "reason": reason,
                "reasons": reasons,
            }
        )
        if decision == "include":
            counters["review_included"] += 1
            records_by_id[rid] = record
        else:
            counters["review_excluded"] += 1

    unknown_decisions = sorted(set(decisions) - flagged_ids)
    if unknown_decisions:
        preview = ", ".join(unknown_decisions[:5])
        raise ImportFailure(
            "Review decisions contain IDs that are not review candidates for this pinned input: "
            f"{preview}" + (" ..." if len(unknown_decisions) > 5 else "")
        )

    ensure_publication_args(args, counters["review_pending"])

    records = [records_by_id[rid] for rid in sorted(records_by_id)]
    shards = shard_records(records, args.max_shard_bytes)
    manifest = build_manifest(
        lock=lock,
        retrieved_at=retrieved_at,
        publication_status=args.publication_status,
        dataset_version=args.dataset_version,
        published_at=args.published_at,
        release_tag=args.release_tag,
        release_url=args.release_url,
        upstream_sha256=upstream_sha256,
        shards=shards,
        counters=counters,
    )
    validate_instance(manifest, manifest_schema, "manifest")

    output_dir = args.output_dir.resolve()
    if output_dir.exists():
        raise ImportFailure(
            f"Output directory already exists: {output_dir}. Refusing to overwrite it."
        )
    output_dir.parent.mkdir(parents=True, exist_ok=True)
    temp_dir = Path(
        tempfile.mkdtemp(prefix=f".{output_dir.name}.tmp-", dir=output_dir.parent)
    )

    try:
        publish_dir = temp_dir / "publish"
        audit_dir = temp_dir / "audit"
        publish_dir.mkdir()
        audit_dir.mkdir()

        for name, payload, _count in shards:
            (publish_dir / name).write_bytes(payload)

        yaml_text = yaml.safe_dump(
            manifest,
            allow_unicode=True,
            sort_keys=False,
            default_flow_style=False,
        )
        (publish_dir / "manifest.yaml").write_text(yaml_text, encoding="utf-8")

        report = {
            "schema_version": 1,
            "source_id": SOURCE_ID,
            "source_revision": lock["revision"],
            "retrieved_at": retrieved_at,
            "input": {
                "path": lock["path"],
                "bytes": len(data),
                "git_blob_sha1": git_blob_sha1(data),
                "sha256": upstream_sha256,
            },
            "counts": {
                "csv_rows": counters["csv_rows"],
                "canonical_records": len(records),
                "duplicate_rows_removed": counters["duplicate_row"],
                "empty_prompts_removed": counters["empty_prompt"],
                "malformed_rows_removed": counters["malformed_row"],
                "review_flagged": counters["review_flagged"],
                "review_included": counters["review_included"],
                "review_excluded": counters["review_excluded"],
                "review_pending": counters["review_pending"],
            },
            "publication_status": args.publication_status,
            "review_complete": counters["review_pending"] == 0,
        }
        write_json(audit_dir / "review-report.json", report)
        if args.publication_status == "staging":
            write_jsonl(
                audit_dir / "review-queue.jsonl",
                sorted(review_queue, key=lambda item: item["id"]),
            )
        write_json(
            audit_dir / "review-decisions-applied.json",
            sorted(decision_log, key=lambda item: item["id"]),
        )
        (audit_dir / "README.txt").write_text(
            "Local curation audit material. Do not copy review-queue.jsonl into the "
            "public dataset. Only files under publish/ are publication candidates.\n",
            encoding="utf-8",
        )

        temp_dir.rename(output_dir)
    except Exception:
        shutil.rmtree(temp_dir, ignore_errors=True)
        raise

    print(
        json.dumps(
            {
                "output_dir": str(output_dir),
                "publish_dir": str(output_dir / "publish"),
                "audit_dir": str(output_dir / "audit"),
                "records": len(records),
                "shards": len(shards),
                "pending_review": counters["review_pending"],
                "input_sha256": upstream_sha256,
                "publication_status": args.publication_status,
            },
            sort_keys=True,
        )
    )
    return 0


if __name__ == "__main__":
    try:
        raise SystemExit(main())
    except ImportFailure as exc:
        print(f"ERROR: {exc}", file=sys.stderr)
        raise SystemExit(2)
