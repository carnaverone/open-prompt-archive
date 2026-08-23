# Scripts

This directory contains deterministic curation tooling used to ingest and maintain Open Prompt Archive. Tooling is subordinate to the dataset policies and source-review decisions; it must never expand an approved source scope on its own.

## Current tooling

```text
scripts/
├── requirements.txt
└── import/
    └── prompts_chat.py
```

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

Install its curation dependencies with:

```bash
python -m pip install -r scripts/requirements.txt
```

Example staging build:

```bash
python scripts/import/prompts_chat.py \
  --input /path/to/prompts.csv \
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

## Review decisions

The optional `--review-decisions` file is a JSON object keyed by deterministic prompt record ID.

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
