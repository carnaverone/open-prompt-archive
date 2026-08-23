# Source Registry

`sources/sources.yaml` is the canonical registry of upstream prompt sources considered by Open Prompt Archive.

The registry is validated conceptually against [`schema/source.schema.json`](../schema/source.schema.json).

## Current reviewed sources

| Source | Status | Claimed / effective license | Approved Open Prompt Archive scope |
|---|---|---|---|
| [prompts.chat](reviews/prompts-chat.md) | `approved` | `CC0-1.0` | Prompt text/data only |
| [DiffusionDB](reviews/diffusiondb.md) | `approved` | `CC0-1.0` | Prompt text + prompt-generation metadata; media excluded |
| [BigScience PromptSource / P3](reviews/bigscience-promptsource.md) | `approved` | `Apache-2.0` | Prompt template definitions + prompt-specific metadata; underlying datasets excluded |
| [YouMind — Nano Banana Pro](reviews/youmind-nano-banana-pro.md) | `quarantined` | `CC-BY-4.0` claimed | None; bulk corpus license scope unresolved |
| [YouMind — GPT Image 2](reviews/youmind-gpt-image-2.md) | `quarantined` | `CC-BY-4.0` claimed | None; bulk corpus license scope unresolved |
| [YouMind — Seedance 2](reviews/youmind-seedance-2.md) | `quarantined` | `CC-BY-4.0` claimed | None; bulk corpus license scope unresolved |

These decisions are intentionally source- and scope-specific. `approved` does not mean every asset in an upstream repository may be mirrored. See each review file for the exact approved material and exclusions.

No prompt corpus from a quarantined source may be committed to `data/` merely because the upstream repository carries an open-license file.

> **Review-status note:** `quarantined` is an Open Prompt Archive curation state, not an allegation that an upstream project is acting unlawfully or that its license declaration is invalid. It means only that this archive has not yet obtained enough evidence to redistribute the intended corpus under its own stricter provenance standard.

## Source states

- `candidate` — discovered or proposed, not yet reviewed.
- `review` — license/provenance evidence is being evaluated.
- `approved` — redistribution basis and intended import scope are verified.
- `quarantined` — unresolved rights/provenance concern; metadata only, no prompt corpus distribution.
- `rejected` — unsuitable for the main archive.

Only `approved` sources may contribute prompt records to `data/`.

## Minimum review information

A source record should identify:

- stable `source_id`;
- canonical name and URL;
- upstream owner/maintainer;
- source type;
- review status;
- license identifier;
- direct license evidence when available;
- whether the license scope was actually verified;
- attribution requirements;
- exact review/import scope;
- pinned revision when practical;
- discovery/review dates;
- media-mirroring decision.

## Human-readable reviews

Complex reviews are documented under [`sources/reviews/`](reviews/) using stable source IDs or unambiguous source names.

Review notes should link to primary evidence and clearly distinguish:

- the license claimed by the upstream project;
- the scope for which Open Prompt Archive verified redistribution;
- unresolved third-party-rights questions;
- media that is explicitly excluded;
- the revision against which the decision was made.

## Review principle

**An upstream open-source license is evidence, not a substitute for provenance analysis.**

When a repository aggregates prompts from unrelated authors, social networks, forums, or other external sources, Open Prompt Archive verifies whether the upstream project actually has authority to place those records under the claimed license. If that link cannot be established, the source remains metadata-only until stronger evidence is available.

The inverse also matters: when a project has a clear contribution workflow that treats prompt templates themselves as contributions to a licensed work, Open Prompt Archive may approve that narrowly defined prompt/template layer while still excluding independently licensed datasets or media referenced by those prompts.
