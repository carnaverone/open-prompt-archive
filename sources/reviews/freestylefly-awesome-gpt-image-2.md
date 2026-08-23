# Source Review — freestylefly / awesome-gpt-image-2

- **Source ID:** `freestylefly-awesome-gpt-image-2`
- **Canonical repository:** `https://github.com/freestylefly/awesome-gpt-image-2`
- **Upstream owner:** freestylefly
- **Reviewed revision:** `de6a8ad89b6308dc49b316fcd9f7a56bf2a73273`
- **Review date:** 2026-08-23
- **Decision:** `quarantined`
- **Repository license:** `MIT`
- **Bulk prompt import:** not approved
- **Images/media:** not approved

## Evidence reviewed

1. The repository root contains a standard MIT license naming freestylefly.
2. The README describes the project as an industrial prompt/template library and advertises hundreds of reverse-engineered cases.
3. The project's own disclaimer states that its research/organization work references and uses publicly available prompt-library content from **YouMind** and **OpenNana**.
4. The disclaimer further states that the prompt cases and generated images derive their original inspiration/data from public communities, that third-party rights remain with original authors/platforms, and that the repository does not guarantee third-party content is available for commercial use.
5. The project states that it attempts to preserve original source links and provides a takedown mechanism.

## License-scope concern

The repository's MIT license is clear for repository-authored software and original project material, but the project's own provenance statement establishes that a material portion of the prompt gallery is derived from or based on externally sourced community prompt content.

A top-level MIT file therefore cannot, by itself, establish redistribution authority over the full prompt corpus.

The fact that prompts may have been rewritten, reverse-engineered, normalized, or restructured does not automatically resolve copyright/provenance questions concerning the source material. Open Prompt Archive does not infer clean relicensing solely from transformation.

## Quarantine rule

Open Prompt Archive may retain:

- repository metadata;
- the claimed repository MIT license;
- this provenance review;
- links to upstream source/disclaimer evidence.

It must not copy the bulk prompt gallery into `data/` or a release asset while record-level rights remain unresolved.

## Potential future subsets

A mechanically identifiable subset could later become eligible if evidence establishes that specific prompts are:

- authored originally by the repository maintainer/contributors and clearly covered by MIT;
- independently licensed by the original external author under compatible terms;
- derived exclusively from a source whose prompt rights have already been separately approved by Open Prompt Archive and whose transformation remains compatible with that license.

Any such subset requires its own evidence-backed filter and must not be inferred from a generic "rewritten" or "reverse-engineered" label.

## Media decision

`not-allowed`.

The repository contains generated/example images and references to external/public-community images. Prompt-text review does not establish independent media rights, so Open Prompt Archive will not mirror those media assets under this source decision.

## Re-review triggers

Re-review if:

- the project publishes a clear data/content license separate from its software license;
- record-level provenance and licensing become machine-readable and sufficiently complete;
- original-only content can be reliably isolated from externally sourced/derived cases;
- direct rights grants from underlying prompt authors become available.

## Conclusion

**QUARANTINED for bulk prompt import.** The repository is openly licensed as software, but its own disclaimer confirms substantial third-party/community provenance that prevents Open Prompt Archive from treating the complete gallery as a clean MIT prompt dataset.
