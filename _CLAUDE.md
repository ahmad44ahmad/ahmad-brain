---
id: vault-operating-manual
title: Vault Operating Manual
type: wiki
status: active
tags: [vault-rules, claude-config, operating-manual]
created: 2026-04-24
updated: 2026-04-24
summary: >-
  Authoritative vault rules. LLM-only consumer (Claude). English + markdown.
  Karpathy LLM Wiki pattern + Kepano skills + MADR decisions.
  Auto-loaded by every Claude Code session in this directory.
related: [[0001-vault-architecture]]
---

# Vault Operating Manual

**Read this first, every session.** Authoritative rules live here. Full rationale in [[0001-vault-architecture]].

## Who reads this vault

**Claude only.** The human owner never opens Obsidian. He interacts exclusively through Claude Code in this directory. Every design choice optimises for LLM retrieval, not human browsing.

## Absolutes

- **Language:** English is the default for prose, analysis, headings, and structure. Arabic is permitted only as data: `aliases:` values, proper nouns inline, verbatim quotes in blockquotes, untranslatable governmental terms with one-time English gloss. No running Arabic prose. Arabic-heavy sources preserved verbatim in `raw/` with `-ar` suffix; the `wiki/` distillation is English with Arabic quotes as needed. See [[0002-language-policy-and-sources-folder]] for the full policy.
- **Format:** Markdown only. No docx, xlsx, pdf, or plugin-specific syntax.
- **Frontmatter:** Every note has YAML frontmatter matching the schema below. No exceptions.
- **Atomicity:** Medium-density wiki pages (500–2000 words). Not Zettelkasten fragments, not encyclopaedia dumps.
- **IDs, not paths:** Wikilinks use `[[id]]`, not titles, not file paths. Titles change; ids don't.
- **Append-only decisions:** ADRs in `decisions/` are numbered and never edited. Supersede with a new ADR.
- **Raw is immutable:** Files in `raw/` are never modified. Claude writes only to `wiki/`, `decisions/`, `log/`, `index/`.

## Frontmatter schema

```yaml
---
id: <stable-kebab-case-slug>          # REQUIRED. Never renamed.
title: <human-friendly title>         # REQUIRED.
type: source | wiki | decision | log | person | project | concept | entity | synthesis | moc
status: active | draft | superseded | archived
aliases: []                           # alternative names, strings
tags: []                              # flat, plural, kebab-case
created: YYYY-MM-DD
updated: YYYY-MM-DD
summary: >-                           # ~50-word dense abstract, LLM pre-filter
  One paragraph.
related: [[slug-1]], [[slug-2]]       # explicit graph edges
# Optional when applicable:
source: drive:<fileId> | url:<...> | voice:<ts> | session:<id>
valid_from: YYYY-MM-DD                # bi-temporal — fact's real-world start
learned_at: YYYY-MM-DD                # bi-temporal — when vault learned it
confidence: high | medium | low
# Decisions only:
supersedes: <id>
superseded-by: <id>
deciders: [ahmad, claude]
---
```

## Folder contract

| Folder | Purpose | Write mode |
|---|---|---|
| `raw/` | Ingested sources — Drive exports, PST dumps, voice transcripts, web clips | **Append only.** Never edit. |
| `wiki/people/` | One note per human entity. Stable `id`. | Append + edit |
| `wiki/projects/` | Basira, habibi-tts, pt-modeling, hrsd-work, etc. | Append + edit |
| `wiki/concepts/` | Mental models, frameworks, doctrines (CRPD, EFQM, disability-compass) | Append + edit |
| `wiki/entities/` | Organisations, policies, locations, regulations (MHRSD, CRC Al-Baha) | Append + edit |
| `wiki/sources/` | Distilled external-source notes — one per source (PST, mbox, Drive folder, interview). `source:` frontmatter mandatory. | Append + edit |
| `wiki/synthesis/` | Cross-cutting original essays, retrospectives, MOCs | Append + edit |
| `decisions/` | ADRs (NNNN-slug.md), MADR-style | **Append only.** New ADR to supersede. |
| `log/` | `YYYY-MM-DD.md`, one per active day | **Append only** within a day's file. |
| `index/` | Regeneratable MOCs (people, projects, timeline, open-questions) | Overwrite OK. |
| `.claude/skills/` | Kepano skills + custom vault skills | Per-skill SKILL.md |

No `00-Inbox`, no PARA-style numeric folders, no `90-Meta`. The 2-level cap is enforced.

## When to write where

- **Ahmad dumps raw context** (voice msg, doc paste, file upload) → `raw/<source-type>/YYYY-MM-DD-<slug>.md` with full verbatim preserved. Then cook into `wiki/`.
- **A new person mentioned** → create `wiki/people/<slug>.md` with stable id + link all references to it.
- **A new project begins** → create `wiki/projects/<slug>.md`. Sub-facets as separate notes in same folder, linked via `related:`.
- **A decision is made** → new ADR `decisions/NNNN-<slug>.md`. Never edit prior ADRs.
- **Session-level work happens** → append to today's `log/YYYY-MM-DD.md`. One file per active day.
- **An index needs refresh** → regenerate `index/*.md` from current wiki frontmatter; do not edit indexes by hand.

## Retrieval patterns (when Ahmad asks a question)

1. Read `_CLAUDE.md` (this file).
2. Read `index/` if the question is broad ("who's approving Basira?", "what's active?").
3. `grep` wiki frontmatter for `type:` + `tags:` matching the question.
4. Follow `related:` edges as needed; stop at depth 2.
5. If no match: check `raw/` for relevant sources; synthesize into a new `wiki/` note if the answer warrants permanent memory.
6. For factual claims with dates, prefer notes where `confidence: high` and `valid_from:` post-dates other candidates.

## Skills available

Under `.claude/skills/`:
- `obsidian-markdown` — Obsidian Flavored Markdown syntax (wikilinks, callouts, embeds)
- `obsidian-bases` — `.base` YAML query views (grep-friendly alternative to Dataview)
- `obsidian-cli` — Obsidian CLI operations
- `json-canvas` — JSON Canvas spec for structured graphs
- `defuddle` — web clipping into clean markdown

Custom vault skills (planned, Phase C+): `/reconcile`, `/lint`, `/log-session`, `/regenerate-indexes`.

## Memory ↔ vault boundary

- **Memory (`~/.claude/projects/C--Users-aass1/memory/`)** = always-loaded hot cache. Profile, language policy, feedback rules, vault pointer, glossary. ~20 small files max.
- **Vault (`C:\dev\ahmad-brain\`)** = on-demand store. Everything else.
- Migration direction is memory → vault. Never reverse. Shrunk memory files keep a one-line pointer to the vault entity.

## Never

- Overwrite a file in `raw/`.
- Edit an accepted ADR body (only status/superseded-by).
- Write running prose in Arabic (English prose only; Arabic as data per [[0002-language-policy-and-sources-folder]]).
- Use PARA / nested folders / numeric prefixes.
- Create a wikilink to a non-existent id — create the stub note first.
- Hold Arabic text outside `raw/`.

## Self-audit (on explicit trigger, not scheduled)

- **`/lint`** — validate every `wiki/` note has required frontmatter + resolvable `[[links]]`.
- **`/reconcile`** — flag contradictions (two notes asserting opposite claims about the same id).
- **`/regenerate-indexes`** — rebuild `index/*.md` from current wiki frontmatter.

## Provenance

Architecture defined in [[0001-vault-architecture]]. Prior PARA layout (sessions 1-6) still on disk under old folders; being migrated in Phase B.
