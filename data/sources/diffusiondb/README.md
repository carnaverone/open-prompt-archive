# DiffusionDB — Publication Contract

This directory is reserved for Open Prompt Archive metadata and manifests for the approved prompt-only DiffusionDB scope.

## Source lock

- **Source ID:** `diffusiondb`
- **Canonical upstream:** `https://github.com/poloclub/diffusiondb`
- **Reviewed revision:** `bf0b01ee26119e16436fa67656ccb611f61be95f`
- **Effective dataset license:** `CC0-1.0`
- **Source review:** [`sources/reviews/diffusiondb.md`](../../../sources/reviews/diffusiondb.md)
- **Registry entry:** [`sources/sources.yaml`](../../../sources/sources.yaml)

## Approved Open Prompt Archive scope

Approved:

- prompt text;
- stable upstream record/image identifier when useful for provenance;
- generation metadata directly associated with the prompt, where retained deliberately;
- upstream content-safety scores when useful for documented filtering.

Not approved for this repository's current scope:

- image bytes;
- multi-terabyte upstream media archives;
- unnecessary user/account identifiers;
- unrelated upstream software assets.

The media exclusion is an Open Prompt Archive scope decision and does not modify the upstream DiffusionDB license declaration.

## Upstream data model

The DiffusionDB metadata tables document fields including:

```text
image_name
prompt
part_id
seed
step
cfg
sampler
width
height
user_name
timestamp
image_nsfw
prompt_nsfw
```

Open Prompt Archive is not intended to reproduce the entire upstream schema. It extracts only the fields needed for prompt reuse, model/generation context, filtering, and provenance.

## Canonical mapping

| Upstream field | Open Prompt Archive use | Default decision |
|---|---|---|
| `prompt` | `prompt` | Include when record passes publication policy. |
| `image_name` | `source.upstream_id` | May be retained as the upstream stable record reference. |
| `seed` | optional generation metadata | Retain only if the canonical record model explicitly supports it or a documented extension is adopted. |
| `step` | optional generation metadata | Same rule as above. |
| `cfg` | optional generation metadata | Same rule as above. |
| `sampler` | optional generation metadata | Same rule as above. |
| `width`, `height` | optional generation metadata | Do not imply current-model compatibility. |
| `image_nsfw` | filtering input | May be used to filter; need not be published. |
| `prompt_nsfw` | filtering input | May be used to filter; need not be published. |
| `user_name` | none by default | Exclude. It is unnecessary for the prompt archive's core purpose. |
| `timestamp` | none by default | Exclude unless a later provenance requirement is explicitly justified. |

If generation parameters are not representable without changing `schema/prompt.schema.json`, do not smuggle them into unrelated fields. Schema evolution must precede publication of those fields.

## Record type

DiffusionDB prompt text is associated with text-to-image generation. Canonical published records should therefore use:

```text
type: image
```

Model associations should reflect the reviewed upstream context and should not be generalized into claims about compatibility with unrelated image models.

## License metadata

Published prompt records use:

```json
{
  "license": {
    "spdx": "CC0-1.0",
    "attribution_required": false,
    "attribution": null,
    "scope_verified": true
  }
}
```

Open Prompt Archive should nevertheless retain `DiffusionDB` as the source for provenance and research reproducibility.

## Content and privacy filtering

The upstream datasheet explicitly documents that harmful, NSFW, or sensitive prompt content may remain in the corpus despite upstream moderation.

The import must therefore apply a reproducible filtering policy before publication. At minimum:

- do not publish secrets/credentials accidentally present in prompt text;
- minimize unnecessary personal data;
- apply the project's public content policy consistently;
- document thresholds/rules used with upstream NSFW scores if those scores drive filtering;
- report counts of excluded records in the manifest.

Filtering a record means excluding it from a published snapshot; it does not authorize silently rewriting the original prompt.

## Distribution strategy

DiffusionDB contains roughly 1.8 million unique prompts in its large dataset and an upstream image corpus measured in terabytes. It should therefore **not** be replayed into ordinary Git history as one giant tracked dataset.

Open Prompt Archive should publish a prompt-only normalized snapshot using the large-dataset path defined in [`docs/DISTRIBUTION_POLICY.md`](../../../docs/DISTRIBUTION_POLICY.md):

```text
Git repository
├── data/sources/diffusiondb/README.md
├── data/sources/diffusiondb/manifest.yaml
├── compact sample/index metadata (optional)
└── checksums / release references

GitHub Release
├── diffusiondb-prompts-<version>-part-00000.jsonl.gz
├── ...
└── optional derived Parquet resources
```

Actual resource names, counts, sizes, and hashes must be generated from the final artifacts.

## Publication gate

A DiffusionDB snapshot is publishable only after:

1. exact upstream source artifact/revision is pinned;
2. field-retention/exclusion rules are frozen;
3. content filtering is deterministic and documented;
4. normalization preserves prompt semantics;
5. records validate against the canonical prompt schema;
6. resource counts and SHA-256 hashes are generated;
7. the manifest validates against `schema/manifest.schema.json`;
8. large snapshot resources are published immutably under a versioned dataset release;
9. dataset card/changelog record the new source snapshot.
