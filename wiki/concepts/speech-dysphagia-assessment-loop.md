---
id: speech-dysphagia-assessment-loop
title: "Speech & Dysphagia Assessment Loop — The Swallowing-Safety Cross-Service Wire"
type: concept
status: active
aliases:
  - dysphagia-loop
  - swallowing-safety
  - SLP-forms
  - نموذج-النطق-والبلع
  - meal-monitoring-trigger
tags:
  - concept
  - speech-language
  - dysphagia
  - clinical-forms
  - basira-v4
  - cross-service-triggers
created: 2026-06-16
updated: 2026-06-16
valid_from: 2024-01-01
learned_at: 2026-06-16
confidence: high
source: local:C:\Users\aass1\Desktop\Medical-Forms-Harvest\forms\03_speech.md
related:
  - "[[mhrsd-rehab-center-forms]]"
  - "[[rehab-nursing-observation-forms]]"
  - "[[rehab-forms-to-basira-v4-build-map]]"
  - "[[basira-v4-cross-service-triggers]]"
  - "[[basira-v4-requirements-ledger]]"
summary: >-
  The speech-language (SLP) form set (6 forms) plus the cross-department
  swallowing-safety loop it anchors: initial screening → articulation exam
  (Arabic place-of-articulation table) → orofacial exam → case history →
  dysphagia bedside evaluation + diet/strategy recommendations, fed by the
  nursing meal-monitoring sheet whose coughing/choking, weight-loss, and
  recurrent-chest-infection flags are the SLP referral trigger. The paper
  source-of-truth for V4's dysphagia auto-close interlock and the soft-diet
  cross-service triggers.
---

# Speech & Dysphagia Assessment Loop

## What this note carries

The speech department prints 6 forms, but its durable value is not the form count (that is in [[mhrsd-rehab-center-forms]]) — it is the **cross-department swallowing-safety loop** that threads SLP and nursing together. This is the real paper origin of Basira V4's dysphagia interlock, so it earns a concept note rather than being summarised away. Source is the clean `forms/03_speech.md`; the Arabic text layer was font-corrupted in the PDF and recovered visually, with English kept verbatim including original print typos.

## The SLP assessment chain

The six forms run as a clinical sequence:

1. **Initial screening** — first-pass communication/swallowing screen.
2. **Articulation exam** — preserves the **Arabic place-of-articulation table** verbatim (the مخارج الحروف grid), kept as data, not translated.
3. **Orofacial exam** — structural/motor exam of the oral mechanism.
4. **Case history** — communication + feeding developmental history.
5. **Dysphagia bedside evaluation (MFH-03-05)** — the swallowing-safety assessment proper, ending in **diet-texture and strategy recommendations** (e.g., pureed/soft, posture, pacing).
6. **Diet/strategy recommendation output** — the directive the rest of the center acts on.

## The loop (why this is a wire, not just a form set)

The dysphagia evaluation does not stand alone — it is **fed by the nursing meal-monitoring sheet (MFH-03-06)**. The monitoring sheet's flags are the referral trigger:

- coughing / choking / loss of bolus control during meals,
- progressive weight loss (the nursing weight/BMI chart — see [[rehab-nursing-observation-forms]]),
- recurrent chest infections (aspiration signal).

Any of these raises an SLP dysphagia referral; the bedside evaluation then writes back a diet-texture directive. That round trip — **nursing observes → SLP assesses → diet/texture directive flows back to catering and nursing** — is the loop. It is the structured ground truth behind V4's dental→soft-diet / dysphagia→pureed cross-service triggers ([[basira-v4-cross-service-triggers]]) and the dysphagia auto-close interlock: a dysphagia assessment post-dating an open referral resolves it, fail-safe (only referrals raised before the assessment).

## Why this matters for Basira V4

This loop is the canonical example of the KNOW→SERVE pattern the whole corpus maps onto ([[rehab-forms-to-basira-v4-build-map]]): a per-meal observation in one service transactionally raising a directive another service must honour, with a safety hold rather than a silent gap. Digitizing the meal-monitoring sheet and the bedside-evaluation output with their exact flags is what makes the interlock real rather than a UI promise. Build governance via [[basira-v4-requirements-ledger]].

## Provenance

- **Source:** `forms/03_speech.md` in the local Medical-Forms-Harvest (2026-06-05). Blank templates, no PHI. The raw `_raw/03_speech.txt` (staff-committee names + سري header) is excluded from the vault and kept local.
- **Method:** distilled 2026-06-16 from the verified clean file; the meal-monitoring linkage is cross-confirmed against the nursing set in [[rehab-nursing-observation-forms]].
