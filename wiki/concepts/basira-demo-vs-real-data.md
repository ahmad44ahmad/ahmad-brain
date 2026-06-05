---
id: basira-demo-vs-real-data
title: "Basira Demo-vs-Real Data — live-DB inventory + demo-by-design"
type: concept
status: active
aliases:
  - demo-vs-real-data
  - basira-data-reality
tags:
  - basira
  - basira-v4
  - data-model
  - demo-data
  - pdpl
  - concept
created: 2026-06-04
updated: 2026-06-04
source: local-fs:C:\Users\aass1\Desktop\Basira-REBUILD\03-GAPS-AND-DATA-ASK.md
summary: >-
  Where Basira's real data actually lives versus what the app ships. ONE real
  ~145-147-person roster sits on a single Supabase project (V1 and V2 both wrote
  there); V3 production (Railway) is demo/seed only; Google Drive holds the real
  KPIs and إعاشة data. V4 ships DEMO beneficiaries by design — realistic Al-Baha
  diagnoses, no PII, a national-ID plug-in seam — so demo completeness is
  intentional, not a defect. A prisma db pull against live Supabase is mandatory
  before any merge, and the real roster is currently anon-readable (a live PDPL risk).
related:
  - "[[basira-v4-rebuild]]"
  - "[[mhrsd-cyber-policy-library]]"
  - "[[basira-rebuild-kb]]"
  - "[[mhrsd-kpi-landscape-2024-2026]]"
---

# Basira Demo-vs-Real Data

A reusable mental model for any Basira V4 session: **what data is real, where it lives, and why the app ships
demo data on purpose.** It answers the recurring question "what real data exists and where?" without re-reading
the knowledge base ([[basira-rebuild-kb]]). It is the data-reality counterpart to the build decisions in ADR
[[0003-basira-v4-architecture]] (§6 demo beneficiaries) and the access model in [[basira-v4-org-roles-rbac]].

## The live-DB inventory (three stores, one holds real people)

| Store | What it holds | Status |
|---|---|---|
| **Supabase `ruesovrbhcjphmfdcpsa`** | The **one real-data pool**: a single ~145-147-person male-section roster (generated 2025-12-23) + clinical PHI + the Al-Baha advocacy/accountability narrative. **V1 AND V2 both wrote here — same project, same people.** | Real data; schema diverged from every repo SQL file (introspect, don't trust the SQL). |
| **Railway Postgres (V3 prod)** | **Demo/seed only** — a ~6k-line `prisma/seed.ts` that proves the back-end↔front-end loop. No real beneficiaries. | Demo by design. |
| **Google Drive** (`admin@albahah.app`) | The real `beneficiaries_list` + `قاعدة_بيانات_الإعاشة` sheets, real 2022/2025 KPIs (the KPI-realism anchor), and the إعاشة nutrition model. | Real; catalogued in [[drive-catalog]]. |

The single most important consequence: the real roster lives in **one** Supabase project, not three, and its
**live schema diverged** from every committed SQL file — so a `prisma db pull` against the live database is
**mandatory** before any migration; the repo SQL is a divergent partial mirror.

## Demo completeness is BY DESIGN, not a defect

V4 ships **DEMO beneficiaries** from the start: fake names, **no national ID, no real مستفيد number**, but
**realistic Al-Baha diagnoses** spanning the real population spectrum (ذكور/نساء wards, مجهولو النسب, ages from
the 20s to ~60, employable / Boccia-and-table-tennis athletes / care-only). This is a deliberate choice, echoing
the v2/v3 philosophy that the *demo* data is fully populated (to prove the loop and explain the system to the
ministry) while *real* data is sparse and uninterconnected by design — the ministry rebuilds and integrates its
own databases later. The plug-in seam: an "add beneficiary" flow takes a national-ID / مستفيد-number, pulls the
basic social-research record from the ministry DB, and **auto-provisions** the empowerment program, إعاشة
program, care team, social worker, and family linkage — so demo rows become real rows transparently, with no
change to app behavior. Diagnosis exists to prevent a service mismatch, **never as a ceiling**.

## The standing data-safety rules

- **PHI stays LOCAL.** The real roster is never committed or pushed. (Eight Basira/PHI repos were public on
  GitHub in 2026-06 with real beneficiary SQL in history — all made private; that exposure must never recur.)
- **Live PDPL exposure to lock down in the ETL.** The Supabase project was left with **RLS off + `GRANT ALL`
  to `anon`** after a 2026-04-14 recovery, so the ~145 real persons are currently anon-readable. The V4 ETL is
  the last read from an exposed DB — lock it on load (identity + access-ledger; **no masking/classification**,
  per the settled security model in [[0003-basira-v4-architecture]]).
- **The dev/pitch tier carries synthetic data only.** Real PII loads ONLY into the future KSA-resident
  production Postgres; residency is the ministry's post-approval call, not a build blocker.

## Why this matters for KPIs

Grounding V4's numbers in the real 2022/2025 KPI history (via Drive, see [[mhrsd-kpi-landscape-2024-2026]]) is
the anti-fabrication discipline: V4 KPIs are anchored to real center actuals (e.g. the 73-staff /
2-beneficiaries-employed figures in `harvest/14-c`), not invented. Honesty over green applies to data as much
as to engines.
