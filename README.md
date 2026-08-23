# Open Prompt Archive

> Open-source, provenance-first and license-aware AI prompt dataset infrastructure.

**Open Prompt Archive** curates redistributable AI prompts from verified public sources and normalizes them into machine-readable records with explicit provenance, licensing, attribution and integrity metadata.

The project is designed for **image generation, video generation, LLMs, AI agents, coding, audio, 3D and other generative-AI workflows**. It is intended to support local search, SQLite/FTS, Parquet, RAG, APIs, CLI tools and MCP integrations without losing the legal and technical provenance of the underlying data.

## Scope boundary

This repository is an archive of **third-party openly redistributable prompt sources**.

**Carnaverone Studio first-party prompts are intentionally not published in this repository.** They are outside the scope of Open Prompt Archive and should remain in separate first-party/private repositories or products.

Open Prompt Archive is also intentionally **not**:

- a blind web scrape;
- a dump of publicly visible prompts with unknown rights;
- a mirror of private, paywalled or access-controlled services;
- a place to silently relicense third-party content;
- an automatic mirror of third-party images, video or audio.

## Core principles

1. **Provenance first** — every imported record must remain traceable to a source.
2. **License-aware** — public availability is not treated as redistribution permission.
3. **No silent relicensing** — imported content keeps its upstream license and attribution obligations.
4. **Deterministic processing** — normalization and derived indexes should be reproducible.
5. **Deduplicate without erasing history** — identical prompt text may have multiple legitimate provenance records.
6. **Agent-readable by design** — repository policies, schemas and task-specific skills are explicit and machine-consumable.
7. **No fake verification** — `approved` and `verified: true` are evidence-backed states, not guesses.

## Data pipeline

```text
candidate source
      ↓
license + scope evidence
      ↓
provenance review
      ↓
source status
      ↓
approved source only
      ↓
import
      ↓
normalize
      ↓
validate
      ↓
deduplicate while preserving provenance
      ↓
canonical JSONL
      ↓
derived SQLite / FTS / Parquet / RAG indexes
```

## Repository structure

```text
open-prompt-archive/
├── README.md
├── AGENTS.md
├── CONTRIBUTING.md
├── LICENSE
├── NOTICE.md
├── .github/
│   ├── copilot-instructions.md
│   ├── instructions/
│   │   └── dataset.instructions.md
│   └── skills/
│       └── source-license-audit/
│           └── SKILL.md
├── data/
│   └── README.md
├── docs/
│   ├── LICENSING_POLICY.md
│   └── REPOSITORY_DISCOVERABILITY.md
├── schema/
│   └── prompt.schema.json
├── scripts/
│   └── README.md
└── sources/
    └── sources.yaml
```

## Canonical prompt record

Every normalized record should answer four questions:

1. What is the prompt?
2. Where did it come from?
3. Under what terms may it be redistributed?
4. Can its provenance be verified later?

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

The canonical schema is [`schema/prompt.schema.json`](schema/prompt.schema.json).

## Source approval states

| State | Meaning |
| --- | --- |
| `candidate` | Discovered but not reviewed. |
| `review` | License and provenance evidence are being checked. |
| `approved` | Redistribution basis and source scope have been verified for the intended import. |
| `quarantined` | A rights, provenance or integrity question remains unresolved. |
| `rejected` | Not suitable for the main archive. |

A GitHub license badge, public repository or downloadable file is **not** sufficient evidence by itself.

## Licensing model

This repository uses a **per-source / per-record licensing model**.

- Original software and tooling in this repository are licensed under the root [`LICENSE`](LICENSE).
- Imported prompt data retains its upstream license.
- Attribution requirements remain attached to the relevant source or record.
- Ambiguous, incompatible or unverifiable sources are excluded from the main dataset.
- Third-party media is not automatically mirrored.

See [`docs/LICENSING_POLICY.md`](docs/LICENSING_POLICY.md).

### Initial review allowlist

The following licenses may be considered after source-scope and provenance verification:

- `CC0-1.0`
- `CC-BY-4.0`
- `CC-BY-SA-4.0` when share-alike obligations can be preserved correctly
- `MIT`
- `Apache-2.0`
- `BSD-2-Clause`
- `BSD-3-Clause`
- clearly documented public-domain material

The following are excluded from the main archive by default:

- `UNKNOWN`
- `NOASSERTION`
- no license
- `All Rights Reserved`
- non-commercial-only terms such as `CC-BY-NC-*`
- custom terms that prohibit redistribution
- copied or aggregated material with unresolved third-party rights

## AI agent support

Open Prompt Archive is structured so coding and research agents can operate with less ambiguity:

- [`AGENTS.md`](AGENTS.md) defines repository-wide agent rules.
- [`.github/copilot-instructions.md`](.github/copilot-instructions.md) provides GitHub Copilot repository instructions.
- [`.github/instructions/dataset.instructions.md`](.github/instructions/dataset.instructions.md) applies stricter rules to dataset and source-registry changes.
- [`.github/skills/source-license-audit/SKILL.md`](.github/skills/source-license-audit/SKILL.md) provides a reusable GitHub Agent Skill for source/license auditing.

The goal is to make source review and dataset maintenance repeatable across human contributors, GitHub Copilot and other Agent Skills-compatible AI systems.

## Planned outputs

The canonical archive may generate:

- JSONL datasets;
- SQLite + FTS indexes;
- Parquet datasets;
- deterministic hashes/manifests;
- local CLI search;
- RAG indexes;
- API and MCP interfaces.

Derived artifacts must remain reproducible from canonical source data and must not weaken provenance or licensing metadata.

## Contributing

Contributions are welcome for:

- candidate open datasets;
- license/provenance evidence;
- source corrections;
- schema improvements;
- import and validation tooling;
- deterministic deduplication;
- search and indexing infrastructure.

Before proposing prompt data, read [`CONTRIBUTING.md`](CONTRIBUTING.md) and [`docs/LICENSING_POLICY.md`](docs/LICENSING_POLICY.md).

## Discoverability

The project intentionally uses descriptive terminology such as **AI prompt dataset**, **prompt engineering**, **generative AI prompts**, **image prompts**, **video prompts**, **LLM prompts**, **agent prompts**, **open data**, **provenance**, **prompt licensing**, **RAG** and **MCP** so that the repository remains understandable to both people and code-search systems without keyword stuffing.

Repository metadata and recommended GitHub topics are maintained in [`docs/REPOSITORY_DISCOVERABILITY.md`](docs/REPOSITORY_DISCOVERABILITY.md).

## Project status

**Bootstrap / source-audit phase.** Repository governance and machine-readable conventions are being established before large third-party imports begin.

No source should be considered approved merely because it has been discussed, linked or listed as a candidate.

## Maintainer

Open Prompt Archive is maintained by **Carnaverone Studio** as an open-source/open-data infrastructure project.

---

**Important:** Licensing and provenance information in this repository is maintained for dataset governance and does not constitute legal advice.
