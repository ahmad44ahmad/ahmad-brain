---
id: mhrsd-2025-kpi-portfolio
title: "MHRSD 2025 KPI Portfolio — تعميم 28597 (Comprehensive Rehab Centers)"
type: source
status: active
aliases:
  - kpi-2025
  - تعميم-28597
  - 2025-performance-indicators
  - مؤشرات-الأداء-2025
  - albaha-scorecard-2025
tags:
  - 999-docs
  - kpis
  - performance-measurement
  - mhrsd
  - rehabilitation-centers
  - 2025
  - albaha-center
  - basira-evidence-stack
created: 2026-04-25
updated: 2026-04-25
valid_from: 2025-01-05
learned_at: 2026-04-25
confidence: high
source: drive-folder-jsonl:#5, gemini-summary:2026-04-24
summary: >-
  English distillation of the official 2025 KPI portfolio for MHRSD's 36
  comprehensive rehabilitation centers, anchored by تعميم 28597 (6/7/1446H ≈
  5 January 2025). The binding scorecard that turns center performance into
  individual director accountability. Departmental weights: Medical 30%,
  Nursing 25%, Pharmacy 12%, Social composite. ~40% of KPI inventory remains
  un-enumerated in the JSONL — verify against source PDF when citing
  specifics. Two zero-event medical KPIs flagged for the empowerment-thesis
  "صفر حوادث" under-reporting anti-pattern. Ahmad named personally as
  رئيس قسم الجودة in the ministerial field-visit form.
related:
  - "[[mhrsd-2025-kpi-portfolio-ar]]"
  - "[[999-albaha-qms-bcp]]"
  - "[[al-baha-quality-project-2024]]"
  - "[[empowerment-vocabulary]]"
  - "[[ahmad-2025-achievements]]"
  - "[[mhrsd-leadership]]"
  - "[[mhrsd-dev-sector-esystems]]"
  - "[[albaha-center-org]]"
  - "[[albaha-regional-admin]]"
  - "[[nasser-alqahtani]]"
  - "[[hrsd-work]]"
  - "[[social-handicap-compass]]"
  - "[[drive-vault-coverage-audit]]"
---

# MHRSD 2025 KPI Portfolio — تعميم 28597

## What this document is

A 21-file Drive folder titled *2025 مؤشرات الأداء البداية* ("2025 Performance Indicators — Initial Set"). Anchored by *تعميم رقم 28597، تاريخ 6/7/1446هـ* (≈ **5 January 2025 Gregorian**) — the binding ministerial circular that establishes the 2025 KPI portfolio for **all 36 MHRSD comprehensive rehabilitation centers**, including Al-Baha.

**Ownership.** Issued by the Ministry (وزارة الموارد البشرية والتنمية الاجتماعية), routed through *وكالة التأهيل والتوجيه الاجتماعي* — currently held by [[nasser-alqahtani]] (replaced Al-Wuhaibi).

**Audience.** Center directors + quality officers + heads of medical / nursing / social / pharmacy / support departments across the 36-center network, with regional social-supervision offices (e.g., Al-Baha — see [[nuwaira]]) as cc-recipients.

**Shape.** A centralised portfolio designed to **unify performance-measurement methodology kingdom-wide** and serve as the basis for **التقييم الرسمي للأداء** (official performance evaluation) of each center director. KPIs are *not advisory* — non-compliance is attributable to the director personally.

## Position in the stack

This note pairs with three siblings:

- [[999-albaha-qms-bcp]] — methodology synthesis (operational QMS framework that *implements* monthly data capture feeding these KPIs).
- [[al-baha-quality-project-2024]] — Al-Baha-side evidence corpus (F-2.1 sibling). The center's quality work *reports into* this portfolio.
- [[ahmad-2025-achievements]] — the 10 approved achievements all map (provisionally) to KPIs in this portfolio.

The triangulation: ministry issues the scorecard → Al-Baha center implements via QMS → Ahmad's individual achievements map to specific KPI satisfactions → Al-Qarni endorses → portfolio updates next year.

## تعميم 28597 — the master circular

| Field | Value |
|---|---|
| **Number** | 28597 |
| **Hijri date** | 6/7/1446 H |
| **Gregorian** | ≈ 5 January 2025 |
| **Issuing authority** | الوزارة (MHRSD ministerial) |
| **Routing agency** | وكالة التأهيل والتوجيه الاجتماعي |
| **Authoritative artefact** | *تعميم حقيبة مؤشرات الاداء لمراكز التاهيل الشامل للعام 2025م.pdf* |
| **Mandate** | Center administrations *must* (يطالب) achieve the targets and maintain supporting documentation. Basis for official performance evaluation. |
| **Scope** | All 36 comprehensive rehabilitation centers |

The "البداية / initial set" in the folder name implies an iterative cycle — a Q2/mid-year revised set is plausible but not surfaced by the catalog.

## KPI inventory by department

The portfolio organises into departmental buckets with explicit weights summing toward the center's aggregate score. The Gemini summary gives near-complete numerics for Medical and Nursing, structural-only for Social, and weight-only for Pharmacy. **Significant un-enumerated content remains** — see Red Flags §3.

### Medical — **30%** of center score

| KPI (AR) | English gloss | Polarity | Target | Weight | Formula |
|---|---|---|---|---|---|
| عدد حالات التقييد خلال الشهر الحالي | Restraint-use cases | + | 100% | 4% | (20 − cases) / 20 × 100 |
| عدد حالات الإصابات الجسيمة | Serious injuries | − | **0%** ⚠️ | **10%** | 100 − ((total − injuries) / total × 100) |
| الأمراض المعدية الواجبة للإبلاغ | Notifiable infectious-disease cases | + | 100% | 4% | (5 − new cases) / 5 × 100 |
| الإصابات الناتجة عن السقوط | Fall-related injuries | + | 100% | 4% | (5 − fall injuries) / 5 × 100 |
| نسبة المستفيدين المحالين والمقبولين | Referral acceptance rate | + | 100% | 2% | Accepted / Referred × 100 |

**Listed sum: 24%; bucket weight: 30% → 6% un-enumerated** in the JSONL pass.

### Nursing — **25%** of center score

| KPI (AR) | English gloss | Polarity | Target | Weight | Aggregation |
|---|---|---|---|---|---|
| نوبات الصرع | Seizure episodes handled | − | <10% | 3% | Interim |
| قرح الفراش | Pressure ulcers (bedbound) | + | 100% | 4% | Interim |
| تدخل الهلال الأحمر | Red Crescent emergency call-outs | − | <10% | 5% | Interim |
| التحاليل المخبرية الدورية | Periodic lab-test coverage | + | 100% | 2% | Cumulative — semi-annual |
| العيادات المتخصصة | Specialist-clinic coverage | + | 100% | 2% | Cumulative — quarterly |

**Listed sum: 16%; bucket weight: 25% → 9% un-enumerated.**

### Pharmacy — **12%** of center score

Weight known; **zero individual KPIs enumerated** in the JSONL. Fully un-enumerated until the source PDF is read.

### Social — weight unspecified in JSONL (composite indicators, quarterly)

Three composite areas, each with sub-KPI weights:

1. **تنمية المهارات (Skill development).** Sub-KPIs: % training-plan execution, % beneficiary training (~40% of sub-bucket), % family participation. Independence skills (eating, toileting) + social skills (behaviour modification). Evidence: *استمارة التدريب*.
2. **البرامج والأنشطة (Programmes & activities).** Sub-KPIs: % internal activities (~30%), % external activities (~30%), % family participation (~20%), % external-body participation (~20%). **Annual target: 192 activities/year = 12 internal + 4 external per month.** Evidence: *نموذج رقم (1–3)*.
3. **التواصل الأسري (Family communication).** Sub-KPIs: external visits, internal visits, video calls (~35%), phone calls. Evidence: *سجل الزيارات*. Ministry's worked example draws from **Al-Baha January 2025: 254 total beneficiaries, 243 reached, 143 of 254 from outside the region** — geographic friction → heavy reliance on video.

### Administration & Quality (implicit)

The field-visit form (*استمارة الزيارات الميدانية*) records center demographics — Al-Baha: 254 residents = 133 M / 121 F — and lists organisational structure. The form **names "أحمد عبد الله الشهري — رئيس قسم الجودة"** explicitly. Ahmad appears by name in the ministerial artefact for the 2024–25 portfolio period. Personally load-bearing.

## Scorecard structure / weighting

The model is an **additive weighted sum across departments** (not a balanced-scorecard four-perspective). Named bucket weights (4 of 5+):

| Bucket | Weight |
|---|---|
| Medical | 30% |
| Nursing | 25% |
| Pharmacy | 12% |
| Social | unspecified (composite) |
| **Sum (named)** | **67%** |

The remaining ~33% covers Social + any additional buckets not surfaced by Gemini.

**Aggregate score → rubric band:**

- ممتاز (Excellent): 80–100%
- جيد جداً (Very good): 60–79%
- جيد (Good): inferred middle band
- ضعيف (Weak): <40% or <60% — **inconsistent in source**

⚠️ **Band threshold inconsistency**: the source uses both "<60%" and "<40%" as the "weak" cutoff in adjacent rows. This is a real source ambiguity — likely *per-department* thresholds rather than a single rubric. Verify against the PDF before quoting any specific band.

## Honest claim flagging

Three structural concerns the wiki note must surface, not bury:

### 1. Zero-event medical KPIs — under-reporting anti-pattern

The medical bucket includes two zero-event targets:

- *الإصابات الجسيمة* — target **0%**, weight **10%** (largest single weight).
- *حالات التقييد* — formula rewards absence of recorded restraint.

Both sit inside the empowerment-thesis "صفر حوادث / طغيان المؤشرات الكمية" anti-pattern documented in [[drive-vault-coverage-audit]] §3.3 (Critique vocabulary). When staff are scored on the *absence* of an event, behavioural incentives shift toward **under-reporting** rather than reduction. The KPI design effectively criminalises honest documentation of clinically necessary restraint or unavoidable injury.

When this portfolio is cited (e.g., as evidence under [[basira-leadership-compass]]), this critique should travel with it. The portfolio's design embeds the very pathology Ahmad's empowerment thesis names.

### 2. Medical-model framing throughout

KPI naming uses medical-model language: "أمراض معدية", "حالات التقييد", "نوبات الصرع", "إصابات", "تدخل الهلال الأحمر". There is no counter-metric for therapeutic engagement, dignity preservation, or beneficiary self-report. This is straightforward for a 2025 portfolio (the social→empowerment policy pivot post-dates it), but **the framing tension should be preserved** — the portfolio is current operational reality even as the policy direction officially repudiates its underlying model.

### 3. ~40% of scorecard un-enumerated

Pharmacy (12%) + Social weight (unspecified) + 6% Medical + 9% Nursing = roughly 40% of the actual scorecard is not enumerated in the JSONL summary. Cite this portfolio's framework with confidence; cite specific KPI numerics with explicit "JSONL gap — verify against source PDF" caveats.

## Tie-in to the 10 2025 achievements (inferred — flag explicitly)

Plausible KPI-to-achievement mappings (verify against [[ahmad-2025-achievements]] before citing):

| Likely achievement domain | Likely KPI |
|---|---|
| Infection-control training / Wiqaya–Hisn registration | Medical *الأمراض المعدية* (4%) |
| Fall-prevention program | Medical *الإصابات الناتجة عن السقوط* (4%) |
| Restraint-reduction / least-restrictive environment | Medical *حالات التقييد* (4%) — flagged for under-reporting risk |
| Pressure-ulcer prevention (PT-led positioning protocols) | Nursing *قرح الفراش* (4%) |
| PT-supported specialist-clinic throughput | Nursing *العيادات المتخصصة* (2%) |
| Family-communication / video-visit rollout | Social *التواصل الأسري* (composite) |
| Activities & external-community programs | Social *البرامج والأنشطة* (192/year target) |
| PT training-plan execution | Social *تنمية المهارات* |
| Quality-chief / QMS-BCP work | Field-visit form names Ahmad as رئيس قسم الجودة; supports umbrella scorecard |

## Load-bearing Arabic quotes

- *"حقيبة مؤشرات الأداء (KPIs) لمراكز التأهيل الشامل للعام 2025م"* — canonical name.
- *"تعميم رسمي (الرقم: 28597، التاريخ: 6/7/1446هـ) من الوزارة يطالب إدارات المراكز بتحقيق مستهدفات هذه المؤشرات"* — binding clause.
- *"توحيد منهجية قياس أداء المراكز على مستوى المملكة"* — the *why*: kingdom-wide unification.
- *"ضمان تحقيق الأهداف الاستراتيجية للوزارة في مجالات الخدمات الاجتماعية والصحية والتشغيلية"* — three domain pillars.
- *"التقييم الرسمي للأداء"* — the framing that turns KPIs into individual-accountability instruments.
- *"المستهدف 192 نشاطاً سنوياً، بمعدل 12 داخلي و 4 خارجي شهرياً"* — hard operational target.
- *"مؤشر يناير 2025 بالباحة يوضح أن 143 مستفيداً خارج المنطقة"* — Al-Baha datum embedded in the ministerial portfolio (Al-Baha is a worked example, not just a recipient).
- *"أحمد عبد الله الشهري — رئيس قسم الجودة"* — Ahmad named in the ministerial field-visit form.

## Cross-references

**Evidenced (strong link):**

- [[999-albaha-qms-bcp]] — operational QMS that implements monthly data capture feeding these KPIs.
- [[al-baha-quality-project-2024]] — sibling F-2.1; Al-Baha side reports into this scorecard.
- [[ahmad-2025-achievements]] — 10 achievements map (provisionally) to specific KPIs.
- [[mhrsd-leadership]] — issuing authority. [[nasser-alqahtani]] is current وكيل.
- [[albaha-center-org]] — receiving center; field-visit form names the org structure.
- [[albaha-regional-admin]] / [[nuwaira]] — regional oversight layer; cc-recipient.
- [[hrsd-work]] — umbrella project.
- [[mhrsd-2025-kpi-portfolio-ar]] — Arabic raw companion.

**Inferred / methodological:**

- [[mhrsd-dev-sector-esystems]] — digital surface that likely consumes monthly KPI reports.
- [[social-handicap-compass]] — KPI design embeds medical-model framing the social-handicap compass repudiates; tension worth preserving.
- [[basira-leadership-compass]] — the leadership-compass surface is the natural decision-layer above this scorecard.

## Red flags / open questions

1. **~40% scorecard un-enumerated** in JSONL — Pharmacy fully, Social weight, 6% Medical, 9% Nursing. Read PDF before citing complete inventory.
2. **Band threshold inconsistency** ("<60%" vs "<40%" for "weak") — possibly per-department; verify.
3. **Zero-event KPI anti-pattern** — Serious Injuries 0% target / 10% weight; Restraint formula. Surface critique alongside any citation.
4. **2026 supersession status unknown** — given today is 2026-04-25, a 2026 portfolio almost certainly exists. This file is historical/comparative.
5. **"البداية / initial set"** in folder name implies an iterative cycle. A revised mid-year set may exist; not surfaced.
6. **Folder fileId not yet resolved** — JSONL stores idx, not Drive folder IDs. Resolve via Drive MCP `title contains '2025 مؤشرات الأداء'` when targeted reads are needed.
7. **Carry-over signal**: *نماذج مؤشرات الاداء للعام 2024 (القسم الاجتماعي).xlsx* — social-side form pulled forward from 2024 unchanged. Suggests the social-side revision lagged.
8. **Signatory not captured in JSONL** — read PDF first page to capture.

## Provenance

- **Drive folder JSONL idx:** #5. See [[drive-folders-master-index]].
- **Folder fileId:** unresolved.
- **Issuing body:** الوزارة (MHRSD ministerial).
- **Routing agency:** وكالة التأهيل والتوجيه الاجتماعي. Current وكيل: [[nasser-alqahtani]].
- **Circular instrument:** تعميم رقم 28597، 6/7/1446 H ≈ 5 January 2025.
- **Source-summary author:** Google Gemini, single pass (idx #5, ~5,297 chars).
- **Personal anchor:** Ahmad named in the ministerial field-visit form as *رئيس قسم الجودة* — the document carries personal historical weight beyond methodology.
- **Distilled:** 2026-04-25 (F-2.2 of the audit ingestion plan).
