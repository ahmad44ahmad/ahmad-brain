---
id: two-doors-empowerment-model
title: "Two-Doors Empowerment Model — Family-Return vs Vocational (and the Bare-Enum Catch)"
type: concept
status: active
aliases:
  - two-doors
  - two-exit-doors
  - vocational-door
  - exit-destination-discriminator
tags:
  - concept
  - empowerment
  - de-institutionalization
  - basira-v4
  - build-completeness
created: 2026-06-16
updated: 2026-06-16
learned_at: 2026-06-16
confidence: high
source: local:C:\dev\basira-v4\docs\PLAN-v4-R3.md
summary: >-
  The empowerment mission has two exit doors out of institutional care —
  family-return (الإرشاد الأسري → the طي القيد closure gate) and vocational
  rehabilitation (التأهيل المهني: training→placement→employment→طي القيد). A
  2026-06-16 plan-review catch: the family-return door got the full S142 build
  while the vocational door shipped only as a bare enum, no workflow — a
  structural blind spot a G-row build can't see. Plus the exit-destination
  discriminator the ledger needs so a triumph isn't counted as a death.
related:
  - "[[basira-v4-disability-empowerment-model]]"
  - "[[tai-alqaid-closure-gate]]"
  - "[[family-fear-barrier]]"
  - "[[training-development-project]]"
  - "[[alternative-services-catalogue]]"
  - "[[empowerment-ledger-vs-custodial-return]]"
  - "[[de-institutionalization-moc]]"
---

# Two-Doors Empowerment Model

## The frame

The empowerment mission has **two exit doors** out of institutional care — two distinct routes by which a resident leaves the comprehensive-rehab center for a more independent life:

1. **Family-return / community integration** — الإرشاد الأسري (family guidance) dismantles the demand-side fear ([[family-fear-barrier]]), the resident returns home, and the case closes through the طي القيد two-committee gate ([[tai-alqaid-closure-gate]]), routing into the alternative-services menu ([[alternative-services-catalogue]]).
2. **Vocational rehabilitation (التأهيل المهني)** — training → placement → employment → طي القيد + printed certificate. The *employment* exit, the other half of the mission's promise.

Both route a resident OUT; **"success = the center closes" depends on both doors**, not one. The service-track list lives in [[basira-v4-disability-empowerment-model]] (vocational rehab is track #2 there); this note is the **two-doors lens** over it and the build-completeness catch it surfaced.

## The catch (a 2026-06-16 plan-review finding)

The two doors were built with **wildly asymmetric depth**:

- The **family-return door got the full treatment** — a multi-slice build (`S4-FAM-a/b/c`), the `FamilyGuidancePlan` state machine, and the **S142 طي-القيد keystone** with a tri-state interlock (`in-center → moved_home/file_open → file_closed`).
- The **vocational door existed only as a bare ENUM value** — scattered across rows as `targetTrack = vocational`, with no workflow. **Missing entirely:** internal-vs-external training mode; the employer/association contract + supervisor sign-off + ministry approval; and — critically — the **placement → employment → طي القيد + print-certificate interlock**, which is the *exact structural parallel* to the family-return interlock that earned S142 its own keystone slice. The perf-eval instruments (نموذج 7/9/10/11) had no home either.

**This is live, not theoretical:** the center is opening a vocational section this quarter, and the directive's own target org is renamed «التمكين والتأهيل المهني» (Empowerment & Vocational Rehabilitation).

## Why it was nearly missed — the reusable lesson

A G-row / ledger-driven build sees `vocational` as an enum value and assumes it is *covered*. Only an **adversarial completeness lens that names the two doors and asks "do both have symmetric depth?"** catches that one door is a full workflow and the other is a dropdown. The general lesson: **when a domain has N symmetric exits/doors, build-completeness must verify each door has equal depth — a door represented only as an enum value is a structural blind spot, not a built capability.** (Compare the "conveyor-invisible" pattern, where a capability with no row at all is skipped: [[de-institutionalization-moc]] cluster context; build-method in the conveyor-invisible note.)

## Corollary — the exit-destination discriminator

The two doors expose a second catch in the measurement layer: the custodial statistical return **cannot distinguish an empowering exit (family-return, vocational placement) from a death or a transfer** — all three show only as "a lower count." The fix is that **every طي-القيد closure must carry an `exitDestination`** ∈ {family_return, vocational_placement, day_care, death, moh_transfer, …} so the ledger groups by it and a death and a triumph are never the same row. This is the discriminator that lets [[empowerment-ledger-vs-custodial-return]] read an exit as a win rather than as institutional shrinkage — and `vocational_placement` must be one of its values.

## Provenance

- **Source:** the 2026-06-16 Basira V4 plan-review (`C:\dev\basira-v4\docs\PLAN-v4-R3.md`; finding F1 + the exit-destination discriminator in `C:\Users\aass1\.claude\scratch\v4-plan-review-2026-06-16\C-critique-empowerment.md`). Memory-as-pointer — the build rows + field shapes live in R3 + the gap-ledger, not here.
- **Method:** distilled 2026-06-16; the service-track definitions are not restated (they are in [[basira-v4-disability-empowerment-model]]); this note carries only the two-doors framing, the build-asymmetry catch, and the discriminator.
