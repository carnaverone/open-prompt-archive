# Source Review — BigScience PromptSource / P3 prompt templates

- **Source ID:** `bigscience-promptsource`
- **Canonical repository:** `https://github.com/bigscience-workshop/promptsource`
- **Upstream project:** BigScience PromptSource / Public Pool of Prompts (P3)
- **Reviewed revision:** `7dab96a3eeb3717cea633705135ebc488885d709`
- **Review date:** 2026-08-23
- **Decision:** `approved`
- **Approved scope:** repository-authored/contributed prompt template definitions under `promptsource/templates/` and their prompt-specific metadata
- **Underlying datasets/examples:** excluded
- **Associated media:** excluded

## Evidence reviewed

1. The repository root `LICENSE` is Apache License 2.0.
2. Apache-2.0 defines intentionally submitted contributions to the licensed work and states that, unless explicitly stated otherwise, contributions intentionally submitted for inclusion are provided under the same license.
3. The PromptSource README describes P3 as a collection of natural-language prompts stored as standalone structured files in the repository and identifies the repository as the tool used to create and share them.
4. `CONTRIBUTING.md` instructs contributors to write prompt templates and submit them to the repository through pull requests.
5. The canonical prompt corpus is present under `promptsource/templates/` at the reviewed revision.

## License assessment

**Effective license for the reviewed repository prompt-template work:** `Apache-2.0`.

The licensing chain is materially stronger than a third-party aggregation with a wrapper license: the repository describes contributors as authoring prompts for inclusion, contribution happens through project pull requests, and Apache-2.0 explicitly addresses contributions intentionally submitted to the licensed work.

## Critical scope boundary

PromptSource templates are functions over external datasets. The approval **does not include the underlying datasets, examples, labels, generated prompted examples, or third-party dataset content** merely because a PromptSource template references their field names.

Open Prompt Archive may redistribute the prompt-template expressions and prompt-specific metadata that form part of the licensed PromptSource work. It must not materialize and republish underlying dataset rows unless those datasets pass separate licensing/provenance review.

Similarly, prompt references to papers or datasets do not make those referenced works part of this approval.

## Import conditions

A future import may retain:

- template UUID when available as `source.upstream_id`;
- prompt/template name as title;
- Jinja prompt template text;
- prompt-specific metadata such as language, original-task flags, answer-choice template metadata, and references when representable without importing third-party dataset content;
- canonical dataset/subset identifiers as provenance/classification metadata.

The import must:

- pin the reviewed revision;
- preserve the Apache-2.0 license and applicable attribution/notices;
- identify BigScience PromptSource/P3 as the upstream source;
- preserve template semantics rather than rendering templates against external dataset examples;
- avoid claiming that downstream datasets share the Apache-2.0 license;
- avoid copying generated examples that contain external dataset text.

## Data-model note

PromptSource records are **templates**, not always standalone literal prompts. Open Prompt Archive should preserve Jinja expressions as prompt text and mark their templated nature through a documented classification/metadata convention before publication rather than flattening them into fabricated example prompts.

If the current canonical schema cannot express required template metadata cleanly, schema evolution should precede import.

## Media decision

`not-allowed` for the initial Open Prompt Archive scope. Repository screenshots, logos, paper figures, and other media are not required for a prompt-template archive.

## Re-review triggers

Re-review if:

- repository licensing changes;
- prompt templates move into an independently licensed artifact;
- a planned import begins to include rendered dataset examples or underlying dataset content;
- specific templates contain externally copied text whose licensing cannot be explained by the repository contribution model.

## Conclusion

**APPROVED for the repository's prompt-template definitions and prompt-specific metadata under Apache-2.0, with external dataset content explicitly excluded.**
