# Repository Discoverability

Open Prompt Archive should be easy to understand and find through GitHub search, general search engines, code search and AI/agent indexing without resorting to keyword stuffing.

## Recommended GitHub description

Use this repository description:

> Provenance-first, license-aware open AI prompt dataset for image, video, LLM, agent, coding, audio and 3D workflows.

## Recommended GitHub topics

Use a focused set of relevant topics rather than every possible synonym:

- `ai-prompts`
- `prompt-engineering`
- `prompt-dataset`
- `generative-ai`
- `image-generation`
- `video-generation`
- `llm`
- `ai-agents`
- `open-data`
- `dataset`
- `provenance`
- `licensing`
- `rag`
- `mcp`
- `sqlite`

Topics should reflect actual repository capabilities. Remove or delay topics for features that do not yet exist in usable form.

## README strategy

The README should naturally contain the phrases users are likely to search for, especially near the beginning:

- AI prompt dataset
- prompt engineering
- generative AI prompts
- image prompts
- video prompts
- LLM prompts
- AI agent prompts
- open prompt library
- prompt provenance
- prompt licensing
- open data

Do not create artificial keyword blocks or repeat phrases solely for ranking.

## GitHub search and indexing principles

Maintain:

1. a specific repository name and description;
2. a strong first paragraph in `README.md`;
3. accurate GitHub topics;
4. descriptive file and directory names;
5. stable releases when datasets/tooling become versioned;
6. changelogs or release notes for meaningful public milestones;
7. inbound links from relevant documentation/projects when appropriate;
8. machine-readable schemas and source manifests;
9. useful issue/PR history rather than automated noise;
10. consistent terminology across README, docs and metadata.

Search ranking is controlled by GitHub/search engines and cannot be guaranteed. Optimize for relevance, accuracy, authority and real project use rather than attempting to manipulate ranking.

## Agent discoverability

The repository exposes several layers of machine-readable guidance:

- `AGENTS.md` for general agent governance;
- `.github/copilot-instructions.md` for GitHub Copilot repository context;
- `.github/instructions/*.instructions.md` for path-specific constraints;
- `.github/skills/*/SKILL.md` for reusable task-specific Agent Skills;
- `schema/prompt.schema.json` for canonical record structure;
- `sources/sources.yaml` for source status and provenance.

This hierarchy should remain concise and non-conflicting.

## Future public metadata

When the first stable dataset release exists, consider adding:

- `CITATION.cff` if the project is intended to be cited academically;
- release artifacts with checksums;
- dataset cards for major published snapshots;
- a changelog;
- a project website or documentation page with canonical links;
- package or dataset registry metadata if distribution moves to PyPI, Hugging Face or another registry.

Do not advertise counts, compatibility or supported formats until they are generated and verified from the repository itself.
