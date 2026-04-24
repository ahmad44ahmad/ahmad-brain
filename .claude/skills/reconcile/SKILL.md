---
name: reconcile
description: Detect deterministic contradictions and drift risk across vault notes — malformed or out-of-order dates, broken ADR supersede chains, id/alias collisions, stale drafts, and duplicate tags. Read-only; prints a categorised report. Complements /lint (shape) with /reconcile (semantics).
---

# /reconcile — Vault contradiction detector

## When to run

- Before major content-migration sessions (baseline the vault state).
- After any session that added or edited multiple notes.
- Monthly as a vault-health check.
- Before handing the vault off to another Claude session.

## What it checks

1. **Date integrity** — `created`, `updated`, `valid_from`, `learned_at` must be `YYYY-MM-DD` and ordered: `created ≤ updated`; `valid_from ≤ updated`.
2. **ADR supersede-chain reciprocity** — if note X has `supersedes: [[Y]]`, then Y must have `superseded-by: [[X]]` (and vice versa).
3. **ID / alias collisions** — no alias value on one note may equal the `id` or an alias of a different note.
4. **Stale drafts** — notes in `status: draft` older than 14 days get surfaced so they either get promoted or deleted.
5. **Duplicate tags within a note** — same tag listed twice in the same note's `tags:` list.

## What it does NOT do

- Semantic contradiction detection (would need an LLM pass). Deterministic only.
- Fix anything. Read-only — you decide how to resolve each finding.
- Cross-vault drift (e.g., memory files pointing to moved vault files) — run manually when needed.

## How to run

```bash
python .claude/skills/reconcile/reconcile.py
```

Exit 0 clean, 1 if any findings. Findings printed to stdout grouped by check type.

## Why this exists

Static content migration (Phase D) surfaces lots of drift: dates copied from memory files, ADR chains with one-sided links, aliases that shadow another note's id. `/lint` catches shape issues; `/reconcile` catches semantic issues. Paired, they cover the two failure modes that bit us during the 2026-04-24 bootstrap (YAML corruption + stale Al-Wuhaibi claim in the leadership map).

## Provenance

Built 2026-04-24 as Phase D tooling (see [[log-2026-04-24]]).
