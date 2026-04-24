---
id: pst-mailbox-hrsd
title: PST Mailbox Analysis — Ahmad's HRSD Work Email (2023-2026)
type: source
status: active
aliases: [pst-analysis, hrsd-outlook-backup, exchange-mailbox]
tags: [pst, exchange, mailbox, hrsd-email, metadata-only, sampled]
created: 2026-04-21
updated: 2026-04-24
source: drive:1z_cj5HVKhrZu4encg2esfLlBZ7koA8qWOPfozxk_lK8
related:
  - "[[sent-mbox-hrsd]]"
  - "[[mhrsd-era-timeline]]"
  - "[[ahmad-formal-assignments]]"
  - "[[ali-alqarni]]"
  - "[[hamed-alruwaili]]"
  - "[[khalid-alzahrani]]"
summary: >-
  2.2 GB PST of Ahmad's HRSD Outlook mailbox covering 2025-03 → 2026-03
  (inbox/sent) with deleted items reaching back to 2019 (MLSD era).
  2,582 messages full-indexed. Real totals: 2172 inbox, 154 sent, 606
  total contacts. Dovetails with snapshot PST-A (2023-11 → 2025-01).
  Primary query surface is now the merged archive
  [[pst-mailbox-hrsd-merged]].
---

# PST Analysis — Ahmad's HRSD Work Mailbox (sampled 2026-04-21)

## Provenance

- **Raw PST:** `D:\backup22222 (1).pst` (2.2 GB) → Drive fileId `1IbT2nc4Mj4GDNV6yCzUdweHnKfqt6Rac` in folder `1a1g8_1MXirMZP59Z237gCie989syxBGq` ("pst. export النسخة الاحتياطية من بريد العمل"). Exported to mbox at `D:\pst-archive\raw\` on 2026-04-21 and indexed into FTS5 SQLite at `D:\pst-archive\search\messages.sqlite` (README: `D:\pst-archive\README.md`).
- **Full SENT folder** as mbox: `sent.mbox` (803 MB) → Drive fileId `1p6N8nfYqHZnmE1i553iW_trqM3z5hmhY` (superseded by the full mbox set under `D:\pst-archive\raw\`).
- **Extraction script:** `pst_extract.py` → Drive fileId `1_TnZf6lAs4M0ZABjry8li916zaCmKGcV` (superseded locally by `C:\Users\aass1\.claude\plans\pst_export_mbox.py`).
- **Summary JSON:** `pst-summary.json` → Drive fileId `1d1pd_8OTvb3kFPEPMj1RPud3D0XKn99X`.
- **Individual .eml extractions:** Drive folder `1sMlLdFXW9e_9Yu2m3xduO2HFc3O1-UBS` (numbered files like 544.eml, 569.eml, 999.eml, 1244.eml, 1500.eml, 1698.eml, 1822.eml).
- **Companion archive:** [[pst-mailbox-hrsd-snapshot-a]] — dovetails with this one (different date range, ~no overlap, reaches back to 2015 in Drafts). Cross-archive diff via `C:\Users\aass1\.claude\plans\pst_archive_diff.py`.
- **Sampling cap note:** the initial 2026-04-21 sampled analysis used an Aspose evaluation license (50 items per folder). Subsequent full extraction under the licensed Aspose key produced the complete 2,582-message index in `D:\pst-archive\search\`. Numbers below reflect the sampled analysis; real folder totals are 2,172 inbox / 154 sent / 146 deleted / 105 drafts / 234 calendar / 261 contacts / 345 recipient-cache / 5 sync.

## Scope

**Ahmad's active HRSD employment 2023-10-12 → 2026-03-01** (the PST backup's date range). Ahmad's voice claim of "7-8 years using ministry email since ~2014" is now **partially verified** via the sibling snapshot [[pst-mailbox-hrsd-snapshot-a]] — PST-A's Drafts folder reaches back to 2015-10-19 (MOSA era, `23200@mosa.gov.sa`) and PST-C's own Deleted folder has MLSD-era items from 2019-04-25 (`TABS@mlsd.gov.sa`). Pre-2023 coverage is Drafts/Deleted fragmentary, not full inbox/sent — the latter likely lives in the OneDrive Google Takeout mbox (4.2 GB, currently cloud-only).

Confirmed by extraction:
- Sender of ~118 outgoing/draft messages: "Ahmad A. Alshahri"
- Domain: `hrsd.gov.sa` (one external address `f.d@hrsd.gov.sa` seen)
- All 50 contacts tagged "وزارة الموارد البشرية والتنمية الاجتماعية"
- Exchange internal-format addresses dominate

## Folder totals vs. sampled

| Folder | Total | Sampled |
|---|---|---|
| علبة الوارد (Inbox) | **2,172** | 50 |
| العناصر المرسلة (Sent) | 154 | 50 |
| العناصر المحذوفة (Deleted) | 146 | 50 |
| المسودات (Drafts) | 105 | 50 |
| جهات الاتصال (Contacts) | 261 | 50 |
| Recipient Cache | 345 | 0 |
| التقويم (Calendar) | 234 | 50 |
| Sync Issues | 5 | 5 |

**Total contacts across Contacts + Recipient Cache = 606.**

## Distribution lists (not individuals)

- **مركز التواصل** (Communication Center) — 69 messages sampled. MHRSD central broadcast DL. Deputy-minister meeting invites, workshops, campaigns, senior-leadership comms.
- **التواصل الداخلي بمنطقة الباحة** (Al-Baha Internal Comms) — regional DL.
- **Yammer** — HRSD corporate social. `noreply@eu.yammer.com` digests.

## Colleagues observed (Al-Baha / regional)

- إبراهيم الزهراني
- خالد الزهراني → [[khalid-alzahrani]]
- خالد مطر الزهراني (أبو أسامة) → may be same as [[khalid-mutr]], verify
- بندر الزهراني (head of وحدة التأهيل المجتمعي per other source)
- حسن الزهراني
- عبدالله لافي الغامدي
- سعيد أبو عمر الغامدي
- سعيد أبو صالح الغامدي
- وائل الغامدي
- هاني الغامدي
- لطيفة الغامدي
- صالحة الغامدي
- نوير الغامدي (verify vs [[nuwaira]] — likely not the same Nuwaira since this one is Al-Ghamdi family)
- محمد علي الشهري (appears twice, likely same person)
- علي القرني → [[ali-alqarni]]

## Colleagues observed (central / named)

- **Hamed Al-Ruwaili** → [[hamed-alruwaili]] — dedicated calendar meeting "لقاء مع أ.حامد الرويلي حول ملتقى الموارد البشرية في المناطق"
- Mona Alahidab
- Maha Alshehri
- Abdulaziz Asiri
- Abdulaziz A. Alghamdi
- Basheer Alalarimi
- Turki Almadhi
- Ali Alshahrani
- Asma'a Alqahtani
- mushabab alshehri
- راكان محمد الدامغ
- يوسف السراح
- طامي العلياني
- معيض الشمراني
- فوزيه الخريش
- ساير الجعيد
- إيمان الخميس
- ناصر العسيري
- عبدالله الحميدي
- مبارك الصاعدي
- ماجد الثنيان
- معاذ الزين دوش
- محمد حنيتم
- جمال أفراس
- عبدالله إبراهيم الزهراني
- عبدالله المري
- هيثم (النهارية — verify if unit, not person)

## Unit / functional mailboxes (not people)

- فريق خدمات الإعاشة (Food-service team)
- وحدة خدمات المرافق (Facilities services unit)
- وحدة شؤون المناطق (Regional affairs unit)
- وحدة الدعم - الإدارة العامة لخدمات الفروع (Branches support unit)
- مركز إدارة الكوارث والأزمات الرئيسي (Crisis & disaster management center)
- ايميل رفع الملاحظات على المقاولين (Contractor-feedback mailbox)
- منصة ملتقى الباحثين الصحيين - المعهد الوطني لأبحاث الصحة

## Programs / initiatives seen

- **تعاطف** (Ta'atof) — MHRSD welfare initiative (appeared as a contact entry)

## Recurring themes (subject-token frequency in sample)

| Token | Count | Meaning |
|---|---|---|
| دعوة | 59 | invitation |
| لحضور | 48 | to attend |
| لقاء | 38 | meeting |
| الورشة / ورشة | 34 | workshop |
| وكيل | 16 | deputy minister |
| سعادة | 16 | "His Excellency" |
| ابتكارثون | 14 | innovation hackathon (MHRSD annual) |
| المهارات | 12 | skills |
| الاجتماعية | 11 | social (services) |
| التأهيل | 10 | rehabilitation |
| كبار السن | 8 | elderly |
| الزهايمر | 6 | Alzheimer's |
| يوم اليتيم العربي | 6 | Arab Orphan Day (annual) |
| التميز المؤسسي | 5 | institutional excellence |
| المرأة - العنف | 5 | violence against women |

## Deputy-minister positions on Ahmad's invite DL (from calendar)

- وكيل الشؤون الاستراتيجية وتحقيق الرؤية
- وكيل تطوير رأس المال البشري
- وكيل تنمية المجتمع
- وكيل شؤون العمل
- وكيل سياسات سوق العمل
- وكيل إدارة رأس المال البشري
- وكيل الشؤون الدولية
- المشرف العام التنفيذي لوكالة تجربة العميل
- وكيل الضمان الاجتماعي والتمكين
- **وكيل التأهيل والتوجيه الاجتماعي** (PT-relevant; current = [[nasser-alqahtani]])
- وكيل الوزارة للتوطين
- نائب الوزير لقطاع التنمية الاجتماعية
- نائب الوزير لقطاع العمل
- وكيل الوزارة للشؤون العمالية
- وكيل التحول الرقمي
- وكيل الوزارة للخدمات المساندة والفروع

## Recurring workshop domains

- مراكز الرعاية النهارية لكبار السن (Elderly daycare centers)
- خدمات الرعاية الاجتماعية المنزلية (Home social-care)
- سجل المراقب الاجتماعي (Social monitor logbook)
- معايير مكافحة العدوى (Infection control)
- خدمات العلاج الطبيعي (PT services) — **Ahmad's direct domain**; one "Canceled: اجتماع خدمات العلاج الطبعي" seen
- مرافقي المرضى (Patient escorts training)
- الأدوية والمستلزمات الطبية في دور الرعاية

## Quality / excellence cluster

- جائزة التميز المؤسسي (Institutional Excellence Award)
- مؤشرات الأداء (KPIs)
- الخطة السنوية التشغيلية (Annual op plan)
- خارطة المخاطر (Risk map)

## Digital-transformation cluster

- حماية البيانات / البيانات غير المهيكلة (Data protection / unstructured data)
- منصة التأهيل والتوجيه الاجتماعي (Rehab & guidance platform)
- التحول المالي بالوزارة (Financial transformation)

## HR-ops cluster

- بدل النقل (Transport allowance)
- مستلمي المركبات (Vehicle-receipt list)
- صرف مكافأة مباشرة (Direct bonuses)
- الانفاق الوظيفي (Job spending)

## Folder tree (Outlook default — no custom organization)

```
أعلى ملف بيانات Outlook/
├── علبة الوارد (Inbox, 2172)
├── العناصر المرسلة (Sent, 154)
├── العناصر المحذوفة (Deleted, 146)
├── المسودات (Drafts, 105)
├── جهات الاتصال (Contacts, 261)
│   ├── الشركات (Companies, 0)
│   ├── Recipient Cache (345, not scanned)
│   └── GAL / Organizational / PeopleCentric (0)
├── التقويم (Calendar, 234)
├── Sync Issues (5)
├── Spambox / Junk (0)
├── ExternalContacts (0)
├── Tasks / Notes / Journal (0)
├── Yammer root (0)
└── RSS / Files / Quick Steps (0)
```

## Gaps — what a full read would add

- Full contact list (606, not 50).
- True top-20 senders by actual count (sample truncated).
- Conversation chains (who Ahmad replies to).
- Email signatures → titles, job roles, phone numbers.
- Dates + threads over 2+ year span.
- Attachments (policy docs, drafts, reports Ahmad sent).

To do full read: (a) free Aspose 30-day license at purchase.aspose.com/temporary-license, or (b) MSVC + libpff-python, or (c) parse `sent.mbox` directly (Python `mailbox` module, no license needed — **recommended for SENT-focused analysis**).

## Not captured intentionally

- Email bodies (only metadata)
- Attachment content
- Drafts of personal messages
- Deleted items (not authoritative)
- Sync Issues / Junk

## Action items deferred

- [ ] Request a full mbox parse of `sent.mbox` — Ahmad says the SENT messages matter most. This is ~800MB of text, parseable in minutes with zero license constraints.
- [ ] Map the 261 contacts → identify who else besides the 50 people-files already in vault deserve their own note.
- [ ] Extract signatures from sent messages to populate `title`, `email`, `phone` for people files.
- [ ] Cross-reference [[khalid-mutr]] kunya (أبو أسامة) against PST — verify it's the same Khalid Mutr as the current center director.
- [ ] Verify "نوير الغامدي" in PST vs [[nuwaira]] (Umm Abdulmalik, family name unknown) — likely different people.
