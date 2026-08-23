# prompts.chat — Publication Contract

This directory is reserved for normalized Open Prompt Archive records derived from the approved `prompts-chat` source.

## Source lock

- **Source ID:** `prompts-chat`
- **Canonical upstream:** `https://github.com/f/prompts.chat`
- **Reviewed revision:** `25cb43d6e61974e66f3650cbc5a65482bc592552`
- **Primary input:** `prompts.csv`
- **Pinned Git blob SHA-1:** `1bc70c691fb71cc11d8b5031efd0e1ba1b4a0697`
- **Pinned byte size:** `5,632,658`
- **Effective prompt-data license:** `CC0-1.0`
- **Machine-readable acquisition lock:** [`source.lock.json`](source.lock.json)
- **Source review:** [`sources/reviews/prompts-chat.md`](../../../sources/reviews/prompts-chat.md)
- **Registry entry:** [`sources/sources.yaml`](../../../sources/sources.yaml)

The reviewed upstream license explicitly identifies `prompts.csv`, `PROMPTS.md`, and user-submitted prompt text as CC0 prompt data. Repository code, interactive-book content, branding, and unrelated media are outside this import scope.

The importer must verify the exact Git blob identity before parsing. Git blob identity is calculated as SHA-1 over `blob <byte-length>\0<raw-bytes>`, matching Git's object model. A same-named file with different bytes is rejected.

## Preferred upstream input

Use the pinned `prompts.csv` at the reviewed revision as the primary tabular input for deterministic import.

Observed upstream columns at the reviewed revision:

```text
act
prompt
for_devs
type
contributor
```

The upstream CSV is the acquisition format. It is **not** Open Prompt Archive's canonical publication format.

## Canonical mapping

| Upstream field | Open Prompt Archive field | Rule |
|---|---|---|
| `act` | `title` | Preserve source text; use `null` only when the field is empty. |
| `prompt` | `prompt` | Preserve semantic content exactly. Do not rewrite, translate, summarize, or "improve" the prompt. |
| `contributor` | `source.author` | Preserve non-email public identifiers/handles when present. Exact email identifiers are omitted from public `source.author` as deterministic privacy minimization. The original upstream field remains part of the frozen record-ID input so source identity remains reproducible. |
| `type` | source classification input | Raw field is not published as a model-compatibility claim. |
| `for_devs` | source classification input | Raw field is not published in v1. |

Canonical record `type` is `llm` for this source in normalization v1. `models`, `tags`, and `language` are not invented from generic upstream labels.

## Stable record identifiers — frozen v1 algorithm

The first publication contract freezes the following deterministic identifier algorithm.

For each decoded CSV record, construct this ordered JSON array:

```json
[
  "prompts-chat-id-v1",
  "<act>",
  "<prompt>",
  "<for_devs>",
  "<type>",
  "<contributor>"
]
```

Serialize it as UTF-8 JSON with:

- `ensure_ascii = false`;
- separators exactly `,` and `:` with no added spaces;
- source field values preserved exactly as returned by the CSV parser.

Then compute SHA-256 over those bytes and publish:

```text
prompts-chat-<full-64-character-lowercase-sha256>
```

The full digest is used rather than a short prefix. Input row order is **not** part of the identifier. Exact duplicate decoded rows therefore produce the same identifier and are collapsed deterministically; the duplicate count is recorded in the manifest.

Normalization algorithm version: `prompts-chat-v1`.

## License metadata

Every published record from this source must include:

```json
{
  "license": {
    "spdx": "CC0-1.0",
    "attribution_required": false,
    "attribution": null,
    "scope_verified": true
  }
}
```

`source.author` preserves eligible non-email upstream contributor identifiers even though attribution is not a CC0 obligation. Exact email identifiers are not republished in this field.

## Provenance metadata

Every published record must identify:

- `source.source_id: prompts-chat`;
- the pinned upstream file URL;
- the reviewed source revision;
- source-relative CSV row position for that pinned revision;
- retrieval/import date;
- SHA-256 of the preserved prompt UTF-8 text;
- `provenance.verified: true`;
- `provenance.modified: false` when prompt semantics are preserved.

CSV decoding and deterministic JSON serialization are transport transformations only; v1 does not rewrite prompt text.

## Content review

Open licensing does not automatically require publication of every upstream row.

The v1 importer applies deterministic screening for:

- empty or malformed rows;
- exact decoded-row duplicates;
- private-key-like blocks;
- token/credential-like strings;
- email-address-like content requiring privacy review;
- a narrow set of terms indicating possible credential theft, malware distribution, phishing, ransomware, keylogging, infostealing, or spam-campaign purpose.

Heuristic matches are **review candidates, not automatic findings of wrongdoing or actual credential exposure**. They are held out of candidate publication shards until an explicit `include` or `exclude` decision is supplied. Problematic prompts are not silently rewritten.

Contributor metadata receives a separate deterministic privacy-minimization pass. Exact email identifiers in the upstream `contributor` field are omitted from public `source.author`; non-email handles in mixed contributor fields are preserved. The importer records the number of affected records and removed email identifiers in its audit report and manifest notes. This metadata minimization does not alter prompt text or the frozen record-ID input.

The staging importer separates:

```text
<build>/
├── publish/   # candidate manifest + JSONL shards
└── audit/     # local review material; do not publish review-queue.jsonl
```

`audit/review-queue.jsonl` may contain text intentionally held for review and must not be copied into the public dataset.

## Import tooling

Canonical importer:

```text
scripts/import/prompts_chat.py
```

It requires a local copy of the pinned CSV and never downloads upstream content itself. This keeps acquisition explicit and allows the script to verify the exact Git object before normalization.

Example staging invocation:

```bash
python scripts/import/prompts_chat.py \
  --input /path/to/prompts.csv \
  --output-dir build/prompts-chat-2026-08-23 \
  --retrieved-at 2026-08-23
```

The output directory must not already exist. Curation dependencies are listed in `scripts/requirements.txt`.

A `published` manifest cannot be generated while review candidates remain unresolved and requires explicit dataset-version and publication-date metadata.

## Distribution

The upstream CSV is approximately 5.6 MB. Normalized data is sharded deterministically with an 8 MiB target by default, below the repository's preferred roughly-10-MiB text-shard target when practical.

Canonical public layout:

```text
data/sources/prompts-chat/
├── README.md
├── source.lock.json
├── manifest.yaml
├── part-00000.jsonl
└── ...
```

Only the files under an importer's `publish/` directory are publication candidates. Local audit files remain outside the canonical public dataset.

## Publication gate

No JSONL file in this directory should be described as a released dataset until:

1. source bytes match `source.lock.json` exactly;
2. v1 deterministic mapping and record IDs reproduce;
3. every record validates against `schema/prompt.schema.json`;
4. all content-policy review candidates have explicit decisions;
5. exclusion and duplicate counts are generated from the actual input;
6. record counts are generated from final artifacts;
7. exact artifact byte sizes and SHA-256 checksums are generated;
8. `manifest.yaml` validates against `schema/manifest.schema.json`;
9. only publication-candidate files are promoted into `data/`;
10. `DATASET_CARD.md`, `CHANGELOG.md`, and release metadata are updated from actual published artifacts.
