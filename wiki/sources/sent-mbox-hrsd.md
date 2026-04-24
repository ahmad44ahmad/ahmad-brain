---
id: sent-mbox-hrsd
title: Sent Mailbox Analysis — Ahmad's HRSD Outbox (2025-03 → 2026-02)
type: source
status: active
aliases: [sent-mbox-analysis, hrsd-sent-folder]
tags: [sent-mbox, outbox, metadata-only, parsed, hrsd-email]
created: 2026-04-24
updated: 2026-04-24
source: drive:1p6N8nfYqHZnmE1i553iW_trqM3z5hmhY
related:
  - "[[pst-mailbox-hrsd]]"
  - "[[ali-alqarni]]"
  - "[[khalid-alzahrani]]"
  - "[[khalid-mutr]]"
  - "[[ahmad-formal-assignments]]"
summary: >-
  Python-mailbox parse of 802 MB sent.mbox. 51 unique messages after dedup
  (raw 154). Date range 2025-03-03 → 2026-02-23 (1 year). Top recipient
  Ali Al-Qarni (19 msgs). Confirmed emails wired to people files. Thematic
  clusters: quality-file handover, ISO 9001 roadmap, beneficiary-satisfaction,
  Basira rollout, HR compliance, formal grievance.
---

# Sent Mailbox Analysis — 2026-04-24

Full parse of `sent.mbox` (802.7 MB on disk) via Python `mailbox` module. **No raw bodies retained in vault.** Raw jsonl metadata stays at `C:\Users\aass1\ahmad-brain-import\messages-deduped.jsonl` (gitignored).

## Hard numbers

- **Raw messages in mbox:** 154
- **Unique after dedup (date+subject+to+preview_len):** **51**
- **Date range:** 2025-03-03 → 2026-02-23 (~12 months)
- **Parse errors:** 0

**Critical scope note:** sent.mbox only covers ~1 year (2025-03 → 2026-02), NOT the 7-8 years of email history Ahmad mentioned. Older sent archives either (a) do not exist in this backup, (b) live in a different PST on Drive, or (c) were never exported from the MOSA/MLSD-era mailboxes. **Action deferred:** look for older archives in Drive (search for older .pst / .ost / .mbox files).

Size explanation: the mbox is 802 MB for only 51 unique messages because each message has a ~7-12 MB signature-image block (ministry logo + staff signature images embedded in every email), plus the mbox stored each message ~3x due to concatenated exports.

## Confirmed email addresses (identity layer)

| Person | Email | Role |
|---|---|---|
| **Ahmad Al-Shahri** (self, work) | `a.a.alshahri015@hrsd.gov.sa` | — |
| Ahmad Al-Shahri (personal) | `aass112001@gmail.com` | — |
| [[ali-alqarni]] — Ali Al-Qarni | `a.a.alqarni010@hrsd.gov.sa` | Former Al-Baha center manager |
| [[khalid-alzahrani]] — Khalid bin Saleh Al-Zahrani | `k.s.alzahrani004@hrsd.gov.sa` | Regional GM + Dev Sector Assistant |
| [[khalid-mutr]] — Khalid Mutr **Al-Zahrani** | `k.m.alzahrani003@hrsd.gov.sa` | NEW center director (2026-04) — family name is Al-Zahrani (previously unknown) |

## Other HRSD addresses observed (no people-file yet — create on signal)

| Email | Send-count | Likely identity |
|---|---|---|
| `s.a.alghamdi013@hrsd.gov.sa` | 9 | **Key collaborator** — quality/initiatives work. Create people file when named. |
| `y.a.alghamdi@hrsd.gov.sa` | 4 | Quality-file collaborator ("العمل على ملف الجودة") |
| `b.a.alzahrani2@hrsd.gov.sa` | 4 | B.A. Al-Zahrani — possibly [[bandar-alzahrani]]? Verify (head of وحدة التأهيل المجتمعي) |
| `a.a.alghamdi030@hrsd.gov.sa` | 2 | Recipient of grievance letter (شكوى و تظلم) — likely HR |
| `a.m.alqarni@hrsd.gov.sa` | 1 | The *other* Al-Qarni (per PST analysis — Muhammad A. Alqarni at HRSD central) |
| `s.m.alelyani@hrsd.gov.sa` | 1 | S.M. Al-Elyani |
| `s.s.alghamdi006@hrsd.gov.sa` | 1 | S.S. Al-Ghamdi |
| `a.n.alshahri@hrsd.gov.sa` | 1 | Another Al-Shahri at HRSD |
| `hani@hrsd.gov.sa` | 1 | Hani (per PST analysis — Hani Al-Ghamdi) |

## Functional mailboxes observed

| Email | Purpose |
|---|---|
| `crc_baha@hrsd.gov.sa` | Comprehensive Rehab Center Al-Baha (مركز التأهيل الشامل) |
| `duhr@hrsd.gov.sa` | Attendance/absence tracking system |
| `duhr_notify@hrsd.gov.sa` | Attendance notifications |

## Message timeline (all 51 unique, chronological)

| # | Date | → To | Subject | Theme |
|---|---|---|---|---|
| 1 | 2025-03-03 | Al-Qarni | مسودة "محضر إثبات تكرار واقعة تجاوز التسلسل الإداري" | HR — hierarchy-bypass report on employee Samira |
| 2 | 2025-03-06 | Al-Qarni | رد: الاجتماع المناطقي | Regional meeting follow-up |
| 3 | 2025-03-09 | Al-Qarni | مسودة دليل قياس رضا المستفيدين ذوي الإعاقة الفكرية | **Beneficiary-satisfaction research for ID disabilities** |
| 4 | 2025-07-01 | Al-Qarni | رد: اجتماع دعم فروع المناطق في الخطط التشغيلية | Regional-branch operational-plan support |
| 5 | 2025-07-20 | Al-Qarni | **تسليم ملف الجودة - فرصة للتجديد والتطوير** | **Quality-file handover** |
| 6 | 2025-08-16 | A.A. Alghamdi030 (HR?) | شكوى و تظلم بشأن التقصير في واجب التدريب والتطوير المهني | **Formal grievance — training & professional development** |
| 7–10 | 2025-10-01 | self / S.S. Alghamdi | التخصصات الاجتماعية (الجزء الثاني) | Social specialties — multi-part series |
| 11 | 2025-10-11 | Al-Qarni | رد: تحديث صك أرض مركز التأهيل الشامل | Center land-deed update |
| 12 | 2025-11-05 | S.A. Alghamdi | رد: محاضر استلام رقم3 | Reception minutes #3 |
| 13 | 2025-11-09 | Al-Qarni | مذكرة نظامية و إدارية بشأن عملكم بالحماية الاجتماعية | Formal memo — social-protection work |
| 14 | 2025-11-13 | Y.A. Alghamdi | رد: العمل على ملف الجودة بالمركز لجميع الأقسام | **Quality file — all departments** |
| 15 | 2025-11-15 | S.A. Alghamdi | تفريغ الفواتير نموذج رقم 3 | Invoice processing form 3 |
| 16 | 2025-11-15 | S.A. Alghamdi | النسخة النهائية الجاهزة للتوقيع | Final version for signature |
| 17 | 2025-11-17 | S.M. Alelyani | التخصصات الاجتماعية | Social specialties |
| 18 | 2025-11-17 | B.A. Alzahrani | للزميل سعيد | "For colleague Saeed" — forwarded material |
| 19 | 2025-11-17 | Al-Qarni | إعادة توجيه: العمل على ملف الجودة بالمركز | Forward — quality file |
| 20 | 2025-11-18 | self | Hg | Note to self |
| 21 | 2025-11-19 | S.A. Alghamdi | المبادرات المعدة من قبل الزملاء | Colleague-prepared initiatives |
| 22 | 2025-11-19 | S.A. Alghamdi | جدارات | Competencies (Jadarat) |
| 23 | 2025-11-24 | Al-Qarni | الرد على ملاحظات الفرع | Response to branch feedback |
| 24 | 2025-11-25 | Al-Qarni | تقييم | Evaluation |
| 25 | 2025-11-25 | S.A. Alghamdi | المبادرة بصيغة PDF | **Initiative as PDF (likely Basira)** |
| 26 | 2025-11-25 | S.A. Alghamdi | **خارطة طريق الحصول على شهادة الأيزو 9001** | **ISO 9001 certification roadmap** |
| 27 | 2025-11-25 | S.A. Alghamdi | نموذج | Form |
| 28 | 2025-11-30 | Al-Qarni | توقيع | Signature |
| 29 | 2025-12-03 | duhr_notify | رد: اشعار معالجة غياب | Absence processing |
| 30 | 2025-12-03 | self | تقييم | Evaluation |
| 31 | 2025-12-03 | self | رابط تطبيق إدارة بيانات المستفيدين | **Beneficiary Data Management app link** |
| 32 | 2025-12-03 | self | الدليل التعريفي والتشغيلي لنظام إدارة المستفيدين الذكي (صفر ورق) | **Basira — smart beneficiary-management system intro/ops guide (zero-paper)** |
| 33 | 2025-12-04 | duhr_notify | رد: اشعار معالجة غياب | Absence processing |
| 34 | 2025-12-04 | self | تقييم 2025 | 2025 evaluation |
| 35 | 2025-12-04 | duhr | إعادة توجيه: اشعار معالجة غياب | Absence forward |
| 36 | 2025-12-04 | self | التقييم الذاتي ، تقييم الأداء 2025م | **Self-assessment + performance review 2025** |
| 37 | 2025-12-07 | self | S | Stub |
| 38 | 2025-12-09 | self | المخاطر | Risks |
| 39 | 2025-12-09 | self | مبا | Stub (truncated) |
| 40 | 2025-12-16 | Al-Qarni | إعادة توجيه: بشأن اعتماد جداول الباحثين والمراقبين الاجتماعيين | Social monitors/researchers schedule approval |
| 41 | 2025-12-16 | duhr | إعادة توجيه: اشعار معالجة غياب | Absence forward |
| 42 | 2025-12-18 | personal gmail | إعادة توجيه: دليل نظام مراقبة مخزون الإعاشة بالفروع الإيوائية | **Food-service inventory monitoring system** |
| 43 | 2025-12-18 | S.A. Alghamdi | خارطة الطريق الكاملة لصرف مكافأة مباشرة الأموال العامة | **Public-funds direct-bonus disbursement roadmap** |
| 44 | 2025-12-18 | Al-Qarni | إعادة توجيه: خارطة الطريق الكاملة لصرف مكافأة مباشرة | Forward — direct-bonus roadmap |
| 45 | 2025-12-18 | Y.A. Alghamdi | التوقيع بعدة أحجام | Signature in multiple sizes |
| 46 | 2025-12-18 | Y.A. Alghamdi | التوقيع نسخة نهائية | Signature — final version |
| 47 | 2025-12-21 | Al-Qarni | مسودة رد على الملاحظات | Draft response to feedback |
| 48 | 2026-01-11 | self | Gg | Note to self |
| 49 | 2026-01-18 | [[khalid-mutr]] | إعادة توجيه: البيان الختامي وجرد الصندوق مع كشف حساب للمطابقة لعام 2025 | **Year-end 2025 financial closing + reconciliation** |
| 50 | 2026-02-04 | crc_baha@ | رد: تقرير المتابعة الدورية لمعايير خدمات الأشخاص ذوي الإعاقة | **Periodic monitoring — disability-services standards** |
| 51 | 2026-02-23 | [[khalid-alzahrani]] | بشأن تسوية وضع وظيفي، وطلب إلغاء تسجيل أيام الغياب مع المبررات | **Employment-status resolution + absence-days cancellation request** |

## Thematic clusters (what Ahmad actually works on — from sent evidence)

| Theme | Msg count | Maps to |
|---|---|---|
| Quality file handover + ISO 9001 roadmap | 7+ | [[ahmad-formal-assignments]] #1 Quality |
| Beneficiary satisfaction research (ID disabilities) | 2 | [[ahmad-formal-assignments]] #5 Disability |
| Basira / smart beneficiary-management / zero-paper | 3+ | Basira project |
| Social specialties (التخصصات الاجتماعية) multi-part | 5 | Operational framework |
| HR / attendance / evaluation | 10+ | HR compliance + self-defense |
| Strategic initiatives (المبادرات) | 4 | [[ahmad-formal-assignments]] #2 Strategic Partnerships |
| Food-service inventory / procurement oversight | 3 | Operational oversight |
| Center financial-closing + reconciliation | 1 | Financial oversight |
| Disability-services monitoring standards | 1 | [[ahmad-formal-assignments]] #5 Disability + #6 Non-gov committee |
| Regional branches operational-plan support | 2 | [[ahmad-formal-assignments]] #2 Strategic Partnerships |

## Notable individual messages (high-signal)

1. **Msg #1 (2025-03-03)** — the employee Samira hierarchy-bypass memo to Al-Qarni. Reflects operational HR conflict that Ahmad had to formally document.
2. **Msg #3 (2025-03-09)** — beneficiary satisfaction research draft for people with intellectual disabilities. Academic-quality output.
3. **Msg #5 (2025-07-20)** — "تسليم ملف الجودة" (handing over the quality file) — title says "فرصة للتجديد والتطوير" (opportunity for renewal). Implies a transition point in Quality role.
4. **Msg #6 (2025-08-16)** — formal grievance about training/professional-development failure. Routed to A.A. Alghamdi030 (HR). A "paper-trail" action — important for institutional memory.
5. **Msg #26 (2025-11-25)** — **ISO 9001 roadmap**. Sent to S.A. Alghamdi013 (key collaborator). Maps to Quality assignment.
6. **Msg #32 (2025-12-03)** — **Basira intro/operational guide** ("صفر ورق"). The formal rollout doc.
7. **Msg #50 (2026-02-04)** — periodic disability-services monitoring report. Maps to the Non-gov Rehab Committee assignment.
8. **Msg #51 (2026-02-23)** — last sent message. Employment-status resolution addressed to Regional GM Khalid Al-Zahrani. Personal/administrative.

## Gaps

- [ ] Signature images in the mbox could be OCR'd to extract full names + titles of each HRSD recipient — deferred.
- [ ] Older archives (pre-2025-03) not in this mbox — search Drive for other exports.
- [ ] Raw body content NOT saved — if you need exact wording of a specific sent message, ask me to re-parse from `messages-deduped.jsonl` (still on disk).
- [ ] Bodies contain Arabic letters — some previews are truncated at 300 chars; for full-text search we'd index the bodies into a local SQLite with FTS5. Deferred.

## Retrieval patterns

- "What did Ahmad send to Al-Qarni about quality?" → grep this file for Al-Qarni rows + quality keyword → get dates + subjects → if full body needed, re-parse from jsonl.
- "When did Ahmad hand over the quality file?" → msg #5, 2025-07-20.
- "What's the ISO 9001 status?" → msg #26 roadmap sent to S.A. Alghamdi013 on 2025-11-25.
- "Who are Ahmad's core working contacts?" → Al-Qarni (19), S.A. Alghamdi013 (9), Y.A. Alghamdi (4), B.A. Al-Zahrani (4) — top collaborators.
