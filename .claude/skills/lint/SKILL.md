---
name: lint
description: Validate every vault note — required frontmatter keys, allowed type values, resolvable wikilinks in both frontmatter and body, and canonical shape of link-list fields (related, amends, supersedes, superseded-by). Read-only; prints a categorised report.
---

# /lint — Vault linter

## When to run

- After any batch of note edits, especially memory-to-vault migrations.
- Before committing a large change-set.
- When the YAML `related:` corruption gotcha might have struck (see log 2026-04-24 Phase D notes).

## What it checks

1. **Required frontmatter keys** — every note in `wiki/`, `decisions/`, `log/` must have `id`, `title`, `type`, `status`, `tags`, `created`, `updated`, `summary`.
2. **Allowed `type:` values** — `source | wiki | decision | log | person | project | concept | entity | synthesis | moc`.
3. **Wikilink resolution** — every `[[slug]]` reference in frontmatter list-fields and body prose must resolve to a note with `id: slug`.
4. **Link-field shape** — `related:`, `amends:`, `supersedes:`, `superseded-by:` must be either absent, a single string, or a multiline list of quoted strings (`- "[[slug]]"`). Flags comma-inline `related: [[a]], [[b]]` (ambiguous YAML) and nested-list `- - slug` (Obsidian corruption).
5. **Duplicate ids** — no two notes share an `id`.

## How to run

From the vault root:

```bash
python .claude/skills/lint/lint.py
```

Exit code 0 if clean, 1 if any issues found. Report printed to stdout.

## What it does NOT do

- Fix anything. Read-only.
- Check body-text broken links beyond wikilinks (regular markdown links are out of scope).
- Chase `related:` graph depth or flag weak connections.

For auto-fixing the `related:` field shape, use the companion one-shot script `normalize_wikilinks.py` in this same skill folder.

## Provenance

Built 2026-04-24 as part of Phase D custom-skills work (see [[log-2026-04-24]]).
