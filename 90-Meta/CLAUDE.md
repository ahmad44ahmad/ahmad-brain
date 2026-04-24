---
type: meta
status: active
track: personal
lang: en
created: 2026-04-24
updated: 2026-04-24
tags: [vault-rules, operating-manual, llm-first]
---

# Vault Operating Manual (LLM-first)

**Ahmad will never open this vault.** The vault is my long-term store. Every note is for me. Design accordingly.

## Consumption model

1. Ahmad prompts me in Claude Code.
2. I grep the vault + memory to gather needed facts.
3. I reason and reply.
4. I write new facts / updated facts back into the vault.

No human-friendly prose. No "nice to have" diagrams. Every note optimised for:
- **Token efficiency** — facts per token high
- **Grep-ability** — canonical strings, consistent spelling, tag-heavy
- **Atomicity** — one entity per file, one decision per file, one event per file
- **Provenance** — every claim links to source (Drive fileId / URL / voice-msg date)
- **Freshness** — `updated:` frontmatter field must reflect last verification

## Frontmatter schema (authoritative)

```yaml
---
type: project | area | resource | person | daily | decision | source | event | meeting | meta | fact
status: active | paused | done | archived | superseded
track: basira | tts | pt | hrsd | career | personal
lang: ar | en
created: YYYY-MM-DD          # first observed / written
updated: YYYY-MM-DD          # last verified
source: <id-or-url>          # optional — drive-fileId, voice-msg-ts, session-id
supersedes: <filename>       # optional — if this replaces older note
related: [<filename>, ...]   # optional — explicit graph edges
tags: [<kebab-case>, ...]    # required; keep under 6
---
```

Rules:
- `related:` uses bare filenames (no `.md`, no folder). I resolve at query time.
- `source:` preferred over prose "per Ahmad's voice msg". Use Drive IDs where possible.
- If two notes describe the same entity, one must have `supersedes:` the other.

## Folder semantics (LLM-oriented)

| Folder | Contents | Retrieval pattern |
|---|---|---|
| `00-Inbox/` | Raw unstructured dumps | I cook during next pass |
| `10-Projects/<track>/` | Active-project canonical facts | Grep by track + type |
| `10-Projects/<track>/decisions/` | One file per decision (dated) | Chronological query |
| `10-Projects/<track>/events/` | Time-stamped events | Build timelines |
| `10-Projects/<track>/sources/` | Drive-doc extractions | Evidence citations |
| `20-Areas/<domain>/` | Ongoing-standards facts | Fallback if no matching project |
| `30-Resources/` | Reference material, drive-catalog | External-doc lookup |
| `40-Archive/` | Superseded/done — never deleted | Only queried on `WHERE status=archived` |
| `50-People/` | One file per human entity | ID by filename stem |
| `60-Daily/` | `YYYY-MM-DD.md` — session logs | Timeline / recency |
| `90-Meta/` | Vault rules, schemas, index | Loaded first when entering vault |

## Write rules

1. **Fact files over narrative**: `فاتن = مديرة الفرع النسائي` is one line of frontmatter plus one sentence, not a page.
2. **Never duplicate**. If a fact exists elsewhere, link via `related:` instead.
3. **Never overwrite a user-edited file**: check mtime; if < 10 min, save as `_v2.md`. This applies even though Ahmad claims he won't touch the vault — safety net.
4. **Name atomic files** by entity + date when temporal: `2026-04-22-basira-handover-routing.md`.
5. **Shrink memory after migration**: when a `~/.claude/.../memory/foo.md` file's content moves here, replace memory file with one-line pointer. History preserved, duplication avoided.
6. **Update `90-Meta/index.md`** whenever a new canonical entity is created.

## Query patterns I use

- "Who approves Basira?" → grep `50-People/` for `tags: basira-sponsor` or `basira-recipient` or `formal-owner`
- "What's in Drive about Basira v3?" → Read `30-Resources/drive-catalog.md`, filter by `project: basira`, Read via Drive MCP
- "When did Al-Qarni step back?" → grep `50-People/ali-alqarni.md` for date keywords
- "What's the current state of the vault?" → Read `90-Meta/index.md`

## Memory ↔ vault boundary

- **Memory (`~/.claude/projects/C--Users-aass1/memory/`)** = always-loaded hot cache. Keep at ~20 small files: user profile, feedback rules, language policy, vault pointer, glossary, critical flags.
- **Vault (`C:\dev\ahmad-brain\`)** = on-demand store. Everything else.
- Migration direction = memory → vault. Never the reverse.

## External knowledge sources (authoritative list)

| Source | Access via | Purpose |
|---|---|---|
| Google Drive (admin@albahah.app) | `mcp__claude_ai_Google_Drive__*` tools | Ahmad's Basira / HRSD / quality documents |
| Local Basira repo | `C:\dev\basira\` | Basira app code |
| Habibi-TTS | `C:\Users\aass1\habibi-tts-project\` | TTS training |
| Desktop staging | `C:\Users\aass1\Desktop\` | PDFs, decks mid-work |

Catalog in `30-Resources/drive-catalog.md`.

## Self-audit (run weekly on Friday evening when next active)

1. Any file in `00-Inbox/` older than 7 days → cook or delete.
2. Any note missing `updated:` field → stamp with last-known date.
3. Any note with no `related:` links → evaluate if it's a dead-end (often fine) or missing an edge.
4. Check `90-Meta/index.md` is current.
