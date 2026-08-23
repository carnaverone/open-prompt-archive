# Changelog

All notable changes to Open Prompt Archive's public dataset structure, policies, source decisions, and releases are documented here.

The project does not yet publish a versioned prompt corpus. Entries in the **Unreleased** section describe repository/bootstrap and curation changes rather than a dataset release.

## Unreleased

### Added

- Dataset-first project scope and repository structure.
- Canonical dataset card.
- Source-first contribution model.
- Licensing and provenance review policies.
- Source registry and review-state model.
- Code of Conduct, governance, security, and takedown policies.
- GitHub issue forms for source proposals, licensing/provenance corrections, data-quality reports, and removal/rights review.
- Dataset citation metadata.
- Human-readable source reviews for prompts.chat, DiffusionDB, and three YouMind OpenLab prompt collections.
- Published source-review index under `sources/README.md`.

### Changed

- Reframed the repository from general prompt tooling infrastructure to a curated open prompt dataset/archive.
- Clarified that Carnaverone Studio first-party/proprietary prompts are outside the repository's scope.
- Clarified that quarantined or rejected sources may retain review metadata but not redistributable prompt corpus content.
- Strengthened prompt/source schemas so published records require evidence-backed license scope and verification state.

### Source decisions

- `prompts-chat` — **approved** for prompt text/data explicitly covered by upstream `CC0-1.0`; site code, book content, branding, and media excluded.
- `diffusiondb` — **approved** for prompt text and prompt-generation metadata under upstream `CC0-1.0`; associated images/media excluded and content-policy filtering required before publication.
- `youmind-nano-banana-pro` — **quarantined** for bulk import because the repository claims `CC-BY-4.0` while the corpus includes community/external-source prompts whose record-level license authority is not yet sufficiently verified.
- `youmind-gpt-image-2` — **quarantined** for the same bulk-corpus license-scope concern.
- `youmind-seedance-2` — **quarantined** for the same bulk-corpus license-scope concern.

### Data

- No large third-party prompt corpus has been released yet.
- Only sources marked `approved` in `sources/sources.yaml` are eligible for import into `data/`.
