# Wuyoscar GPT-Image2-Skill — Review Hold

This source directory is **metadata-only while the source is in `review` status**. No prompt records from Wuyoscar GPT-Image2-Skill are currently eligible for publication into Open Prompt Archive.

## Source reference

- **Source ID:** `wuyoscar-gpt-image2-skill`
- **Canonical upstream:** `https://github.com/wuyoscar/GPT-Image2-Skill`
- **Reviewed revision:** `068dd9e24aadc8731e46f38548ca4dcd94515d35`
- **Repository license:** `MIT`
- **Registry status:** `review`
- **Source review:** [`sources/reviews/wuyoscar-gpt-image2-skill.md`](../../../sources/reviews/wuyoscar-gpt-image2-skill.md)

## Why publication is paused

The earlier restricted-subset design relied on the upstream contribution rule that repo-generated/original gallery examples should be marked `Original`, while outside-source entries retain `Author + Source` attribution.

Deeper inspection of the canonical reference-gallery files at the pinned revision showed a third label: `Curated`. The upstream README describes `Curated` as repo-curated **or substantially reworked**. That is not equivalent to proof of repository-original authorship or authority to relicense every underlying prompt under MIT.

The pinned gallery therefore contains at least three provenance concepts that cannot currently be collapsed safely:

```text
Original      → documented contribution concept
Curated       → repo-curated or substantially reworked; rights scope unresolved
Author+Source → explicit outside-source provenance
```

Until the record-level boundary is verified, `license.scope_verified` is `false` for prompt publication from this source.

## Current rule

Do **not** create or commit:

- `part-*.jsonl` prompt shards;
- prompt samples presented as approved data;
- manifests with `publication.status: published`;
- release assets containing this source's prompt text.

Do not treat `Curated` as a synonym for `Original`.

Explicit outside-source prompts remain excluded unless their original rights are independently verified. Images and other media remain excluded regardless of prompt review status.

## What may remain here

This directory may contain only compact source-review/publication-planning metadata while status is `review`.

A new publication contract should replace this hold notice only after `sources/sources.yaml` returns the source to `approved` with a mechanically verifiable scope.

## Evidence needed to reopen publication

Useful evidence includes:

- authoritative upstream clarification that a defined `Curated` subset is authored/licensed under MIT;
- a canonical and mechanically identifiable `Original` subset with no conflicting provenance signal;
- record-level author/contributor/license metadata;
- direct original-author licenses for specific externally sourced entries.

See the human-readable source review for the full rationale.
