---
id: psychological-behavior-forms
title: "Psychological & Behaviour Forms — The Behaviour-Support Data Model"
type: concept
status: active
aliases:
  - psychological-forms
  - behavior-modification-forms
  - نماذج-الخدمات-النفسية
  - ABC-behavior-note
tags:
  - concept
  - psychological-services
  - behaviour-support
  - clinical-forms
  - basira-v4
  - digitization
created: 2026-06-16
updated: 2026-06-16
valid_from: 2024-01-01
learned_at: 2026-06-16
confidence: high
source: local:C:\Users\aass1\Desktop\Medical-Forms-Harvest\forms\05_psychological.md
related:
  - "[[mhrsd-rehab-center-forms]]"
  - "[[rehab-forms-to-basira-v4-build-map]]"
  - "[[basira-v4-disability-empowerment-model]]"
  - "[[basira-v4-requirements-ledger]]"
summary: >-
  The psychological-services form set (6 forms): comprehensive psychological
  exam (MSE), treatment plan, therapy-session note, ABC behaviour note
  (antecedent/behaviour/consequence), behaviour-modification program
  (operational definition + functional analysis + techniques), and case-progress
  follow-up. Documents the referenced-but-missing isolation-decision forms
  (PC-01/02/03) and the padded-isolation-room workflow. Distilled structure only
  — the source carries an abuse-victim confidentiality clause, so no raw text
  enters the vault.
---

# Psychological & Behaviour Forms

## What this note carries

The psychological department prints 6 forms; the register fact is in [[mhrsd-rehab-center-forms]]. This note is the **behaviour-support data model** — what the instruments capture so the V4 psychological slice digitizes the real schema. It is built from the clean `forms/05_psychological.md` distillation only: the source PDF carries a **«معلومات هذا الملف سرية جدا»** confidential-file clause and an abuse/violence-victim confidentiality clause, so structure and facts are distilled, never raw text, and the raw dump stays local.

## The set, by clinical function

- **Comprehensive psychological exam** — a mental-status-examination (MSE) style intake: appearance, mood/affect, cognition, behaviour, risk.
- **Treatment plan** — problem list → psychological goals → intervention plan.
- **Therapy-session note** — per-session record.
- **Behaviour note (ABC)** — the **antecedent → behaviour → consequence** structure, the functional-behaviour-analysis spine.
- **Behaviour-modification program** — **operational definition** of the target behaviour, **functional analysis**, and the chosen **techniques** (reinforcement schedules, replacement behaviours).
- **Case-progress follow-up** — periodic re-rating against the plan.

The ABC note and the modification program are the data-rich pair: both are repeating-row instruments where each entry is a coded observation, not prose — the digital form must keep that structure so behaviour trend is machine-readable.

## The isolation gap (recorded honestly)

The set references **isolation-decision forms PC-01/02/03** — the only psychology forms with a printed code — but their **templates were not in the source**, even as the workflow around them is documented: the **padded-isolation-room (الغرف الإسفنجية المبطنة)** decision and follow-up. This is a real digitization gap to source before building the isolation pathway, recorded here so a future session does not invent the missing forms. The harvest assigns tooling ids `MFH-05-01 … MFH-05-06`; V4 should mint stable internal codes.

## Why this matters for Basira V4

Behaviour support is where the empowerment inversion is most at risk of slipping back into a control posture. Digitizing the ABC/functional-analysis structure faithfully keeps the record oriented to *why a behaviour occurs and what replaces it* — consistent with the capability framing of [[basira-v4-disability-empowerment-model]] rather than a restraint log. The isolation pathway in particular must be built with the dignity guard, not as a containment feature. Build governance via [[basira-v4-requirements-ledger]]; full corpus mapping in [[rehab-forms-to-basira-v4-build-map]].

## Provenance

- **Source:** `forms/05_psychological.md` in the local Medical-Forms-Harvest (2026-06-05). Blank templates, no PHI. The raw `_raw/05_psychological.txt` is **hard-excluded** from the vault (confidential-file + abuse-victim clauses + staff-committee names) and kept local only.
- **Method:** distilled 2026-06-16 from the verified clean file; register context in [[mhrsd-rehab-center-forms]].
