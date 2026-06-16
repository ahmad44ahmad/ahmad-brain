---
id: basira-v4-build-verification-lessons
title: "Basira V4 Build-Verification Lessons — Aggregation Fixtures, Safe-Close, the [verify] Register"
type: synthesis
status: active
aliases:
  - aggregation-golden-fixtures
  - per-session-safe-close
  - verify-register
  - v4-build-lessons
tags:
  - synthesis
  - lessons
  - build-discipline
  - verification
  - anti-drift
  - basira-v4
created: 2026-06-16
updated: 2026-06-16
learned_at: 2026-06-16
confidence: high
source: local:C:\dev\basira-v4\docs\PLAN-v4-R3.md
summary: >-
  Three durable build-verification lessons from the 2026-06-16 V4 plan review,
  sharpening "honesty over green": aggregation rows need a golden-fixture verify
  (known inputs → exact counter), not the form-shaped browser+DB readback; the
  per-session safe-close migration sequence (incl. the S142 trap where
  git-checkout wipes uncommitted new fields); and one consolidated [verify]
  register where flagged numbers stay flagged — never asserted, never
  "corrected" against the source-of-truth.
related:
  - "[[basira-v4-compass-and-anti-drift]]"
  - "[[basira-v4-engines-and-corpus]]"
  - "[[basira-v4-rebuild]]"
  - "[[basira-v4-requirements-ledger]]"
---

# Basira V4 Build-Verification Lessons

Three engineering lessons from the 2026-06-16 V4 plan review. Each **sharpens the "honesty over green" discipline** of [[basira-v4-compass-and-anti-drift]] §4 — they are the verify/close *mechanics* the constitution implies but did not spell out.

## Lesson 1 — Aggregation rows need a golden-fixture verify, not browser+DB

The standing rule is *"verified in a browser AND at the DB, screenshotted — or it didn't happen."* That is the **right shape for forms, gates, and in-transaction triggers** (a row landed where it should). It is the **wrong shape for aggregations** — a ledger, a KPI roll-up, a 714-point self-assessment score, the 126-criterion IPC instrument. An aggregation's correctness is not "a row landed" but **"given input rows X, the computed counter/score = Y."** Proving a row exists proves nothing about whether the *number* is right.

The fix: every aggregation slice requires a **golden fixture** — seed a known input set, assert the *exact* expected counter — and is ✅ only after that fixture passes. A ledger that renders a number nobody proved is the correct number is «وهم الإنجاز» (the illusion of achievement) wearing a green check — the very thing the compass polices.

**Three verify modes, name them all:** form = browser + DB readback · trigger = in-transaction row readback · **engine/aggregate = golden fixture + cron-readback.**

## Lesson 2 — Per-session safe-close (the migration safe-sequence + context-threshold handoff)

The additive-migration safe-sequence, proven and gotcha-laden, must be an explicit protocol step (it lived only in session memory):

**provider-swap (`sed`) → migrate-diff (confirm `ADD COLUMN`, ZERO drops) → db-push-Neon → restore-sqlite-via-`sed` (provider-line ONLY) → generate.**

The load-bearing trap (**the S142 lesson**): use `git checkout` to restore the schema **only if the schema change is already committed** — otherwise `git checkout` **wipes the uncommitted new fields** you just added. A new session following a protocol that says "restore the schema" without this caveat can silently destroy a slice's own work.

Plus the close discipline that ran every session but wasn't in the plan: at **~70–80% context, safe-handoff BEFORE the next slice** — commit/push, stamp §2/§2.1, **commit the ledger in the same session** (ledger-drift rule), and write the 3-copy NEXT-SESSION-PROMPT (in-project + Desktop + MEMORY pointer).

## Lesson 3 — The consolidated [verify] / data-gap register

Scattered `[verify]` / `[UNVERIFIED]` / `[UNSOURCED]` flags drift toward being silently hardened into fact. Consolidate them into **one register**; every item stays flagged, never asserted, **never "corrected" against the source-of-truth (Ahmad)**:

- **"127 processes"** — an OPEN reconciliation vs the 73–89 process inventory (different denominators, not one wrong number). Never assert 127 as fact; never "correct" Ahmad's figure.
- **SAR figures** (allowance bands, stipends, SROI ratio) — RTL-glyph-reversal risk; asserted-as-fact in places but `[verify]` at source. The SROI composite stays an *argument*, banned as a headline metric.
- **The 125% kpiClass ceiling** — an Ahmad *directive*, NOT ministry-sourced. Label it as such.
- **After-care window (6mo→1yr)** — `[UNVERIFIED]` (operational, not in the regulation).
- **`[UNSOURCED]` engine rules** (seizure-cluster backstop, the "any sign" dysphagia rule, safeguarding thresholds) — keep flagged; **port a threshold only after verifying the `[REAL]` source CONTAINS it** (the S130 lesson). The risk is a future session hard-coding a flagged number by accident.

A single register is what makes "never invent, never correct the source" enforceable instead of aspirational.

## Why these are in the vault

They are durable, reusable build-verification method — not V4 build-state. They extend the compass's "honesty over green" ([[basira-v4-compass-and-anti-drift]] §4) and the engine-fixture discipline ([[basira-v4-engines-and-corpus]]) with the *exact mechanics* (fixture-shape per row-type, the migration trap, the flag register) that keep a ledger-driven build honest.

## Provenance

- **Source:** the 2026-06-16 Basira V4 plan-review (`C:\dev\basira-v4\docs\PLAN-v4-R3.md` §S5.5/§S6/§S7; `…\scratch\v4-plan-review-2026-06-16\C-critique-integrity.md §2/§3` + `C-FINDINGS-PACKAGE.md §5`). Memory-as-pointer — the per-row protocol text lives in R3.
- **Method:** distilled 2026-06-16; lessons stated as durable method, V4-specific row IDs cited only as examples.
