# Open Prompt Archive — Dataset Card

## Dataset summary

**Open Prompt Archive** is a curated, multi-source dataset of AI prompts that may be redistributed under verified terms. Its distinguishing feature is not prompt volume; it is the preservation of **source provenance, license evidence, attribution obligations, and review status** for every approved source and published record.

The dataset is intended to support prompt research, benchmarking, search, retrieval, curation, and downstream tooling while keeping upstream licensing information visible and auditable.

## Current status

**Pre-release / bootstrap.**

The repository is currently establishing the source registry, review process, contribution workflow, and canonical schema. No large third-party prompt corpus should be considered published until sources are explicitly marked `approved` and records are present under `data/`.

Published counts must be derived from repository data. Do not infer counts from candidate-source marketing claims or upstream repository descriptions.

## Dataset scope

Planned prompt modalities include:

- image generation;
- video generation;
- large language models;
- AI agents;
- coding;
- audio and speech;
- 3D and scene generation;
- other generative-AI workflows where a reusable prompt representation is meaningful.

The dataset is source-driven and model-agnostic. Model names may be recorded as metadata but do not imply endorsement, guaranteed compatibility, or affiliation.

## Data sources

Data may enter the archive only from sources that complete the source-review process documented in [`docs/SOURCE_REVIEW_PROCESS.md`](docs/SOURCE_REVIEW_PROCESS.md).

Each source record should identify, where available:

- canonical source URL;
- upstream owner or maintainer;
- source type;
- exact revision, tag, commit, or snapshot;
- retrieval/review date;
- license identifier;
- license evidence location;
- attribution requirements;
- scope notes;
- review status;
- media-mirroring status.

The canonical source registry is [`sources/sources.yaml`](sources/sources.yaml).

## Data collection and curation

The archive does not treat public accessibility as redistribution permission.

The curation pipeline is:

1. discover or receive a source proposal;
2. identify the canonical source and owner;
3. collect license and provenance evidence;
4. verify that the claimed license actually covers the prompt content;
5. check for third-party aggregation or conflicting rights signals;
6. approve, quarantine, or reject the source;
7. import only approved prompt content;
8. normalize records without silently changing prompt meaning;
9. validate against the canonical schema;
10. deduplicate without erasing provenance;
11. publish with source and license metadata intact.

## Licensing

Open Prompt Archive is **multi-license at the data layer**.

Imported prompts retain their upstream license and attribution obligations. The repository's root software license does not relicense imported prompt content.

A source is not approved solely because its repository has a license file. Reviewers must verify that the license scope covers the actual prompt content being imported, especially when the source aggregates material from websites, social networks, blogs, or other creators.

See [`docs/LICENSING_POLICY.md`](docs/LICENSING_POLICY.md).

## Provenance

Every published prompt must remain traceable to an approved source entry. Provenance metadata should preserve stable identifiers, revision information, retrieval dates, integrity hashes where practical, modification state, and attribution data.

When identical prompt text appears in multiple verified sources, deduplication must not erase those distinct provenance claims.

See [`docs/PROVENANCE_POLICY.md`](docs/PROVENANCE_POLICY.md).

## Personal data and sensitive content

Prompt text can contain names, handles, personal information, or references to real people even when the prompt itself is openly licensed. Open licensing does not remove privacy, publicity, or safety concerns.

Records may therefore be excluded, redacted, or removed under the content and takedown policies even when a source license otherwise permits redistribution.

The archive does not intentionally collect credentials, private messages, leaked material, private datasets, or access-controlled content.

## Associated media

Prompt licensing does not automatically license linked or accompanying images, video, audio, likenesses, trademarks, or other media.

The default policy is:

- prompt text and verified metadata may be archived when approved;
- external preview URLs may be retained when useful;
- third-party media is not mirrored unless its rights are verified independently.

## Intended uses

Potential uses include:

- prompt search and retrieval;
- prompt engineering research;
- comparative analysis across models or modalities;
- dataset studies;
- quality evaluation;
- taxonomy and classification work;
- local indexes and retrieval systems;
- educational exploration of openly licensed prompt patterns.

## Out-of-scope uses and limitations

Open Prompt Archive does not guarantee that:

- a prompt will work on every model;
- an upstream model or provider permits every downstream use;
- prompt text is factually correct, safe, unbiased, or high quality;
- an open prompt license resolves trademark, privacy, publicity, or model-provider terms;
- every historical source URL will remain available indefinitely.

Users remain responsible for complying with the licenses and terms applicable to the records and systems they use.

## Dataset quality

Quality is evaluated along multiple dimensions:

- provenance completeness;
- license confidence;
- attribution completeness;
- schema validity;
- duplicate handling;
- source stability;
- metadata consistency;
- content integrity.

The project does not use raw corpus size as a substitute for quality.

## Excluded data

The main dataset excludes by default:

- sources with unknown or ambiguous redistribution rights;
- material marked all-rights-reserved;
- non-commercial-only sources unless a separate clearly labeled collection is explicitly established in the future;
- private, paywalled, leaked, or access-controlled material;
- copied third-party aggregations whose original rights cannot be established;
- Carnaverone Studio first-party or proprietary prompt collections.

## Corrections and removals

Credible licensing, attribution, privacy, or provenance disputes should trigger review. Disputed prompt content may be removed from distribution while metadata necessary to document the review history is retained.

See [`docs/TAKEDOWN_POLICY.md`](docs/TAKEDOWN_POLICY.md).

## Versioning

The dataset will use explicit release/version identifiers once prompt data begins to be published. Source revisions and record provenance are tracked independently from repository release versions.

## Citation

Use [`CITATION.cff`](CITATION.cff) to cite the archive itself. Downstream users must also preserve any record-specific or source-specific attribution required by upstream licenses.

## Maintainer

**Carnaverone Studio**
