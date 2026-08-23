# BigScience PromptSource / P3 — Publication Contract

This directory is reserved for normalized Open Prompt Archive records derived from the approved PromptSource/P3 **prompt-template layer only**.

## Source lock

- **Source ID:** `bigscience-promptsource`
- **Canonical upstream:** `https://github.com/bigscience-workshop/promptsource`
- **Reviewed revision:** `7dab96a3eeb3717cea633705135ebc488885d709`
- **Effective prompt-template license:** `Apache-2.0`
- **Approved upstream area:** `promptsource/templates/`
- **Source review:** [`sources/reviews/bigscience-promptsource.md`](../../../sources/reviews/bigscience-promptsource.md)

## Scope boundary

PromptSource templates operate on independently licensed datasets. Open Prompt Archive may archive the **template expressions and prompt-specific metadata**, but it must not turn those templates into a back door for redistributing the underlying datasets.

Do not publish:

- rendered prompt examples containing external dataset rows;
- dataset questions, contexts, articles, labels, or other source examples merely because a Jinja template can access them;
- cached/manual dataset files;
- generated P3 training/evaluation examples unless the underlying dataset rights are separately reviewed.

## Canonical content

A PromptSource prompt is a templated program-like natural-language instruction, commonly containing Jinja expressions and an input/target separator.

The canonical archived `prompt` value should therefore preserve the original template expression rather than replacing variables with fabricated examples.

Example shape:

```text
{{premise}}
Question: Does this imply that "{{hypothesis}}"? Yes, no, or maybe?
||| {{answer_choices[label]}}
```

## Identifier mapping

PromptSource exposes UUIDs for templates. When a stable upstream template UUID is available:

- retain it as `source.upstream_id`;
- derive the Open Prompt Archive ID deterministically from `source_id + upstream UUID`;
- do not replace an existing upstream UUID with a title-based slug.

Recommended shape:

```text
bigscience-promptsource-<upstream-uuid>
```

## Metadata mapping

Useful prompt-specific metadata may include:

- template name/title;
- dataset and subset identifier as source context;
- template UUID;
- language metadata;
- original-task flag;
- answer-choice template metadata;
- prompt/template reference;
- metrics metadata when it describes the prompt task rather than copying external dataset content.

If the canonical prompt schema cannot represent a useful field cleanly, omit it or evolve the schema deliberately. Do not overload unrelated fields.

## Record type

Canonical records should generally use:

```text
type: llm
```

because the templates are natural-language task prompts for language-model workflows.

## License and attribution

Every published record must preserve:

```text
Apache-2.0
BigScience PromptSource / P3 provenance
reviewed revision
applicable upstream attribution/copyright notices
```

Do not assign Apache-2.0 to the external datasets referenced by a template.

## Semantic fidelity

Preserve Jinja syntax, separators, literal strings, conditionals, and answer-choice expressions. Formatting changes that alter template behavior count as semantic modification and must not occur silently.

## Publication gate

Before publication:

1. enumerate templates only from the reviewed source area;
2. preserve upstream UUIDs;
3. verify template parsing/serialization does not alter semantics;
4. exclude rendered external dataset examples;
5. retain Apache-2.0 notices;
6. validate canonical records against `schema/prompt.schema.json`;
7. generate exact record counts and SHA-256 checksums;
8. create a manifest conforming to `schema/manifest.schema.json`.
