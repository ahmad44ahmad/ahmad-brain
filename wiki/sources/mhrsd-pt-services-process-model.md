---
id: mhrsd-pt-services-process-model
title: "MHRSD PT Services Process Model — The Un-Extracted Scope Layer"
type: source
status: active
aliases:
  - pt-services-process-model
  - physiopp-process-layer
  - نمذجة-العلاج-الطبيعي-المصدر
tags:
  - source
  - physical-therapy
  - pt-modelling
  - basira-v4
  - process-model
  - mhrsd
created: 2026-06-16
updated: 2026-06-16
learned_at: 2026-06-16
confidence: high
source: local:C:\Users\aass1\Desktop\Basira-Knowledge-Library\phase-2R\modules\pt-physical-therapy.md
related:
  - "[[pt-modeling]]"
  - "[[mhrsd-rehab-center-forms]]"
  - "[[pt-assessment-form-structure]]"
  - "[[basira-v4-requirements-ledger]]"
  - "[[basira-v4-disability-empowerment-model]]"
  - "[[al-baha-center-policies]]"
summary: >-
  The process/scope layer of the official MHRSD PT services-modeling document —
  physiopp 001–014 (14 numbered work procedures), 4 PT job descriptions, the unit
  org chart + objectives, and equipment/cadre/annual-KPI specs. This layer is
  un-extracted: the forms harvest (MFH-01) took only the document's forms pages
  (32–40); the process layer (pp.1–31, 41–44) sits on the shelf un-harvested. The
  scope grounding a Basira V4 PT module would be built from. Distinct from the
  pt-modeling PROJECT (the work) and the forms catalogue (the forms layer).
---

# MHRSD PT Services Process Model

## What this source is — and the layer it recovers

The official **«نمذجة خدمات العلاج الطبيعي»** is one artifact with two layers. The **forms layer** (pp.32–40) was harvested into the 6 PT forms ([[pt-assessment-form-structure]], catalogued in [[mhrsd-rehab-center-forms]]). The **process/scope layer** — enumerated by the document's own index but extracted by no one — is what this note records. It is distinct from [[pt-modeling]] (the *project* to update the national manual) and from the forms catalogue: this is the source-artifact's **scope/procedure content**, the layer a V4 PT module would be built from.

A Phase-2R top-down shelf walk (2026-06-08) surfaced it: the PT artifact and the PT services-modeling document are **byte-identical** (`العلاج الطبيعي .pdf` = `نمذجة العلاج الطبيعي نسخة محدثة.pdf`, 2,493,135 b), with editable Arabic + English twin `.docx` files on the same Drive shelf.

## The process layer (structure — content un-extracted)

The document's non-form pages (pp.1–31, 41–44) carry, per its own index:

- **physiopp 001–014** — fourteen numbered work procedures (the operational SOP spine).
- **Four PT job descriptions** — Head, Senior Specialist, Specialist, Technician, Assistant.
- **Unit org chart + objectives.**
- **Equipment / cadre / annual-KPI specs.**

> **Honest scope flag:** this note records the *structure* of the process layer (the section list above), **not** the verbatim content of each physiopp procedure — that content is **un-extracted** from the source and is not reproduced here. A future build pass should extract the editable twin `نمذجة العلاج الطبيعي نسخة محدثة.docx` to fill it in; this note marks the gap rather than inventing the procedures.

## Build-relevant findings (from the shelf walk)

- **Present but unwired (the enrich-in-place case):** the PT source material is on the shelf and byte-identical to the modeling document, but neither the process layer is extracted into a requirements artifact nor the 6 forms are wired into V4 (PT module coverage = 0% wired, ~67% present). It is grounding to wire, not anything to rebuild.
- **DR-0012 referral-IN parity lead:** the blocked **مرفق١ physician referral-IN** template may be equivalent to `نموذج الإحالة إلى قسم العلاج الطبيعي` (DR-0012) already in the medical-forms pack — a field-parity check could lift that gap.
- **GMFCS / MACS / FIM-like grading** in the PT assessment ground the ICF capacity axis + outcome-of-record with real instruments (detail in [[pt-assessment-form-structure]]).

## PII flag

`حالات تقييم قسم الذكور.xlsx` (males-ward, ~5.5 MB) is **likely real filled PT assessment data** — a high-value field-usage/seed source but **PHI**. It is **not ingested**; never route it to any demo/Vercel tier; handle per the GitHub/Supabase exposure posture.

## Provenance

- **Source:** the Phase-2R `pt-physical-therapy` module-walk (2026-06-08, evaluation-only) + the Drive artifact `نمذجة العلاج الطبيعي نسخة محدثة.docx`. The forms layer was previously harvested; this note records the process layer and its un-extracted status.
- **Method:** distilled 2026-06-16; process-layer *content* deliberately left thin (un-extracted in the source) rather than fabricated. The pt-modeling project ([[pt-modeling]]) anticipated `wiki/sources/` distillations of its source material — this is one.
