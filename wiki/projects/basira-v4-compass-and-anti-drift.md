---
id: basira-v4-compass-and-anti-drift
title: Basira V4 — Compass, Settled Model & Anti-Drift
type: project
status: active
aliases: []
tags:
  - basira
  - basira-v4
  - compass
  - security-model
  - anti-drift
  - project
created: 2026-06-04
updated: 2026-06-16
summary: >-
  The non-negotiable governance for every Basira V4 screen: the compass (KNOW the human, SERVE across services, break barriers); the settled trust-and-ledger security model (every user a pledged مؤتمن, default-open, all access logged — no masking, no classification tiers, no security-spine); disability as social/functional; honesty over green; and the anti-drift checklist plus the §9 NOT-ADOPTED ledger that the rebuild deliberately refuses.
related:
  - "[[basira-v4-rebuild]]"
  - "[[social-handicap-compass]]"
  - "[[basira-v4-engines-and-corpus]]"
  - "[[basira]]"
  - "[[mhrsd-cyber-policy-library]]"
  - "[[basira-v4-build-verification-lessons]]"
source: session:s85-basira-v4-gather
---

This note is the constitution for the [[basira-v4-rebuild]]. Every other V4 design doc points here for the security model and the anti-drift rules. These are CLOSED decisions: do not reopen them, and refuse work that contradicts them. The single sentence that governs the whole codebase: every screen either helps someone KNOW or SERVE a beneficiary, or it does not belong.

## 1. The Compass

Basira is **not an EHR and not an archive**. It is a digital nervous-system (بنية عصبية رقمية, *digital nervous-system*) that makes a rehabilitation center act *as one body* (كجسد واحد), so information creates **impact**, not a filing record — a "Center Operating System," not an app. It works **one layer above the medical model**: it does not treat a body, it dismantles what handicaps a person socially (see [[social-handicap-compass]]).

The mandate, in order: **KNOW the human** (functional + dignity + safety facts) → **SERVE him across every service** (cross-service impact triggers) → **break the societal barrier**. The North Star is المستفيد أولًا (*the beneficiary first*). Disability is **social/functional, never a ceiling** — functional facts (wheelchair, epilepsy, allergy) must *flow* to whoever serves and protects the person; they are never diagnoses to hide. The market thesis: the dominant global frame treats disability as medical-first, so a social-model digital ecosystem has no global parallel — which is exactly why Basira must never collapse back into "another EHR."

## 2. The Settled Security Model (FINAL — do NOT reopen)

This is the authoritative statement of V4 security. It is the deliberate correction of a five-month drift that hollowed V3 across roughly 30 sessions (the evolution is detailed in [[basira-v4-engines-and-corpus]]).

**The model.** Every authenticated user is a مؤتمن (*trusted/entrusted government employee*) who **signs a تعهد** (*pledge/undertaking*), **sees everything needed to serve**, **bears full responsibility** for what he views, and **every access is logged** in `AccessLog` — the ledger is the teeth of the pledge. That is the *whole* model: trust + ledger.

**The hard negatives (these ARE the closed boundary):**
- **NO field-level masking.**
- **NO سري/مقيد (secret/restricted) classification tiers.**
- **NO classification map.** V3's `DATA_CLASSIFICATION_MAP` was the single highest-leverage defect.
- **NO "security spine" / Semgrep classification machinery.**
- **NO privacy-worship, NO PDPL-hedging as a blocker.**

**The reframe.** The shoe-store privacy reflex exists to protect a credit card; this system protects a human's *right to be known and served*. The data flows to serve; the human chain of trust (مؤتمن + تعهد) plus the immutable access ledger are what protect it.

**What is KEPT** (accountability-positive, not restriction-positive): 2FA login, the signed تعهد gate before any data, the immutable audit-log-as-ledger (extend the append-only DB trigger to all append-only tables), decisions-are-permanent (no-DELETE, `ON DELETE RESTRICT`), and the DSAR/consent module reframed as data-subject **rights** (to be known / accessed / corrected), not as a masking blocker.

**The remote/mobile perimeter — the only place ZTNA-style controls live.** Nafath OIDC + ZTNA + MFA apply **ONLY to the gated remote/mobile path** (the `app/api/*` surface for mobile/Seha/997). They are perimeter control for off-network access, not in-app data classification. On the internal network the مؤتمن opens straight in.

**The ONE genuine restriction — infectious-disease anti-stigma rule.** Infectious-disease status is visible to **direct-care medical roles only** and **hidden on printouts**. This exists for **anti-stigma, NOT privacy** — precisely so the status cannot be used to block housing or community reintegration. It is implemented as a single purpose-built rule, **not** a tiering system, and is the explicit inversion of the old communicable-disease blanket-exclusion (flow-not-hide).

**Why this is correct, not a regression.** V2 proved a client-direct-to-DB architecture *structurally cannot* host server-side masking. V3 proved that a server-side masking/classification spine, even when fully built, went green while protecting nothing (13/14 criticals upheld under adversarial attack; an armed RLS layer would have locked every non-admin out of all 18 empowerment tables — a dormant production outage, not a safety net) AND consumed the months that should have built the clinical surface. The lesson: **enforce accountability at the boundary (identity + ledger); do not bolt masking onto data that must flow.**

## 3. Disability Is Social/Functional, Never a Ceiling

The compass externally validated: the ministry's *own* national report shows the system today measures **Outputs not Outcomes** (وهم الإنجاز, *the illusion of achievement*) and that the medical gateway (البوابة الطبية) forces the medical model. Therefore V4 **starts from "ما أهدافك؟" (what are your goals?) not "ما تشخيصك؟" (what is your diagnosis?)**. Diagnosis is never an eligibility ceiling. V4 is the operational layer of the existing CRPD-anchored community-integration project (see [[community-integration-project]] and the [[empowerment-thesis-corpus]]); the de-institutionalization journey is the central empowerment cross-service trigger.

## 4. Honesty Over Green

The celebrated بصيرة "engines" (predictive نبض, governance auto-CAPA, the SROI index, خوارزمية الإحسان) were **never actually built** — they were aspirational prose, not code. The NotebookLM "SROI/triangulation/Launch-Gate engine" does not exist in V3; `SroiTab` was a slider. V4 builds each capability as a **real, working, verified loop — or claims nothing**. "Working" means real, mergeable, testable: a care event in one service triggers a real DB write in another, and the other service's screen *reads that row*; verified in a browser AND at the DB, screenshotted — or it did not happen. Never render demo data outside an explicit demo guard; never ship a fetcher without a consuming form; never name a thing an "engine" unless an evaluator actually runs.

## 5. The Anti-Drift Checklist

Run this before tool-calling each session. The infra/security drift is named the **"sewer pipe that ate V3."**

1. **Am I about to classify a field / mask data / build security machinery? → STOP. That is the drift.**
2. Am I building a KNOW or a SERVE surface for a real human need? If not, why does it exist?
3. Is the thing I am about to claim actually verified in a browser + DB? If not, do not claim it.
4. Am I shipping one small mergeable real thing, or piling architecture? Ship the small real thing.

Memory anchor: at session close, if **FEATURE:INFRA < 1:5**, the compass has drifted → pivot to a beneficiary-visible track within 1–2 sessions. Other standing rules: pull-don't-invent (everything needed already exists in the three repos + DBs + Drive + vault); persistence-by-construction (a form is not "done" until a characterization test proves the write→read round-trip); ship small/real/mergeable; PHI and secrets stay LOCAL, never committed; DELETE NOTHING; config/effort/ultracode are OFF-LIMITS.

## 6. The NOT-ADOPTED Ledger (§9 — things the rebuild deliberately REFUSES)

These appear in the source corpus and are explicitly rejected. Preserving them prevents a future session from re-adopting them as if they were requirements.

- **Fabricated engines / a Digital-Twin simulation engine** — the harvest already caught and rejected a fake "Digital-Twin simulation engine."
- **CCTV / radar privacy-tiering** (from the IHSAN unified strategy).
- **مقيّد (restricted) document-classification.**
- **SROI / SIB / Pay-for-Success as an app feature** — that is national policy, not a Basira screen (SROI 1:4.2 = pitch; ≥3.5 = aspirational — never swapped).
- **Diagnosis-as-ceiling eligibility gates.**
- **Communicable-disease blanket-exclusion** — V4 **inverts** this to the anti-stigma flow-not-hide rule of §2.
- **Riyadh-only scope** — V4 targets Al-Baha (see [[albaha-center-org]]).
- **Unverified AI-report KPIs** — never quote them as fact.

## 7. Why This Note Exists

V1 → V2 → V3 were each a "do it right" restart that became an unfinished tree, then drifted into infra / security / privacy / classification instead of building the humane core — so the one capability that proves digital transformation (a care event in one service triggering a care action in another) was never built, three times running. **Field-classifying and security-hardening is the *exact* drift that hollowed V3.** This document is the standing guard against a fourth tree. Read it alongside the [[basira-v4-rebuild]] hub and architecture decision [[0003-basira-v4-architecture]]; it inherits the social frame of [[social-handicap-compass]] and answers to المستفيد أولًا above any timing, personal-achievement, or privacy reflex.
