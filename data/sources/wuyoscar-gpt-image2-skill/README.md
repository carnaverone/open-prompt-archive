# Wuyoscar GPT-Image2-Skill — Publication Contract

This directory is reserved for the **approved original-only gallery subset** from Wuyoscar's GPT-Image2-Skill repository.

## Source lock

- **Source ID:** `wuyoscar-gpt-image2-skill`
- **Canonical upstream:** `https://github.com/wuyoscar/GPT-Image2-Skill`
- **Reviewed revision:** `068dd9e24aadc8731e46f38548ca4dcd94515d35`
- **Effective license for approved subset:** `MIT`
- **Source review:** [`sources/reviews/wuyoscar-gpt-image2-skill.md`](../../../sources/reviews/wuyoscar-gpt-image2-skill.md)

## Record-level eligibility rule

The upstream contribution guide distinguishes:

- repo-generated/original examples whose footer ends with `Original`;
- outside-source prompts that must carry visible `Author + Source` attribution.

Open Prompt Archive therefore publishes **only records that satisfy the original-only filter**.

A record is eligible when:

1. it is a canonical gallery entry at the reviewed revision;
2. the entry is explicitly marked `Original` using the upstream convention;
3. no outside author/source attribution indicates third-party origin;
4. its prompt text is included in the licensed repository work;
5. the MIT notice is preserved.

Ambiguous entries are excluded.

## Excluded records and assets

Do not import:

- outside-source prompt entries;
- prompts attributed to external authors or social posts;
- gallery images or reference images;
- screenshots, banners, logos, or other media;
- example output files;
- prompt entries added after the reviewed revision until the source is re-reviewed.

## Canonical mapping

For eligible entries:

| Upstream element | Open Prompt Archive field |
|---|---|
| gallery number / stable heading context | provenance aid only; not assumed immutable by itself |
| title | `title` |
| full prompt text | `prompt` |
| model context | `models: ["gpt-image-2"]` when explicitly attached to the gallery entry/source context |
| original marker | provenance/filter evidence; do not expose as a fake license field |
| source repository | `source.url` / `source.source_id` |

Canonical type:

```text
type: image
```

## Stable IDs

Gallery numbering can change when entries are inserted or reorganized, so it should not be the sole record identity.

Use a deterministic content/source identifier, for example:

```text
wuyoscar-gpt-image2-<content-id>
```

The final content-ID canonicalization algorithm must be frozen before first publication and documented in the manifest/normalization notes.

## License metadata

Every published record must record MIT and retain the relevant upstream copyright/permission notice through source attribution/NOTICE material.

A suitable project-level attribution is:

```text
Wuyoscar / GPT-Image2-Skill — MIT
```

This does not grant rights in trademarks, depicted people, or linked/generated media.

## Fidelity

Prompt text should be preserved as written in the eligible gallery entry. Do not silently translate, optimize, shorten, or modernize prompts during import.

If English and Chinese README variants contain translated prompt variants, treat them as separate upstream representations only when their provenance and semantic relationship can be documented reliably.

## Publication gate

Before a snapshot is published:

1. parse the canonical gallery at the reviewed revision;
2. apply the documented `Original` + no-external-attribution filter;
3. record the number of included and excluded entries;
4. preserve prompt text exactly after transport normalization;
5. generate deterministic IDs;
6. validate every record against `schema/prompt.schema.json`;
7. retain MIT attribution/notice information;
8. generate artifact counts, byte sizes, and SHA-256 checksums;
9. validate the source manifest against `schema/manifest.schema.json`.
