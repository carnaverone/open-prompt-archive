# Open Prompt Archive

> A provenance-first, license-aware archive of reusable AI prompts.

Open Prompt Archive is a public dataset and tooling project for collecting, normalizing, deduplicating, and indexing AI prompts that can be redistributed under clearly verified licenses.

The project is intentionally **not** a blind scrape or a dump of prompts copied from the web. Every imported record is expected to preserve its source, license, attribution requirements, and provenance metadata.

## Goals

- Build a reusable archive for image, video, LLM, agent, audio, 3D, coding, and other generative-AI prompts.
- Accept only content with a sufficiently clear redistribution basis.
- Preserve source attribution and upstream license information per record.
- Normalize heterogeneous prompt collections into a common schema.
- Detect duplicates without destroying provenance.
- Produce machine-friendly datasets suitable for local search, SQLite/FTS, RAG, CLI tools, APIs, and MCP integrations.
- Keep the archive auditable and useful for both humans and automated agents.

## Non-goals

- Scraping private, paywalled, access-controlled, or rate-limited services in ways that violate their terms.
- Treating a repository-level software license as proof that every third-party prompt or image inside that repository is redistributable.
- Rehosting third-party preview images unless their rights are independently verified.
- Removing attribution or provenance from imported content.

## Repository layout

```text
open-prompt-archive/
├── README.md
├── LICENSE
├── NOTICE.md
├── CONTRIBUTING.md
├── docs/
│   └── LICENSING_POLICY.md
├── schema/
│   └── prompt.schema.json
├── sources/
│   └── sources.yaml
├── data/
│   └── README.md
└── scripts/
    └── README.md
```

As the project grows, normalized datasets may be published as JSONL and derived indexes may be generated as SQLite/FTS, Parquet, or other distribution formats.

## Canonical record model

Each imported prompt should carry enough metadata to answer four questions:

1. **What is the prompt?**
2. **Where did it come from?**
3. **Under what terms may it be redistributed?**
4. **Can we verify that provenance later?**

Example:

```json
{
  "id": "example-source-000001",
  "prompt": "A cinematic portrait with soft volumetric light...",
  "type": "image",
  "models": ["example-model"],
  "tags": ["portrait", "cinematic"],
  "source": {
    "name": "Example Source",
    "url": "https://example.org/source",
    "author": "Example Author"
  },
  "license": {
    "spdx": "CC-BY-4.0",
    "attribution_required": true
  },
  "provenance": {
    "retrieved_at": "2026-08-23",
    "sha256": "<sha256-of-canonical-record-or-source-content>",
    "verified": true,
    "modified": false
  }
}
```

The canonical JSON Schema lives in [`schema/prompt.schema.json`](schema/prompt.schema.json).

## Licensing model

This repository uses a **license-aware, per-source/per-record model**.

- Software and original tooling in this repository are licensed under the root [`LICENSE`](LICENSE).
- Imported prompts **retain their upstream license** and attribution requirements.
- The root software license does **not** relicense imported third-party prompt content.
- Sources with missing, ambiguous, incompatible, or unverifiable redistribution terms are not accepted into the main dataset.
- External preview images are not automatically mirrored.

See [`docs/LICENSING_POLICY.md`](docs/LICENSING_POLICY.md) for the acceptance policy.

## Initial acceptance policy

The main archive is intended for clearly reusable material such as content distributed under licenses including:

- CC0-1.0
- CC-BY-4.0
- CC-BY-SA-4.0, when share-alike obligations can be preserved correctly
- MIT
- Apache-2.0
- BSD-2-Clause
- BSD-3-Clause
- clearly documented public-domain material

A license appearing in this list is **not sufficient by itself**. The source must also have credible provenance and authority to license the content.

Content marked `UNKNOWN`, `NOASSERTION`, `All Rights Reserved`, non-commercial-only, source-unclear, or otherwise legally ambiguous is excluded from the main archive until reviewed.

## Data quality principles

- **Provenance first:** never discard the original source URL or source identifier.
- **No silent relicensing:** imported content keeps its actual license.
- **Deterministic normalization:** transformations should be reproducible.
- **Hashable records:** canonicalized records should support integrity checks.
- **Deduplicate carefully:** identical prompt text from different legitimate sources may share content while retaining multiple provenance records.
- **No fake verification:** `verified: true` means the relevant source and license evidence were actually checked.

## Status

**Bootstrap phase.** The repository structure and policies are being established before third-party datasets are imported. No source should be considered approved merely because it has been discussed or listed as a candidate.

## Contributing

Contributions are welcome, particularly:

- candidate open prompt datasets;
- provenance corrections;
- license evidence;
- normalization and deduplication tooling;
- schema improvements;
- search/indexing tools.

Before contributing prompt data, read [`CONTRIBUTING.md`](CONTRIBUTING.md) and [`docs/LICENSING_POLICY.md`](docs/LICENSING_POLICY.md).

## Project

Open Prompt Archive is maintained by **Carnaverone Studio** as an open-source/open-data infrastructure project.

---

**Important:** This project documents licensing and provenance information for dataset governance. It is not legal advice.