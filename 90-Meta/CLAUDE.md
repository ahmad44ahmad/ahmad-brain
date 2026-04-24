---
type: meta
status: active
track: personal
lang: en
created: 2026-04-24
updated: 2026-04-24
tags: [vault-rules, operating-manual]
---

# Ahmad-Brain Vault — Operating Manual (for Claude)

This file is the operating manual for **this Obsidian vault**. Read it first whenever you open this directory in Claude Code. It is intentionally short. The long user-level rules live in `~/.claude/CLAUDE.md` and `~/.claude/projects/C--Users-aass1/memory/`.

## What this vault is

The deep store for Ahmad's second brain — projects, people, decisions, sources, daily notes. The Claude memory system at `~/.claude/projects/C--Users-aass1/memory/` remains the **hot cache** (profile, feedback rules, glossary). This vault is everything else.

Rule of thumb:
- If a fact must be loaded into every conversation → memory.
- If a fact is queried on demand → vault.

## Folder contract

| Folder | Purpose | What goes in |
|---|---|---|
| `00-Inbox/` | Raw capture | Anything, briefly. Nothing stays > 7 days. Move to a real folder or delete. |
| `10-Projects/` | Active, deadline-bound | basira / habibi-tts / pt-modeling / hrsd-work |
| `20-Areas/` | Ongoing standards, no end date | pt-practice, quality-excellence, career, personal |
| `30-Resources/` | Reference to reuse | arabic-gov-style, ai-models, supabase-react, obsidian-itself |
| `40-Archive/` | Done/dropped — NEVER deleted | Anything that was in 10/20/30 and is no longer active |
| `50-People/` | One file per person | Stable IDs, governance layer, colleagues, family if relevant |
| `60-Daily/` | One file per day, `YYYY-MM-DD.md` | Only create when actually used |
| `90-Meta/` | Vault rules, templates | This file, rules.md, templates/ |

**Move, don't copy.** Archive is a directory, not a tag. A project that ends goes into `40-Archive/` with its full tree.

## Frontmatter contract (REQUIRED on every note)

```yaml
---
type: project | area | resource | person | daily | decision | source | meeting | meta
status: active | paused | done | archived
track: basira | tts | pt | hrsd | career | personal
lang: ar | en
created: YYYY-MM-DD
updated: YYYY-MM-DD
tags: []
---
```

Rules:
- Every field except `tags` is required.
- `type` and `track` are the two most queried fields. Get them right.
- `updated` = last meaningful edit (not every typo fix).
- **One language per note.** If a note needs both Arabic and English, split it into two files and link them via `[[...]]`.
- Arabic notes: filenames in English/transliteration for cross-platform safety (e.g., `ali-alqarni.md` not `علي-القرني.md`). Title inside the file is in Arabic.

## Link conventions

- Use `[[wiki-links]]` not markdown links for intra-vault references.
- Always link people by their file in `50-People/`: `[[ali-alqarni]]`.
- Projects link to people who govern them. People files link back to projects they touch.
- Don't create a new person file for a one-mention name — put them in `30-Resources/people-to-watch.md` until a second mention.

## What Claude should do in this vault

**Primary jobs:**
1. **Capture** — when Ahmad dumps context, write it to `00-Inbox/` with correct frontmatter.
2. **Cook** — turn inbox raw into structured notes in the right folder. Preserve the raw source link.
3. **Connect** — add `[[wiki-links]]` between related notes when they clearly relate.
4. **Query** — use frontmatter + Dataview to answer Ahmad's questions without reading every file.
5. **Audit** — weekly, surface notes with missing/stale frontmatter and notes in `00-Inbox/` older than 7 days.

**Never:**
- Overwrite a user-edited file (check mtime — if < 10 minutes, save as `*_v2.md`).
- Delete anything from `40-Archive/`.
- Mix languages in one file.
- Create a new folder without updating this CLAUDE.md.
- Add CBAHI references, personalization, or Tamkeen/Masarrah/Basira into PT modeling notes. See `~/.claude/projects/C--Users-aass1/memory/feedback_pt_project_rules.md`.

## Memory ↔ vault sync

The canonical pointer is `~/.claude/projects/C--Users-aass1/memory/MEMORY.md`. When a memory file is migrated into the vault:
1. Write the new file in the vault with full frontmatter.
2. Shrink the memory file to a one-line pointer: `See [[vault/path]]`.
3. Update `MEMORY.md` index entry.

Do not delete memory files. They are the history of the decision to migrate.

## Verification before saying "done"

For any vault task, check the user-visible outcome:
- File exists at the path I claimed.
- Frontmatter parses (has all required fields).
- Links resolve (no red `[[broken]]`).
- If I made a claim like "I moved X", grep for the old path to confirm it's gone.

See `~/.claude/projects/C--Users-aass1/memory/feedback_final_step_failures.md` for why this matters.
