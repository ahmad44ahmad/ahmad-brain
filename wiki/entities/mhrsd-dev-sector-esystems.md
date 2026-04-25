---
id: mhrsd-dev-sector-esystems
title: MHRSD Development Sector — Electronic Systems Inventory
type: entity
status: active
aliases:
  - mhrsd-esystems
  - dev-sector-portal
  - بوابة الخدمات الإلكترونية لقطاع التنمية
tags:
  - entity
  - mhrsd
  - digital-systems
  - development-sector
  - basira-integration
created: 2026-04-24
updated: 2026-04-25
valid_from: 2026-04-23
learned_at: 2026-04-23
confidence: medium
source: voice-msg:2026-04-23
related:
  - "[[hrsd-work]]"
  - "[[basira]]"
  - "[[mhrsd-leadership]]"
  - "[[nasser-alqahtani]]"
  - "[[drive-vault-coverage-audit]]"
summary: >-
  Inventory of MHRSD's Development Sector (قطاع التنمية) electronic systems —
  umbrella portal plus four major sub-systems plus two supporting systems.
  Useful for understanding the ministry's current digital surface and for
  Basira integration planning. Each sub-system is a potential integration
  target; priority ordering included.
---

# MHRSD Development Sector — E-Systems Inventory

Ahmad walked through the Development Sector e-systems on 2026-04-23 while preparing materials for the Khalid Saleh strategic file. This is the ministry's current digital landscape for قطاع التنمية (Social Development Sector).

## Umbrella portal

**بوابة الخدمات الإلكترونية لقطاع التنمية** — the main entry point. Links out to:

- المنصة الوطنية للتأهيل والتوجيه الاجتماعي
- برنامج استدامة وتمكين
- المنصة الوطنية للعمل التطوعي
- Individual services (أفراد)

### Individual services at the umbrella level

- **تقييم الإعاقة** (Disability Assessment) — ⚠️ uses the medical model per current policy, contradicting the social-model direction.
- **طلب إعانة مالية** (Financial Assistance Request).
- **شهادة تعريف بالاحتضان** (Fostering Certificate).
- **التسجيل بدون رعاية كبار السن** (Elderly Without Care — registration).

---

## Sub-system 1 — المنصة الوطنية للتأهيل والتوجيه الاجتماعي

**Owner:** وكالة التأهيل والتوجيه الاجتماعي — now [[nasser-alqahtani]].

**Services for private centres:**

- إصدار موافقة مبدئية
- إصدار ترخيص
- تجديد ترخيص
- نقل مركز

**User-account features:**

- تحديث البيانات الشخصية
- استعراض الطلبات السابقة
- التنبيهات والإشعارات
- حفظ طلب

**Ahmad's assessment:** *"يبغالها إعادة تصميم صراحة"* — needs redesign (UX critique from a quality-admin perspective).

**Strategic opening for [[basira]]:** this platform has no governance/decision-surface layer equivalent to the Leadership Compass. Basira could integrate as a decision layer on top of this platform's data.

---

## Sub-system 2 — برنامج استدامة وتمكين

**Likely owner:** الهيئة العامة للأوقاف (Ahmad not 100% certain).

**Strategic objectives:**

- تحقيق الاستدامة المالية
- رفع مساهمة القطاع غير الربحي
- توجيه مصارف الأوقاف

**Three paths (مسارات):**

1. **الاستدامة** — صناديق وقفية (endowment funds).
2. **التمكين** — بناء القدرات (capacity building).
3. **التكامل** — الشراكات التنموية (developmental partnerships).

**Grant-seeker process:**

1. تسجيل الجهة المستفيدة.
2. تقديم الفكرة الأولية للمشروع.
3. تعبئة وثيقة المشروع التفصيلية.
4. رفع تقرير المتابعة الدورية.

**Why it matters for the Khalid Saleh file:** "استدامة وتمكين" is senior-audience language. The strategic file should reference this platform as an existing lever Khalid's reshaped Development Sector vision can harness.

---

## Sub-system 3 — المنصة الوطنية للعمل التطوعي

**Owner:** MHRSD.

**Services:**

- خدمات المتطوعين
- بنك الأفكار (ideas bank)
- البحث عن فرص تطوعية
- إصدار شهادات التطوع
- توثيق الساعات التطوعية
- إدارة الفرق التطوعية

**Ahmad's hook:** he is *"عاشق"* for this platform — has ideas to propose via بنك الأفكار that could serve the Khalid Saleh strategic vision (operationally and narratively).

**Strategic opening:** بنك الأفكار is a latent channel. Ahmad's initiatives (Basira adaptability, community integration model, infection-control framework) could be reframed as volunteer-enabled when scaled beyond Al-Baha.

---

## Sub-system 4 (supporting) — نظام المواعيد

Appointment system for Development Sector beneficiary-facing services.

- حجز موعد إلكتروني
- إعادة جدولة موعد
- المواعيد الافتراضية (virtual appointments)

**Integration note:** the appointment flow is a natural insertion point for a dignity-profile layer from [[basira]]'s Dignity Index spec.

---

## Sub-system 5 (supporting) — الضمان الاجتماعي المطور

Developed Social Security system, post-reform version.

- تعبئة الملف الموحد (Unified File — new, did not exist before)
- إدارة التابعين والمنازل (Dependants + Housing)
- الاستعلام عن الأهلية والاستحقاق
- تقديم الاعتراضات والشكاوى

**Ahmad's observation:** *"الخدمة كأنها فلوس ببلاش يعني وهي ليست كذلك"* — users treat this as free money rather than as a structured entitlement. Behavioural framing issue, not technical.

---

## How to use this inventory

- **For the Khalid Saleh strategic file:** reference these systems as the Development Sector's existing digital assets. Narrative: Basira + community-integration model + infection-control framework are *how* Khalid's vision for the sector extends beyond welfare portals into a coherent digital ecosystem.
- **For Basira integration planning:** priority order — المنصة الوطنية للتأهيل (direct domain overlap) → نظام المواعيد (UX integration for dignity profile) → الضمان المطور (behavioural/entitlement framing).
- **For social-handicap compass work:** several of these systems silently embed the medical model (تقييم الإعاقة framed as deficit). Future work can surface this systematically.

## Gaps

- Actual URLs not captured — verify if published at `hrsd.gov.sa/qitaa-tanmiya` or similar.
- Ownership of برنامج استدامة وتمكين (الأوقاف vs MHRSD vs joint) not definitively confirmed.
- Integration APIs / programmatic access for any of these systems — unknown; presumably closed.

## Provenance

Ahmad's voice message 2026-04-23 walking through the Development Sector e-systems landscape as preparation for the Khalid Saleh strategic file. Migrated from memory file `project_mhrsd_development_sector_esystems.md` on 2026-04-24.
