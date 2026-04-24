---
id: 0001-vault-architecture
title: Vault Architecture — LLM-Only Markdown Second Brain
type: decision
status: accepted
aliases: [vault-architecture, second-brain-blueprint]
tags: [architecture, adr, foundation]
created: 2026-04-24
updated: 2026-04-24
supersedes:
superseded-by:
deciders: [ahmad, claude]
summary: >-
  Canonical architecture for ahmad-brain vault. LLM-only consumer (Claude).
  English + markdown only. Folders: raw/ wiki/ decisions/ log/ index/.
  Rich YAML frontmatter with stable id. MADR for decisions. Karpathy LLM
  Wiki pattern with Kepano skills layer. Replaces prior PARA+Obsidian-UI
  experiment from sessions 1-6 (not deleted, migrated in Phase B).
related: []
---

# ADR-0001 — Vault Architecture

## Context

The vault at `C:\dev\ahmad-brain\` has gone through six bootstrap sessions (2026-04-24) under a PARA-derived folder scheme, Obsidian Git plugin for versioning, and mixed Arabic + English content. Before the migration scales further, Ahmad's constraint set changed:

1. **Ahmad will never open Obsidian.** Sole reader/writer is Claude via filesystem.
2. **Files must be English + markdown** — no Arabic content, no non-markdown formats, no UI-specific plugin syntax.
3. **Future Claude versions must pick up the vault without instruction** — the architecture must be self-explanatory from `_CLAUDE.md` at root.
4. **Token efficiency is load-bearing** — every design choice trades retrieval cost vs. storage.

Research (2026-04-24 parallel sub-agent scan) surfaced a convergent 2025/2026 pattern across:

- **Andrej Karpathy's LLM Wiki gist** (`442a6bf555914893e9891c11519de94f`) — the taproot idea: `raw/` append-only inbox → LLM compiles → `wiki/` evergreen, direct context-load beats RAG under ~100K tokens.
- **kepano/obsidian-skills** (26K stars, Obsidian CEO, updated 2026-04-02) — official Agent Skills spec; works in `.claude/skills/` at vault root; teaches any skills-compatible agent to speak Obsidian-Flavored Markdown + Bases + JSON Canvas.
- **NicholasSpisak/second-brain** (204 stars, 2026-04-07) — cleanest folder realisation of Karpathy's pattern: `raw/ wiki/{sources,entities,concepts,synthesis} decisions/ log/ index/`.
- **eugeniughelbur/obsidian-second-brain** (270 stars, 2026-04-23) — operational extras: `_CLAUDE.md` per directory, bi-temporal frontmatter (`valid_from` + `learned_at`), nightly reconcile agent.
- **huytieu/COG-second-brain** (361 stars) — worker-to-tmp delegation for heavy ingestion, tiered people profiles (stub→moderate→full).
- **MADR (Markdown Architectural Decision Records)** — append-only, numbered, superseded-never-edited — the only defensible audit pattern for Ahmad's "decisions are permanent" governance instinct.
- **Obsidian team direction** — [Bases](https://help.obsidian.md/bases) (successor to Dataview) reads **only YAML frontmatter**, not inline `key::value`. Frontmatter is now the authoritative metadata surface.

Retrospective consensus from r/ObsidianMD / HN / dev blogs (last 6 months): biggest regret is over-designing taxonomy before observing actual usage. LIFT principle (≤2-3 levels deep, keep flat).

## Decision

Adopt the Karpathy + Spisak + Kepano synthesis as the canonical architecture.

### Folder layout (2 levels max)

```
ahmad-brain/
├── _CLAUDE.md             ← vault operating manual (auto-loaded by Claude Code)
├── README.md              ← 1-paragraph pointer to _CLAUDE.md
├── .claude/
│   └── skills/            ← kepano/obsidian-skills cloned here
├── raw/                   ← append-only ingested sources; never edit, only add
│   ├── drive/
│   ├── pst/
│   ├── voice/
│   └── web/
├── wiki/                  ← Claude-synthesized evergreen knowledge
│   ├── people/            ← one note per human entity
│   ├── projects/          ← basira, habibi-tts, pt-modeling, hrsd-work
│   ├── concepts/          ← disability models, quality frameworks, etc.
│   ├── entities/          ← organizations, policies, locations
│   └── synthesis/         ← cross-cutting essays + MOCs
├── decisions/             ← ADRs: append-only, numbered, MADR-style
├── log/                   ← YYYY-MM-DD session notes, append-only
└── index/                 ← Claude-regenerated indexes; safe to rebuild
```

No `00-Inbox`, no PARA numerics, no `90-Meta`. Old PARA tree stays in place only during Phase B migration; to be archived once migrated.

### Frontmatter schema (authoritative — every note has this)

```yaml
---
id: <stable-kebab-case-slug>          # REQUIRED. Never renamed. Often date-prefixed.
title: <human-friendly title>         # REQUIRED.
type: source | wiki | decision | log | person | project | concept | entity | synthesis | moc
status: active | draft | superseded | archived
aliases: []                           # alternative titles, strings
tags: []                              # flat, plural, kebab-case
created: YYYY-MM-DD
updated: YYYY-MM-DD
summary: >-                           # ~50-word dense abstract, LLM pre-filter
  One paragraph.
related: [[slug-1]], [[slug-2]]       # explicit graph edges, wikilinks by id
source: drive:<fileId> | url:<...> | voice:<timestamp> | session:<id>   # when applicable
valid_from: YYYY-MM-DD                # bi-temporal — when fact is true
learned_at: YYYY-MM-DD                # bi-temporal — when vault learned it
confidence: high | medium | low       # for factual claims, optional
# for decisions only:
supersedes: <id>
superseded-by: <id>
deciders: [ahmad, claude]
---
```

Rules:
- `id` is the stable handle. Filenames may be the slug or the slug prefixed by date (`2026-04-24-<slug>.md`).
- Wikilinks use `[[id]]`, not titles, not paths. Titles change; ids don't.
- `summary` must fit in ~60 tokens — Claude pre-filters on it before reading bodies.
- `related:` is the graph layer. Claude walks it during retrieval.
- `tags:` stay flat and plural (kepano rule). Do not hierarchically nest.

### Note style

- **Medium-density wiki pages**, 500–2000 words per topic, with facets grouped.
- Avoid pure Zettelkasten atomization — fragments inflate retrieval cost for an LLM-only reader.
- Avoid encyclopaedia dumps — if a topic exceeds 2000 words, split by facet into linked notes.

### Decisions (MADR)

- Files: `decisions/NNNN-<slug>.md`, zero-padded sequentially.
- Statuses: `proposed | accepted | deprecated | superseded`.
- To change a decision: create a new ADR that sets `supersedes: NNNN` on itself and `superseded-by: MMMM` on the old one; do **not** edit the old one's body.

### Indexes

Contents of `index/` are regeneratable. Build on demand via Claude walking frontmatter:
- `index/people.md` — all `type: person` with role + track.
- `index/projects.md` — all `type: project` with status.
- `index/timeline.md` — events + decisions chronological.
- `index/open-questions.md` — notes with `status: draft` or unresolved TODOs.

### Skills layer

`kepano/obsidian-skills` cloned into `.claude/skills/` — gives Claude the canonical spec for Obsidian-Flavored Markdown, `.base` YAML query views, JSON Canvas, and `defuddle` web ingestion. Custom skills for this vault (e.g., `/reconcile`, `/lint`, `/log-session`) go under the same directory.

## Consequences

### Positive
- Retrieval is grep-friendly at every layer. `grep -r "type: person" wiki/` is strictly better than navigating PARA.
- Append-only decisions + log give a defensible audit trail matching Ahmad's governance constraint.
- Stable `id:` + wikilinks survive file renames.
- Kepano skills layer is spec-portable: if Ahmad ever switches to OpenCode / Codex / other agent, the vault still works.
- English + markdown makes future parsing cheap — no Arabic tokenization overhead, no Office formats, no plugin-specific syntax.

### Negative
- Phase B migration effort: 35+ existing files need frontmatter rewrite, Arabic → English translation, folder move, and wiki-link conversion. Estimated 1 working session.
- `_CLAUDE.md` at root duplicates some content with `~/CLAUDE.md`; need clean split: global rules in `~/CLAUDE.md`, vault rules in `_CLAUDE.md`.
- The 7 existing people files (50-People) use full Arabic bodies — translation will lose some nuance; Arabic original goes to `raw/voice/` or `raw/drive/` as authoritative source, English wiki version is canonical for retrieval.

### Neutral
- Obsidian UI remains running only as a git-commit daemon (nice-to-have, not required). Could also install a cron job to replace it.
- The deprecated PARA folders stay on disk during Phase B so nothing is lost; moved to `40-Archive/_pre-adr-0001/` after migration and eventually pruned.

## Phased execution

- **Phase A** (this session): Scaffold new folders, install skills, write `_CLAUDE.md`, commit ADR 0001 as the authoritative plan. Leave old structure untouched.
- **Phase B** (next session): Migrate content file-by-file. Translate Arabic → English on the way. Rewrite frontmatter to new schema. Convert links to wikilink-by-id.
- **Phase C**: Generate first version of `index/*.md`. Retire old `90-Meta/` and PARA folders under `40-Archive/_pre-adr-0001/`.
- **Phase D**: Smoke test retrieval — pick 5 queries Ahmad might ask, verify vault answers correctly.
- **Phase E**: Lock architecture into `~/CLAUDE.md` and `MEMORY.md` so future Claude sessions inherit it.

## References

- Karpathy LLM Wiki gist: https://gist.github.com/karpathy/442a6bf555914893e9891c11519de94f
- kepano/obsidian-skills: https://github.com/kepano/obsidian-skills
- NicholasSpisak/second-brain: https://github.com/NicholasSpisak/second-brain
- eugeniughelbur/obsidian-second-brain: https://github.com/eugeniughelbur/obsidian-second-brain
- huytieu/COG-second-brain: https://github.com/huytieu/COG-second-brain
- MADR: https://adr.github.io/madr/
- Obsidian Bases: https://help.obsidian.md/bases
- kepano — file-over-app: https://stephango.com/file-over-app
