# Data Model

Open Prompt Archive separates **source-level review** from **record-level prompt data**.

This separation is intentional: a prompt record is publishable only because it can be traced to a reviewed source whose redistribution basis is documented.

## 1. Source registry

Canonical file: [`sources/sources.yaml`](../sources/sources.yaml)

Schema: [`schema/source.schema.json`](../schema/source.schema.json)

A source entry represents an upstream dataset, repository, project, or other canonical collection.

Important fields include:

- `source_id` — stable internal identifier;
- `canonical_url` — preferred upstream source location;
- `owner` — upstream owner or maintainer;
- `status` — candidate/review/approved/quarantined/rejected;
- `license.spdx` — SPDX identifier when available;
- `license.evidence_url` — direct licensing evidence;
- `license.scope_verified` — whether the evidence was checked against the prompt content;
- `scope` — exact reviewed/approved import scope;
- `reviewed_revision` — revision pin where practical;
- `media_mirroring` — independent media-rights decision.

## 2. Prompt records

Schema: [`schema/prompt.schema.json`](../schema/prompt.schema.json)

A prompt record represents one normalized reusable prompt and its metadata.

Every record must reference an approved `source_id`.

Core fields:

- `id` — stable record identifier;
- `prompt` — prompt text;
- `type` — modality/use class;
- `models` — upstream-declared or reviewed model associations;
- `tags` — normalized descriptive metadata;
- `source` — record-level source reference and upstream identifiers;
- `license` — effective record license/attribution metadata;
- `provenance` — retrieval, verification, integrity, and modification state;
- `media` — external or independently approved associated-media metadata.

## 3. Source versus record licensing

A source-level approval establishes that some defined content scope may be imported. Record-level licensing preserves the effective license and attribution that apply to each published prompt.

This allows the archive to handle sources where:

- all prompts share one license;
- different records have different authors;
- attribution varies by record;
- only part of a larger repository is actually covered by an open license.

## 4. Identifiers

Identifiers should be stable and deterministic where practical.

Recommended pattern:

```text
<source_id>-<upstream_or_stable_record_id>
```

Do not reuse an identifier for materially different content.

## 5. Dates

Use ISO 8601 calendar dates (`YYYY-MM-DD`) for source discovery/review and prompt retrieval metadata unless a schema explicitly requires a more precise timestamp.

## 6. URLs

Prefer canonical HTTPS URLs.

When both a source-level URL and item-specific URL exist, retain both through source and record metadata rather than replacing one with the other.

## 7. Hashes

Use SHA-256 when integrity hashes are recorded.

A hash identifies the reviewed/imported representation; it does not prove authorship, originality, or license validity.

## 8. Deduplication

Prompt text may be identical across sources. The data model must preserve provenance even when content is deduplicated for indexing or distribution.

The canonical archive should never lose the ability to reconstruct which approved source(s) supplied a given prompt.

## 9. Associated media

Media metadata is separate from prompt-text rights. A prompt record may link to external media without implying permission to mirror or redistribute that media.

`mirrored: true` should be used only when the media itself has been independently reviewed for redistribution.

## 10. Derived formats

JSONL, Parquet, SQLite/FTS, search indexes, embeddings, or other derived representations may be produced later, but they must be reproducible from canonical data and must not discard source/license metadata.
