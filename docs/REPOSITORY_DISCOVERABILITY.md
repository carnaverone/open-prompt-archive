# Repository Discoverability

Open Prompt Archive should be easy to understand and find through GitHub search, general search engines, code/data indexing, and AI/agent retrieval without keyword stuffing or unsupported claims.

## Recommended GitHub description

Use this repository description:

> Curated open AI prompt dataset with verified licensing, provenance and attribution for image, video, LLM and agent prompts.

This wording prioritizes what the repository **is now**: a curated dataset/archive with licensing and provenance controls.

## Recommended GitHub topics

Use a focused set of topics that reflect the repository's current scope:

- `ai-prompts`
- `prompt-engineering`
- `prompt-dataset`
- `prompt-library`
- `generative-ai`
- `open-data`
- `dataset`
- `provenance`
- `licensing`
- `creative-commons`
- `image-generation`
- `video-generation`
- `llm`
- `ai-agents`

Add narrower topics such as coding/audio/3D only when the published dataset actually contains meaningful coverage in those categories.

Do not add `mcp`, `sqlite`, `rag`, or other tooling topics merely because they are possible future uses. Topics should describe current repository content/capabilities.

## README search strategy

The README should use high-value phrases naturally near the beginning and in descriptive headings:

- AI prompt dataset;
- open prompt dataset;
- prompt engineering;
- generative AI prompts;
- image prompts;
- video prompts;
- LLM prompts;
- AI agent prompts;
- prompt library;
- prompt provenance;
- prompt licensing;
- open data.

Do not create artificial keyword blocks, hidden text, repeated synonym lists, or exaggerated counts solely for ranking.

## GitHub and web indexing principles

Maintain:

1. a specific repository name and concise About description;
2. an accurate first paragraph in `README.md`;
3. focused GitHub topics;
4. descriptive file/directory names;
5. stable dataset releases when data is published;
6. `CITATION.cff` and dataset-card metadata;
7. changelog/release notes for material public milestones;
8. source registry and machine-readable schemas;
9. useful issue/PR history rather than automated activity noise;
10. consistent terminology across README, dataset card, docs, source records, and releases;
11. legitimate inbound references from projects/research that actually use the dataset.

Search ranking is controlled by GitHub and external search engines and cannot be guaranteed. Optimize for accuracy, relevance, authority, reuse, citations, and real community activity.

## Data/agent discoverability

The repository exposes machine-readable and agent-readable context without making agent tooling the public identity of the project:

- `DATASET_CARD.md` — dataset summary, scope, limitations, curation and use;
- `CITATION.cff` — citation metadata;
- `schema/prompt.schema.json` — prompt record contract;
- `schema/source.schema.json` — source registry contract;
- `sources/sources.yaml` — source-review status and evidence metadata;
- `AGENTS.md` — repository governance for AI-assisted work;
- `.github/skills/` — optional specialized review guidance.

The dataset and its evidence remain the primary product. Agent configuration is supporting infrastructure.

## Release discoverability

When the first verified prompt corpus is ready, each stable release should publish or document:

- version identifier;
- release date;
- verified record/source counts generated from data;
- included source IDs;
- license distribution summary;
- integrity/checksum information for release artifacts where practical;
- material schema/policy changes;
- known limitations.

Consider publishing stable snapshots to a recognized dataset registry such as Hugging Face or Zenodo later, with the GitHub repository retained as the canonical governance/provenance source.

## Claims policy

Do not advertise:

- prompt counts that were copied from upstream marketing;
- model compatibility that was not verified;
- license verification that did not occur;
- rankings such as “largest”, “best”, or “most complete” without defensible evidence.

Credibility is itself a discoverability asset for a provenance-first dataset.
