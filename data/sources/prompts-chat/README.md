# prompts.chat — Publication Contract

This directory is reserved for normalized Open Prompt Archive records derived from the approved `prompts-chat` source.

## Source lock

- **Source ID:** `prompts-chat`
- **Canonical upstream:** `https://github.com/f/prompts.chat`
- **Reviewed revision:** `25cb43d6e61974e66f3650cbc5a65482bc592552`
- **Effective prompt-data license:** `CC0-1.0`
- **Source review:** [`sources/reviews/prompts-chat.md`](../../../sources/reviews/prompts-chat.md)
- **Registry entry:** [`sources/sources.yaml`](../../../sources/sources.yaml)

The reviewed upstream license explicitly identifies `prompts.csv`, `PROMPTS.md`, and user-submitted prompt text as CC0 prompt data. Repository code, interactive-book content, branding, and unrelated media are outside this import scope.

## Preferred upstream input

Use the pinned `prompts.csv` at the reviewed revision as the primary tabular input for a deterministic import.

Observed upstream columns at the reviewed revision:

```text
act
prompt
for_devs
type
contributor
```

The upstream CSV is the acquisition format. It is **not** Open Prompt Archive's canonical publication format.

## Canonical mapping

| Upstream field | Open Prompt Archive field | Rule |
|---|---|---|
| `act` | `title` | Preserve text; trim only surrounding transport whitespace if necessary. |
| `prompt` | `prompt` | Preserve semantic content exactly. Do not rewrite or "improve" the prompt. |
| `contributor` | `source.author` | Preserve upstream contributor value when present. CC0 does not require attribution, but this archive retains provenance. |
| `type` | source metadata / classification input | Do not claim model compatibility from the generic upstream type alone. |
| `for_devs` | classification input | May inform a normalized tag only if the transformation is documented and deterministic. |

Canonical record `type` should be `llm` for records from the upstream chat-prompt corpus unless record-level evidence justifies another modality.

## Stable record identifiers

The source CSV does not provide a guaranteed immutable record identifier for every row. Open Prompt Archive therefore requires a deterministic identifier derived from source-controlled content.

Recommended identifier policy:

```text
prompts-chat-<content-id>
```

where `<content-id>` is a stable lowercase hexadecimal digest prefix produced from a documented canonicalization of the source row.

The exact canonicalization algorithm must be frozen before the first published snapshot. A later title edit must not silently cause two unrelated records to inherit the same identifier.

## License metadata

Every published record from this source must include:

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

`source.author` may still preserve the upstream contributor even though attribution is not a CC0 obligation.

## Provenance metadata

Every published record must identify:

- `source.source_id: prompts-chat`;
- canonical upstream repository/file URL;
- reviewed source revision;
- retrieval/import date;
- `provenance.verified: true`;
- `provenance.modified: false` when prompt semantics are preserved.

Normalization of CSV quoting, line endings, Unicode transport, or JSON serialization is not a semantic prompt modification when the resulting prompt text is unchanged.

## Content review

Open licensing does not automatically require publication of every upstream row.

Before release, apply the repository's [`CONTENT_POLICY.md`](../../../docs/CONTENT_POLICY.md), including checks for:

- accidentally embedded credentials or secrets;
- unnecessary private/sensitive personal information;
- malformed or empty prompts;
- records that cannot be represented without inventing metadata.

Any exclusion must be counted and documented in the source manifest. Do not silently edit a problematic prompt into a different prompt merely to keep it in the dataset.

## Distribution

The upstream `prompts.csv` at the reviewed revision is approximately 5.6 MB, so a normalized Git-tracked JSONL snapshot is expected to be practical under the repository's distribution policy.

Expected eventual layout:

```text
data/sources/prompts-chat/
├── README.md
├── manifest.yaml
└── part-00000.jsonl
```

Additional shards may be used if the normalized dataset grows beyond the project's preferred shard-size target.

## Publication gate

No JSONL file in this directory should be described as a released dataset until:

1. deterministic mapping is frozen;
2. record IDs are reproducible;
3. every record validates against `schema/prompt.schema.json`;
4. content-policy exclusions are recorded;
5. record counts are generated from the artifact;
6. SHA-256 checksums are generated from the artifact;
7. `manifest.yaml` validates against `schema/manifest.schema.json`;
8. the changelog and dataset card are updated for the release.
