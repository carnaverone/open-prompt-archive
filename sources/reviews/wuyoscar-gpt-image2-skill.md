# Source Review — Wuyoscar GPT-Image2-Skill

- **Source ID:** `wuyoscar-gpt-image2-skill`
- **Canonical repository:** `https://github.com/wuyoscar/GPT-Image2-Skill`
- **Upstream owner:** Wuyoscar and repository contributors
- **Reviewed revision:** `068dd9e24aadc8731e46f38548ca4dcd94515d35`
- **Review date:** 2026-08-23
- **Current decision:** `review`
- **Repository license:** `MIT`
- **Prompt publication scope:** none while record-level provenance is being re-verified
- **Images/media:** excluded

## Why the previous restricted approval was reopened

The initial review relied on the contribution convention documented in `CONTRIBUTING.md`:

- original repo-generated examples should end with `Original`;
- outside-source prompts must preserve visible `Author + Source` attribution.

That appeared to provide a mechanical boundary for an original-only MIT subset.

A deeper check of the canonical gallery at the **same pinned revision** found that the actual reference-gallery files use a third label, `Curated`, for multiple entries. The root README explains `Curated` as a repo-curated **or substantially reworked** prompt/image. That label is broader than `Original` and does not by itself prove that the repository owns or is authorized to relicense the underlying prompt text.

Example evidence at the pinned revision:

- `skills/gpt-image/references/gallery-gaming.md` contains both explicit outside-source entries (`Author + Source`) and entries labeled `Curated`;
- `skills/gpt-image/references/gallery-anime-and-manga.md` likewise mixes explicit outside-source entries and `Curated` entries;
- `README.md` describes the showcase source label `Curated` as repo-curated or substantially reworked;
- `CONTRIBUTING.md` still describes `Original` as the marker for original repo-generated examples.

This creates a provenance-semantic mismatch that must be resolved before Open Prompt Archive publishes prompt text from this source.

## Current license assessment

The repository's root MIT license remains valid evidence for repository-authored material. It is **not** disputed here.

The unresolved question is narrower: which gallery prompt records can be shown, at record level, to be repository-authored or otherwise licensed in a way that permits Open Prompt Archive redistribution under MIT?

`Curated` is not currently treated as equivalent to `Original` because:

1. curation alone does not establish copyright ownership or relicensing authority;
2. substantial rewriting may create new material without automatically clearing rights in source material;
3. the gallery also contains clearly identified external-source prompts, proving that repository contents have mixed provenance;
4. the current documentation uses both `Original` and `Curated` concepts without enough evidence to map every canonical record safely.

Therefore `license.scope_verified` is now `false` for prompt publication from this source until the boundary is clarified.

## What remains clearly excluded

Regardless of the review outcome, the following are outside the current Open Prompt Archive scope:

- gallery prompts explicitly attributed to outside authors or external social posts unless separately licensed by their original rights holder;
- generated images, reference images, screenshots, banners, or other media;
- third-party API/cookbook content copied or mirrored into the repository;
- trademarks, logos, likenesses, or other third-party rights represented in generated outputs;
- records added after the reviewed revision unless a later source review covers them.

## Evidence that could restore a restricted approval

A restricted prompt subset may be approved later if at least one reliable rule can be demonstrated, for example:

- canonical entries explicitly marked `Original` with no contradictory provenance signal;
- upstream documentation stating that a defined `Curated` subset is authored by or licensed to the repository under MIT;
- record-level metadata linking entries to contributors and license grants;
- commit/contribution evidence establishing repository authorship for specific prompts;
- direct licenses from original outside authors for identifiable records.

The archive may approve a smaller mechanically identifiable subset even if the complete gallery remains mixed-origin.

## Import rule while status is `review`

**No prompt records from this source may be committed to `data/` or attached to a dataset release.**

The source directory may retain review metadata and a hold notice, but no prompt corpus should be generated from `Curated`, `Original`, or outside-source entries until the registry returns to `approved` with a verified scope.

## Re-review triggers / resolution

Resolve this review when:

- upstream clarifies the exact meaning and rights scope of `Curated`;
- a mechanically verifiable `Original` subset is confirmed to exist in the canonical gallery representation;
- record-level contribution/license evidence is available;
- or a later upstream revision introduces a clearer provenance model.

## Conclusion

**REVIEW OPEN.** The root MIT license is acknowledged, but the canonical gallery's `Curated`/`Original`/outside-source provenance semantics are not currently strong enough for Open Prompt Archive to publish prompt text from this source. No media is approved.
