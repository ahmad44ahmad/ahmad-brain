---
id: basira-v4-disability-empowerment-model
title: Basira V4 — Disability Taxonomy & Empowerment/Integration Model
type: project
status: active
aliases: []
tags:
  - basira
  - basira-v4
  - disability
  - empowerment
  - crpd
  - integration
  - project
created: 2026-06-04
updated: 2026-06-16
summary: >-
  How Basira V4 classifies disability without letting it become a ceiling: a 6-group taxonomy (~70 codes) and device-appropriateness rules used to prevent allocation mismatch, never to gate services. Adopt functional-fit guards, reject the مادة الصرف severity tiers and 8-track exclusion gates as disbursement-policy artifacts. CRPD-anchored de-institutionalization is the central empowerment trigger; start from goals, not diagnosis.
related:
  - "[[basira-v4-rebuild]]"
  - "[[social-handicap-compass]]"
  - "[[community-integration-project]]"
  - "[[empowerment-thesis-corpus]]"
  - "[[999-disability-care-empowerment-strategy]]"
  - "[[beneficiary-rights-document]]"
  - "[[basira-capability-domain-catalog]]"
  - "[[two-doors-empowerment-model]]"
source: session:s85-basira-v4-gather
---

## Purpose and scope

This note records how V4 represents disability and drives empowerment **without making disability a ceiling**. It covers the ministry's 6-group disability taxonomy, the device-appropriateness rules V4 adopts versus the severity gates it rejects, the integration-eligibility model and its eight service tracks, the CRPD anchors, and the open barrier-legend question. The organizational structure (the 5-department backbone, role list, and the Al-Baha instance) was extracted from the same source batch but belongs to its sibling note — see [[basira-v4-org-roles-rbac]]; this note links out for org and does not reproduce the chart.

Governing principle, drawn from the ministry's own self-diagnosis: the only entry into ministry services today is a disability-assessment step that mandatorily requires an original medical report to set disability type and degree, which locks the whole system into a medical model that asks "what is your diagnosis, which standard service fits it?" V4 inverts this. The KNOW surface leads with goals, barriers, and function; diagnosis is attached only as a mismatch-prevention fact that flows to whoever serves. See [[social-handicap-compass]].

> ما أهدافك وكيف ندعمك لتحقيقها؟ — *what are your goals and how do we support you in reaching them?* — replaces ما تشخيصك؟ — *what is your diagnosis?* — as the opening question. This frame is externally validated: it is the ministry's own report that names the medical gateway as the philosophical barrier.

## The 6-group disability taxonomy

Independently corroborated across two sources (the Al-Baha device-entitlement table جدول تصنيف الإعاقات وأجهزتها المساعدة — *disability classification and assistive-devices schedule*, and جدول الاعاقات الجديد — *the new disability table*). Exactly six top-level groups keyed by a thousands-code, ~70 individual codes total:

| Code | Group (Arabic) | English | Example sub-groups |
|---|---|---|---|
| 1000 | الإعاقات الجسدية | Physical | 1100 paralysis · 1200 amputation · 1300 weakness · 1605 deformities |
| 2000 | الإعاقات الذهنية | Intellectual | 2100 intellectual disability |
| 3000 | الإعاقات الحسية | Sensory | 3100 one / 3200 two / 3300 three sensory impairments |
| 4000 | الإعاقات النفسية | Psychological | 4100 chronic psychological |
| 5000 | الإعاقات المرضية | Medical/disease | 5100 body-parts · 5200 anemia · 5300 blood diseases · 5400 various |
| 6000 | الإعاقات المركبة | Compound/multiple | 6800 multiple disabilities |

The sub-group codes (1100/1200/1300...) give a ready-made second-level coding scheme V4 can reuse. The taxonomy is kept as a **reference lookup**, useful for (a) seeding realistic demo diagnoses across the spectrum and (b) auto-provisioning assistive-device needs when a beneficiary is added. The code is a convenience; the function is the truth. A code never caps a person.

## Compass resolution — appropriateness rules ADOPT, severity tiers REJECT

This is the load-bearing distinction. The Al-Baha table is, by construction, a severity-gated entitlement schedule, and that creates genuine tension with the V4 line. The resolution splits the document cleanly.

**ADOPT — the device-appropriateness rules (the ضوابط الصرف — *disbursement controls* — functional-fit subset):** these match function to device and are exactly the anti-mismatch logic V4 wants:
- A power wheelchair (كرسي كهربائي) requires intact cognition and vision AND age ≤ 75.
- No duplicate device from the same category for one beneficiary (wheelchairs excepted: a bath chair plus a regular chair are both allowed).
- A lightweight active-spec wheelchair (4–6 spec) requires proof of employment, study, or a driving licence.
- No double-issue of a power wheelchair plus a lightweight active chair.
- A special-spec device needs a treating-physician plus PT-specialist/audiologist report justifying the specific need.

These are functional-fit guards, not dignity gates — they prevent issuing the wrong device, e.g. no power wheelchair to someone without the cognition/vision/functional fit to use it safely.

**REJECT as a service-access gate — the مادة الصرف (*disbursement article*) severity tiers:** these map disability severity directly to device count, cash value, and renewal interval, and are a budget artifact (funded under budget line 27221, "معينات ذوي الاحتياجات الخاصة" — *assistive aids for people with special needs*):
- 23أ severe → up to 3 core devices · ~20000 SAR
- 23ب moderate → up to 2 · 14000 SAR
- 24أ mild → up to 1 · 10000 SAR
- 24ب lower-mild tier · 4000 SAR

The clean discriminator: the same disbursement policy **excludes residential-branch residents entirely** (plus non-Saudis and the state-hospitalized). That exclusion would remove exactly V4's own population — which is precisely why the severity/cash gating is a disbursement-policy axis, not a clinical-service axis. Adopt the appropriateness rules into the "prevent mismatched allocation" engine; document the severity tiers faithfully so V4 speaks the ministry's language; never let them enter the KNOW→SERVE clinical core, or they reintroduce the medical-model ceiling V4 explicitly rejects. The same pathology class recurs as a *funding-mechanism* instance in the custodial monthly statistical return — the **motor-ability tier** (طريح فراش/مقعد/متحرك) sets care-staffing ratios and funding, so dependency is rewarded and an improving resident *loses the center money*; see [[empowerment-ledger-vs-custodial-return]] for the generalization and its empowerment-ledger counterweight.

## Integration-eligibility model — the 8 service tracks

The community-integration initiative ([[community-integration-project]]) is the flagship empowerment program and the best fit for the V4 compass; V4 should present itself as that project's operational layer. Its real intake workbook defines 8 service tracks, each with a definition and eligibility gate, plus a 9th does-not-meet-criteria sheet:

1. **Day care** (الرعاية النهارية) — severe/moderate disability with cognitive delay, not in education, age ≥ 2, IQ < 50 (≥ 50 routes to education instead).
2. **Vocational rehab** (التأهيل المهني) — the employment entry; can benefit from vocational programs, mild-or-better disability (IQ ≥ 50), age 15–45 (waivable).
3. **Residential / comprehensive rehab** (التأهيل الشامل) — severe/multiple, cannot benefit from education or vocational, with no first-degree provider (منقطع/يتيم) and no pension > 3999 SAR.
4. **Extended medical care** (الرعاية المديدة) — chronic illness, cannot self-care; 5 patient levels defined.
5. **Social home care** (الرعاية المنزلية الاجتماعية) — CRPD Art. 19-based; bedridden, medically stable, has a provider, suitable family housing.
6. **Medical home care** (الرعاية الطبية المنزلية) — MoH-licensed, physician-led plan, skilled nursing.
7. **Orphans** (الأيتام) — Saudi children without suitable care, age < 7.
8. **Elderly** (كبار السن) — age ≥ 60, age-related (not disability-caused) inability to self-care.

**Recommend, never deny.** Every one of these gates — the IQ < 50 cutoffs, the epilepsy/psychiatric exclusions, the age windows, the no-pension > 3999 rule, and the 9-value disqualification enum (IQ > 50 · no intellectual disability · severity mild-to-moderate · psychiatric disorder · communicable disease · admission-barring conditions · intractable epilepsy · self/other-dangerous psychiatric disorder · self/other-dangerous behavioral disorder) — is preserved as **faithful documentation of how the ministry routes today**, used as functional inputs that suggest a fitting track and show the reason. None is wired as a hard deny inside V4. The most-dependent, who are excluded from nearly every track here, are exactly whom V4 serves via quality-of-care-as-empowerment. Two old gates are explicitly barriers V4 *dismantles*: the **communicable-disease blanket exclusion** (replaced by the anti-stigma flow-not-hide rule — infectious status flows to direct-care medical roles and is suppressed only on external printouts, so the person is served, not excluded), and the **Riyadh-only home-care scope** (adapted to Al-Baha for the V4 demo).

## Intake form, candidacy, and the de-institutionalization trigger

The real intake instrument is a ~16-field "بيانات" sheet repeated across tracks. **Proposed** V4 add-beneficiary schema (these are design shapes drawn from the form, not built capability): quadronomial name · gender · national ID (demo = null; real plugs in later) · DOB-Hijri/age · **beneficiary number** (the always-present key, present even with no national ID) · current service type · parents alive · who he lives with · legal-guardian name/ID/relation · family region/district · family income bracket · **other services the beneficiary or family needs** (the cross-service-routing seed) · specialist notes · are services available in the family region · expected enrolment year · reason-criteria-not-met (track 9 only).

The workbook also carries a 2020→2024 plan that transfers comprehensive-rehab residents OUT to less-institutional tracks, by year, as a percentage of the resident population. This **de-institutionalization plan is the empowerment cross-service trigger**: a resident is not a static record — he carries a candidacy for transfer to a more empowering setting, scheduled over time. The arrow, not the bed, is the unit of progress. Proposed shape: `IntegrationCandidacy { beneficiaryId, targetTrack, expectedYear, eligibilityChecks[], status, reasonIfNotMet }`, surfaced as a KNOW→SERVE action ("this person is ready for home-based care / vocational rehab") that also routes to the right external sector — MoH home-care, MoE schooling, housing, charity. See [[basira-v4-cross-service-triggers]]. This is the empowerment analogue of the proven dental→soft-diet wire.

## CRPD anchors and de-institutionalization

The initiative is anchored in the UN Convention on the Rights of Persons with Disabilities (signed by KSA in 2008): **Article 23** (respect for home and the family — obligating the state to give families information, services, and support to raise their member with a disability) and **Article 19** (living independently and being included in the community — the basis for the social home-care track). The Model Gap named in the ministry's own report is sharp: the stated goal is community inclusion, yet the operating model is the segregated comprehensive-rehab center, which as a total institution manufactures the isolation it is meant to cure. De-institutionalization — moving the person from institutional warehousing toward community living — is therefore THE central empowerment cross-service trigger, not an afterthought.

## The B1–B10 social-handicap barrier legend — RECOVERED VERBATIM (corrected S85)

**Correction (2026-06-04, verified against primary source):** an earlier draft of this note claimed only B1/B2/B4/B6/B7/B8 survive and recommended defining the legend fresh from CRPD. That was **wrong.** The complete 10-code legend is present **verbatim** in the primary source `C:\dev\basira\supabase\sql\022_barrier_type_annotations.sql` (and `harvest/02-v2.md`): **B1** عائق passive physical · **B2** تحدٍّ procedural friction · **B3** خصم declared adversary · **B4** مضادّ systemic resistance · **B5** داعم مزيّف fake supporter (signs but blocks) · **B6** مصدر خوف stigma source · **B7** خوف internalized fear · **B8** عُرف اجتماعي unwritten social norm · **B9** ثقافة تابو cultural taboo · **B10** مُسلَّم ديني unquestioned (religious) dogma.

It is also **already wired**: migration 022 annotates real columns with the barrier(s) they signal via `COMMENT ON COLUMN` (`beneficiaries.mobility_type → B1`; `daily_care_logs.mood → B6,B7`; etc.), and the requirements ledger §A–§D already tags capabilities with these codes. **Decision: keep the V2-attested nature-axis legend as canonical** (medical→social→cultural spectrum, the exact social-not-medical frame); use CRPD only as a *secondary* defensibility anchor plus an orthogonal `crpd_domain` tag for the life-domains V2's axis doesn't name (work/education/health/community-living). Redefining on CRPD axes would corrupt every existing barrier tag. See [[basira-v4-rebuild]] PLAN §5.2 / §7-D2. The earlier "define fresh" instruction rested on this note's false premise and is void pending Ahmad's confirmation.

## Honesty flags carried forward

- The 16-field schema and `IntegrationCandidacy` are proposed shapes from real forms, not yet built.
- Several strategic source documents in the corpus are AI-generated with hallucinated specifics; their diagnostic themes (the medical-vs-social model shift, outputs-vs-outcomes) are used as framing only, never as facts of record. Unverified figures (e.g. an "84% lack an emergency plan" stat) are treated as illustrative, not cited KPIs. The outputs-vs-outcomes critique and real KPI trajectory live in [[mhrsd-kpi-landscape-2024-2026]].
- No surveillance/camera capability is adopted; the safety-plan gap is answered with per-beneficiary plans and behavioral alternatives to restraint, consistent with the compass.
