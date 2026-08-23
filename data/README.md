# Data Directory

This directory is reserved for **approved redistributable prompt data**.

The canonical dataset is source-partitioned so that provenance and licensing remain easy to audit. Modality/model indexes may be generated later as derived views rather than becoming the primary storage model.

## Rules

- Do not add prompt content before its source is registered and marked `approved` in `sources/sources.yaml`.
- Do not place candidate, quarantined, or rejected prompt corpora in this directory.
- Canonical prompt records must validate against `schema/prompt.schema.json`.
- Every record must reference its approved `source_id`.
- Preserve effective upstream license and attribution metadata at record level.
- Preserve reviewed source revision and provenance where available.
- Do not silently relicense imported content.
- Do not mirror third-party images/media unless their redistribution rights are independently verified.
- Do not mix unrelated sources into one canonical file merely for convenience.

## Canonical organization

Preferred structure:

```text
data/
└── sources/
    ├── <source_id>/
    │   ├── prompts.jsonl
    │   └── README.md        # optional source-specific distribution notes
    └── ...
```

If one upstream source contains materially different record-level licenses that cannot be represented safely in one distribution file, split the output by license or another auditable boundary rather than hiding the distinction.

## Derived views

Future generated distributions may provide views such as:

```text
image
video
llm
agent
coding
audio
3d
multimodal
```

or SQLite/FTS, Parquet, search indexes, and other machine-friendly formats.

Derived files must be reproducible from canonical data and must preserve source/license metadata.

## Current status

No large third-party prompt corpus is published yet. This is intentional: source provenance and license scope are being established before ingestion begins.
