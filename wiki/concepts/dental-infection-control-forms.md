---
id: dental-infection-control-forms
title: "Dental & Infection-Control Forms — Charting + Sterilization Regime"
type: concept
status: active
aliases:
  - dental-forms
  - FDI-charting
  - نماذج-الأسنان
  - sterilization-chart
tags:
  - concept
  - dental
  - infection-control
  - clinical-forms
  - basira-v4
  - digitization
created: 2026-06-16
updated: 2026-06-16
valid_from: 2024-01-01
learned_at: 2026-06-16
confidence: high
source: local:C:\Users\aass1\Desktop\Medical-Forms-Harvest\forms\02_dental.md
related:
  - "[[mhrsd-rehab-center-forms]]"
  - "[[rehab-forms-to-basira-v4-build-map]]"
  - "[[al-baha-ic-archive]]"
  - "[[basira-v4-cross-service-triggers]]"
  - "[[basira-v4-requirements-ledger]]"
summary: >-
  The dental form set (7 forms): FDI charting + OHI-S + CPITN evaluation, a
  phased problem-list / treatment-need, the treatment record, the daily
  sterilization/disinfection chart, the brushing-method training
  acknowledgement, a daily round schedule, and a monthly brushing chart. Ties to
  the center infection-control regime (the source PDF is IPC-heavy) and to V4's
  dental→soft-diet cross-service trigger.
---

# Dental & Infection-Control Forms

## What this note carries

Dental prints 7 forms; the register fact is in [[mhrsd-rehab-center-forms]]. This note captures the **dental clinical data model and its infection-control content** — the dental source PDF is unusually heavy on IPC policy, which is why this concept stands alongside the clinical charting rather than folding into the catalogue. Source is the clean `forms/02_dental.md`; the raw dump (staff-committee names + سري header) stays local.

## The set, by function

- **Dental charting** — **FDI tooth notation** chart, **OHI-S** (Simplified Oral Hygiene Index), and **CPITN** (Community Periodontal Index of Treatment Needs) — the three standard oral-health indices.
- **Problem list / treatment need** — a **phased** plan (urgent → routine), keyed to the charting.
- **Treatment record** — per-visit procedures performed.
- **Daily sterilization / disinfection chart** — the IPC instrument: instrument-cycle logging, surface disinfection, the infection-control regime for the dental suite.
- **Brushing-method training acknowledgement** — beneficiary/guardian sign-off on oral-hygiene instruction.
- **Daily round schedule** + **monthly brushing chart** — the preventive-care cadence (group oral-hygiene rounds).

## The infection-control thread

The daily sterilization chart connects dental to the center-wide infection-control program distilled in [[al-baha-ic-archive]] — the same notifiable-disease and precaution discipline that the DR-coded infectious-disease notification and the nursing isolation forms carry, here applied to the dental suite. Digitizing the sterilization chart as a structured daily log (not a paper checklist) makes IPC compliance auditable in V4 rather than aspirational.

## The cross-service wire

Dental findings — broken/painful dentition, post-extraction status — feed the **dental→soft-diet trigger** ([[basira-v4-cross-service-triggers]]): a dental directive raises a diet-texture change that catering and nursing must honour, the same loop shape as the dysphagia thread.

## Why this matters for Basira V4

Two slices live here: the dental charting form (indices as structured fields, not free text) and the sterilization chart as an IPC daily log. Build governance via [[basira-v4-requirements-ledger]]; the corpus-wide KNOW→SERVE mapping is in [[rehab-forms-to-basira-v4-build-map]]. Dental prints no form codes, so V4 mints internal ones (harvest tooling ids `MFH-02-01 … MFH-02-07`).

## Provenance

- **Source:** `forms/02_dental.md` in the local Medical-Forms-Harvest (2026-06-05); several dental forms were image-sourced and reconstructed from page renders. Blank templates, no PHI. Raw text excluded from the vault, kept local.
- **Method:** distilled 2026-06-16 from the verified clean file; IPC linkage cross-walks with [[al-baha-ic-archive]].
