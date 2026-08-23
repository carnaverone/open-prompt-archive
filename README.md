# Open Prompt Archive

> A curated open dataset of AI prompts with verified licensing, provenance, and attribution.

**Open Prompt Archive** is a public, source-driven archive for redistributable AI prompts. Third-party prompt data enters the archive only when its redistribution basis can be verified and its source, license, attribution, scope, and provenance can be preserved.

The project is designed to cover **image prompts, video prompts, LLM prompts, AI agent prompts, coding prompts, audio prompts, 3D prompts, and other generative-AI prompt formats** without turning public availability into an assumption of permission.

## Status

**Pre-release / active curation.**

Source review is operational. No large versioned prompt corpus has been released yet. Source approval and dataset publication are deliberately separate gates: an approved source must still pass deterministic normalization, content review, schema validation, manifest generation, exact counting, and artifact checksum verification before publication.

The first `prompts.chat` importer and acquisition lock now exist, but no prompt count or dataset release is claimed until the complete pinned upstream file can be processed and the resulting artifacts pass the publication checklist.

No prompt count, model-compatibility claim, license claim, or verification status should be published unless repository evidence supports it.

## Reviewed sources

| Source | Status | Effective / claimed license | Approved archive scope |
|---|---|---|---|
| [prompts.chat](sources/reviews/prompts-chat.md) | **Approved** | `CC0-1.0` | Prompt text/data only |
| [DiffusionDB](sources/reviews/diffusiondb.md) | **Approved** | `CC0-1.0` | Prompt text + selected generation metadata; media excluded |
| [BigScience PromptSource / P3](sources/reviews/bigscience-promptsource.md) | **Approved** | `Apache-2.0` | Prompt templates + prompt-specific metadata; underlying datasets excluded |
| [Wuyoscar GPT-Image2-Skill](sources/reviews/wuyoscar-gpt-image2-skill.md) | **Review reopened** | `MIT` repository license | No prompt publication while `Curated` / `Original` provenance semantics are re-verified |
| [freestylefly / awesome-gpt-image-2](sources/reviews/freestylefly-awesome-gpt-image-2.md) | **Quarantined** | `MIT` repository license | No bulk import; external/community provenance unresolved |
| [YouMind — Nano Banana Pro](sources/reviews/youmind-nano-banana-pro.md) | **Quarantined** | `CC-BY-4.0` claimed upstream | No bulk import; license scope unresolved |
| [YouMind — GPT Image 2](sources/reviews/youmind-gpt-image-2.md) | **Quarantined** | `CC-BY-4.0` claimed upstream | No bulk import; license scope unresolved |
| [YouMind — Seedance 2](sources/reviews/youmind-seedance-2.md) | **Quarantined** | `CC-BY-4.0` claimed upstream | No bulk import; license scope unresolved |

The canonical machine-readable registry is [`sources/sources.yaml`](sources/sources.yaml).

`Review` and `Quarantined` are Open Prompt Archive curation states, **not allegations that an upstream project is unlawful or that its repository license is invalid**. They describe whether this archive currently has enough evidence to redistribute the intended prompt scope under its provenance standard.

## Scope

Open Prompt Archive is for **third-party prompt collections that can be redistributed under verified terms**.

### In scope

- Prompt datasets with explicit redistribution rights.
- Openly licensed repositories whose license scope actually covers the prompt content being imported.
- Public-domain prompt collections with credible provenance.
- Evidence-backed subsets of mixed-origin repositories when eligibility can be determined reliably at record level.
- Source metadata, attribution, revision pins, license evidence, and review records.
- Normalized machine-readable prompt records.
- Licensing, provenance, attribution, and data-quality corrections.

### Out of scope

- Carnaverone Studio first-party, private, or proprietary prompt collections.
- Blind scraping of prompt websites or social platforms.
- Publicly visible prompts with unknown or ambiguous redistribution rights.
- Paywalled, private, leaked, access-controlled, or credential-gated material.
- Third-party images, video, or audio unless their rights are independently reviewed.
- Silent relicensing of upstream material.

**Carnaverone Studio prompts are intentionally not published in this repository.**

## Curation workflow

```text
DISCOVER
   ↓
SOURCE PROPOSAL
   ↓
LICENSE + PROVENANCE REVIEW
   ↓
┌────────────┬──────────┬─────────────┬──────────────┐
│ APPROVED   │ REVIEW   │ QUARANTINED │ REJECTED     │
└─────┬──────┴──────────┴─────────────┴──────────────┘
      ↓
SOURCE-SPECIFIC PUBLICATION CONTRACT
      ↓
NORMALIZE WITHOUT REWRITING PROMPTS
      ↓
CONTENT + PRIVACY REVIEW
      ↓
SCHEMA VALIDATION
      ↓
MANIFEST + COUNTS + SHA-256
      ↓
VERSIONED PUBLICATION
```

Only `approved` source scopes proceed downward into prompt publication. A source in `review`, `quarantined`, or `rejected` state may remain documented at metadata/review level, but its unapproved prompt corpus must not be committed to `data/` or attached to a release.

## Core policies

- [`docs/LICENSING_POLICY.md`](docs/LICENSING_POLICY.md)
- [`docs/PROVENANCE_POLICY.md`](docs/PROVENANCE_POLICY.md)
- [`docs/SOURCE_REVIEW_PROCESS.md`](docs/SOURCE_REVIEW_PROCESS.md)
- [`docs/CONTENT_POLICY.md`](docs/CONTENT_POLICY.md)
- [`docs/TAKEDOWN_POLICY.md`](docs/TAKEDOWN_POLICY.md)
- [`docs/DISTRIBUTION_POLICY.md`](docs/DISTRIBUTION_POLICY.md)
- [`docs/PUBLICATION_CHECKLIST.md`](docs/PUBLICATION_CHECKLIST.md)

## Canonical data organization

Prompt data and source-specific publication/review metadata are partitioned **by source** so licensing and provenance boundaries stay auditable.

```text
data/
└── sources/
    ├── prompts-chat/
    ├── diffusiondb/
    ├── bigscience-promptsource/
    └── wuyoscar-gpt-image2-skill/   # review hold; metadata only
```

Approved source directories begin with a publication contract describing the exact reviewed revision, eligible records, field mapping, exclusions, license handling, and publication gate. A directory for a source whose review has been reopened may instead contain a hold notice and must not contain approved prompt shards.

Current source-specific notes/contracts:

- [`data/sources/prompts-chat/README.md`](data/sources/prompts-chat/README.md)
- [`data/sources/diffusiondb/README.md`](data/sources/diffusiondb/README.md)
- [`data/sources/bigscience-promptsource/README.md`](data/sources/bigscience-promptsource/README.md)
- [`data/sources/wuyoscar-gpt-image2-skill/README.md`](data/sources/wuyoscar-gpt-image2-skill/README.md)

Model/modality views and formats such as Parquet, SQLite/FTS, or search indexes may later be generated as **derived distributions**. They do not replace the canonical source/provenance model.

## First deterministic importer

The first source-specific importer is [`scripts/import/prompts_chat.py`](scripts/import/prompts_chat.py).

It verifies the pinned `prompts.chat` Git blob before parsing, preserves prompt text, freezes a deterministic SHA-256 record-ID algorithm, validates generated records, separates local audit/review material from publication candidates, computes artifact counts/checksums, and refuses `published` status while review candidates remain unresolved.

The exact upstream acquisition lock is [`data/sources/prompts-chat/source.lock.json`](data/sources/prompts-chat/source.lock.json). Curation tooling is documented in [`scripts/README.md`](scripts/README.md).

## Canonical record model

Every published record is traceable to an approved source and carries its effective license.

```json
{
  "id": "example-source-000001",
  "prompt": "A cinematic portrait with soft volumetric light...",
  "type": "image",
  "models": ["example-model"],
  "tags": ["portrait", "cinematic"],
  "source": {
    "source_id": "example-source",
    "name": "Example Source",
    "url": "https://example.org/source",
    "author": "Example Author",
    "revision": "<reviewed-revision>"
  },
  "license": {
    "spdx": "CC-BY-4.0",
    "attribution_required": true,
    "attribution": "Example Author / Example Source",
    "scope_verified": true
  },
  "provenance": {
    "retrieved_at": "2026-08-23",
    "sha256": "<sha256-integrity-hash>",
    "verified": true,
    "modified": false
  }
}
```

Machine-readable contracts:

- [`schema/prompt.schema.json`](schema/prompt.schema.json) — published prompt records;
- [`schema/source.schema.json`](schema/source.schema.json) — source registry;
- [`schema/manifest.schema.json`](schema/manifest.schema.json) — staged/published source snapshot manifests.

See [`docs/DATA_MODEL.md`](docs/DATA_MODEL.md).

## Licensing model

Open Prompt Archive is intentionally **multi-license at the data layer**.

- Repository-authored software, schemas, templates, and documentation use the root [`LICENSE`](LICENSE) unless stated otherwise.
- Imported prompt data retains its effective upstream license.
- Attribution, notice, and share-alike obligations remain attached to the relevant imported records.
- A software license on an aggregator is not automatically treated as a license for externally sourced prompt content.
- Record-level or subset-level approval is preferred when a mixed-origin source exposes a reliable provenance boundary.
- Labels such as `curated`, `edited`, or `rewritten` do not by themselves prove original authorship or relicensing authority.
- Associated media is excluded by default.
- SPDX identifiers are used where practical; repository-authored files also use REUSE-compatible metadata.

See [`NOTICE.md`](NOTICE.md) and [`docs/LICENSING_POLICY.md`](docs/LICENSING_POLICY.md).

## Contributions

Contributions are welcome, but the project is **source-first rather than prompt-dump-first**.

Useful contributions include:

- proposing a clearly licensed prompt source;
- providing stronger license evidence for a candidate, review, or quarantined source;
- identifying a mechanically verifiable open subset of a mixed-origin source;
- correcting attribution or provenance;
- reporting malformed/duplicate records;
- requesting removal or rights review;
- improving dataset documentation or schemas.

Do **not** submit a copied prompt dump merely because it is publicly accessible.

Start with [`CONTRIBUTING.md`](CONTRIBUTING.md). Structured GitHub issue forms are available for source proposals, licensing/provenance corrections, data-quality reports, and removal/rights review.

## Distribution

Small, reviewable prompt datasets may be stored in Git as deterministic JSONL shards. Very large source snapshots keep manifests, reviews, checksums, and compact metadata in Git while immutable prompt-only artifacts are published through versioned GitHub Releases.

This keeps the repository useful to humans, GitHub search, and AI tooling without turning every clone into a multi-gigabyte data transfer.

See [`docs/DISTRIBUTION_POLICY.md`](docs/DISTRIBUTION_POLICY.md).

## Repository structure

```text
open-prompt-archive/
├── README.md
├── DATASET_CARD.md
├── CITATION.cff
├── CONTRIBUTING.md
├── CODE_OF_CONDUCT.md
├── GOVERNANCE.md
├── SECURITY.md
├── CHANGELOG.md
├── LICENSE
├── LICENSES/
├── NOTICE.md
├── REUSE.toml
│
├── data/
│   └── sources/           # source-partitioned publication/review areas
├── sources/
│   ├── sources.yaml       # canonical review registry
│   └── reviews/           # human-readable evidence and decisions
├── schema/                # prompt/source/manifest contracts
├── scripts/               # deterministic curation tooling
├── tests/                 # curation contract tests
├── docs/                  # curation and dataset policies
└── .github/               # contribution forms and repository guidance
```

## Dataset card and citation

[`DATASET_CARD.md`](DATASET_CARD.md) is the canonical human-readable description of dataset scope, composition, provenance, licensing, limitations, curation, and intended use.

For research, evaluation, tooling, or downstream datasets, use [`CITATION.cff`](CITATION.cff). Individual upstream attribution obligations still apply to the records reused.

## Governance and responsible reuse

Open Prompt Archive uses lightweight maintainer-led governance. Maintainers are responsible for evidence review, source approval, scope decisions, corrections, and removals. See [`GOVERNANCE.md`](GOVERNANCE.md).

An open license on prompt text does not automatically resolve model terms, trademarks, privacy, publicity rights, personal data, or rights in linked media. Open Prompt Archive records licensing/provenance evidence for dataset governance; it does not provide legal advice.

## Maintainer

Maintained by **Carnaverone Studio**.
