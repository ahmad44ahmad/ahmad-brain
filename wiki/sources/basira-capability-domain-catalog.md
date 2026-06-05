---
id: basira-capability-domain-catalog
title: "Basira Empowerment Redesign — Capability-Domain Catalog, Clinical Instruments & HRSD Pathways"
type: source
status: active
aliases:
  - capability-domain-catalog
  - empowerment-redesign-artifacts
  - مكتبة-المجالات-القدراتية
  - 11-capability-domains
  - hrsd-five-pathways
  - tawafuq
  - mowaamah
  - bitaqat-qudra
tags:
  - basira
  - basira-v4
  - empowerment
  - disability
  - capability-domains
  - clinical-instruments
  - hrsd-pathways
  - crpd
  - source
created: 2026-06-05
updated: 2026-06-05
source: local:C:\Users\aass1\Desktop\empowerment-redesign\
summary: >-
  The operational/clinical layer the empowerment-strategy vault notes lacked.
  Captures the 11-domain capability taxonomy as Basira's navigation axis
  (replacing diagnosis), the named evidence-based instrument stack (ICF, SIS-A,
  Schalock QoL, PCP/MAPS, Active Support, PBS/NICE-NG11, Customized Employment),
  the 5 official HRSD service pathways + the 2024 amendment, the foundational-track
  rule, and the Saudi vocational ecosystem (Tawafuq/Mowaamah/Qaderoon). NOT a
  restate of the maturity model or coined lexicon — those live in the related notes.
related:
  - "[[basira-v4-disability-empowerment-model]]"
  - "[[basira-v4-rebuild]]"
  - "[[empowerment-thesis-corpus]]"
  - "[[community-integration-project]]"
  - "[[999-disability-care-empowerment-strategy]]"
  - "[[empowerment-vocabulary]]"
  - "[[beneficiary-rights-document]]"
---

# Basira Empowerment Redesign — Capability-Domain Catalog, Clinical Instruments & HRSD Pathways

## Why this note exists (and the exact delta it carries)

The empowerment vault is already strong on **doctrine and language**: the 1.0→2.0→3.0 maturity model and coined
lexicon ([[empowerment-thesis-corpus]], [[empowerment-vocabulary]]), the de-institutionalisation strategy + KPIs
([[community-integration-project]]), and the master strategy portfolio ([[999-disability-care-empowerment-strategy]]).
The V4 note [[basira-v4-disability-empowerment-model]] carries the **ministry's own administrative artifacts** — the
6-group device-entitlement taxonomy, the 8 *service-eligibility* tracks, the 16-field intake form, the B1–B10 barrier
legend.

This note carries the one layer none of those hold: the **international-evidence-based clinical/operational design**
of the Basira v3 Empowerment Module redesign (Desktop `empowerment-redesign\` Artifacts A–C). Do not confuse its two
pathway-like structures with the ones already vaulted:
- The **5 HRSD *service pathways*** here (Preparation/Employment/Integration/Residential/Day) are the *regulatory
  program tracks* a beneficiary lives inside — distinct from the **8 *service-eligibility tracks*** in
  [[basira-v4-disability-empowerment-model]] (intake routing gates).
- The **11 capability domains** here are the *teaching/navigation axis* — distinct from the **6-group disability
  taxonomy** there, which is a *device-allocation lookup*.

## The architectural pivot — capability domain replaces diagnosis as the navigation axis

The redesign's enforced rule: programs, goals, sessions, dashboards and reports are organised by **capability domain,
never by disability type**. Diagnosis is a medical attribute on the profile; it never appears as a filter, category,
or navigation axis. This is the *operational mechanism* for the "start from goals not diagnosis" frame already in
[[basira-v4-disability-empowerment-model]] and [[empowerment-vocabulary]] — this note supplies the concrete 11-axis
structure that makes it shippable.

**The 11 capability domains** (each maps to one Schalock QoL dimension and one ICF chapter):

| # | Domain | الاسم | QoL anchor | ICF |
|---|---|---|---|---|
| 1 | Mobility & Physical Function | الحركة والوظائف الجسدية | Physical Wellbeing | d4 |
| 2 | Self-feeding | الإطعام الذاتي | Physical Wellbeing | d550 |
| 3 | Social Interaction | التفاعل الاجتماعي | Interpersonal Relations | d7 |
| 4 | Communication | التواصل | Self-Determination | d3 |
| 5 | Self-care & Hygiene | العناية الذاتية والنظافة | Physical Wellbeing | d5 |
| 6 | Domestic Skills | المهارات المنزلية | Personal Development | d6 |
| 7 | Community Skills | المهارات المجتمعية | Social Inclusion | d460/d470/d860 |
| 8 | Functional Cognitive | المهارات المعرفية الوظيفية | Personal Development | d1 |
| 9 | Recreation & Leisure | الترفيه والاستجمام | Emotional Wellbeing | d920 |
| 10 | Pre-vocational | المهارات قبل المهنية | Personal Development | d825/d840 |
| 11 | Vocational | المهارات المهنية | Material Wellbeing + Rights | d845/d850/d855 |

Each domain decomposes to 12–15 *behaviourally observable* sub-skills, each probe-able with the standard 6-level
prompt hierarchy **I / V / G / M / P / F** (Independent / Verbal / Gestural / Model / Partial-physical / Full-physical).
Default mastery = 80% Independent across 3 consecutive sessions + 1 generalisation probe; foundational-track mastery is
**QoL/engagement-weighted instead of independence-weighted**.

## The evidence-based instrument & practice stack (named, with their data-model homes)

The distinctive payload — the named international instruments the redesign adopts and where each lands (ARTIFACT-C):

- **ICF / ICF-CY + WHODAS 2.0** — functioning frame; capacity-vs-performance gap = the *environmental-barrier signal*. Codes surfaced as plain-Arabic sentences, not `e3601.2`.
- **SIS-A / SIS-C** (Supports Intensity Scale) — drives `support_intensity_level ∈ {minimal, intermittent, extensive, pervasive}`, which sets review cadence + foundational-track auto-enrolment. `clinical_judgment` allowed so under-resourced centres aren't blocked.
- **Schalock & Verdugo 8-domain QoL** — the **outcome of record** (POS/GENCAT). Goal-mastery is only a *process* indicator; QoL movement is the outcome.
- **Vineland-3 + ABAS-3** — adaptive-behaviour scales; explicitly *not* IQ-equivalents and *not* a basis for pathway assignment.
- **AIR Self-Determination Scale** — *capacity* vs *opportunity* subscales separate; the gap surfaces structural barriers in the centre itself.
- **Person-Centered Planning** (PATH / MAPS / one-page) — MAPS default for high-support-needs; the beneficiary's verbatim words under "صوت المستفيد".
- **Supported Decision-Making (CRPD Art. 12)** layered with ولي الأمر (*legal guardian*) — guardian is *one* decision partner, not sole authority; ISP needs the beneficiary's own consent timestamp before activation (`beneficiary_consented_at` + `guardian_consented_at` separate).
- **Active Support** (Mansell/Beadle-Brown) — engagement-% in 15-min windows becomes a centre KPI; minimum-prompt, fade-within-session.
- **PBS / NICE NG11** — restrictive practices logged with justification + 28-day mandatory-review; PRN-psychotropic-as-restraint surfaceable.
- **Supported Employment** — IPS (place-then-train), **Customized Employment** (Griffin-Hammis Discovery), **Project SEARCH**; sheltered-workshop is *not* a Programs-Library option (only a last-resort `placement_type`).
- **AAC incl. Saudi Sign Language (SSL)** — per-beneficiary lexicon across `verbal/sign_ssl/pecs/sgd/gesture/mixed`; SSL is a first-class legally-recognised modality.

## The 5 official HRSD service pathways + the 2024 amendment

Grounded in the **Ramadan/September 2024 ministerial amendment** to the *Regulations of Social and Vocational Programs
for PWDs* (per ARTIFACT-A §3.2): reorganised around 5 named pathways, made the **ISP the regulator-facing artefact**,
mandated beneficiary participation as a *validity* condition, embedded SSL reasonable-accommodation, and tied vocational
placements to Tawafuq. **APD** (هيئة رعاية الأشخاص ذوي الإعاقة, *Authority for the Care of PWDs*) is the
licensing/inspection regulator.

> ⚠️ Article numbers in the artifacts' compliance report are **placeholders** keyed to CRPD/Saudi-PWD-regulation
> structure — the exact Gazette article numbers must be substituted before any ministry submission.

The 5 pathways: **مسار الإعداد** (Preparation) · **مسار التشغيل** (Employment) · **مسار الإدماج** (Community
Integration) · **مسار الإيواء** (Residential — goal-of-record is *high QoL in the residential setting*, not exit) ·
**مسار النهاري** (Day Service).

**Severe-support-needs rule (load-bearing, stamped 2026-05-17):** these beneficiaries are **not a sixth pathway**.
They stay inside الإيواء/النهاري with `support_intensity_level = 'pervasive'`, routed to the foundational track
**«التمكين التأسيسي»** (*foundational empowerment* — program P17, Active-Support-default, QoL-weighted mastery) inside
the same Programs Library. This preserves the regulator's 5-pathway structure while giving the highest-need population
a named evidence-based answer.

## Saudi vocational ecosystem (the program-integration layer)

Named here for the first time in the vault as *operational integration points* (vs the strategic
Pay-for-Success/individual-budgets frame in [[empowerment-thesis-corpus]]):
- **توافق Tawafuq** — HRSD/HADAF national PWD-employment program. **بطاقة قدرة (Kudra card)** = employer-subsidy eligibility; **Article 28** = 4% quota for 25+-employee firms (already in [[999-disability-care-empowerment-strategy]]); job-coach funding; sign-language call centre.
- **مواءمة Mowaamah** — establishment accessibility certification (Gold/Silver/Bronze); surfaced as a centre KPI.
- **قادرون Qaderoon** — Business Disability Network; member partners are higher-likelihood Customized-Employment candidates.
- **إحسان Ehsan** — social-services platform; no live integration in scope (future dignity-profile ↔ Ehsan link).

## Data-model shape (ARTIFACT-C, additive migration)

Additive PostgreSQL/Prisma migration (idempotent, RLS-ready). Reference tables `capability_domains` / `qol_domains` /
`pathways` / `icf_code_dictionary` / `programs` (P01–P17); per-beneficiary `pathway_assignments`, the named assessment
tables above, `pcp_documents`, `isps` (+ `isp_team_members.is_decision_partner`), `engagement_sessions`,
`behavior_plans/_incidents`, and the partnership stack `partners`/`mous`/`placements`/`transition_plans`. Key
existing-table additions: `beneficiaries.support_intensity_level` + `current_pathway_id`, and on `rehab_goals` the
pivot column `capability_domain_id` (what is taught) coexisting with legacy `domain` (who teaches). **ISPs are never
deleted** — supersession via `previous_isp_id`. The ISP cannot save without `valued_role_ar` (Social Role
Valorization, Wolfensberger).

## Honest flags

- Artifacts A–C are a **design proposal for v3**, not built capability — same status caveat as the proposed schemas in [[basira-v4-disability-empowerment-model]]. Treat the 11 domains + instrument stack as the **specification to port into V4**, not as shipped.
- The 2024-amendment article numbers are unverified placeholders (see warning above).
- Demo archetypes + Al-Baha vocational tracks (ARTIFACT-A §5.4 / B §11) are demo content, not doctrine — not reproduced here.
- Artifacts D (IA roadmap), E (dashboards), F (demo seed) are build-spec, not knowledge — not distilled.
