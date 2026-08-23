# Dataset Distribution Policy

Open Prompt Archive is a GitHub-native curation project, but the repository must remain practical to clone, review, index, and contribute to as the corpus grows.

This policy separates **Git-tracked canonical metadata** from **large immutable dataset snapshots**.

## Goals

- Keep the Git repository useful to humans, GitHub search, code search, and AI/agent tooling.
- Avoid turning normal clones into multi-gigabyte data transfers.
- Preserve reproducibility through pinned source revisions, manifests, and checksums.
- Publish large prompt corpora without sacrificing provenance or license metadata.
- Keep dataset releases immutable and auditable.

## What belongs in normal Git history

The repository should track:

- policies and governance documentation;
- `sources/sources.yaml`;
- source review records;
- JSON Schemas;
- dataset manifests and indexes;
- small and medium prompt-data shards when their size remains Git-friendly;
- checksums and release metadata;
- compact samples used to document the canonical record format.

Large upstream images, video, audio, model files, archives, caches, and transient generated indexes do not belong in normal Git history.

## Canonical text shard format

When prompt data is stored directly in Git, prefer deterministic **JSON Lines (`.jsonl`)** grouped by approved source.

Recommended layout:

```text
data/
└── sources/
    └── <source-id>/
        ├── manifest.yaml
        ├── part-00000.jsonl
        ├── part-00001.jsonl
        └── ...
```

Each JSONL record must validate against `schema/prompt.schema.json`.

### Internal shard-size target

For reviewability and clone health, Open Prompt Archive should target prompt-text shards of roughly **10 MiB or less** when practical.

This is a project-level engineering target, not a GitHub platform limit. Shards may be larger when justified, but normal Git objects should remain comfortably below GitHub's 100 MiB per-file ceiling.

## Large datasets

A source such as DiffusionDB may contain millions of unique prompts. Replaying the entire upstream dataset directly into Git history would create unnecessary repository growth.

For large snapshots, use:

1. a Git-tracked manifest;
2. deterministic source/revision metadata;
3. generated prompt-only snapshot assets;
4. cryptographic checksums;
5. a tagged GitHub Release for the published snapshot.

GitHub currently permits release assets under **2 GiB per file** and up to 1,000 assets per release. Large snapshot files should therefore be split below that platform ceiling and preferably much smaller for practical reuse.

Release assets may use formats such as:

- `.jsonl.gz` for transparent streaming/reprocessing;
- `.parquet` for analytical workflows;
- `.csv.gz` only when the source schema is naturally tabular and quoting can be preserved reliably.

The canonical semantic model remains the JSON Schema and source manifest, not a particular derived storage engine.

## Git LFS

Git LFS is not the default distribution mechanism for prompt text.

Reasons:

- it adds a separate quota and client workflow;
- users without Git LFS receive pointer files rather than normal dataset content;
- immutable release snapshots are a better fit for very large generated dataset artifacts.

Git LFS may be adopted later for a narrowly justified asset class, but only through an explicit governance decision.

## Source manifest requirements

Every imported source directory or released large snapshot must have a manifest containing at least:

- Open Prompt Archive source ID;
- canonical upstream URL;
- reviewed upstream revision/snapshot;
- effective prompt-data license;
- license evidence URL;
- approved import scope;
- retrieval/import date;
- record count;
- excluded-field policy;
- normalization version;
- shard filenames/resources;
- SHA-256 checksums;
- known filtering decisions;
- link to the human-readable source review.

Counts and checksums must be generated from actual published artifacts, not estimated manually.

## Source-specific publication strategy

### prompts.chat

This source is small enough that a normalized Git-tracked JSONL representation may be appropriate after the first deterministic import is prepared and validated.

### DiffusionDB

Open Prompt Archive must **not** mirror DiffusionDB's multi-terabyte image corpus.

The approved scope is prompt text and selected prompt-generation metadata. A prompt-only export should be published as a versioned large-dataset snapshot, with Git tracking only its manifest, checksums, source revision, and compact samples/indexes.

### Quarantined sources

No prompt corpus, Git shard, release asset, or other redistributed dataset artifact may be created from a quarantined source. Metadata and review evidence only are allowed until the source is approved.

## Release versioning

Dataset releases should use explicit dataset versions once prompt records are actually published, for example:

```text
v0.1.0-dataset
v0.2.0-dataset
```

A release should document:

- source additions/removals;
- source revision changes;
- licensing/provenance decision changes;
- record counts by source/modality/license;
- normalization/schema version;
- removals and corrections;
- SHA-256 checksums for release assets.

## Reproducibility

A published snapshot is reproducible only when a downstream user can determine:

1. exactly which upstream source revision was reviewed;
2. exactly what scope was approved;
3. exactly what transformations and filters were applied;
4. exactly which artifact was published;
5. whether that artifact matches its recorded checksum.

## Platform constraints

GitHub platform limits and billing rules may change. Before publishing unusually large artifacts, maintainers should re-check the current official GitHub documentation rather than relying on historical limits recorded in this repository.

---

This policy governs distribution architecture. It does not override licensing, provenance, content, privacy, or takedown requirements elsewhere in the repository.
