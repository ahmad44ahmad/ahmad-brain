---
id: 0002-language-policy-and-sources-folder
title: Language Policy Refinement + wiki/sources/ Folder
type: decision
status: accepted
aliases:
  - adr-0002
  - bilingual-policy
  - sources-subdir
tags:
  - architecture
  - adr
  - amendment
  - language-policy
created: 2026-04-24
updated: 2026-04-24
supersedes:
superseded-by:
amends:
  - "[[0001-vault-architecture]]"
deciders:
  - ahmad
  - claude
summary: Amends ADR-0001. Softens "English only" to "English prose, Arabic allowed as data values (proper nouns, titles, aliases, verbatim quotes)". Adds wiki/sources/ as 6th wiki subfolder for distilled external-source notes, so sources stay flat at 2 levels instead of nested 3 levels under projects.
related:
  - "[[0001-vault-architecture]]"
---

# ADR-0002 — Language Policy Refinement + `wiki/sources/`

## Context

ADR-0001 established two rules that on execution review prove too rigid:

### Rigidity 1 — absolute English

ADR-0001 §Decision says: *"Language: English only. No Arabic content in vault files."*

This is lossy in three specific cases:

1. **Proper nouns.** علي القرني, نوير أم عبدالملك, خالد بن صالح الزهراني — the Arabic spelling is the *identity*. Transliteration ("Ali Al-Qarni") is a label; the Arabic form carries the accurate distinguishing information (family lineage بن صالح, kunyas أبو فيصل / أم عبدالملك). Stripping Arabic == losing retrieval keys for Arabic queries.
2. **Governmental register.** Terms like سعادة, مرتبة ممتازة, وكيل, نائب الوزير, صك, محضر إخلاء طرف are not translatable 1:1 — they are positions in a specific Saudi bureaucratic hierarchy. Their English approximations ("His Excellency", "excellent rank", "deputy minister") lose the governance-weight that matters when Ahmad writes to ministers or wakala offices.
3. **Direct quotations.** When Ahmad's sent-mbox shows he wrote "سعادة مدير المركز - سلّمه الله" on 2025-03-03, that sentence is *evidence*. Translating it to "Esteemed Center Director — may God preserve him" is distortion: the original is Arabic, the record should preserve the original, and the citation value depends on exactness.

### Rigidity 2 — no third-level depth

ADR-0001 §Folder layout caps depth at 2 levels. This forces source-distillations like `wiki/sources/pst-mailbox.md` to live either at the wrong level or in the wrong folder. Without a top-level `wiki/sources/`, source notes would go into `wiki/projects/hrsd-work/` pushing the tree to 3 levels, or `wiki/synthesis/` which conflates distilled-from-external with original-cross-cutting.

## Decision

### Amendment 1 — Language policy

**English is the default language for prose, analysis, and structure.** Arabic is explicitly permitted in the following contexts:

- **Titles and aliases:** `title: Ali Al-Qarni` with `aliases: [علي القرني, علي عوض القرني, أبو خالد]` is preferred over English-only.
- **Proper nouns inline:** People's names, organisation names, policy names, place names, kunyas (أبو فيصل, أم عبدالملك), honorifics (سعادة, معالي) — write in Arabic the first time they appear, optionally followed by English transliteration in parentheses.
- **Direct quotes:** When citing what Ahmad or a colleague actually wrote or said, preserve verbatim in Arabic inside markdown blockquotes or code spans.
- **Untranslatable terms:** Governmental-register terms (وكيل, مرتبة ممتازة, صك, محضر, بلاغ), when the English equivalent loses meaning, keep in Arabic with one-time gloss.

**Prohibited:**
- Running prose in Arabic (analysis, summaries, descriptions, introductions).
- Arabic section headings (use English headings).
- Arabic in YAML keys (values OK; `id:` stays slug-ASCII).
- Mixing languages mid-sentence gratuitously.

**Arabic-heavy source material** (voice transcripts, Arabic docs, PST Arabic bodies) → preserve verbatim in `raw/`. The `wiki/` distillation is English prose with Arabic quotes/names where ADR-0002 permits.

### Amendment 2 — `wiki/sources/` added

Add `wiki/sources/` as a sixth top-level `wiki/` subfolder:

- **`wiki/sources/`** — distilled summaries of specific external sources: PST analysis, sent-mbox analysis, a Drive folder digest, a transcribed interview. Each note has `source:` frontmatter pointing to the raw file/Drive ID. Flat — no sub-folders.
- Replaces: previously source-distillations lived under `10-Projects/<name>/sources/` (3 levels, deprecated).
- Distinct from `wiki/synthesis/`: synthesis = original cross-cutting analysis Claude writes; sources = Claude's distillation of one specific external artefact.

Updated folder contract:

| Folder | Purpose |
|---|---|
| `wiki/people/` | One note per human entity |
| `wiki/projects/` | Basira, habibi-tts, pt-modeling, hrsd-work |
| `wiki/concepts/` | Frameworks, doctrines, models |
| `wiki/entities/` | Organisations, policies, locations |
| `wiki/sources/` | **NEW** — distilled external-source notes (one per source) |
| `wiki/synthesis/` | Cross-cutting original essays, MOCs |

### Amendment 3 — file naming for Arabic-source preservation

When preserving Arabic source verbatim in `raw/` alongside an English distillation:

- Arabic source: `raw/<type>/<slug>-ar.md` (suffix `-ar` marks language)
- English distillation: `wiki/sources/<slug>.md` or `wiki/people/<slug>.md` etc. (no suffix)
- Both files share the same `id` slug stem; distillation's `source:` frontmatter points to the raw file.

## Consequences

### Positive
- Arabic identity and governmental-register evidence preserved — no lossy translation.
- Queries in Arabic ("من هو أبو فيصل") hit aliases and find the right note.
- Source-distillations get a clean home; project folders stay focused on project artefacts.
- Depth stays at 2 levels everywhere in `wiki/`.

### Negative
- Migration effort increases slightly: must decide per-note where Arabic belongs (aliases / quotes / raw preservation).
- Need to be careful not to slide back into Arabic prose — the rule against running Arabic analysis must be enforced by discipline, not structure.

### Neutral
- ADR-0001 §Decision language policy paragraph is amended, not superseded — the rest of ADR-0001 stands.

## Phased execution notes

Phase B migration (immediately after this ADR) proceeds under ADR-0002's refined rules:
1. English prose.
2. Arabic in `aliases:` for all people + all Arabic-named organisations/policies.
3. Arabic governmental terms kept inline with English gloss on first use.
4. Arabic-heavy source files (foundation docs, Gemini summaries of 3 Drive folders) → preserve Arabic in `raw/drive/`; write English distillation in `wiki/sources/` or `wiki/synthesis/`.

## References

- [[0001-vault-architecture]] — parent ADR being amended.
- Spisak `wiki/sources/` precedent: https://github.com/NicholasSpisak/second-brain
