---
id: rehab-forms-to-basira-v4-build-map
title: "Rehab Forms → Basira V4 Build Map — The KNOW→SERVE Bridge"
type: synthesis
status: active
aliases:
  - forms-to-v4-map
  - know-serve-bridge
  - digitization-build-map
tags:
  - synthesis
  - basira-v4
  - digitization
  - cross-service-triggers
  - clinical-forms
created: 2026-06-16
updated: 2026-06-16
valid_from: 2026-06-16
learned_at: 2026-06-16
confidence: high
source: local:C:\Users\aass1\Desktop\Medical-Forms-Harvest\00-INDEX.md
related:
  - "[[mhrsd-rehab-center-forms]]"
  - "[[pt-assessment-form-structure]]"
  - "[[rehab-nursing-observation-forms]]"
  - "[[speech-dysphagia-assessment-loop]]"
  - "[[psychological-behavior-forms]]"
  - "[[dental-infection-control-forms]]"
  - "[[basira-v4-cross-service-triggers]]"
  - "[[basira-v4-requirements-ledger]]"
  - "[[basira-v4-rebuild]]"
summary: >-
  The KNOW→SERVE bridge: how the 61-form MHRSD rehab-center paper corpus maps
  onto the Basira V4 build. Which forms become humane-form slices, which become
  cross-service triggers (transfer hand-off, infectious-disease/isolation,
  dysphagia/meal loop, seizure/glucose, dental→soft-diet), the multidisciplinary
  care plan (DR-0002/0003) as the interdisciplinary spine, and the digitization
  gaps to source. The actionable "so what" over the five department data models.
---

# Rehab Forms → Basira V4 Build Map

## Why this note exists

The catalogue ([[mhrsd-rehab-center-forms]]) says *what exists*; the five department concept notes say *what each form captures*. This synthesis says **what to build** — it maps the 61-form corpus onto the V4 build so the digitization sequence is driven by the real clinical structure, not by an AI-invented schema. It is the "so what" layer over the data models.

## Two shapes the corpus collapses into

Every form becomes one of two V4 objects:

1. **Humane-form slices** — a paper form ≈ one `basira-humane-form` (forms are the app's dominant LoC sink and the biggest lever under the ≤40k-LoC target). The dense slices: the PT assessment ([[pt-assessment-form-structure]]), the 21 nursing forms ([[rehab-nursing-observation-forms]]), the psychological behaviour set ([[psychological-behavior-forms]]), the dental charting + sterilization log ([[dental-infection-control-forms]]), and the SLP set ([[speech-dysphagia-assessment-loop]]).
2. **Cross-service triggers** — a row in one form transactionally raising a directive another service reads ([[basira-v4-cross-service-triggers]]). These are the forms whose *value is the wire*, not just the record.

## The trigger map (the load-bearing half)

| Trigger | Paper origin | Direction |
|---|---|---|
| **Dysphagia / meal-monitoring loop** | nursing meal-monitoring sheet → SLP bedside evaluation | observation → assessment → diet-texture directive back to catering + nursing |
| **Seizure → outing-safety hold** | nursing seizure-event log (RN-0004) | event → safety hold on outings |
| **Glucose → insulin gate** | daily blood-sugar + insulin sheet | reading → insulin-release gate |
| **Dental → soft diet** | dental treatment record / findings | finding → diet-texture change |
| **Transfer hand-off** | RN-0018 / RN-0019 transfer-OUT/IN pair | discharge → receiving-service intake gate |
| **Infectious-disease / isolation** | DR-0013 notification + nursing isolation follow-up | notification → isolation precautions + IC |

The dysphagia loop is the proven exemplar of the pattern (and the basis for the dysphagia auto-close interlock); the others share its shape — observe, assess, gate or hold, never a silent gap.

## The interdisciplinary spine

The unified medical set's **multidisciplinary care plan + interdisciplinary rounds (DR-0002 / DR-0003)** is the connective tissue: it is where PT, nursing, SLP, psychology, and dental findings are supposed to converge into one plan. In V4 this is the surface that reads from all the department slices — the structural answer to the "hollow shells / forms that don't talk" gap the rebuild targets ([[basira-v4-rebuild]]).

## Digitization gaps to source (don't invent)

Carried forward from the department notes so the build doesn't silently fabricate them:

- PT assessment **page-1 demographics**, and **مرفق 1** (referral-IN) + **مرفق 4** (session schedule).
- Psychology **isolation-decision forms PC-01/02/03** (coded but templates absent).

These are real source-acquisition tasks, not modelling decisions.

## Build sequencing

Nursing is the next slice (P1) — largest set, densest trigger source. The order is governed by [[basira-v4-requirements-ledger]] and the rebuild plan [[basira-v4-rebuild]]. The discipline throughout: digitize the *exact* field set and ordinal scales so the engine layer reads trend and fires interlocks — a نسخة رقمية مطابقة, not a redesign.

## Provenance

- **Source:** `00-INDEX.md` + `forms/*.md` in the local Medical-Forms-Harvest (2026-06-05, 6-agent extraction). Blank templates, no PHI; raw Arabic dumps excluded from the vault under the PII gate.
- **Method:** synthesised 2026-06-16 across the five department concept notes and the catalogue.
