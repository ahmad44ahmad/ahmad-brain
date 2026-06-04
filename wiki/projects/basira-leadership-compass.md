---
id: basira-leadership-compass
title: Basira — Leadership Compass (بوصلة القيادة)
type: project
status: active
aliases:
  - بوصلة القيادة
  - leadership-compass
  - strategic-decision-room
tags:
  - project
  - basira
  - feature
  - leadership
  - governance
  - decision-support
created: 2026-04-24
updated: 2026-06-04
source: local-repo:C:\dev\basira\src\modules\leadership-compass\
related:
  - "[[basira]]"
  - "[[basira-sovereign-decks]]"
  - "[[999-albaha-qms-bcp]]"
  - "[[basira-v4-rebuild]]"
summary: >-
  Strategic decision surface inside Basira for senior leadership (مساعد التنمية,
  المدير العام, and above). Seven tabs, shipped on v2 on 2026-04-22. Not a
  dashboard — a decision-oriented workspace. Decision-first, honest-mirror,
  epistemically humble, with append-only decision history.
---

# Basira — Leadership Compass

## What it is

«بوصلة القيادة» is a strategic-level feature inside [[basira]], designed on 2026-04-22 for senior-leadership audiences — مساعد التنمية (Deputy for Development), المدير العام (General Director), and above. It is not a dashboard and not operational. It is a decision-oriented workspace where data serves the decision, not the reverse.

## Route and code locations

- **URL:** `/leadership-compass`
- **Module:** `C:\dev\basira\src\modules\leadership-compass\`
- **Migration:** `C:\dev\basira\supabase\sql\024_leadership_compass.sql`
- **Types:** `C:\dev\basira\src\types\leadership-compass.ts`
- **Sidebar section:** «القيادة الاستراتيجيّة» (own top-level section in the 9-section sidebar)
- **Design rationale:** `C:\dev\basira\docs\strategic-decision-room-proposal.md`

## The seven tabs

| # | Tab | Purpose |
|---|---|---|
| 1 | القرارات المُعلَّقة | Pending decisions with full evidence stack and four actions: approve / reject / delay / request more evidence. |
| 2 | المرآة الصادقة | Structural patterns the system surfaces, including uncomfortable ones. Deliberately not hidden. |
| 3 | اتّجاهات 12 شهراً | Six KPI curves with target lines and data-quality labels (real / partial / modeled). |
| 4 | محاكاة السيناريوهات | Budget-allocation simulator with three strategies and side-by-side comparison. |
| 5 | اكتشف | Auto-surfaced interventions worth scaling. Frame is "best practice," never "best center." |
| 6 | سجلّ القرارات | Historical decisions with outcomes at 3, 6, and 12 months plus the lesson learned. **No delete.** |
| 7 | أفق السياسات | Weak-signal radar for policy issues on a 6–18 month horizon. |

## Non-negotiable design principles

1. **Decision-first.** Every tab ends in an action. Data exists to move a decision forward.
2. **Honest mirror.** Uncomfortable patterns are surfaced by design, not hidden.
3. **Epistemic humility.** Confidence levels are declared ("preliminary / moderate / strong"; "real / partial / modeled").
4. **Time-respecting.** Summary visible in seconds, full detail on demand.
5. **Decision permanence.** No `DELETE` on the `strategic_decisions` table. Enforced at the database and RLS layer, not only in the UI. Rejected and failed decisions are kept with their lessons.
6. **Barrier linkage.** Every item cites which B1–B10 (from the launchpad §6.2) it addresses.
7. **HRSD palette + RTL.** Consistent with ministerial identity throughout.

A new tab proposal must pass all seven. If it cannot, it does not belong in the Leadership Compass — build it elsewhere in Basira.

## State at the 2026-04-22 handoff

- All seven tabs functional with seed data: 3 decisions, 4 mirror findings, 6 trajectory metrics × 3 levels, 4 discoveries, 5 ledger entries, 5 policy signals.
- Lint: 0 errors. Type-check: 0 errors. Visual verified on all tabs.
- **Migration 024 not yet applied** to Supabase — Ahmad applies via dashboard or MCP.
- Seeds are placeholder; real Supabase queries pending v3.0.
- RLS policies permissive in dev; الوكالة tightens at deployment.

## Extension rules

- **New decision category:** extend `DecisionCategory` union in `src/types/leadership-compass.ts` + add the label in `DECISION_CATEGORY_LABELS`.
- **New mirror rule:** add a detection query in Supabase and seed via `honest_mirror_findings`. Shape template in `data/seed-mirror.ts`.
- **Real-data integration for v3.0:** replace the `SEED_*` imports in each tab with Supabase hooks. Data shapes match 1:1 with the table schemas in migration 024.

## Do not

- Add a `DELETE` button on decisions — breaks the preservation principle at both UI and data layers.
- Reframe as operational ("KPI explorer," "performance metrics"). This is strategic.
- Display Ahmad's name anywhere on the surface. Institutional voice only.
- Add rankings between centers. Principle: best practice, not best center.
- Hide failures in the Decision Ledger. The lessons are the point.

## V4 status (2026-06-04)

V3 deleted the Leadership Compass instrument — it kept only a dead ~739-LoC stub. The V4 rebuild ([[basira-v4-rebuild]]) **restores the design, not the seed**: the seven non-negotiable principles above — decision-first, honest-mirror, epistemic humility, time-respecting, **decision-permanence** (no `DELETE` on `strategic_decisions`, enforced at the DB), **barrier-linkage** (every item cites its B1–B10), HRSD palette + RTL — all carry forward unchanged. What V4 drops is the placeholder seed data, not the instrument. The decision-permanence rule is consistent with V4's settled "decisions are permanent" governance in ADR [[0003-basira-v4-architecture]].

## Provenance

Split from the Basira project hub on 2026-04-24 during Phase D memory-to-vault migration (see [[log-2026-04-24]]). Upstream memory file `project_basira_leadership_compass.md` retained as a one-line pointer.
