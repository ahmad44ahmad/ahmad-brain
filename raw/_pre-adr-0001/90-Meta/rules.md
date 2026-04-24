---
type: meta
status: active
track: personal
lang: en
created: 2026-04-24
updated: 2026-04-24
tags: [vault-rules, capture-policy]
---

# Vault Rules — Capture, Review, Survival

Short rules. If a rule isn't here, don't assume it exists.

## Capture

- **Inbox is disposable.** Dump to `00-Inbox/` with any filename. Don't overthink naming — the cook step renames it.
- **Every note needs frontmatter.** Even a one-liner in Inbox. Templater handles this via the `Tab` new-note hotkey.
- **One language per note.** Split if needed.
- **Names.** Filenames in English/transliteration (cross-platform). Titles inside files can be Arabic.

## Review

- **Weekly, Friday evening:** walk `00-Inbox/` top to bottom. Every file either:
  - Moves to its real folder with clean frontmatter, or
  - Moves to `40-Archive/`, or
  - Gets deleted (only if genuinely valueless).
- **Monthly, first of month:** walk the memory index (`MEMORY.md`). Remove pointers to finished projects. Move deep content into the vault.
- **Quarterly:** audit `40-Archive/`. Don't delete — but consolidate if a track has 30+ stale files.

## Naming

- Kebab-case, lowercase: `ali-alqarni.md`, `basira-v2-dashboard.md`.
- Date prefix for time-bound notes: `2026-04-24-wakalat-meeting.md`.
- No spaces, no caps, no Arabic in filenames.

## Never

- **Never overwrite a user-edited file.** If mtime < 10 min, save as `_v2`. See `feedback_never_overwrite_user_files.md`.
- **Never delete from `40-Archive/`.** It is the history layer.
- **Never mix languages in one note.** Split.
- **Never put CBAHI / personalization / Tamkeen / Masarrah in PT modeling files.** See `feedback_pt_project_rules.md`.
- **Never commit credentials** (API keys, tokens). Use `.env` outside the vault.

## Git

- Obsidian Git plugin auto-commits every 30 min.
- Manual push weekly during Friday review.
- If a conflict appears: don't force-resolve. Ask Ahmad.
