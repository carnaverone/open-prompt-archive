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
- Source-specific publication contracts for approved sources under `data/sources/`.
- Human-readable evidence reviews for prompts.chat, DiffusionDB, BigScience PromptSource/P3, Wuyoscar GPT-Image2-Skill, freestylefly/awesome-gpt-image-2, and three YouMind OpenLab collections.
- Published source-review index under `sources/README.md`.

### Changed

- Reframed the repository from general prompt tooling infrastructure to a curated open prompt dataset/archive.
- Clarified that Carnaverone Studio first-party/proprietary prompts are outside the repository's scope.
- Clarified that quarantined or rejected sources may retain review metadata but not redistributable prompt corpus content.
- Strengthened prompt/source schemas so published records require evidence-backed license scope and verification state.
- Adopted source-partitioned canonical data organization rather than model-first storage.
- Added a scalable Git-vs-release distribution model for very large prompt datasets.
- Added restricted-subset approval as a first-class curation strategy for mixed-origin repositories when a reliable record-level provenance boundary exists.

### Source decisions

- `prompts-chat` — **approved** for prompt text/data explicitly covered by upstream `CC0-1.0`; site code, book content, branding, and media excluded.
- `diffusiondb` — **approved** for prompt text and selected prompt-generation metadata under upstream `CC0-1.0`; associated images/media excluded and content-policy filtering required before publication.
- `bigscience-promptsource` — **approved** for prompt template definitions and prompt-specific metadata under `Apache-2.0`; independently licensed underlying datasets and rendered dataset examples excluded.
- `wuyoscar-gpt-image2-skill` — **approved as a restricted subset** under `MIT`: only gallery entries explicitly marked `Original` and not attributed to outside sources; external-source entries and all media excluded.
- `freestylefly-awesome-gpt-image-2` — **quarantined** for bulk import because its own disclaimer documents substantial YouMind/OpenNana/community provenance that is not resolved by the repository-level MIT license.
- `youmind-nano-banana-pro` — **quarantined** for bulk import because the repository claims `CC-BY-4.0` while the corpus includes community/external-source prompts whose record-level license authority is not yet sufficiently verified.
- `youmind-gpt-image-2` — **quarantined** for the same bulk-corpus license-scope concern.
- `youmind-seedance-2` — **quarantined** for the same bulk-corpus license-scope concern.

### Data

- No large third-party prompt corpus has been released yet.
- Only records within the explicitly approved scope of an `approved` source are eligible for publication into `data/` or dataset release artifacts.
- First planned small-source publication path is the normalized prompts.chat CC0 corpus; DiffusionDB will use the large-snapshot distribution path rather than normal Git history.
