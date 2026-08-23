# Changelog

All notable changes to Open Prompt Archive's public dataset structure, policies, source decisions, and releases are documented here.

Dataset releases are versioned independently from reviewed upstream source revisions.

## [0.1.0] - 2026-08-23

### Data

- Published the first canonical dataset snapshot from the approved `prompts-chat` source.
- Published 2,134 canonical `CC0-1.0` prompt records from upstream revision `25cb43d6e61974e66f3650cbc5a65482bc592552`.
- Published one 7,736,751-byte JSONL shard with SHA-256 `ba8377b874c621e44d8c9b321c1ef1f95d7565867186b5e5fb8c2f908402a77c`.
- Used frozen normalization algorithm `prompts-chat-v1`.
- Resolved all 10 heuristic content-review candidates explicitly; all 10 were included and zero remain pending.

### Privacy

- Added deterministic contributor privacy minimization for `prompts.chat`.
- Removed 1,072 email identifiers from public `source.author` metadata across 1,069 records while retaining eligible non-email handles.
- Prompt text and frozen record-ID inputs remain unchanged by contributor metadata minimization.

### Tooling

- Raised the Python CSV parser field limit only to the verified source-blob size so legitimate prompts larger than Python's default 128 KiB limit import safely.
- Added regression coverage for large CSV fields and contributor-email minimization.

## Unreleased

### Added

- Dataset-first project scope and repository structure.
- Canonical dataset card and citation metadata.
- Source-first contribution model.
- Licensing, provenance, content, takedown, and distribution policies.
- Dataset publication checklist.
- Source registry and evidence-based review-state model.
- Prompt, source-registry, and dataset-manifest JSON Schemas.
- Code of Conduct, governance, and security documentation.
- GitHub issue forms for source proposals, licensing/provenance corrections, data-quality reports, and removal/rights review.
- Source-specific publication contracts/hold notices under `data/sources/`.
- Human-readable evidence reviews for prompts.chat, DiffusionDB, BigScience PromptSource/P3, Wuyoscar GPT-Image2-Skill, freestylefly/awesome-gpt-image-2, and three YouMind OpenLab collections.
- Published source-review index under `sources/README.md`.
- Exact `prompts.chat` acquisition lock for reviewed `prompts.csv`: 5,632,658 bytes, Git blob SHA-1 `1bc70c691fb71cc11d8b5031efd0e1ba1b4a0697`.
- Deterministic `prompts.chat` importer under `scripts/import/prompts_chat.py` with frozen `prompts-chat-v1` record IDs, schema validation, content-review hold logic, JSONL sharding, counts, byte sizes, SHA-256 checksums, and manifest generation.
- Independent `scripts/validate_publication.py` release gate that revalidates current source approval/revision/license state, resource paths, bytes, SHA-256, JSONL schemas, canonical-ID uniqueness, and manifest counts without trusting importer-generated claims.
- Curation contract tests for Git blob identity, multiline CSV fidelity, stable IDs, prompt provenance hashes, review screening, sharding, checksum tamper detection, duplicate-ID rejection, and staging-vs-published validation.

### Changed

- Reframed the repository from general prompt tooling infrastructure to a curated open prompt dataset/archive.
- Clarified that Carnaverone Studio first-party/proprietary prompts are outside the repository's scope.
- Clarified that non-approved sources may retain review metadata but not redistributable prompt corpus content.
- Strengthened prompt/source schemas so published records require evidence-backed license scope and verification state.
- Adopted source-partitioned canonical data organization rather than model-first storage.
- Added a scalable Git-vs-release distribution model for very large prompt datasets.
- Added restricted-subset approval as a possible curation strategy for mixed-origin repositories only when a reliable record-level provenance boundary exists.
- Froze the `prompts.chat` identifier algorithm to SHA-256 over an exact UTF-8 JSON-array canonicalization of all five decoded upstream CSV fields; full 64-character digests are used.
- Separated importer output into `publish/` and local-only `audit/` so content held for review cannot be mistaken for a publication artifact.
- Made independent validation of the exact final candidate directory an explicit publication checklist requirement; importer self-validation alone is not sufficient.
- Reopened the Wuyoscar GPT-Image2-Skill provenance review after deeper inspection showed canonical `Curated` entries alongside explicit outside-source entries while upstream contribution guidance separately uses `Original` for repo-generated examples.

### Source decisions

- `prompts-chat` — **approved** for prompt text/data explicitly covered by upstream `CC0-1.0`; site code, book content, branding, and media excluded.
- `diffusiondb` — **approved** for prompt text and selected prompt-generation metadata under upstream `CC0-1.0`; associated images/media excluded and content-policy filtering required before publication.
- `bigscience-promptsource` — **approved** for prompt template definitions and prompt-specific metadata under `Apache-2.0`; independently licensed underlying datasets and rendered dataset examples excluded.
- `wuyoscar-gpt-image2-skill` — **review reopened**. The root repository remains MIT-licensed, but `Curated` is not treated as equivalent to `Original` or as proof of relicensing authority. No prompt records are currently approved from this source pending a stronger mechanical provenance boundary.
- `freestylefly-awesome-gpt-image-2` — **quarantined** for bulk import because its own disclaimer documents substantial YouMind/OpenNana/community provenance that is not resolved by the repository-level MIT license.
- `youmind-nano-banana-pro` — **quarantined** for bulk import because the repository claims `CC-BY-4.0` while the corpus includes community/external-source prompts whose record-level license authority is not yet sufficiently verified.
- `youmind-gpt-image-2` — **quarantined** for the same bulk-corpus license-scope concern.
- `youmind-seedance-2` — **quarantined** for the same bulk-corpus license-scope concern.

### Data

- Only records within the explicitly approved scope of an `approved` source are eligible for publication into `data/` or dataset release artifacts.
- DiffusionDB will use the large-snapshot distribution path rather than normal Git history.
