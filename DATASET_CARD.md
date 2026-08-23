# Open Prompt Archive — Dataset Card

## Dataset summary

**Open Prompt Archive** is a curated, multi-source dataset of AI prompts that may be redistributed under verified terms. Its distinguishing feature is not prompt volume; it is the preservation of **source provenance, license evidence, attribution obligations, approved scope, and review status** for each source and published record.

The dataset is intended to support prompt research, search, retrieval, curation, benchmarking, and downstream tooling while keeping licensing and provenance auditable.

## Current status

**Dataset v0.1.0 / active curation.**

The first published source snapshot is `prompts-chat` v0.1.0:

- 2,134 canonical records;
- upstream revision `25cb43d6e61974e66f3650cbc5a65482bc592552`;
- effective license `CC0-1.0`;
- normalization `prompts-chat-v1`;
- one 7,736,751-byte JSONL shard;
- SHA-256 `ba8377b874c621e44d8c9b321c1ef1f95d7565867186b5e5fb8c2f908402a77c`;
- all 10 heuristic review candidates explicitly resolved;
- 1,072 contributor email identifiers omitted from public metadata across 1,069 records.

The source-review system remains active for additional sources. A source being `approved` does **not** mean its records are already published. Publication additionally requires source-specific mapping, deterministic identifiers, content/privacy review, schema validation, exact record counts, manifests, and artifact checksums.

Published counts are derived from actual archive artifacts rather than upstream marketing claims or repository descriptions.

## Reviewed source composition

Current source decisions are maintained in [`sources/sources.yaml`](sources/sources.yaml) and explained under [`sources/reviews/`](sources/reviews/).

For dataset v0.1.0 and the current source-review state:

- **prompts.chat** — approved for prompt text/data under `CC0-1.0`;
- **DiffusionDB** — approved for prompt text and selected prompt-generation metadata under `CC0-1.0`, with media excluded;
- **BigScience PromptSource / P3** — approved for prompt-template definitions and prompt-specific metadata under `Apache-2.0`, with underlying datasets and rendered examples excluded;
- **Wuyoscar GPT-Image2-Skill** — review reopened; no prompt records are currently approved for publication while the `Curated` / `Original` provenance boundary is re-verified;
- **freestylefly / awesome-gpt-image-2** — quarantined for bulk import because repository-level MIT licensing does not resolve the project's documented external/community provenance;
- three reviewed **YouMind OpenLab** prompt collections — quarantined for bulk import pending stronger evidence that the claimed repository license covers the externally collected prompt corpus.

`Quarantined` is an internal Open Prompt Archive curation state. It is not a legal finding against an upstream project.

## Dataset scope

Planned prompt modalities include:

- image generation;
- video generation;
- large language models;
- AI agents;
- coding;
- audio and speech;
- 3D and scene generation;
- other generative-AI workflows where reusable prompt representation is meaningful.

The dataset is source-driven and model-agnostic. Model names may be recorded as provenance or compatibility metadata when supported by the source, but do not imply endorsement, guaranteed compatibility, or affiliation.

## Data sources

Data may enter the archive only from sources that complete the review process documented in [`docs/SOURCE_REVIEW_PROCESS.md`](docs/SOURCE_REVIEW_PROCESS.md).

Each source record identifies, where applicable:

- canonical source URL;
- upstream owner/maintainer;
- source type;
- exact reviewed revision, tag, commit, or snapshot;
- discovery/review date;
- license identifier;
- direct license evidence;
- whether license scope was actually verified;
- attribution requirements;
- approved or reviewed import scope;
- review status;
- media-mirroring decision;
- human-readable review file.

The canonical source registry is [`sources/sources.yaml`](sources/sources.yaml).

## Data collection and curation

The archive does not treat public accessibility as redistribution permission.

The curation pipeline is:

1. discover or receive a source proposal;
2. identify the canonical source and upstream owner;
3. collect license and provenance evidence;
4. verify that the claimed license actually covers the content intended for import;
5. check for third-party aggregation or conflicting rights signals;
6. define the exact eligible scope — which may be a restricted subset rather than the whole source;
7. approve, quarantine, or reject the source/scope;
8. write a source-specific publication contract;
9. import only records inside the approved scope;
10. normalize without silently changing prompt meaning;
11. apply content/privacy review;
12. validate canonical records and manifests;
13. generate exact counts and SHA-256 checksums;
14. publish through the appropriate Git/release distribution path.

See [`docs/PUBLICATION_CHECKLIST.md`](docs/PUBLICATION_CHECKLIST.md).

## Canonical organization

Published data is source-partitioned:

```text
data/
└── sources/
    └── <source-id>/
        ├── README.md
        ├── manifest.yaml
        └── part-*.jsonl
```

For very large datasets, only the source publication contract, manifest, checksums, and compact metadata may live in ordinary Git history; immutable prompt-only snapshots may be distributed as versioned release assets.

See [`docs/DISTRIBUTION_POLICY.md`](docs/DISTRIBUTION_POLICY.md).

## Licensing

Open Prompt Archive is **multi-license at the data layer**.

Imported prompts retain their effective upstream license and attribution/notice obligations. The repository's root software/documentation license does not relicense imported prompt content.

A source is not approved solely because its repository has a license file. Reviewers verify that the license scope covers the actual prompt content intended for import, especially when a source aggregates material from websites, social networks, blogs, forums, or other creators.

Mixed-origin repositories may receive a **restricted-subset approval** when a reliable, evidence-backed record-level rule separates repository-original/open material from externally sourced material.

See [`docs/LICENSING_POLICY.md`](docs/LICENSING_POLICY.md).

## Provenance

Every published prompt remains traceable to an approved source entry and reviewed source revision. Provenance metadata should preserve stable identifiers, source URLs, retrieval dates, integrity hashes where practical, modification state, and attribution data.

When identical prompt text appears in multiple verified sources, deduplication must not erase distinct provenance or licensing claims.

See [`docs/PROVENANCE_POLICY.md`](docs/PROVENANCE_POLICY.md).

## Prompt fidelity

Open Prompt Archive is an archive, not an automatic prompt rewriting service.

During ingestion, prompt text must not be silently:

- rewritten;
- summarized;
- translated;
- "improved";
- optimized for another model.

Transport-only normalization is allowed when deterministic and semantics-preserving. Semantic modifications require explicit modification metadata and compatible license handling.

## Personal data and sensitive content

Prompt text can contain names, handles, personal information, or references to real people even when openly licensed. Open licensing does not remove privacy, publicity, or safety concerns.

Records may therefore be excluded, redacted only when policy and provenance allow it, or removed under the content/takedown process even when a source license otherwise permits redistribution.

The archive does not intentionally collect credentials, private messages, leaked material, private datasets, or access-controlled content.

## Associated media

Prompt licensing does not automatically license linked or accompanying images, video, audio, likenesses, trademarks, or other media.

Default policy:

- approved prompt text and metadata may be archived;
- external preview URLs may be retained when useful and lawful;
- third-party media is not mirrored unless rights are independently reviewed and the source registry explicitly permits mirroring.

Current approved sources use `media_mirroring: not-allowed` for their initial archive scope.

## Intended uses

Potential uses include:

- prompt search and retrieval;
- prompt-engineering research;
- comparative analysis across prompt families or modalities;
- dataset studies;
- quality and provenance evaluation;
- taxonomy/classification work;
- reproducible local indexes and retrieval systems;
- educational exploration of openly redistributable prompt patterns.

## Out-of-scope uses and limitations

Open Prompt Archive does not guarantee that:

- a prompt will work on every model;
- an upstream model/provider permits every downstream use;
- prompt text is factually correct, safe, unbiased, or high quality;
- an open prompt license resolves trademark, privacy, publicity, or model-provider terms;
- every historical source URL will remain available indefinitely;
- an `approved` source means every file or asset in that repository is approved.

Users remain responsible for complying with licenses and terms applicable to the records and systems they use.

## Dataset quality dimensions

Quality is evaluated across:

- provenance completeness;
- license-scope confidence;
- attribution completeness;
- source/revision stability;
- schema validity;
- prompt fidelity;
- deterministic identifiers;
- duplicate handling;
- content/privacy filtering;
- artifact integrity;
- metadata consistency.

Raw corpus size is not treated as a substitute for quality.

## Excluded data

The main dataset excludes by default:

- unknown or ambiguous redistribution rights;
- all-rights-reserved material without another permission basis;
- non-commercial-only sources unless a separate clearly labeled collection is explicitly established in the future;
- private, paywalled, leaked, or access-controlled material;
- copied third-party aggregations whose original rights cannot be established;
- records outside a source's approved subset;
- unreviewed associated media;
- Carnaverone Studio first-party or proprietary prompt collections.

## Corrections and removals

Credible licensing, attribution, privacy, or provenance disputes trigger review. Disputed prompt content may be removed from distribution while metadata necessary to document the correction history is retained.

See [`docs/TAKEDOWN_POLICY.md`](docs/TAKEDOWN_POLICY.md).

## Versioning

The dataset uses explicit versions for published prompt snapshots. Source revisions are pinned independently from archive release versions.

A versioned release should identify source revisions, record counts, schema/normalization version, material license/provenance changes, and SHA-256 checksums for distributed artifacts.

## Citation

Use [`CITATION.cff`](CITATION.cff) to cite the archive itself. Downstream users must also preserve record/source-specific attribution and notices required by upstream licenses.

## Maintainer

**Carnaverone Studio**
