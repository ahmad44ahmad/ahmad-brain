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
updated: 2026-05-06
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
  - "[[basira-evidence-stack]]"
  - "[[mhrsd-kpi-landscape-2024-2026]]"
  - "[[999-albaha-qms-bcp]]"
  - "[[empowerment-thesis-corpus]]"
  - "[[empowerment-vocabulary]]"
  - "[[aman-mustadam-initiative]]"
  - "[[999-institutional-excellence-innovation]]"
  - "[[999-zero-paper-master]]"
  - "[[ahmad-engineering-substrate]]"
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

### Operational evidence layer (added 2026-05-06)

The seven pillars above are *attestations*. Beneath them sits an **operational evidence layer** — the documented MHRSD KPI surface, the contractor SLAs, the branch quality unit oversight, and the Q1→Q3 progression dashboard. Both layers travel together in any pitch:

- **Map of the operational layer**: [[basira-evidence-stack]] — categorises 14 evidence sources under four pitch claims (governance / measurement / empowerment / escalation), with reading order by audience.
- **KPI surface map**: [[mhrsd-kpi-landscape-2024-2026]] — five-layer architecture exposing five named operational gaps that map directly to Basira features.

Use the seven pillars to *open* a pitch (institutional credibility); use the operational layer to *close* it (Basira solves real measured pain).

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

## Current state (as of 2026-04-27)

**VM-demo polish landed on `v2`.** Two commits pushed to `origin/v2` overnight before the Vice Minister (Development Sector, MHRSD) visit:

- `8b6096b` (Tier 4) — Legal Shield page (route `/legal-shield`, 4 compliance pillars + cert-issuance + audit trail), director-approval workflow on `FamilyMediaFeed`, IoT vitals → `useVitalsAlertsStore` → SmartAlertsPanel wiring with response-speed capture, MedicationAdministration `administeredBy`+`administeredAt` record + "تصدير PDF" header, MorningPulse wired to `useWelcomeStats`.
- `3e266b8` (Tier 0–3) — institutional voice (footer byline replaced with department/ministry attribution), governmental register on Welcome + Login + Header, demo-path blocker fixes (DignityProfile enum reconciliation, SocialResearchWizard data-corruption fix, EmpowermentPlanBuilder + SocialDashboard fully arabized, "مريض" → "حالة" sanitization, typos), Karama demo profile **محمد/أبو سعد at beneficiary id `172`** (`MOCK_DIGNITY_PROFILES[1]`), cup-of-water SMART goal, 3 strategic-tracks banner above 9 domains, **127 → 132 operations** with 5 supervisory-form-derived ops in `qualityProcesses.ts:1448-1496` (ids 128–132 covering contracting + facility audits), SROICard sourced from new `src/data/sroiAssumptions.ts` (NEF/SSE methodology), `riskAnalysisService.ts` Arabic-keyword extraction (`بلع`/`انفعال`/`عدوان` → score) + Morse-aligned factors, `staffingOptimizerService.ts` ward-aware burnout signals (consecutive shifts, overtime-7d, ratio imbalance, sick-leave) with Northern/Southern/Women's-section presets, `governanceService.ts` bottom-up rollup from leaves, new `familyEngagementService.ts` (4-factor 0–100 score with 50% intervention threshold).

37 files modified + 4 new files (`sroiAssumptions.ts`, `familyEngagementService.ts`, `useVitalsAlertsStore.ts`, `LegalShieldPage.tsx`). TS check 0 errors. Playwright signature verified on Welcome + Dashboard + Empowerment + Family + Alerts + Legal Shield + Pulse + Quality Manual. **Ahmad recorded the new narration video** with the polished UI; narration aligned to actual code (66k LoC, 132 ops, computed SROI ratio).

**Two decisions still pending** from the older inventory; deferred post-VM-demo:

1. Polish and integrate two AI engines further, keep the current codebase.
2. Rebuild from zero, targeting <40K lines with cleaner architecture.

Shipped artefacts in the handover packet: Basira v2 operational manual (PDF, Drive `1DCzQ2QL...`); Basira v3 technical design + security addendum (docx); Basira_v3_Empowerment_Architecture deck (pptx); executive memo (gdoc); Regional-GM pitch docs (`Basira_Pitch_GM_AlBaha.md` + v1/v2); video voiceover script (AR, Drive `1nC5Rxrv4WnOZX5N59HOMth498r5b4PkqdQFAgi4GwUI`); cybersecurity alignment folder for 2026 NCA/CSCC regulations; three sovereign HTML decks at `Desktop/Basira-5-visuals/` (see [[basira-sovereign-decks]]). The Leadership Compass (see [[basira-leadership-compass]]) shipped on v2 on 2026-04-22 at route `/leadership-compass`.

Technical signals to pair with the evidence stack for senior audiences: **SROI 1:4.2** (now computed via NEF/SSE methodology with deadweight 25% / attribution 30% / displacement 5% applied), **ISO 9001 100% alignment**, **11-document compliance packet** mapped to HRSD + NCA ECC-2:2024 + CSCC-1:2019, **100% audit trail**, **132 documented operations**, **7 AI engines wired with score-feeding inputs** (no more pure slogans).

**Demo path validated 2026-04-27**: `/` → `/dashboard` → `/empowerment` (click أبو سعد) → `/family-portal` → `/alerts` → `/legal-shield` → `/quality/manual` → `/sroi`.

MHRSD official designation for Basira in the achievement system: **مبادرة صفر ورق (Zero Paper)**, one of Ahmad's 2025 achievements approved 2025-12-03 by [[ali-alqarni]].

For Basira's product anatomy as written-up in narrative form — 5-component architecture (Master Record / Rehab+Empowerment / Clinical / ملف الكرامة / Logistics), 3 strategic goals (أنسنة الرعاية / صفرية الورق / الحوكمة الاستباقية), and design-doctrine vocabulary (بوصلة, مساعد الظل, هندسة الكرامة) — see [[999-zero-paper-master]]. That doc is Gemini-synthesised and *describes* features as if deployed, so quote it in "as designed" mode rather than "as deployed". The evidence stack above is the institutional-claims source; F-5.1 ([[999-institutional-excellence-innovation]]) is the excellence-framework source; F-5.3 ([[999-zero-paper-master]]) is the product-architecture source.

## Open gaps

- Exact year and official name of the First-Arab Quality Award (UAE) — the heaviest gap in the evidence stack. Ask Ahmad.
- High-resolution digital copies of both Excellence certificates + the Red Crescent certificate + the ranking screenshot.
- Signing authority for the second Excellence certificate if different from Al-Wuhaibi.
- SPA / واس announcement for the 2019 Al-Baha Disability Advisory Council founding.
- Tie Basira to [[research-initiatives-portfolio]] as the digital layer across Aman Mustadam, Tamkeen, and Ihsan-before-Measure.
- **Apply Supabase migration 024 (Leadership Compass) — still pending after 2026-04-27 polish.** Compass UI runs on local seeds; works visibly but a "is this live data" question exposes the seam. Apply via Supabase dashboard SQL Editor (60 seconds).
- **Untracked WIP at session close 2026-04-27** (NOT auto-committed pending Ahmad decision): `CLAUDE.md` (modified), `docs/code-strategic-map-2026-04-23.md`, `docs/elevenlabs-voice-research-2026-04-23.md`, `docs/walkthrough-inventory-2026-04-23.md`, `src/modules/grc/components/`, `video-production/`, `walkthrough-screenshots/`. Last two may contain sensitive demo content; repo is public — review before commit.
- **Ihsan personality-inference engine deferred** — current code uses a manual `<select>`. Real inference (5-6 weighted signals from incidents/visits/sleep regularity → personalityType) is post-VM-demo work.
- Dependabot moderate CVE on `Beneficiary-System-Clean-Backup` default branch (security advisory #28). Non-blocking for VM demo; address post-visit.

## Provenance

Hub consolidated 2026-04-24 from six memory files (`project_basira_canonical_path`, `project_basira_evidence_stack`, `project_basira_leadership_compass`, `project_basira_sovereign_decks`, `feedback_basira_governance_layer`, `feedback_basira_forbidden_trinity`) under the Phase D migration task from [[log-2026-04-24]]. Earlier version was a stub pointing to these memory files; facets for Leadership Compass and Sovereign Decks split into sibling notes [[basira-leadership-compass]] and [[basira-sovereign-decks]] to keep this hub under the 2000-word ceiling per [[0001-vault-architecture]].
