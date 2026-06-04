---
id: basira-v4-org-roles-rbac
title: Basira V4 — Org Structure, Roles & Access Model
type: project
status: active
aliases: []
tags:
  - basira
  - basira-v4
  - org-structure
  - rbac
  - roles
  - project
created: 2026-06-04
updated: 2026-06-04
summary: >-
  Basira V4's organisational backbone and access model, distilled from the real comprehensive-rehab-center org charts (generic + Al-Baha) and Ahmad's S84 ministry decisions: a 4-level دائرة-to-section tree with five departments plus a director-reporting quality department, the مؤتمن default-open security model with one infectious-disease anti-stigma rule, and the demo-beneficiary / national-ID plug-in data model. Flags the missing department backbone V4 must adopt.
related:
  - "[[basira-v4-rebuild]]"
  - "[[albaha-center-org]]"
  - "[[al-baha-center-policies]]"
  - "[[basira-v4-disability-empowerment-model]]"
source: session:s85-basira-v4-gather
---

## Why this note exists

Basira V4 settled its *role list* and its *security philosophy* early, but it had no model of the organisation those roles live inside. This note distils the real center org structure (from the ministry-generic chart and the Al-Baha-populated instance) and Ahmad's S84 ministry-context decisions into one access-model reference. The headline gap it surfaces: V4 has the role list but **lacks the department backbone** to house a multidisciplinary care team — that backbone is the main input to Plan #2 (the rebuild structure). See [[basira-v4-rebuild]] and the center detail in [[albaha-center-org]].

## Organisational backbone (4 levels)

The center org chart defines exactly four hierarchy levels, in this order:

1. **مدير المركز** (center director) — top of the chart. At Al-Baha this is Ali bin Awad Al-Qarni ([[ali-alqarni]]), Ahmad's direct manager.
2. **قسم** (department / division).
3. **وحدة** (unit).
4. **شعبة** (section / branch — the leaf level).

So the chain is director → department → unit → section. Departments contain units; units contain sections.

### Departments reporting to the director

Five operational departments plus two cross-cutting offices report **directly** to the director:

- **قسم الخدمات الطبية** (Medical Services) — contains وحدة العلاج الطبي (medical treatment: physician, nursing, pharmacy, dental, psychological therapy, nutrition) and **وحدة العلاج التأهيلي** (rehabilitative treatment: physical therapy, occupational therapy, speech & language, medical records). **Physical therapy lives here**, as a specialty line under وحدة العلاج التأهيلي.
- **قسم المالية والتشغيل** (Finance & Operations) — disbursement/procurement (including الإعاشة, the catering/kitchen sub-section where the dental→soft-diet wire lands), maintenance & operations, and custody/assets.
- **قسم الخدمات الاجتماعية** (Social Services) — community rehabilitation, social follow-up, and family counseling (housing the social specialists, social observers/monitors, programs & activities, training, and aftercare).
- **قسم الخدمات المساندة** (Support Services) — administrative communications/archiving, human resources, IT (the نظام التأهيل / rehab-system unit), PR & media, and security & safety.
- **قسم الجودة** (Quality Department) — **reports DIRECTLY to the director**, not nested under another department. At Al-Baha it is headed by Ahmad himself. This is the seat that maps to V4's quality role (see below).
- **السكرتارية** (Secretariat) — cross-cutting office.

The brief described "four departments PLUS quality PLUS secretariat"; the source chart actually lists **five** operational departments (the support-services department is the fifth, distinct from the others). V4 should model the full five-department backbone, with quality as a sixth division reporting to the director and the secretariat as a cross-cutting office.

### Al-Baha-only addition

The Al-Baha instance adds one structural element absent from the generic ministry template: **المشرفة الإدارية لقسم الإناث** (administrative supervisor of the female section). This reflects an operational male/female ward split — قسم الذكور (male section) is the unmarked default and قسم النساء (female section) gets a named administrative supervisor. It is a supervision overlay, not a duplicated set of full departments. Demo cohort beneficiaries span both wards (see [[basira-v4-disability-empowerment-model]]).

### PT-naming variance (flag, do not silently reconcile)

The PT department's own procedures manual treats PT as a standalone **قسم** reporting to الإدارة الطبية and headed by a رئيس قسم العلاج الطبيعي. The operating org charts instead place it as a وحدة-level specialty under قسم الخدمات الطبية. Same function, two altitudes of naming — keep both in mind when modeling, and treat the operating-chart placement (وحدة العلاج التأهيلي) as canonical for the org backbone.

## Roles

V4's settled role list, cross-checked against the real chart:

- **مدير** (director) — all permissions; carries overall responsibility and urgent-case authority.
- **طبيب** (doctor / physician).
- **مسؤول الجودة** (quality officer) — **NOT "مدير الجودة"**. The real chart confirms this: it structures quality as a قسم reporting to the director and **never uses the title "مدير الجودة"**. مسؤول الجودة = the person heading that department.
- **أخصائي اجتماعي** (social specialist).
- **Entry-scoped roles** — operational staff scoped to where they enter data (some enter medical, some social). The real chart's long roster of clinical, social, finance/ops, and support roles (PT specialists/technicians, OT, speech therapists, nurses, social monitors, HR/IT/security officers, warehouse keepers, procurement/catering/clothing officers, etc.) slots into this bucket.
- **الإدارة العامة لرعاية وتأهيل ذوي الهمم** (General Administration for the Care & Rehabilitation of People of Determination) — note the official term is now **ذوي الهمم** (people of determination), not ذوي الإعاقة.
- **وكلاء الوزارة** (ministry deputies) — for the decision/approval engines.

### Delegation and temporary permissions

Required, not optional. Ahmad delegates (e.g. quality-KPI permissions) to a trusted colleague during leave or Eid; operating-company (non-government) staff hold no accounts but act under delegation. V4 must model temporary and delegated permissions, not just static role grants. This matters more once the ministry privatises center operation and the agency becomes supervisory.

## Access model

The access model is settled and deliberately simple — see the fuller rationale in [[basira-v4-rebuild]] and policy context in [[al-baha-center-policies]].

- **Default = OPEN.** Every authenticated user is a **مؤتمن** (trusted government employee) who signs a **تعهد** (pledge). They operate on a ministry-locked PC inside a center (ministry email + password login; no USB/CD; perimeter handled by the ministry environment). The credit-card / privacy-worship reflex does **not** apply.
- **No field masking, no سري/مقيد classification tiers, no security-spine.** This is an explicit anti-drift rule: field-classifying and security-hardening were the drift that hollowed V3.
- **Every access is logged** in AccessLog. Accountability replaces gatekeeping.
- **The ONE genuine restriction — infectious-disease status** (e.g. التهاب كبد وبائي / Hepatitis B): visible only to **direct-care medical roles (doctor, nurse)** and **suppressed on external printouts/exports**. The rationale is **anti-stigma, NOT privacy** — broadcasting it makes staff fear contact and can block services like charity housing (الإسكان الخيري). It removes a societal barrier, so it *serves* the compass; implement it as a single purpose-built rule, not a tiering system.

Overarching directive, repeated verbatim by Ahmad:

> لا تعقّد الأمور · لا تجعل الخصوصية عبادة · لا تضع عوائق.

("Don't complicate things · don't worship privacy · don't put up barriers.")

## Data model and CRUD

- **Beneficiaries = all DEMO** from the start: fake names, **no national ID, no real مستفيد number** — but **realistic diagnoses** so the demo covers the real population spectrum (the ~10-case Al-Baha cohort detailed in [[basira-v4-disability-empowerment-model]]).
- **Employees = real-ish** — real-style names are fine; they already appear in quality/governance operations. An employee's *actual* role can differ from their base title (e.g. a PT specialist working in Quality/IPC) and roles can change (e.g. secondment to Digital Transformation), so role must be mutable.
- **Full CRUD** on both beneficiaries and employees (add/edit/delete).
- **The plug-in model (must work without changing app behavior):** an "add beneficiary" flow takes a national-ID / مستفيد-number, pulls the basic social-research record from the ministry database, and **auto-provisions** the empowerment program, nutrition/الإعاشة program, care team, assigned social worker, and family linkage. Demo rows are transparently replaceable by real rows — same flow as adding a new beneficiary. The مستفيد-number is the always-present key (some beneficiaries — e.g. مجهولو النسب, unknown parentage — have no national ID but always have a مستفيد-number).

This is why data residency is not a blocker: the real beneficiary data already exists in ministry databases (today used only for statistics); post-approval the ministry's Digital Transformation and Compliance agencies handle hosting/residency/integration and connect via API. V4 ships demo data and designs the plug-in seam.

## Plan #2 input — the missing piece

The actionable finding for the rebuild structure (Plan #2): **V4 has the role LIST but not the DEPARTMENT BACKBONE.** The roles currently float without an org home for a multidisciplinary care team. V4 should adopt the five-department backbone (الطبية / المالية والتشغيل / الاجتماعية / المساندة) plus قسم الجودة reporting to the director, as the structure that houses the roles, scopes entry-roles to their department, and gives the cross-service triggers a real organisational topology to route through. Source detail and the disability-classification table sit in [[albaha-center-org]] and [[basira-v4-disability-empowerment-model]].
