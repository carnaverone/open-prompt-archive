#!/usr/bin/env python3
"""Acquire the exact reviewed prompts.chat CSV without weakening the source lock.

The destination is retained only if the downloaded bytes match the byte length
and Git blob SHA-1 already pinned in data/sources/prompts-chat/source.lock.json.
No authentication, mirror fallback, or floating branch is supported.
"""

from __future__ import annotations

import argparse
import hashlib
import json
import os
import sys
import tempfile
import urllib.error
import urllib.parse
import urllib.request
from pathlib import Path
from typing import Any


SOURCE_ID = "prompts-chat"
ALLOWED_HOST = "raw.githubusercontent.com"
ALLOWED_OWNER_REPO_PREFIX = "/f/prompts.chat/"


class AcquisitionFailure(RuntimeError):
    """Raised when the exact reviewed acquisition cannot be established."""


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Download and verify the exact reviewed prompts.chat prompts.csv."
    )
    parser.add_argument(
        "--output",
        required=True,
        type=Path,
        help="Destination for the verified prompts.csv; must not already exist.",
    )
    parser.add_argument(
        "--receipt",
        type=Path,
        default=None,
        help="Optional JSON path for an acquisition-integrity receipt.",
    )
    parser.add_argument(
        "--timeout",
        type=float,
        default=60.0,
        help="Network timeout in seconds; default 60.",
    )
    return parser.parse_args()


def repo_root() -> Path:
    return Path(__file__).resolve().parents[2]


def load_json(path: Path) -> Any:
    try:
        return json.loads(path.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError) as exc:
        raise AcquisitionFailure(f"Cannot read valid JSON from {path}: {exc}") from exc


def git_blob_sha1(data: bytes) -> str:
    header = f"blob {len(data)}\0".encode("ascii")
    return hashlib.sha1(header + data).hexdigest()


def validate_locked_url(lock: dict[str, Any]) -> str:
    raw_url = lock.get("raw_url")
    if not isinstance(raw_url, str):
        raise AcquisitionFailure("Source lock does not contain a raw_url string.")

    parsed = urllib.parse.urlparse(raw_url)
    if parsed.scheme != "https" or parsed.hostname != ALLOWED_HOST:
        raise AcquisitionFailure(
            f"Locked raw_url must use https://{ALLOWED_HOST}, got {raw_url!r}."
        )
    if not parsed.path.startswith(ALLOWED_OWNER_REPO_PREFIX):
        raise AcquisitionFailure(
            f"Locked raw_url escapes expected upstream repository: {raw_url!r}."
        )
    revision = lock.get("revision")
    path = lock.get("path")
    expected_path = f"{ALLOWED_OWNER_REPO_PREFIX}{revision}/{path}"
    if parsed.path != expected_path:
        raise AcquisitionFailure(
            "Locked raw_url does not encode the exact reviewed revision/path: "
            f"expected {expected_path!r}, got {parsed.path!r}."
        )
    if parsed.query or parsed.fragment:
        raise AcquisitionFailure("Locked raw_url must not contain a query or fragment.")
    return raw_url


def verify_bytes(data: bytes, lock: dict[str, Any]) -> dict[str, Any]:
    expected_bytes = lock.get("bytes")
    expected_blob = lock.get("git_blob_sha1")
    if not isinstance(expected_bytes, int) or expected_bytes < 0:
        raise AcquisitionFailure("Source lock bytes value is invalid.")
    if not isinstance(expected_blob, str) or len(expected_blob) != 40:
        raise AcquisitionFailure("Source lock git_blob_sha1 value is invalid.")

    actual_bytes = len(data)
    if actual_bytes != expected_bytes:
        raise AcquisitionFailure(
            f"Downloaded byte size mismatch: expected {expected_bytes}, got {actual_bytes}."
        )

    actual_blob = git_blob_sha1(data)
    if actual_blob != expected_blob:
        raise AcquisitionFailure(
            f"Downloaded Git blob mismatch: expected {expected_blob}, got {actual_blob}."
        )

    return {
        "bytes": actual_bytes,
        "git_blob_sha1": actual_blob,
        "sha256": hashlib.sha256(data).hexdigest(),
    }


def download_locked_bytes(raw_url: str, timeout: float) -> bytes:
    if timeout <= 0:
        raise AcquisitionFailure("--timeout must be greater than zero.")

    request = urllib.request.Request(
        raw_url,
        headers={
            "User-Agent": "open-prompt-archive-curation/1",
            "Accept": "text/plain,application/octet-stream;q=0.9,*/*;q=0.1",
        },
        method="GET",
    )
    try:
        with urllib.request.urlopen(request, timeout=timeout) as response:
            final_url = response.geturl()
            parsed = urllib.parse.urlparse(final_url)
            if parsed.scheme != "https" or parsed.hostname != ALLOWED_HOST:
                raise AcquisitionFailure(
                    f"Unexpected download redirect outside {ALLOWED_HOST}: {final_url!r}."
                )
            data = response.read()
    except (urllib.error.URLError, TimeoutError, OSError) as exc:
        raise AcquisitionFailure(f"Pinned source download failed: {exc}") from exc
    return data


def write_exclusive(path: Path, data: bytes) -> None:
    path = path.resolve()
    if path.exists():
        raise AcquisitionFailure(f"Destination already exists: {path}")
    path.parent.mkdir(parents=True, exist_ok=True)

    fd, temp_name = tempfile.mkstemp(prefix=f".{path.name}.tmp-", dir=path.parent)
    temp_path = Path(temp_name)
    try:
        with os.fdopen(fd, "wb") as handle:
            handle.write(data)
            handle.flush()
            os.fsync(handle.fileno())
        os.replace(temp_path, path)
    except Exception:
        try:
            temp_path.unlink(missing_ok=True)
        finally:
            raise


def main() -> int:
    args = parse_args()
    root = repo_root()
    lock_path = root / "data" / "sources" / SOURCE_ID / "source.lock.json"
    lock = load_json(lock_path)
    if lock.get("source_id") != SOURCE_ID:
        raise AcquisitionFailure(f"Unexpected source identity in {lock_path}.")

    raw_url = validate_locked_url(lock)
    output = args.output.resolve()
    if output.exists():
        raise AcquisitionFailure(f"Destination already exists: {output}")
    if args.receipt is not None and args.receipt.resolve().exists():
        raise AcquisitionFailure(f"Receipt destination already exists: {args.receipt.resolve()}")

    data = download_locked_bytes(raw_url, args.timeout)
    integrity = verify_bytes(data, lock)

    # Persist only after all source-identity checks pass.
    write_exclusive(output, data)

    receipt = {
        "schema_version": 1,
        "source_id": SOURCE_ID,
        "repository": lock["repository"],
        "revision": lock["revision"],
        "path": lock["path"],
        "raw_url": raw_url,
        "bytes": integrity["bytes"],
        "git_blob_sha1": integrity["git_blob_sha1"],
        "sha256": integrity["sha256"],
        "output": str(output),
        "verified": True,
    }

    if args.receipt is not None:
        receipt_path = args.receipt.resolve()
        receipt_path.parent.mkdir(parents=True, exist_ok=True)
        write_exclusive(
            receipt_path,
            (json.dumps(receipt, indent=2, sort_keys=True) + "\n").encode("utf-8"),
        )

    print(json.dumps(receipt, sort_keys=True))
    return 0


if __name__ == "__main__":
    try:
        raise SystemExit(main())
    except AcquisitionFailure as exc:
        print(f"ERROR: {exc}", file=sys.stderr)
        raise SystemExit(2)
