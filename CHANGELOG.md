# Changelog

All notable changes to Open Prompt Archive's public dataset structure, policies, source decisions, and releases are documented here.

The project does not yet publish a versioned prompt corpus. Entries in **Unreleased** describe repository and curation changes rather than a dataset release.

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
- Curation contract tests for Git blob identity, CSV fidelity, stable IDs, review screening, sharding, and schema-valid generated objects.

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

- No large third-party prompt corpus has been released yet.
- Only records within the explicitly approved scope of an `approved` source are eligible for publication into `data/` or dataset release artifacts.
- The first planned small-source publication path remains the normalized prompts.chat CC0 corpus.
- The complete pinned prompts.chat blob is verified by source identity but exceeds the current connector's file-materialization limit; no count, acquisition SHA-256, manifest, or shard is claimed from a partial response.
- DiffusionDB will use the large-snapshot distribution path rather than normal Git history.
