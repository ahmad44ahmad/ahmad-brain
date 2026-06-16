---
id: mhrsd-ipc-inspection-instrument
title: "MHRSD IPC Inspection Instrument — 18-Domain Criteria Structure"
type: source
status: active
aliases:
  - ipc-inspection-instrument
  - 18-domain-ipc-criteria
  - معايير-مكافحة-العدوى-الدور-الاجتماعية
tags:
  - source
  - infection-control
  - inspection-instrument
  - basira-v4
  - mhrsd
  - quality-management
created: 2026-06-16
updated: 2026-06-16
learned_at: 2026-06-16
confidence: high
source: drive:1oUri3HFJtjNvTEYxMNLtvRGKbh1hd8De
related:
  - "[[al-baha-ic-archive]]"
  - "[[basira-v4-requirements-ledger]]"
  - "[[mhrsd-rehab-center-forms]]"
  - "[[albaha-center-org]]"
  - "[[hrsd-work]]"
summary: >-
  The official MHRSD infection-prevention-control inspection instrument for
  social-care / rehab homes — 18 inspection domains / ~120 weighted sub-criteria,
  each scored مطابق(2) / مطابق جزئيًا(1) / غير مطابق(0) / NA, with a per-criterion
  verification method: D=documents, O=observation, SI=staff-interview. Complements
  al-baha-ic-archive (the program + Ahmad's trainer credential) by capturing the
  criteria field-structure. The criteria model Basira V4's IpcInspection (G-027)
  needs — it currently hard-codes only 5 items. Structure only; the filled
  Al-Baha instance is excluded per the PII gate.
---

# MHRSD IPC Inspection Instrument

## What this source is

The ministry's official IPC inspection instrument for social-care / rehabilitation homes (وحدة مكافحة العدوى, إدارة سلامة المستفيدين). It complements [[al-baha-ic-archive]] — that note covers the IC *program*, the 9-policy bundle, the BICSL-RC credential, and the committee governance; **this is the inspection *instrument*** the program is audited against. Distilled **structure-only**: the source is a *filled* Al-Baha instance carrying real compliance scores, resident/capacity/staff counts, and named officials — **all excluded here per the PII gate**; only the reusable instrument structure is recorded.

## The scoring model

- **Score scale (per criterion):** مطابق **(2)** / مطابق جزئيًا **(1)** / غير مطابق **(0)** / **NA** (لا ينطبق).
- **Verification method (per criterion):** **D** = مستندات (documents) · **O** = ملاحظة (observation) · **SI** = مقابلة الممارس الصحي (staff interview). A criterion can carry more than one method (e.g. `D/SI`).
- A criterion may carry a **note** — the real-world reason a score was "partial" — which a digital form must capture (a free-text field, not just the ordinal).

## The 18 domains (~120 sub-criteria)

| # | Domain (المعيار) | Sub-criteria |
|---|---|---:|
| 1 | برنامج مكافحة العدوى — IPC programme | 11 |
| 2 | نظافة/تطهير الأيدي — hand hygiene | 6 |
| 3 | مستلزمات الوقاية الشخصية — PPE | 4 |
| 4 | التدريب والتعليم — training & education | 3 |
| 5 | آداب السعال — cough etiquette | 3 |
| 6 | التباعد الاجتماعي — social distancing | 1 |
| 7 | الزوار والزيارات — visitors | 4 |
| 8 | الأمراض التنفسية والمعدية — respiratory/infectious disease | 10 |
| 9 | صحة العاملين — staff health | 3 |
| 10 | أدوات الاستخدام الواحد — single-use devices | 1 |
| 11 | تقنية التطهير — asepsis / disinfection technique | 13 |
| 12 | النفايات الطبية — medical waste | 9 |
| 13 | التخزين الطبي — medical storage | 7 |
| 14 | عيادة الأسنان — dental clinic | 12 |
| 15 | النقل الإسعافي — ambulance transport | 3 |
| 16 | الخدمات الغذائية — food services | 16 |
| 17 | المغسلة — laundry | 10 |
| 18 | صحة بيئة المنشأة — facility environmental health | 10 |

≈ 126 criterion lines across the 18 domains. Each is one row of `criterion · method(D/O/SI) · score(2/1/0/NA) · note`.

## Why this matters for Basira V4 (G-027)

V4's `IpcInspection` model hard-codes only **5 items** (handHygiene / ppe / surfaces / waste / isolation). The real instrument is **18 domains × per-criterion (score + verification-method + note)**. So **G-027 is not "verify the 5 items"** — it is "the schema needs an 18-domain criteria model with a per-criterion score, verification method, and note." This is **additive / in-place** — no rebuild. The dental-clinic domain (#14) is notable as the cross-link to the dental IPC forms ([[dental-infection-control-forms]] in the forms corpus, [[mhrsd-rehab-center-forms]]).

## Provenance

- **Source:** `معايير مكافحة العدوى الدور الاجتماعية` (Drive fileId `1oUri3HFJtjNvTEYxMNLtvRGKbh1hd8De`, native xlsx), via a Phase-2R crown-jewel extract (2026-06-08). **Criteria structure only** — the filled Al-Baha compliance scores, the per-domain %, the resident/capacity/staff counts, and the named officials (including Ahmad as IPC officer and the center director) are **excluded** and stay local; this note carries the reusable instrument shape, not the instance.
- **Method:** distilled 2026-06-16; faithful domain/criteria-count transcription, no filled-instance data ingested.
