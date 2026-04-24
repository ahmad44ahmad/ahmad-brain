---
id: basira
title: Basira — Digital-Transformation System for Rehabilitation Centers
type: project
status: active
aliases:
  - بصيرة
  - basira-system
  - مبادرة صفر ورق
  - Zero Paper
tags:
  - project
  - basira
  - digital-transformation
  - rehabilitation
  - al-baha-pilot
  - governance
created: 2026-04-24
updated: 2026-04-25
source: local-repo:C:\dev\basira\
related:
  - "[[basira-leadership-compass]]"
  - "[[basira-sovereign-decks]]"
  - "[[ismail-alghamdi]]"
  - "[[khalid-alzahrani]]"
  - "[[khalid-mutr]]"
  - "[[nasser-alqahtani]]"
  - "[[nuwaira]]"
  - "[[research-initiatives-portfolio]]"
  - "[[ahmad-formal-assignments]]"
  - "[[drive-catalog]]"
  - "[[999-albaha-qms-bcp]]"
summary: >-
  Ahmad's flagship digital-transformation system (بصيرة / "Zero Paper") for
  Saudi comprehensive rehabilitation centers. Vite 6 + React + TypeScript local
  repo at C:\dev\basira\. Built 2024+ under a self-imposed "forbidden trinity"
  (no budget, no staff, no one's time). Framing: not a request for approval —
  a digital translation of approvals the Al-Baha center has already earned.
  Handover governance starts at Regional GM, never at center level.
---

# Basira (بصيرة)

## One-line definition

Basira is the digital layer that scales validated operational excellence from one comprehensive rehabilitation center (Al-Baha) to thirty-six nationwide. It is not a pilot asking for approval — it is the codified expression of credentials the center already holds.

## Repository and local state

- **Canonical path:** `C:\dev\basira\` (flattened 2026-04-16 from an earlier double-nested location). All other paths on disk — `C:\Users\aass1\Basira\`, `C:\Users\aass1\Basira-1\`, `D:\basira-5.0-*\` — are experimental branches or design-doc drafts and are NOT what "بصيرة" or "dev server" refers to.
- **Active branch:** `v2`. Tag `v1.0.0-zero-paper` on `main` freezes the MHRSD-endorsed state of 2025-12-03; never work on `main` unless explicitly instructed.
- **Stack:** Vite 6.4.1, React, TypeScript; dev server on port 5175 (strict). Launch with `cd /c/dev/basira && npm run dev`.
- **Scale:** ~66,000 lines TS/TSX as of 2026-04.
- **Skill for session work:** `basira-dev` under `~/.claude/skills/`.
- **GitHub remote:** `ahmad44ahmad/Beneficiary-System-Clean-Backup`.
- **Preview URL on file:** `https://beneficiary-system-clean-backup-1y4j4hzyw.vercel.app`.

Current UI signature (as of 2026-04-22, v2) is dark-by-default, a persuasive landing page with hero + 4 stat cards + 5 pillars, a 320-px sidebar with 9 sections (الرئيسية · الخدمات الطبية · الخدمات الاجتماعية · الحوكمة والجودة · العمليات · الذكاء والتنبؤ · التقارير · القيادة الاستراتيجيّة · الإدارة). If a UI verifier flags a mismatch against an older signature (light theme, 300-px sidebar, "Beneficiary System Clean Backup" badge, flat 10-item governance list) the verifier reference is stale — do not "fix" the code.

## The forbidden trinity (الثلاثية الحرام)

From the first day of the project, Ahmad imposed three rules on himself — if any one is broken, the project is considered failed by its own standard regardless of technical outcome:

1. **لا طلب ميزانيّة** — no budget requested, ever.
2. **لا طلب موظّفين** — no additional staff assigned.
3. **لا استقطاع من وقت أحد** — no colleague's hours taken.

> *"من يوم بدَأت التطبيق هذا كان عندي الثلاثية الحرام... يُفشل هذا المشروع إذا طلبت فلوساً، يُفشل إذا طلبت موظّفين معي، يُفشل إذا أخذت من وقت أحدٍ أيّ شيء. ويَعني الآن أرى أنّي نجحت."* — Ahmad, 2026-04-23

All three have held for 2+ years. The trinity turns every skeptical objection into reinforcement — "we don't have budget" becomes "it never needed a budget, it's already built"; "we'd need to free up staff" becomes "no one was freed, no one was assigned"; "it would steal time from operations" becomes "it didn't — verified over two years." It is also the moral floor that denies critics the standard dismissal that Ahmad is "creating problems to solve" or expanding scope for personal gain.

**Every Basira pitch should lead or close with the trinity.** Frame it as a design choice that succeeded, not as sacrifice or grievance — never write "despite receiving no support"; always write "by design, and by success."

The trinity also authorises Ahmad's step-aside posture: he has explicitly said a different region or center may be a better pilot if its leadership is more enthusiastic. He wants the project to succeed, not specifically to succeed under his authorship — and because he owes no one, he can walk away without institutional debt.

## Evidence stack (seven external pillars)

The strategic framing — *"يجب أن نُظهر الامتثال، ونبرز فكرة أننا الأول عربياً"* — rests on a seven-pillar ladder of independent, government-issued attestations. Lead any institutional correspondence with these, not with Basira's technical specs.

1. **Red Crescent 5-Star Emergency Safety Compliance (October 2025).** Issued by هيئة الهلال الأحمر السعودي for مركز التأهيل الشامل بالباحة — Administrative Building. First center in Saudi Arabia to receive this level at the 2025 assessment tier; gives historic priority. Valid one year. Framed on Ahmad's desk.
2. **Wakala Excellence Certificate — twice (2022 + one other year).** Issued by وكالة التأهيل والتوجيه الاجتماعي. The 2022 certificate was signed by د. عبدالله الوهيبي (then-wakil); current wakil is [[nasser-alqahtani]]. Basis: >80% performance for the evaluation year. Institutional recognition that persists across wakil transitions.
3. **Rank #2 rehabilitation center in the Kingdom (recent, 97% tied).** MHRSD central performance monitoring. Sits on the top-performers board alongside 99% for عمل offices, 100% for ضمان, 98% for تنمية.
4. **Rank #1 (tied with Jeddah) care offices in the Kingdom — 2018.** Methodology: mystery shopper + family satisfaction + visit-quality. *"كانت آخر مرة ينعمل بين المراكز"* — effectively the last public inter-center ranking the ministry published. Quality is accumulated, not newly claimed.
5. **First Arab in Quality (UAE regional ceremony).** Received by [[ismail-alghamdi]] on behalf of the Al-Baha center. Year and official award name still to verify. The heaviest single pillar because it establishes regional-first excellence, a personal bond with the strategic patron, and matches Minister Al-Rajhi's "الأول على العالم" ambition.
6. **Ten approved 2025 performance achievements.** All rated 5★ priority, all marked "تم اعتماد الإنجاز" by [[ali-alqarni]] on 2025-11-25. Span بصيرة / Zero Paper, ISO 9001, حوكمة الإعاشة, تمكين, جودة, مكافحة العدوى, خطة إخلاء, خارطة طريق ذوي الإعاقة, شراكات استراتيجية. Cross-link in [[ahmad-2025-achievements]].
7. **حِصن + NCA alignment.** Registration in نظام حِصن (MoH Riyadh, WHO-affiliated infection-control surveillance) gives cross-ministerial credibility. The 11-document compliance packet at `C:\dev\basira\docs\` + `SECURITY.md` maps Basira proactively to NCA ECC-2:2024 + CSCC-1:2019.

Supporting recognitions: a 2024 Certificate of Appreciation from الإدارة العامة لدعم وتمكين الأشخاص ذوي الإعاقة (the Empowerment & Disability Support chain — the correct institutional frame for Basira's social-model storyline); a 2019 founding of the Al-Baha Disability Advisory Council; and Ahmad's 2017 role in the Mott MacDonald baseline study of MHRSD rehabilitation centers at Minister Al-Rajhi's arrival, when he computed per-beneficiary direct expenditure across 7,825 beneficiaries at 38 centers.

### Canonical narrative

> «مركز التأهيل الشامل بالباحة حاز الامتثال الكامل 5/5 من الهلال الأحمر (2025)، وشهادة التميز من وكالة التأهيل مرّتين، ويقف في المركز الثاني على مستوى المملكة بمعدل 97% من التقييم الوزاري، ويحمل جائزة الأول عربياً في الجودة. بصيرة ليست طلباً لاعتماد — بصيرة هي الطبقة الرقمية التي تترجم هذه الاعتمادات من مركز واحد إلى 36 مركزاً.»

**Non-negotiable framing rules.** Do not list Basira's technical specs without leading with the external evidence stack. Do not generalise ("5-star" applies to the administrative building, not the whole center). Do not use Ahmad's name in the narrative — frame as "المركز" achieved these. Pair each evidence item with the institutional patron that issued it. Update the stack as new attestations land (e.g. the 2026 excellence certificate when issued).

## Governance layer (handover approval chain)

Rule validated 2026-04-22: any Basira handover, review, or institutional-approval surface must start **at or above** the Regional General Manager level. The center itself is the test subject — naming it as the approval authority is a structural conflict of interest, and center-level leadership turns over too frequently to serve as a stable governance anchor. Ahmad's verbatim reasoning:

> *"The general manager of administration in Al-Baha, maybe at the end of the day he cannot push it without feeling some punishment coming. Why? Because at the end of the day, the center is the one who works on its main field. So, yeah, I do think it's not a good idea. You start from the general manager."*

The chain, in order of approach:

1. **Regional GM** — [[khalid-alzahrani]] (Khalid bin Saleh Al-Zahrani / أبو فيصل, المدير العامّ للإدارة بمنطقة الباحة + مساعد قطاع التنمية). First endorsement. Step 0 for any Basira escalation.
2. **Primary patron** — [[ismail-alghamdi]] (Assistant Minister Shared Services + Quality General Administration + Development Sector mandate, مرتبة ممتازة). The "front door" to the ministry.
3. **Formal domain owner** — [[nasser-alqahtani]] (Deputy Minister for Rehabilitation and Social Guidance, replaced Al-Wuhaibi). Copy recipient, not primary addressee.
4. **Center director** — [[khalid-mutr]] (new as of 2026-04). Pitch recipient at center level, with Regional GM + [[nuwaira]] (مديرة الإشراف الاجتماعي) as CC.

Post-handover governance lives with الوكالة (وكالة التأهيل والتوجيه الاجتماعي). Security and compliance approvals route through إدارة الأمن السيبرانيّ في الوزارة.

**Excluded from institutional Basira surfaces:** مدير مركز التأهيل الشامل بالباحة as an approval layer; قيادة المركز as a category; any specific individual by name, including [[ali-alqarni]] — his 2025 endorsements of Ahmad's achievements are HR records, a different context, and do not count as a compensating SoD control for Basira governance. When an AI-drafted handover doc or SECURITY packet suggests "مدير المركز" or "قيادة المركز" as an approver, reject and escalate to Regional GM.

## Current state (as of 2026-04-24)

The codebase is functional but carrying modification tax. Two decisions pending:

1. Polish and integrate two AI engines, keep the current codebase.
2. Rebuild from zero, targeting <40K lines with cleaner architecture.

Shipped artefacts in the handover packet: Basira v2 operational manual (PDF, Drive `1DCzQ2QL...`); Basira v3 technical design + security addendum (docx); Basira_v3_Empowerment_Architecture deck (pptx); executive memo (gdoc); Regional-GM pitch docs (`Basira_Pitch_GM_AlBaha.md` + v1/v2); video voiceover script (AR); cybersecurity alignment folder for 2026 NCA/CSCC regulations; three sovereign HTML decks at `Desktop/Basira-5-visuals/` (see [[basira-sovereign-decks]]). The Leadership Compass (see [[basira-leadership-compass]]) shipped on v2 on 2026-04-22 at route `/leadership-compass`.

Technical signals to pair with the evidence stack for senior audiences: **SROI 1:4.2** (social return on investment), **ISO 9001 100% alignment**, **11-document compliance packet** mapped to HRSD + NCA ECC-2:2024 + CSCC-1:2019, **100% audit trail**.

MHRSD official designation for Basira in the achievement system: **مبادرة صفر ورق (Zero Paper)**, one of Ahmad's 2025 achievements approved 2025-12-03 by [[ali-alqarni]].

## Open gaps

- Exact year and official name of the First-Arab Quality Award (UAE) — the heaviest gap in the evidence stack. Ask Ahmad.
- High-resolution digital copies of both Excellence certificates + the Red Crescent certificate + the ranking screenshot.
- Signing authority for the second Excellence certificate if different from Al-Wuhaibi.
- SPA / واس announcement for the 2019 Al-Baha Disability Advisory Council founding.
- Tie Basira to [[research-initiatives-portfolio]] as the digital layer across Aman Mustadam, Tamkeen, and Ihsan-before-Measure.
- Apply Supabase migration 024 (Leadership Compass) — still pending at handoff.

## Provenance

Hub consolidated 2026-04-24 from six memory files (`project_basira_canonical_path`, `project_basira_evidence_stack`, `project_basira_leadership_compass`, `project_basira_sovereign_decks`, `feedback_basira_governance_layer`, `feedback_basira_forbidden_trinity`) under the Phase D migration task from [[log-2026-04-24]]. Earlier version was a stub pointing to these memory files; facets for Leadership Compass and Sovereign Decks split into sibling notes [[basira-leadership-compass]] and [[basira-sovereign-decks]] to keep this hub under the 2000-word ceiling per [[0001-vault-architecture]].
