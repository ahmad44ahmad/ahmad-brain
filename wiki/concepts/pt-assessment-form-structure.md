---
id: pt-assessment-form-structure
title: "Physiotherapy Assessment Form Structure — The PT Clinical Data Model"
type: concept
status: active
aliases:
  - pt-assessment
  - physiotherapy-data-model
  - نموذج-تقييم-العلاج-الطبيعي
  - GMFCS-MACS-capture
tags:
  - concept
  - physical-therapy
  - clinical-forms
  - basira-v4
  - digitization
  - rehabilitation
created: 2026-06-16
updated: 2026-06-16
valid_from: 2024-01-01
learned_at: 2026-06-16
confidence: high
source: local:C:\Users\aass1\Desktop\Medical-Forms-Harvest\forms\01_physical_therapy.md
related:
  - "[[mhrsd-rehab-center-forms]]"
  - "[[rehab-forms-to-basira-v4-build-map]]"
  - "[[basira-v4-requirements-ledger]]"
  - "[[basira-v4-disability-empowerment-model]]"
summary: >-
  The clinical data model behind the MHRSD comprehensive-rehab-center
  physiotherapy form set (6 forms, مرفق 2-8). One multi-page assessment captures
  sensation, reflexes, tone, ROM, muscle power, selective motor control,
  gross-motor milestones graded on a 7-point FIM-style assistance legend, and
  GMFCS/MACS outcome measures, then a problem list → goals → plan; supported by
  progress note, discharge summary, clinic referral, orthotics/prosthetics
  request, and a session-not-conducted notice. The field-level spec for the
  Basira V4 PT humane-form slice.
---

# Physiotherapy Assessment Form Structure

## What this note carries

The register-level fact — that PT has 6 forms coded as attachments مرفق 2-8 — already lives in [[mhrsd-rehab-center-forms]]. This note is the **clinical data model**: what the PT instruments actually capture, field by field, so the Basira V4 PT slice digitizes the real ministry schema rather than an AI-invented one. Source is the clean English distillation `forms/01_physical_therapy.md` (pp. 32–40); the raw Arabic page text is excluded under the PII gate and never enters the vault.

## The core assessment (the multi-page instrument)

The load-bearing form is the comprehensive PT evaluation. Its sections, in order:

- **Neuromuscular status** — sensation, deep tendon reflexes (DTRs), muscle tone (spasticity/rigidity/hypotonia), passive and active range of motion (ROM), manual muscle power, and **selective motor control** (the ability to isolate a movement, central in cerebral-palsy assessment).
- **Functional motor control** — coordination, hand function, postural control (sitting/standing balance).
- **Gross-motor milestones** — graded against a **7-point FIM-style assistance legend** (from fully dependent to fully independent), the assessment's quantitative spine.
- **Standardised outcome measures** — **GMFCS** (Gross Motor Function Classification System) and **MACS** (Manual Ability Classification System), the internationally recognised CP severity bands.
- **Gait analysis** — ambulation pattern, assistive-device use.
- **Clinical reasoning block** — a **problem list → short- and long-term goals → treatment plan**, the part that turns measurement into an intervention.

The data shape matters for V4: the milestone and ROM rows are repeating tabular fields with a fixed assistance/score column, not free text — the digital form must preserve the ordinal scale so the engine layer can read trend, not prose.

## The supporting forms

Five satellites complete the set:

- **Progress note** — periodic re-measurement against the assessment baseline.
- **Discharge summary** — outcome at end of episode.
- **Clinic referral** — onward referral to a specialty clinic.
- **Orthotics/Prosthetics (O&P) request** — device prescription.
- **Session-not-conducted notice** — the structured record of a missed session and its reason (attendance/clinical-hold governance, not a clinical measure).

## Honest gaps before building

The harvest flags three missing source artefacts, faithfully:

- The PT **assessment form's page-1 demographics** was not in the source PDF (the clinical body pages were).
- **مرفق 1** (referral-IN) and **مرفق 4** (session schedule) are referenced as attachments but their templates were not printed.

These must be sourced to complete the digital replica — recorded here so a future build session does not silently invent them. The harvest assigns tooling ids `MFH-01-01 … MFH-01-06`; Basira V4 should mint stable internal codes since PT prints none.

## Why this matters for Basira V4

This is the field-faithful spec for the PT humane-form slice. The 7-point assistance legend and GMFCS/MACS bands are the measurement substrate the empowerment model ([[basira-v4-disability-empowerment-model]]) reads as capability rather than deficit — the same inversion the KNOW→SERVE bridge ([[rehab-forms-to-basira-v4-build-map]]) carries across the whole corpus. Digitization is governed through [[basira-v4-requirements-ledger]].

## Provenance

- **Source:** `forms/01_physical_therapy.md` in the local Medical-Forms-Harvest (6-agent extraction, 2026-06-05). Blank templates, no PHI. The raw `_raw/01_physical_therapy.txt` is excluded from the vault (staff-committee names + سري header) and kept local as provenance only.
- **Method:** distilled 2026-06-16 from the verified clean department file; register context in [[mhrsd-rehab-center-forms]].
