from __future__ import annotations

import csv
import hashlib
import importlib.util
import io
import json
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
MODULE_PATH = ROOT / "scripts" / "import" / "prompts_chat.py"
SPEC = importlib.util.spec_from_file_location("prompts_chat_importer", MODULE_PATH)
assert SPEC is not None and SPEC.loader is not None
MODULE = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(MODULE)


class PromptsChatImporterTests(unittest.TestCase):
    def test_git_blob_identity_matches_git_object_rule(self) -> None:
        payload = b"hello\n"
        expected = hashlib.sha1(b"blob 6\0hello\n").hexdigest()
        self.assertEqual(MODULE.git_blob_sha1(payload), expected)

    def test_multiline_prompt_survives_csv_decode_exactly(self) -> None:
        prompt = "Line one\nLine two, with comma\nLine three"
        buffer = io.StringIO(newline="")
        writer = csv.writer(buffer, lineterminator="\r\n")
        writer.writerow(MODULE.EXPECTED_COLUMNS)
        writer.writerow(["Example", prompt, "FALSE", "TEXT", "tester"])
        data = buffer.getvalue().encode("utf-8")

        reader = MODULE.decode_csv(data)
        row = next(reader)
        self.assertEqual(row["prompt"], prompt)

    def test_record_id_is_deterministic_and_field_sensitive(self) -> None:
        row = {
            "act": "Example",
            "prompt": "Do the thing.",
            "for_devs": "FALSE",
            "type": "TEXT",
            "contributor": "tester",
        }
        first = MODULE.record_id(row)
        second = MODULE.record_id(dict(row))
        self.assertEqual(first, second)
        self.assertTrue(first.startswith("prompts-chat-"))
        self.assertEqual(len(first.removeprefix("prompts-chat-")), 64)

        changed = dict(row)
        changed["contributor"] = "different"
        self.assertNotEqual(first, MODULE.record_id(changed))

    def test_build_record_preserves_prompt_and_provenance_hash(self) -> None:
        prompt = "Exact spacing  \nand newline."
        row = {
            "act": "Example",
            "prompt": prompt,
            "for_devs": "FALSE",
            "type": "TEXT",
            "contributor": "tester",
        }
        lock = {
            "file_url": "https://example.invalid/prompts.csv",
            "repository": "https://example.invalid/repo",
            "revision": "abc123",
            "license": {
                "spdx": "CC0-1.0",
                "evidence_url": "https://example.invalid/license",
            },
        }
        rid = MODULE.record_id(row)
        record = MODULE.build_record(row, rid, 7, "2026-08-23", lock)
        self.assertEqual(record["prompt"], prompt)
        self.assertFalse(record["provenance"]["modified"])
        self.assertEqual(
            record["provenance"]["sha256"],
            hashlib.sha256(prompt.encode("utf-8")).hexdigest(),
        )
        self.assertEqual(record["source"]["upstream_id"], "csv-row:7")

    def test_review_heuristic_flags_credential_like_material(self) -> None:
        reasons = MODULE.review_reasons(
            "Use this example token ghp_ABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890ABCDEF"
        )
        self.assertIn("github-token-like", reasons)

    def test_sharding_is_deterministic_and_never_drops_large_record(self) -> None:
        row = {
            "act": "Example",
            "prompt": "x" * 100,
            "for_devs": "FALSE",
            "type": "TEXT",
            "contributor": "tester",
        }
        lock = {
            "file_url": "https://example.invalid/prompts.csv",
            "repository": "https://example.invalid/repo",
            "revision": "abc123",
            "license": {
                "spdx": "CC0-1.0",
                "evidence_url": "https://example.invalid/license",
            },
        }
        record = MODULE.build_record(
            row, MODULE.record_id(row), 1, "2026-08-23", lock
        )
        shards = MODULE.shard_records([record], max_bytes=20)
        self.assertEqual(len(shards), 1)
        name, payload, count = shards[0]
        self.assertEqual(name, "part-00000.jsonl")
        self.assertEqual(count, 1)
        decoded = json.loads(payload.decode("utf-8"))
        self.assertEqual(decoded["prompt"], row["prompt"])


if __name__ == "__main__":
    unittest.main()
