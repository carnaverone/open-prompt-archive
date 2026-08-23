# Source Review — DiffusionDB

- **Source ID:** `diffusiondb`
- **Canonical repository:** `https://github.com/poloclub/diffusiondb`
- **Upstream organization:** Polo Club / Georgia Institute of Technology
- **Reviewed revision:** `bf0b01ee26119e16436fa67656ccb611f61be95f`
- **Review date:** 2026-08-23
- **Decision:** `approved`
- **Approved scope:** prompt text and prompt-generation metadata only
- **Associated images/media:** excluded from Open Prompt Archive

## Evidence reviewed

1. The DiffusionDB README explicitly states that the **DiffusionDB dataset is available under CC0 1.0**, while repository Python code is MIT-licensed separately.
2. The project datasheet documents that prompts and generated images were collected from the public Stable Diffusion Discord server.
3. The datasheet records the collection mechanism, timeframe, source channels, and data fields, providing unusually strong provenance for the corpus.
4. The datasheet states that users of the relevant Stable Diffusion beta services agreed to terms forfeiting intellectual-property claims to content provided or received through those services, and that generated material could be used for any purpose.
5. The project provides a data-removal mechanism and documents content-quality and NSFW limitations.

## License assessment

**Effective dataset license:** `CC0-1.0`

DiffusionDB provides an explicit dataset-level CC0 declaration rather than relying on its MIT software license. Its datasheet also documents the upstream collection context and the rights/consent basis relied upon by the dataset creators.

For Open Prompt Archive, approval is intentionally narrower than the full upstream dataset: only prompt text and prompt-generation metadata are in scope.

## Import conditions

An Open Prompt Archive import may include fields such as:

- prompt text;
- source record/image UUID as an upstream identifier;
- generation parameters useful for provenance or model compatibility;
- source revision and retrieval metadata;
- NSFW/toxicity scores when useful for filtering and quality control.

The import must:

- preserve the DiffusionDB source identifier and pinned revision;
- identify the effective prompt-data license as `CC0-1.0`;
- apply Open Prompt Archive content-policy filtering before publication;
- avoid treating Discord usernames or hashes as required public prompt metadata unless needed for provenance and justified by policy;
- avoid mirroring associated images.

## Content and privacy considerations

The upstream datasheet notes that harmful, NSFW, or sensitive prompt content may be present even though the source community had moderation rules. Open Prompt Archive must therefore filter or exclude records that violate its publication policy rather than importing the corpus blindly.

DiffusionDB contains hashed user identifiers and timestamps. Open Prompt Archive does not need those fields for a prompt archive by default and should omit them unless a documented provenance requirement justifies retention.

## Media decision

`not-allowed` for Open Prompt Archive's initial scope.

This decision is a project-scope choice, not a statement that DiffusionDB itself prohibits image redistribution. The archive is intentionally prompt-first and avoids mirroring third-party/generated media without a separate media review.

## Re-review triggers

Re-review if:

- the upstream dataset license changes;
- the CC0 declaration is withdrawn or materially qualified;
- new evidence changes the documented rights basis for the source corpus;
- Open Prompt Archive expands scope to include images or other media.

## Conclusion

**APPROVED for prompt text and prompt-generation metadata under CC0-1.0, subject to content-policy filtering and the scope above.**
