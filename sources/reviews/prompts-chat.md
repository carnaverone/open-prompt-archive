# Source Review — prompts.chat

- **Source ID:** `prompts-chat`
- **Canonical repository:** `https://github.com/f/prompts.chat`
- **Upstream project:** prompts.chat (formerly Awesome ChatGPT Prompts)
- **Reviewed revision:** `25cb43d6e61974e66f3650cbc5a65482bc592552`
- **Review date:** 2026-08-23
- **Decision:** `approved`
- **Approved scope:** prompt text/data only
- **Associated media:** not approved for mirroring by Open Prompt Archive

## Evidence reviewed

1. Repository `LICENSE` explicitly uses a dual-license model and states that `prompts.csv`, `PROMPTS.md`, and all user-submitted prompt text are dedicated to the public domain under **CC0 1.0 Universal**.
2. `LICENSE-CC0` contains the CC0 1.0 Universal legal text.
3. The prompts.chat Terms of Service state that prompts submitted through the platform are immediately and irrevocably released under CC0, that submitters waive copyright and related rights to the extent possible under law, and that users must not submit content infringing third-party intellectual-property rights.
4. `CONTRIBUTING.md` directs prompt contributions through prompts.chat accounts and records contributors.

## License assessment

**Effective prompt-data license:** `CC0-1.0`

The repository provides unusually clear separation between software/site content and prompt data. Prompt content is explicitly identified as CC0 rather than relying on the software license by implication.

The current submission flow also gives direct notice that submitted prompt content is released under CC0. This provides stronger provenance than repositories that merely place a top-level license over prompts collected from unrelated external authors.

## Import conditions

An Open Prompt Archive import may include:

- prompt text from `prompts.csv` and/or `PROMPTS.md`;
- stable upstream prompt identifiers where available;
- title/category/contributor metadata that is part of the prompt dataset;
- canonical source URL and pinned revision metadata.

The import must not assume that unrelated site code, book content, logos, uploaded media, or external links are CC0 merely because prompt data is CC0.

Open Prompt Archive should preserve the upstream source even though CC0 does not require attribution, because provenance is a project-level data-quality requirement.

## Media decision

`not-allowed` for the initial import.

The approved scope is prompt text/data. Preview images, video, audio, trademarks, profile images, and other media are outside this approval unless separately reviewed.

## Re-review triggers

Re-review if:

- the upstream dual-license statement changes;
- submission terms stop applying CC0 to prompt content;
- the canonical prompt files move to a different licensing model;
- imported records are sourced from areas of the project not covered by the explicit prompt-data CC0 statement.

## Conclusion

**APPROVED for prompt text/data under CC0-1.0, at the reviewed revision and within the scope above.**
