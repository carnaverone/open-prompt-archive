# Source Review — Wuyoscar GPT-Image2-Skill

- **Source ID:** `wuyoscar-gpt-image2-skill`
- **Canonical repository:** `https://github.com/wuyoscar/GPT-Image2-Skill`
- **Upstream owner:** Wuyoscar and repository contributors
- **Reviewed revision:** `068dd9e24aadc8731e46f38548ca4dcd94515d35`
- **Review date:** 2026-08-23
- **Decision:** `approved` for a restricted, mechanically identifiable subset
- **Repository license:** `MIT`
- **Approved scope:** prompt text for gallery entries explicitly marked as repository-original (`Original`) and not attributed to an outside source
- **Outside-source entries:** excluded pending independent rights review
- **Images/media:** excluded

## Evidence reviewed

1. The repository root `LICENSE` is the MIT License and identifies Wuyoscar as copyright holder for the licensed repository work.
2. The README presents the project as a GPT Image 2 prompt gallery and reusable prompt library under the repository's MIT license badge.
3. `CONTRIBUTING.md` defines two distinct gallery-entry classes:
   - **original repo-generated examples**, whose footer metadata ends with `Original`;
   - **outside-source prompts**, which must preserve visible `Author + Source` attribution.
4. The contribution rules therefore provide a practical record-level signal that distinguishes repository-original gallery material from externally sourced material.

## License assessment

The complete gallery is **not approved as one undifferentiated MIT corpus**, because the project explicitly allows outside-source prompts whose original rights remain with external authors.

However, the subset explicitly designated by the repository as `Original` is part of the repository-authored/maintained gallery documentation covered by the root MIT distribution, and it can be separated mechanically from externally attributed entries.

**Effective license for the approved subset:** `MIT`.

## Approved record filter

A gallery prompt is eligible only when all of the following are true at the reviewed revision:

1. the entry is part of the canonical repository gallery;
2. its footer/metadata explicitly marks it `Original` according to the repository's documented contribution convention;
3. it does not carry an outside `Author` / external `Source` attribution indicating third-party origin;
4. the prompt text itself is present in the licensed repository work;
5. the import preserves the MIT copyright/license notice required for redistribution.

If an entry has ambiguous provenance, it is excluded rather than guessed into the approved subset.

## Excluded material

This approval does not cover:

- gallery prompts attributed to outside authors or external social posts;
- generated images, reference images, screenshots, banners, or other media;
- third-party API documentation copied by reference;
- external trademarks, logos, or other rights represented in gallery outputs;
- prompts added after the reviewed revision until re-reviewed or covered by a later snapshot decision.

Outside-source prompts may be reconsidered individually if the original author's redistribution license can be verified directly.

## Attribution

MIT redistribution requires preservation of the relevant copyright and permission notice. Open Prompt Archive should record attribution similar to:

```text
Wuyoscar / GPT-Image2-Skill — MIT
```

and retain the canonical repository URL and reviewed revision.

## Content classification

Eligible records are image-generation prompts and should use:

```text
type: image
```

Model metadata may identify `gpt-image-2` when the source entry is explicitly presented for that model. This is source provenance, not a claim that the prompt is incompatible with or optimized for every other image model.

## Re-review triggers

Re-review if:

- the repository changes its license;
- the `Original` / outside-source convention changes;
- original and third-party entries can no longer be distinguished reliably;
- the archive wants to include generated images or other media;
- a specific `Original` designation is credibly disputed.

## Conclusion

**APPROVED only for gallery prompt entries explicitly marked `Original` and not externally attributed, under MIT. Outside-source entries and all media remain excluded.**
