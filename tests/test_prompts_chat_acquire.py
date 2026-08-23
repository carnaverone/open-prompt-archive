from __future__ import annotations

import hashlib
import importlib.util
import tempfile
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
MODULE_PATH = ROOT / "scripts" / "acquire" / "prompts_chat.py"
SPEC = importlib.util.spec_from_file_location("prompts_chat_acquire", MODULE_PATH)
assert SPEC is not None and SPEC.loader is not None
MODULE = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(MODULE)


class PromptsChatAcquireTests(unittest.TestCase):
    def test_locked_url_must_encode_exact_revision_and_path(self) -> None:
        lock = {
            "raw_url": (
                "https://raw.githubusercontent.com/f/prompts.chat/"
                "abc123/prompts.csv"
            ),
            "revision": "abc123",
            "path": "prompts.csv",
        }
        self.assertEqual(MODULE.validate_locked_url(lock), lock["raw_url"])

        changed = dict(lock)
        changed["raw_url"] = (
            "https://raw.githubusercontent.com/f/prompts.chat/main/prompts.csv"
        )
        with self.assertRaises(MODULE.AcquisitionFailure):
            MODULE.validate_locked_url(changed)

    def test_verify_bytes_requires_length_and_git_blob_identity(self) -> None:
        data = b"pinned bytes\n"
        blob = hashlib.sha1(f"blob {len(data)}\0".encode("ascii") + data).hexdigest()
        lock = {"bytes": len(data), "git_blob_sha1": blob}
        result = MODULE.verify_bytes(data, lock)
        self.assertEqual(result["bytes"], len(data))
        self.assertEqual(result["git_blob_sha1"], blob)
        self.assertEqual(result["sha256"], hashlib.sha256(data).hexdigest())

        with self.assertRaises(MODULE.AcquisitionFailure):
            MODULE.verify_bytes(data + b"x", lock)

    def test_exclusive_write_refuses_existing_destination(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            target = Path(tmp) / "prompts.csv"
            MODULE.write_exclusive(target, b"first")
            self.assertEqual(target.read_bytes(), b"first")
            with self.assertRaises(MODULE.AcquisitionFailure):
                MODULE.write_exclusive(target, b"second")
            self.assertEqual(target.read_bytes(), b"first")


if __name__ == "__main__":
    unittest.main()
