---
id: rehab-nursing-observation-forms
title: "Rehab Nursing Observation Forms — The 21-Form Daily-Care Engine (RN-codes)"
type: concept
status: active
aliases:
  - nursing-forms
  - RN-form-set
  - نماذج-التمريض
  - daily-care-engine
tags:
  - concept
  - nursing
  - clinical-forms
  - basira-v4
  - digitization
  - cross-service-triggers
created: 2026-06-16
updated: 2026-06-16
valid_from: 2024-01-01
learned_at: 2026-06-16
confidence: high
source: local:C:\Users\aass1\Desktop\Medical-Forms-Harvest\forms\04_nursing.md
related:
  - "[[mhrsd-rehab-center-forms]]"
  - "[[rehab-forms-to-basira-v4-build-map]]"
  - "[[speech-dysphagia-assessment-loop]]"
  - "[[basira-v4-cross-service-triggers]]"
  - "[[basira-v4-requirements-ledger]]"
summary: >-
  The 21-form nursing daily-care set (RN-0001…RN-0020 + a supplies list), the
  largest department block and the canonical source for the Basira V4 nursing
  slice. Admission assessment, two vital-signs charts, the epilepsy pair
  (seizure-event log + annual grid), daily blood-sugar+insulin sheet, annual
  weight/BMI, I&O + hygiene flow sheet, medication list, isolation follow-up,
  ambulance checklist, and the transfer-OUT/transfer-IN medical hand-off pair.
  The structured origin of V4's seizure / glucose / weight / transfer
  cross-service triggers.
---

# Rehab Nursing Observation Forms

## What this note carries

Nursing is the largest block in the form corpus — 21 forms, and the only department besides the unified medical set that prints **stable codes** (`RN-0001 … RN-0020`, matching the source's own p.88 forms index exactly). The register fact sits in [[mhrsd-rehab-center-forms]]; this note is the **daily-care data model** and, more importantly, the place where several Basira V4 cross-service triggers have their paper origin. Source is the clean `forms/04_nursing.md` distillation; the 245 KB raw text (staff-committee names) stays local.

## The set, by clinical function

- **Intake** — admission nursing assessment; before/after-hospital examination.
- **Vital signs** — two charts: an observation-ward chart and a floor chart (same vitals, different cadence/setting).
- **Epilepsy pair** — **seizure-event log (RN-0004)** capturing per-event detail (time, type, duration, post-ictal state) and the **annual seizure grid (RN-0005)** giving the year-at-a-glance frequency view. Together they are the substrate for a seizure early-warning/outing-safety trigger.
- **Metabolic monitoring** — daily blood-sugar **+ insulin** sheet (the glucose→insulin-release loop); annual weight/BMI chart (the weight-loss signal feeding dysphagia/nutrition).
- **Gendered care** — menstrual chart.
- **Flow sheets** — daily intake & output (I&O) combined with hygiene; medication administration list; laboratory register; free-text nurse's notes.
- **Isolation & infection** — isolation follow-up (pairs with the DR-coded infectious-disease notification and the IC program).
- **Transfer & escort** — **transfer-OUT / transfer-IN medical hand-off pair (RN-0018 / RN-0019)** — the paper origin of the inter-center hand-off trigger; daily ambulance checklist.
- **Family interface** — guardian notification.
- **(reclassify)** item 21 is an annual **supplies requisition**, not a per-beneficiary clinical form — flagged for re-classification.

## The cross-service wires this set feeds

The nursing forms are where Basira's care interlocks become real rather than aspirational ([[basira-v4-cross-service-triggers]]):

- **Seizure log → outing-safety hold.**
- **Daily glucose → insulin-administration gate.**
- **Annual weight/BMI drop + the meal-monitoring sheet → dysphagia/nutrition referral** (the swallowing loop lives in [[speech-dysphagia-assessment-loop]]).
- **Transfer-OUT/IN hand-off → the receiving service's intake gate.**
- **Isolation follow-up → infection-control notification.**

Each is a row in one form transactionally raising a directive another service reads — the outbox-at-one-DB pattern V4 uses in place of an event bus.

## Honest flags

- The set is **adapted from the Coalinga State Hospital nursing manual** (recorded in the source) — useful provenance when reconciling terminology against Saudi practice.
- RN-0001 and RN-0007 had their RTL column order reconstructed, then **visually re-verified** against 300 dpi page images (flag cleared in the harvest).

## Why this matters for Basira V4

Nursing is the next humane-form slice (P1) and the densest trigger source in the corpus. Digitizing it faithfully — the ordinal vitals, the per-event seizure structure, the I&O flow shape — is what lets the engine layer read trend and fire interlocks. Build sequence governed via [[basira-v4-requirements-ledger]]; the full KNOW→SERVE mapping is in [[rehab-forms-to-basira-v4-build-map]].

## Provenance

- **Source:** `forms/04_nursing.md` in the local Medical-Forms-Harvest (2026-06-05). Blank templates, no PHI. `_raw/04_nursing.txt` excluded from the vault (staff-committee names + سري); local-only provenance.
- **Method:** distilled 2026-06-16 from the verified clean file; register context in [[mhrsd-rehab-center-forms]].
