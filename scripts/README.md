# Scripts

This directory contains deterministic curation tooling used to acquire, ingest, verify, and maintain Open Prompt Archive. Tooling is subordinate to dataset policy and source-review decisions; it must never expand an approved source scope on its own.

## Current tooling

```text
scripts/
├── requirements.txt
├── validate_publication.py
├── acquire/
│   └── prompts_chat.py
└── import/
    └── prompts_chat.py
```

## Pinned acquisition

### `acquire/prompts_chat.py`

Acquires only the exact `prompts.csv` object already frozen in `data/sources/prompts-chat/source.lock.json`.

It deliberately does **not** provide a general downloader. The acquisition helper:

- accepts no arbitrary URL;
- accepts no branch name or replacement revision;
- reads the canonical pinned raw URL from the source lock;
- requires HTTPS on `raw.githubusercontent.com` and the exact `f/prompts.chat/<revision>/prompts.csv` path;
- rejects unexpected redirects rather than silently widening the source boundary;
- requires no credential or private access method;
- verifies the exact byte count and Git blob SHA-1 **before** retaining the download;
- computes the acquisition SHA-256 from the actual verified bytes;
- refuses to overwrite an existing destination, including a race-safe exclusive install;
- can emit a machine-readable acquisition receipt.

Example:

```bash
python scripts/acquire/prompts_chat.py \
  --output build/acquisition/prompts-chat/prompts.csv \
  --receipt build/acquisition/prompts-chat/receipt.json
```

The acquisition receipt is evidence for a local curation run; it is not itself a dataset release. The verified CSV still has to pass the importer, content-review process, and independent publication validator.

## Source import

### `import/prompts_chat.py`

Builds a staged or publication-ready candidate snapshot from the approved, pinned `prompts-chat` CSV.

The importer:

- does **not** download upstream content;
- reads `data/sources/prompts-chat/source.lock.json`;
- verifies the exact source byte count and Git blob SHA-1 before parsing;
- requires the exact five reviewed CSV columns;
- preserves prompt text without rewriting;
- generates stable SHA-256-based record IDs using the frozen `prompts-chat-v1` algorithm;
- preserves contributor metadata as provenance;
- validates each generated record against `schema/prompt.schema.json`;
- performs deterministic duplicate handling;
- holds heuristic content/privacy/security candidates for explicit review rather than silently rewriting them;
- writes deterministic JSONL shards;
- computes exact resource counts, bytes, and SHA-256 checksums;
- validates the generated manifest against `schema/manifest.schema.json`;
- refuses to overwrite an existing output directory;
- refuses `published` status while content-review candidates remain unresolved.

Install curation dependencies with:

```bash
python -m pip install -r scripts/requirements.txt
```

Example staging build:

```bash
python scripts/import/prompts_chat.py \
  --input build/acquisition/prompts-chat/prompts.csv \
  --output-dir build/prompts-chat-2026-08-23 \
  --retrieved-at 2026-08-23
```

Output is intentionally separated:

```text
build/prompts-chat-2026-08-23/
├── publish/
│   ├── manifest.yaml
│   └── part-*.jsonl
└── audit/
    ├── README.txt
    ├── review-report.json
    ├── review-decisions-applied.json
    └── review-queue.jsonl       # staging only; never publish blindly
```

Only files under `publish/` are candidates for promotion into the canonical dataset. `audit/review-queue.jsonl` may contain records intentionally held for content/privacy/security review and must not be copied into `data/`.

## Independent publication gate

### `validate_publication.py`

Validates the exact directory that is about to become a canonical source snapshot. This is deliberately separate from importers so a bug in an importer cannot make its own output authoritative merely by generating a manifest.

The validator checks:

- `manifest.yaml` against `schema/manifest.schema.json`;
- the source still exists exactly once in `sources/sources.yaml`;
- the source is still `approved` and `license.scope_verified: true`;
- manifest revision equals the registry's currently reviewed revision;
- manifest effective license equals the source registry license;
- every declared resource exists beneath the supplied source directory;
- resource path safety and canonical `data/sources/<source_id>/<name>` locations;
- exact resource byte counts and SHA-256 checksums;
- every JSONL line parses and validates against `schema/prompt.schema.json`;
- every record references the expected source and effective license;
- canonical IDs are unique across all shards;
- per-resource and manifest-level record counts reconcile;
- no undeclared `part-*.jsonl` shard is present.

Validate a staged candidate before promotion:

```bash
python scripts/validate_publication.py build/prompts-chat-2026-08-23/publish
```

Validate an already committed canonical source snapshot and require final publication state:

```bash
python scripts/validate_publication.py \
  data/sources/prompts-chat \
  --require-published
```

A `PASS` from this validator is a necessary technical gate, not a substitute for the human source/license/content review required by `docs/PUBLICATION_CHECKLIST.md`.

## Review decisions

The optional `--review-decisions` file for `prompts_chat.py` is a JSON object keyed by deterministic prompt record ID.

Minimal form:

```json
{
  "prompts-chat-<sha256>": "include",
  "prompts-chat-<another-sha256>": "exclude"
}
```

Documented form:

```json
{
  "prompts-chat-<sha256>": {
    "decision": "include",
    "reason": "Example address is synthetic and does not expose private data."
  }
}
```

Decisions for IDs that are not review candidates on the pinned input are rejected, preventing stale review files from being silently applied to another corpus state.

## Test coverage

Repository tests exercise the pinned acquisition safeguards, deterministic prompts.chat import primitives, and the independent publication validator. Coverage includes exact revision/path URL locking, byte/Git-blob verification, exclusive destination writes, multiline prompt preservation, stable field-sensitive IDs, prompt SHA-256 provenance, review heuristics, deterministic sharding, checksum tamper detection, duplicate-ID rejection, and the staging-vs-published gate.

With curation dependencies installed:

```bash
python -m unittest discover -s tests -p 'test_*.py'
```

Tests use synthetic fixture records. They are not dataset content and must not be promoted into `data/`.

## General design requirements

Import and maintenance tooling should:

- preserve source identifiers and upstream URLs;
- pin source revisions/snapshots when practical;
- record retrieval dates and hashes;
- validate normalized records against the canonical schema;
- reject or quarantine records with unresolved license/provenance state;
- avoid downloading or mirroring third-party media unless separately authorized;
- produce reproducible output;
- never require committed credentials or secrets;
- keep local review/quarantine material out of public dataset artifacts.

Derived search indexes, SQLite databases, Parquet exports, and caches should be reproducible from canonical tracked data and should not become the source of truth.
