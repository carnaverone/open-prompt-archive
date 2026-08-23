# Open Prompt Archive

> A curated open dataset of AI prompts with verified licensing, provenance, and attribution.

**Open Prompt Archive** is a public, source-driven archive for redistributable AI prompts. It collects prompt data from third-party sources only when the project can verify a credible redistribution basis and preserve the source, license, attribution, and provenance required to reuse that material responsibly.

The archive is intended to cover **image prompts, video prompts, LLM prompts, AI agent prompts, coding prompts, audio prompts, 3D prompts, and other generative-AI prompt formats** over time.

## Status

**Pre-release / curation bootstrap.**

The repository is establishing its dataset policies, source-review process, contribution workflow, and canonical schemas before publishing a large prompt corpus. A source is not considered approved merely because it is public, popular, or listed as a candidate.

No prompt-count, license status, model compatibility, or verification claim should be published unless it is backed by the repository data.

## Scope

Open Prompt Archive is for **third-party prompt collections that can be redistributed under verified terms**.

### In scope

- Prompt datasets with explicit redistribution rights.
- Openly licensed prompt repositories whose license scope actually covers the prompt content.
- Public-domain prompt collections with credible provenance.
- Source metadata, attribution, revision pins, and license evidence.
- Normalized machine-readable prompt records.
- Corrections to provenance, attribution, licensing, categorization, and data quality.

### Out of scope

- Carnaverone Studio first-party or proprietary prompt collections.
- Blind scraping of prompt websites or social platforms.
- Publicly visible prompts with unknown or ambiguous redistribution rights.
- Paywalled, private, leaked, access-controlled, or credential-gated material.
- Third-party images, video, or audio unless their redistribution rights are verified independently.
- Silent relicensing of upstream content.

**Carnaverone Studio prompts are intentionally not published in this repository.**

## Curation model

The project uses a **source-first** workflow:

```text
DISCOVER
   ↓
SOURCE PROPOSAL
   ↓
LICENSE + PROVENANCE REVIEW
   ↓
┌────────────┬─────────────┬──────────────┐
│ APPROVED   │ QUARANTINED │ REJECTED     │
└─────┬──────┴─────────────┴──────────────┘
      ↓
IMPORT
      ↓
NORMALIZE
      ↓
VALIDATE
      ↓
DEDUPLICATE WITHOUT LOSING PROVENANCE
      ↓
PUBLISH
```

A quarantined or rejected source may be documented at the metadata/review level, but its prompt corpus must not be redistributed by this repository while rights remain unresolved.

See:

- [`docs/LICENSING_POLICY.md`](docs/LICENSING_POLICY.md)
- [`docs/PROVENANCE_POLICY.md`](docs/PROVENANCE_POLICY.md)
- [`docs/SOURCE_REVIEW_PROCESS.md`](docs/SOURCE_REVIEW_PROCESS.md)
- [`docs/CONTENT_POLICY.md`](docs/CONTENT_POLICY.md)
- [`docs/TAKEDOWN_POLICY.md`](docs/TAKEDOWN_POLICY.md)

## Dataset record model

Each published prompt record must remain traceable to an approved source.

Example:

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
    "revision": "<commit-tag-or-snapshot>"
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

Canonical contracts:

- [`schema/prompt.schema.json`](schema/prompt.schema.json) — prompt records;
- [`schema/source.schema.json`](schema/source.schema.json) — source registry.

See [`docs/DATA_MODEL.md`](docs/DATA_MODEL.md) for the relationship between source-level review and record-level data.

## Licensing model

Open Prompt Archive is intentionally **multi-license at the data layer**.

- Repository-authored software, schemas, templates, and documentation are licensed under the root [`LICENSE`](LICENSE) unless a file states otherwise.
- Imported prompt data retains the upstream license recorded for its source or record.
- Attribution and share-alike obligations remain attached to imported material.
- A repository-level software license is never treated as proof that aggregated third-party prompts are covered by that license.
- Associated media is not mirrored by default.
- SPDX identifiers are used wherever practical; repository-authored files also carry REUSE-compatible metadata.

See [`NOTICE.md`](NOTICE.md) and [`docs/LICENSING_POLICY.md`](docs/LICENSING_POLICY.md).

## Contributions

Contributions are welcome, but the default contribution path is **source-first rather than prompt-dump-first**.

Good contributions include:

- proposing a clearly licensed prompt dataset or repository;
- supplying stronger license evidence for a candidate source;
- correcting attribution or provenance;
- reporting a duplicate or malformed record;
- reporting content that should be removed or reviewed;
- improving documentation or the dataset schema.

Do **not** submit a copied prompt dump merely because the material is publicly accessible.

Start with [`CONTRIBUTING.md`](CONTRIBUTING.md). GitHub issue forms are provided for source proposals, license/provenance corrections, data-quality reports, and removal/rights review.

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
├── data/                  # approved redistributable prompt data only
├── sources/
│   ├── sources.yaml       # source registry
│   └── reviews/           # human-readable source review records
├── schema/                # machine-readable dataset contracts
├── docs/                  # policies and curation documentation
└── .github/               # contribution forms and supporting agent/repo config
```

## Dataset card

The project maintains [`DATASET_CARD.md`](DATASET_CARD.md) as the canonical human-readable description of dataset scope, composition, provenance, licensing, limitations, curation, and intended use.

The card must distinguish clearly between **current published data** and **planned capabilities**.

## Governance

Open Prompt Archive uses lightweight maintainer-led governance. Maintainers are responsible for source approval, license/provenance review, dataset-policy decisions, corrections, and removals.

See [`GOVERNANCE.md`](GOVERNANCE.md).

## Citation

If you use Open Prompt Archive in research, evaluation, tooling, or another dataset, use the repository citation metadata in [`CITATION.cff`](CITATION.cff). Individual upstream attribution requirements still apply to the prompt records you reuse.

## Responsible reuse

An open license on prompt text does not automatically resolve every other legal or ethical question. Model terms, trademarks, privacy, publicity rights, personal data, and rights in linked media may impose separate constraints.

Open Prompt Archive records provenance and licensing evidence for dataset governance; it does not provide legal advice.

## Maintainer

Maintained by **Carnaverone Studio**.
