# Data Directory

This directory will contain canonical prompt datasets that have passed the repository's source and licensing review.

## Rules

- Do not add third-party prompt data before its source is registered and approved in `sources/sources.yaml`.
- Canonical normalized records should validate against `schema/prompt.schema.json`.
- Preserve provenance and upstream license metadata.
- Do not silently relicense imported content.
- Do not mirror external images/media unless their redistribution rights are independently verified.

## Planned organization

```text
data/
├── image/
├── video/
├── llm/
├── agent/
├── audio/
├── 3d/
├── coding/
└── multimodal/
```

The exact layout may evolve once the first verified source imports are implemented.

## Current status

No third-party prompt dataset is imported yet. This is intentional: source provenance and license scope are being established before ingestion begins.
