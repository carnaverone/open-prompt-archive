from __future__ import annotations

import importlib.util
import json
import unittest
from collections import Counter
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
IMPORTER_PATH = ROOT / "scripts" / "import" / "prompts_chat.py"
SPEC = importlib.util.spec_from_file_location("prompts_chat_importer", IMPORTER_PATH)
assert SPEC is not None and SPEC.loader is not None
IMPORTER = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(IMPORTER)


class PromptsChatImporterTests(unittest.TestCase):
    def setUp(self) -> None:
        self.lock = json.loads(
            (ROOT / "data" / "sources" / "prompts-chat" / "source.lock.json").read_text(
                encoding="utf-8"
            )
        )
        self.prompt_schema = json.loads(
            (ROOT / "schema" / "prompt.schema.json").read_text(encoding="utf-8")
        )
        self.manifest_schema = json.loads(
            (ROOT / "schema" / "manifest.schema.json").read_text(encoding="utf-8")
        )

    def test_git_blob_sha1_matches_git_hash_object(self) -> None:
        # Independently captured from: printf 'test content\n' | git hash-object --stdin
        self.assertEqual(
            IMPORTER.git_blob_sha1(b"test content\n"),
            "d670460b4b4aece5915caf5c68d12f560a9fe3e4",
        )

    def test_csv_decoder_preserves_embedded_crlf(self) -> None:
        data = (
            b"act,prompt,for_devs,type,contributor\r\n"
            b'Test,"line1\r\nline2",FALSE,TEXT,alice\r\n'
        )
        rows = list(IMPORTER.decode_csv(data))
        self.assertEqual(len(rows), 1)
        self.assertEqual(rows[0]["prompt"], "line1\r\nline2")

    def test_v1_record_id_is_frozen(self) -> None:
        row = {
            "act": "Test",
            "prompt": "hello, world",
            "for_devs": "FALSE",
            "type": "TEXT",
            "contributor": "alice",
        }
        self.assertEqual(
            IMPORTER.record_id(row),
            "prompts-chat-9d0081bb834cc4d795e5bf1414dcce798be066fce69fe6d6a234d5e260b5e8e0",
        )

    def test_record_preserves_prompt_and_validates(self) -> None:
        row = {
            "act": "Test",
            "prompt": "  keep this prompt exactly\r\nincluding transport whitespace  ",
            "for_devs": "FALSE",
            "type": "TEXT",
            "contributor": "alice",
        }
        rid = IMPORTER.record_id(row)
        record = IMPORTER.build_record(row, rid, 7, "2026-08-23", self.lock)
        self.assertEqual(record["prompt"], row["prompt"])
        self.assertFalse(record["provenance"]["modified"])
        self.assertEqual(record["source"]["upstream_id"], "csv-row:7")
        IMPORTER.validate_instance(record, self.prompt_schema, "test record")

    def test_review_scanner_flags_candidates_without_rewriting(self) -> None:
        self.assertEqual(IMPORTER.review_reasons("ordinary reusable prompt"), [])
        self.assertIn(
            "email-address-like",
            IMPORTER.review_reasons("Contact jane@example.com for the draft."),
        )
        self.assertIn(
            "potential-abuse-purpose",
            IMPORTER.review_reasons("Design a phishing campaign."),
        )

    def test_sharding_is_deterministic_and_respects_record_boundaries(self) -> None:
        base = {
            "title": None,
            "prompt": "x",
            "type": "llm",
            "models": [],
            "tags": [],
            "language": None,
            "source": {
                "source_id": "prompts-chat",
                "name": "prompts.chat prompt corpus",
                "url": self.lock["file_url"],
                "repository": self.lock["repository"],
                "author": None,
                "upstream_id": "csv-row:1",
                "revision": self.lock["revision"],
            },
            "license": {
                "spdx": "CC0-1.0",
                "url": self.lock["license"]["evidence_url"],
                "attribution_required": False,
                "attribution": None,
                "scope_verified": True,
            },
            "provenance": {
                "retrieved_at": "2026-08-23",
                "sha256": "0" * 64,
                "verified": True,
                "modified": False,
                "transformation": None,
            },
            "media": [],
        }
        records = []
        for index in range(3):
            record = dict(base)
            record["id"] = f"prompts-chat-{index}"
            records.append(record)
        line_size = len(IMPORTER.encode_jsonl(records[0]))
        shards = IMPORTER.shard_records(records, line_size + 1)
        self.assertEqual([count for _name, _payload, count in shards], [1, 1, 1])
        self.assertEqual(
            [name for name, _payload, _count in shards],
            ["part-00000.jsonl", "part-00001.jsonl", "part-00002.jsonl"],
        )

    def test_generated_manifest_validates(self) -> None:
        counters = Counter(
            {
                "duplicate_row": 1,
                "empty_prompt": 0,
                "malformed_row": 0,
                "review_excluded": 1,
                "review_pending": 0,
            }
        )
        shards = [("part-00000.jsonl", b'{"id":"placeholder"}\n', 1)]
        manifest = IMPORTER.build_manifest(
            lock=self.lock,
            retrieved_at="2026-08-23",
            publication_status="staging",
            dataset_version=None,
            published_at=None,
            release_tag=None,
            release_url=None,
            upstream_sha256="a" * 64,
            shards=shards,
            counters=counters,
        )
        IMPORTER.validate_instance(manifest, self.manifest_schema, "test manifest")
        self.assertEqual(manifest["totals"]["record_count"], 1)
        self.assertEqual(manifest["totals"]["resource_count"], 1)


if __name__ == "__main__":
    unittest.main()
