---
id: mhrsd-rehab-center-forms
title: MHRSD Comprehensive-Rehab-Center Paper Forms — Field-Faithful Digitization Catalog
type: source
status: active
aliases:
  - النماذج-الطبية-الموحدة
  - medical-forms-harvest
  - DR-form-codes
  - RN-form-codes
  - rehab-center-forms-catalog
  - Medical Forms Digitization Index
tags:
  - mhrsd-forms
  - al-baha-center
  - basira-v4
  - digitization
  - nursing-forms
  - clinical-forms
  - drive-source
created: 2026-06-05
updated: 2026-06-16
source: local:C:\Users\aass1\Desktop\Medical-Forms-Harvest\
summary: >-
  Field-faithful extraction of all 61 official MHRSD comprehensive-rehab-center
  paper forms from 6 department modeling/policy PDFs (290 pp). Five departments
  plus a unified DR-coded medical set; nursing carries RN-codes. The canonical
  field-level source for Basira V4 form digitization — one paper form maps to
  one humane-form slice. Blank templates, no PHI, local-only.
related:
  - "[[al-baha-center-policies]]"
  - "[[al-baha-ic-archive]]"
  - "[[basira-v4-rebuild]]"
  - "[[basira-v4-requirements-ledger]]"
  - "[[basira-rebuild-kb]]"
  - "[[mhrsd-supervisory-visit-instruments]]"
  - "[[pt-assessment-form-structure]]"
  - "[[rehab-nursing-observation-forms]]"
  - "[[speech-dysphagia-assessment-loop]]"
  - "[[psychological-behavior-forms]]"
  - "[[dental-infection-control-forms]]"
  - "[[rehab-forms-to-basira-v4-build-map]]"
---

# MHRSD Rehab-Center Forms — Digitization Catalog

## What this source is

A field-faithful extraction (verbatim labels, options, table structures, signature blocks) of the **official MHRSD comprehensive-rehab-center (مراكز التأهيل الشامل) paper forms** — pulled from 6 department modeling/policy PDFs totalling 290 pages. Built 2026-06-05 via a 6-agent workflow (one per document), pull-don't-invent. Every form is a **blank template** → no beneficiary PHI → local-only, uncommitted on the Desktop harvest. The Arabic memory digest is the index pointer; this note is the vault distillation that wires it into the graph.

The harvest source documents are the *forms half* of the same institutional corpus that [[al-baha-center-policies]] narrates as policy/procedure text. Where that note captures the department modeling prose (job descriptions, SOPs, org structure), this note captures the **fillable data-entry instruments** those same documents append.

## The tally — 61 forms, 6 documents, 5 departments + 1 unified set

| Doc | Department / set | Forms | Code scheme |
|---|---|---|---|
| `00` | النماذج الطبية الموحّدة 2024 (Unified Medical Forms) | 15 | **DR-0001 … DR-0013** |
| `01` | العلاج الطبيعي (Physical Therapy) | 6 | مرفق 2-8 (attachment refs, no printed code) |
| `02` | الأسنان (Dental) | 7 | none printed |
| `03` | النطق والتخاطب (Speech & Swallowing) | 6 | none printed |
| `04` | خدمات التمريض (Nursing) | 21 | **RN-0001 … RN-0020** + supplies |
| `05` | الخدمات النفسية (Psychological) | 6 | none printed |

~1,356 fields total (a checkbox-group counts as one field). Coverage reconciles per document: form-pages + non-form-pages = the PDF page count, so the extraction is provably complete against each source.

## The code scheme

Only two of six documents carry **printed form codes**, and they are the load-bearing clinical spine:

- **`DR-00xx`** — the unified 2024 medical set (`00`): admission physical-exam, medical assessment, interdisciplinary care-plan + progress notes, prescription, lab requisition, hospital/PT referrals, injury report, inter-section transfer, infectious-disease notification. These are physician-owned, cross-department instruments.
- **`RN-00xx`** — nursing (`04`): the RN-0001…RN-0020 sequence matches the document's own forms index (p.88) exactly — vitals charts, epilepsy follow-up, blood-sugar monitoring, weight, I&O + hygiene, medication list, isolation follow-up, ambulance checklist, transfer-in/out, guardian notification.

PT, dental, speech, and psychology forms carry **no printed code** (PT references them as numbered attachments مرفق 2-8). Basira V4 should mint stable internal codes for those; the harvest already assigns machine-readable ids `MFH-00-01 … MFH-05-06` in `forms/_catalog.json` for tooling.

## What each major group captures

- **Unified medical (DR):** the admission-and-orders backbone — diagnosis capture (cerebral palsy, Down syndrome, autism), vitals, prescriptions, lab orders, referrals, injury/transfer governance, infectious-disease notification.
- **Physical Therapy:** one multi-page assessment (sensation, reflexes, tone, ROM, selective motor control, gross-motor milestones with a 7-point FIM-style assistance legend, gait/ambulation) + progress, discharge, clinic referral, O&P request, and a session-failure notice.
- **Dental:** charting/OHI-S, problem-list + treatment need, treatment record, daily sterilization chart, brushing-training approval, daily rounds, daily brushing chart.
- **Speech & Swallowing:** initial screening, articulation, orofacial exam, case history, and the **dysphagia bedside exam + meal-monitoring sheet** — the swallowing-referral trigger that grounds V4's existing dental→soft-diet / dysphagia→pureed cross-service loops.
- **Nursing:** the 21-form daily-care engine — the canonical source for V4's nursing slice (P1, next).
- **Psychological:** comprehensive psych exam, treatment plan, therapy session, behavior note/modification, case follow-up.

## Department data models (deeper notes)

This catalogue is the register; the field-level clinical data model for each department now lives in its own concept note — [[pt-assessment-form-structure]], [[rehab-nursing-observation-forms]], [[speech-dysphagia-assessment-loop]], [[psychological-behavior-forms]], [[dental-infection-control-forms]] — and the corpus→build mapping (which forms become humane-form slices vs cross-service triggers) is in [[rehab-forms-to-basira-v4-build-map]].

## Why this matters for Basira V4

This is the **field-faithful source of truth for V4 form digitization**: each paper form ≈ one `basira-humane-form` slice (forms are the app's dominant LoC sink and the biggest ≤40k-LoC lever). Ahmad's stated intent is a نسخة رقمية مطابقة (an exact digital replica) per form, so the digital field set must match these labels/options rather than an AI-invented schema. The catalog feeds the V4 requirements work in [[basira-v4-requirements-ledger]] and the rebuild knowledge base in [[basira-rebuild-kb]]; the digitization sequence is governed by [[basira-v4-rebuild]].

The **swallowing thread is the proven cross-service wire**: the speech department's dysphagia bedside exam + meal-monitoring sheet (`03`) is the real paper origin of V4's dental/dysphagia→diet interlock. The nursing isolation + infectious-disease notification forms (`RN-0016`, `DR-0013`) connect directly to the IC program distilled in [[al-baha-ic-archive]] — the same notifiable-disease and isolation-precaution policies, now as data-entry instruments.

## Layout of the harvest

- `00-INDEX.md` — master AR/EN index, per-document coverage table, gaps, digitization notes.
- `forms/<dept>.md` — the digitization source: verbatim sections, fields, options, tables, signatures.
- `forms/_catalog.json` — machine-readable, stable ids `MFH-00-01 … MFH-05-06`.
- `_raw/*.txt` — extracted source text (provenance). `_img_pages/` + `_zip_extract/` — page images (PT + dental forms are image-sourced; the 2024 medical set has a 26-image visual twin).

## Honest flags before building

- **Missing source templates** (referenced, not printed — must be sourced to complete digitization): PT مرفق 1 (referral-in) + مرفق 4 (session schedule) + the PT assessment form's page-1 demographics; psychology **PC-01/02/03** isolation-decision forms (the only psych forms with a printed code, yet templates absent).
- **`uncertain`-flagged**: nursing RN-0001 + RN-0007 RTL column order was reconstructed then *visually re-verified* against 300dpi page images (flag cleared); item 21 (annual supplies) is a requisition/spec list, not a per-beneficiary clinical form — reclassify.
- Speech Arabic text layer was font-corrupted and recovered visually; English kept verbatim including original print typos.
- Classification: most forms header `Classification: Strict / مقيد`. This is **document handling chrome, not a V4 field-masking tier** — per the V4 anti-drift rule, do not let it reintroduce a security-tier system into the rebuild.
