from __future__ import annotations

import hashlib
import json
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path

import yaml


ROOT = Path(__file__).resolve().parents[1]
VALIDATOR = ROOT / "scripts" / "validate_publication.py"
REVISION = "25cb43d6e61974e66f3650cbc5a65482bc592552"


def canonical_record(record_id: str = "prompts-chat-test") -> dict:
    return {
        "id": record_id,
        "title": "Synthetic test prompt",
        "prompt": "Synthetic fixture prompt used only to test publication validation.",
        "type": "llm",
        "models": [],
        "tags": [],
        "language": "en",
        "source": {
            "source_id": "prompts-chat",
            "name": "prompts.chat prompt corpus",
            "url": (
                "https://github.com/f/prompts.chat/blob/"
                f"{REVISION}/prompts.csv"
            ),
            "repository": "https://github.com/f/prompts.chat",
            "author": None,
            "upstream_id": "synthetic-test-only",
            "revision": REVISION,
        },
        "license": {
            "spdx": "CC0-1.0",
            "url": (
                "https://github.com/f/prompts.chat/blob/"
                f"{REVISION}/LICENSE"
            ),
            "attribution_required": False,
            "attribution": None,
            "scope_verified": True,
        },
        "provenance": {
            "retrieved_at": "2026-08-23",
            "sha256": hashlib.sha256(
                b"Synthetic fixture prompt used only to test publication validation."
            ).hexdigest(),
            "verified": True,
            "modified": False,
            "transformation": "Synthetic validator fixture; not publication data.",
        },
        "media": [],
    }


def write_snapshot(directory: Path, records: list[dict]) -> None:
    shard = directory / "part-00000.jsonl"
    payload = b"".join(
        (
            json.dumps(
                record,
                ensure_ascii=False,
                sort_keys=True,
                separators=(",", ":"),
            )
            + "\n"
        ).encode("utf-8")
        for record in records
    )
    shard.write_bytes(payload)

    manifest = {
        "schema_version": 1,
        "source_id": "prompts-chat",
        "source_revision": REVISION,
        "retrieved_at": "2026-08-23",
        "review_file": "sources/reviews/prompts-chat.md",
        "effective_license": {
            "spdx": "CC0-1.0",
            "evidence_url": (
                "https://github.com/f/prompts.chat/blob/"
                f"{REVISION}/LICENSE"
            ),
        },
        "approved_scope": "Synthetic test of the approved prompts.chat publication contract.",
        "record_schema": "schema/prompt.schema.json",
        "normalization": {
            "version": "test-v1",
            "semantic_prompt_changes": False,
            "notes": "Test fixture only.",
        },
        "filters": [],
        "excluded_fields": [],
        "publication": {
            "status": "staging",
            "dataset_version": None,
            "release_tag": None,
            "release_url": None,
            "published_at": None,
        },
        "resources": [
            {
                "name": shard.name,
                "location": f"data/sources/prompts-chat/{shard.name}",
                "format": "jsonl",
                "compression": None,
                "record_count": len(records),
                "sha256": hashlib.sha256(payload).hexdigest(),
                "bytes": len(payload),
            }
        ],
        "totals": {"record_count": len(records), "resource_count": 1},
        "notes": "Synthetic publication-validator test fixture.",
    }
    (directory / "manifest.yaml").write_text(
        yaml.safe_dump(manifest, sort_keys=False), encoding="utf-8"
    )


class PublicationValidatorTests(unittest.TestCase):
    def run_validator(self, directory: Path, *extra: str) -> subprocess.CompletedProcess[str]:
        return subprocess.run(
            [sys.executable, str(VALIDATOR), str(directory), *extra],
            cwd=ROOT,
            text=True,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            check=False,
        )

    def test_valid_staging_snapshot_passes(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            source_dir = Path(tmp)
            write_snapshot(source_dir, [canonical_record()])
            result = self.run_validator(source_dir)
            self.assertEqual(result.returncode, 0, result.stderr)
            payload = json.loads(result.stdout)
            self.assertEqual(payload["status"], "PASS")
            self.assertEqual(payload["records"], 1)
            self.assertEqual(payload["unique_ids"], 1)

    def test_tampered_shard_fails_checksum_gate(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            source_dir = Path(tmp)
            write_snapshot(source_dir, [canonical_record()])
            with (source_dir / "part-00000.jsonl").open("ab") as handle:
                handle.write(b" ")
            result = self.run_validator(source_dir)
            self.assertEqual(result.returncode, 2)
            self.assertIn("Byte count mismatch", result.stderr)

    def test_duplicate_ids_fail(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            source_dir = Path(tmp)
            record = canonical_record()
            write_snapshot(source_dir, [record, record])
            result = self.run_validator(source_dir)
            self.assertEqual(result.returncode, 2)
            self.assertIn("Duplicate canonical record id", result.stderr)

    def test_require_published_rejects_staging(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            source_dir = Path(tmp)
            write_snapshot(source_dir, [canonical_record()])
            result = self.run_validator(source_dir, "--require-published")
            self.assertEqual(result.returncode, 2)
            self.assertIn("manifest status is not 'published'", result.stderr)


if __name__ == "__main__":
    unittest.main()
