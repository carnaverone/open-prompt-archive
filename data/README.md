# Data Directory

This directory is reserved for **approved redistributable prompt data**.

The canonical dataset is source-partitioned so that provenance and licensing remain easy to audit. Modality/model indexes may be generated later as derived views rather than becoming the primary storage model.

See [`docs/DISTRIBUTION_POLICY.md`](../docs/DISTRIBUTION_POLICY.md) for Git-vs-release publication rules, sharding, large-dataset handling, checksums, and snapshot versioning.

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
- Large generated snapshots must not bloat normal Git history merely because the upstream dataset is large.

## Canonical organization

Preferred structure for Git-tracked prompt data:

```text
data/
└── sources/
    ├── <source_id>/
    │   ├── manifest.yaml
    │   ├── part-00000.jsonl
    │   ├── part-00001.jsonl
    │   └── ...
    └── ...
```

Small datasets may require only one JSONL shard. Large datasets may keep only their manifest and compact samples/indexes in Git while versioned snapshot artifacts are published through GitHub Releases according to the distribution policy.

If one upstream source contains materially different record-level licenses that cannot be represented safely in one distribution file, split the output by license or another auditable boundary rather than hiding the distinction.

## Manifests

Every imported source must have a manifest recording the reviewed upstream revision, effective license, review file, import scope, record counts, filters, output resources, and SHA-256 checksums.

Counts and checksums are publication facts and must be generated from the actual artifacts rather than estimated manually.

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

or Parquet, SQLite/FTS, search indexes, and other machine-friendly representations.

Derived files must be reproducible from canonical data and must preserve source/license metadata.

## Current status

Source review has started. `prompts-chat` and `diffusiondb` are approved for defined prompt-only scopes; several YouMind OpenLab collections are currently quarantined pending stronger license-scope evidence.

No large third-party prompt corpus is published yet. This remains intentional until the first deterministic import and manifest can be validated end to end.
