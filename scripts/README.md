# Scripts

This directory is reserved for deterministic tooling used to ingest and maintain Open Prompt Archive.

Planned tooling areas:

```text
scripts/
├── import/
├── normalize/
├── validate/
├── deduplicate/
├── license_audit/
└── export/
```

## Design requirements

Import and maintenance tooling should:

- preserve source identifiers and upstream URLs;
- pin source revisions/snapshots when practical;
- record retrieval dates and hashes;
- validate normalized records against the canonical schema;
- reject or quarantine records with unresolved license/provenance state;
- avoid downloading or mirroring third-party media unless separately authorized;
- produce reproducible output;
- never require committed credentials or secrets.

Derived search indexes, SQLite databases, Parquet exports, and caches should be reproducible from canonical tracked data and should not become the source of truth.
