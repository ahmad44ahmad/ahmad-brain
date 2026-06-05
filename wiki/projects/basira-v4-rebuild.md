---
id: basira-v4-rebuild
title: Basira V4 — Humane-First Rebuild (Hub)
type: project
status: active
aliases: []
tags:
  - basira
  - basira-v4
  - rebuild
  - digital-transformation
  - project
created: 2026-06-04
updated: 2026-06-04
summary: >-
  Orientation hub for the Basira V4 from-scratch rebuild — the operational layer of the CRPD-anchored community-integration project. V1/V2/V3 are hollow parts-bins whose celebrated "engines" were never built; V4 is a lean Next.js 16 + Prisma app with one proven cross-service loop, currently paused after a multi-session knowledge gather.
related:
  - "[[basira-v4-compass-and-anti-drift]]"
  - "[[basira-v4-requirements-ledger]]"
  - "[[basira-v4-cross-service-triggers]]"
  - "[[basira-v4-org-roles-rbac]]"
  - "[[basira-v4-disability-empowerment-model]]"
  - "[[basira-v4-engines-and-corpus]]"
  - "[[0003-basira-v4-architecture]]"
  - "[[basira]]"
  - "[[social-handicap-compass]]"
  - "[[community-integration-project]]"
  - "[[drive-catalog]]"
  - "[[basira-rebuild-kb]]"
  - "[[basira-demo-vs-real-data]]"
  - "[[mhrsd-rehab-center-forms]]"
  - "[[basira-capability-domain-catalog]]"
  - "[[mhrsd-cyber-policy-library]]"
source: session:s85-basira-v4-gather
---

# Basira V4 — Humane-First Rebuild (Hub)

This is the one-screen orientation for the Basira V4 rebuild. Start here, then follow the facet links below. The full Basira product history lives at [[basira]]; this note is specifically the V4 clean-rebuild line begun at session S84 (2026-06-04).

## What V4 is

V4 is the **operational layer of the existing CRPD-anchored مشروع الدمج المجتمعي** (community-integration / de-institutionalization project) — see [[community-integration-project]]. It is not a fresh idea bolted onto a center; it is the software that runs the institution-to-community transition the ministry already committed to. Concretely, Basira is framed as a **Center Operating System for impact** — a unified bio-psycho-social database where the *link* between medical, social, functional, and skill records is the product, not yet another e-archive. The de-institutionalization journey is the central empowerment cross-service trigger.

The compass is fixed and supersedes everything: **KNOW the human** (functional + dignity + safety facts) → **SERVE him across every service** (cross-service impact triggers) → **break the societal barriers** around him. المستفيد أولًا (the beneficiary first). Disability is treated as social/functional, never as a ceiling — see [[social-handicap-compass]]. Every screen either helps someone KNOW or SERVE a real human, or it does not belong. The full compass + the settled access model + the anti-drift checklist live in [[basira-v4-compass-and-anti-drift]].

## Why it exists (the reckoning)

All three prior versions are hollow parts-bins, and the rebuild exists because incremental fixes could not recover them. The two hard truths that forced V4:

1. **The celebrated بصيرة "engines" were never built.** Predictive (نبض / "Nabd"), governance auto-CAPA, the SROI index, the so-called خوارزمية الإحسان — these are aspirational prose in the docs, not working code. They were logged NOT-ADOPTED-as-claimed across the harvest. V4's rule is **honesty over green**: it builds each as a real, verified loop or claims nothing. (The harvest already caught and rejected a fabricated "Digital-Twin simulation engine.")
2. **The ministry's own national report validates the compass.** The current system measures **outputs, not outcomes** ("وهم الإنجاز" — the illusion of achievement), and the **medical gateway** (البوابة الطبية) forces a medical model. So V4 deliberately starts from "ما أهدافك؟" (what are your goals?) rather than "ما تشخيصك؟" (what is your diagnosis?). The social-handicap frame is externally validated, not merely Ahmad's opinion.

The repos remain a parts-bin only — pull KNOWLEDGE, copy no code. V3's salvageable logic (محرك مروءة, burnout-aware staff matching; محرك نبض, abandonment/isolation early-warning) is worth re-implementing, but it is NestJS/BullMQ/Redis-bound in V3 — re-implement the *logic* under the V4 core, do not drag the plumbing. That plumbing ceremony (Turborepo + NestJS + Redis) is precisely what hollowed V3.

## The lean stack

Lean on purpose, as a direct reaction to V3's ceremony:

- **Next.js 16 (App Router) + React 19 + TypeScript** — server actions are the home of the KNOW→SERVE triggers.
- **Prisma 6 + SQLite for local dev now** (`prisma/dev.db`); **Postgres is the decided production target** (the swap is one datasource line). Postgres is *not* wired yet.
- **Plain CSS on the HRSD palette**, RTL Arabic. No Tailwind/UI-kit yet (a deliberate failure-surface reduction).
- Auth: open-straight-in as a seeded مؤتمن (trusted government employee) + cookie; a تعهد (pledge) gate before any data. Nafath/2FA apply only to the future gated remote path.

The architecture rationale — one process, one DB, the direct transactional write *is* the outbox (no broker, no Kafka) — is the ADR [[0003-basira-v4-architecture]].

## The one proven loop

V4 has exactly **one verified cross-service loop**, built and confirmed end-to-end in browser + DB at S84:

A nurse logs a **dental extraction** (`logDentalExtraction` in `app/actions.ts`). In **one transaction** this creates both a `CareEvent` **and** a nutrition `ServiceDirective` (soft diet, 3 days). The kitchen surface (`app/kitchen/page.tsx`) then **reads that directive** — and `sourceCareEventId` links the two rows, so it is a real cross-service wire, not a mock. Every view/create is written to `AccessLog` via `lib/access.ts`, behind the signed تعهد. This single thread is the existence proof for the whole pattern; the design generalisation of it lives in [[basira-v4-cross-service-triggers]].

This is the *only* proven capability. **Build is currently PAUSED** — after the first loop, the project entered a multi-session research/gather phase ("لا تستعجل" — do not rush; "كامل البيانات" — complete the data first). The gather is now essentially complete; the next deliverable is **Plan #2, the rebuild structure** (bounded-context order, the one transactional trigger-dispatcher, engines as pure `lib/engines/*` functions built only when a real loop needs them, and the Supabase→Postgres migration sequence).

## The knowledge base (Desktop)

The pull-don't-invent knowledge base lives at `C:\Users\aass1\Desktop\Basira-REBUILD\` (English, AI-facing). Structure:

- **Synthesis docs** `00`–`03` + `05` + `12`/`13` synthesis: `00-MASTER-SOURCE-INVENTORY` (the map), `01-REQUIREMENTS-LEDGER` (§A–§J), `02-WHY-AND-ANTIPATTERNS`, `03-GAPS-AND-DATA-ASK`, `05-MINISTRY-CONTEXT-AND-DECISIONS-S84`.
- **Raw extracts** `harvest\01`–`13` — the three old codebases (`01`–`03`), vision/compass (`04`), HRSD design (`05`), skills/best-practices (`06`/`10`), evolution + settled security (`07`), data inventory + the live-DB pull (`08`/`08b`), Drive read (`09`), theoretical foundations (`11`), and the two corpus batches (`12-*`, `13-*`).
- **Design layer (Foundation Task 1)** `15`–`17` — the build-ready references Track B implements from: `15-DATA-DICTIONARY` (every field of the ~56 entities), `16-TRIGGER-REGISTRY` (the cross-service edges), `17-DATA-MODEL` (the consolidated schema shape across the 8 bounded contexts + the polymorphic dispatch seam; §7 = the open data-model decisions). The first slice handoff — `P0.2-BUILD-HANDOFF` (Person/KNOW enrich: extend `Beneficiary` + `FunctionalProfile` + `GuardianContact` + the plug-in seam) — is build-ready for Track B. Full catalogue: [[basira-rebuild-kb]].

A caution from the gather: the only real beneficiary data sits in **one** Supabase project (not three), its live schema has diverged from every repo SQL file, and the real roster is anon-readable (RLS off + GRANT anon from a 2026-04-14 recovery) — a live PDPL exposure to lock down during the ETL. The Google Drive reference (owner `admin@albahah.app`, "almost everything is here") is catalogued in [[drive-catalog]].

## The facet notes (read by need)

| Note | One line |
|---|---|
| [[basira-v4-compass-and-anti-drift]] | The compass + the SETTLED access model (every user a مؤتمن who signs a تعهد; default-OPEN; every access in `AccessLog`; NO field masking, NO سري/مقيد tiers, NO security-spine) + the per-session anti-drift checklist. |
| [[basira-v4-requirements-ledger]] | The pull-don't-invent requirements ledger (§A–§J), every item traced to a source, barrier-tagged, and marked REAL vs DEMO. |
| [[basira-v4-cross-service-triggers]] | Cross-service impact triggers, their real paper origins (e.g. استمارة تبليغ مطبخ بالحالة — the kitchen case-notification form), and the single transactional dispatcher/outbox row. |
| [[basira-v4-org-roles-rbac]] | The center org roles (مدير / طبيب / مسؤول الجودة / أخصائي اجتماعي / GA رعاية ذوي الهمم / وكلاء) + delegation, on the default-open access model. |
| [[basira-v4-disability-empowerment-model]] | The empowerment model: 8-track integration eligibility, the 6-group disability taxonomy, the ~16-field intake form, and the B1–B10 social-handicap barrier legend (recovered verbatim from V2 `sql/022`). |
| [[basira-v4-engines-and-corpus]] | Engines real-vs-aspirational (none were ever built) plus the harvested ministry corpus synthesis (QMS/ISO, KPIs, theoretical foundations). |
| [[0003-basira-v4-architecture]] | The architecture decision record: lean Next.js full-stack, one process + one DB, the direct transactional write as the outbox, no broker/microservices. |

Open decisions that the rebuild must NOT silently pick: cross-service interlock semantics (advisory alert vs hard guarded block — existing real procedures are all alert-plus-human-action, so V4 adds hard interlocks like glucose→insulin only as a deliberate improvement) and the re-authored PT clinical assessment form. (The B1-B10 barrier legend is no longer open — it was recovered verbatim; see [[basira-v4-disability-empowerment-model]].) Further data-model-level open decisions (MedicalProfile placement, the 6-class-vs-8-enum integration routing, the insulin band/freshness) are tracked in `17-DATA-MODEL` §7 — catalogue [[basira-rebuild-kb]].
