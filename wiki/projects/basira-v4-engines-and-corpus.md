---
id: basira-v4-engines-and-corpus
title: Basira V4 — Engines (Real vs Aspirational) & Source Corpus
type: project
status: active
aliases: []
tags:
  - basira
  - basira-v4
  - engines
  - corpus
  - sources
  - project
created: 2026-06-04
updated: 2026-06-04
summary: >-
  Two-part record for the Basira V4 rebuild: the honest engines truth (the celebrated "7 بصيرة engines" were never built — only نبض is live, مروءة is real-but-dead code, the rest are DESIGN/CRUD, and the SROI "engine" is a slider; port LOGIC not plumbing) and a navigational map of the ~88 harvested Drive documents (batch-1 12-a..h, 12-b empowerment, batch-2 13-a..e) plus the spine truths they established.
related:
  - "[[basira-v4-rebuild]]"
  - "[[drive-catalog]]"
  - "[[drive-folders-master-index]]"
  - "[[999-zero-paper-master]]"
  - "[[mhrsd-kpi-landscape-2024-2026]]"
source: session:s85-basira-v4-gather
---

This note carries two things the [[basira-v4-rebuild]] depends on: the **engines truth** (which celebrated capabilities actually exist in code versus which are aspirational prose) and the **corpus map** (a navigational index of the harvested Drive documents and the spine truths they established). Both serve one discipline from [[basira-v4-compass-and-anti-drift]]: **honesty over green** — V4 builds real, verified, testable loops or claims nothing.

## Engines — Real vs Aspirational (the honest accounting)

The marketing line is "7 AI engines." The standing directive is to use only the **four real engines** in deliverables and frame the rest as design language. More fundamentally: the celebrated بصيرة engines were **never built as working loops in any version (V1/V2/V3)** — they are aspirational prose backed, at most, by dead code or thin CRUD. Per the ledger (`01-REQUIREMENTS-LEDGER.md §C`), here is the per-engine truth:

- **نبض (nabd, "pulse") — REAL, LIVE in V3.** A config-driven clinical-rule reactor (`rule_key` + `severity` + `related_domains[]` + evidence + thresholds + cooldown; DB-side aggregation; cron-6h → BullMQ → processor; batched O(1)). It is the **only genuine cross-service reactor that exists** — but it does **detection → alert, not interlock**. It runs five real rules: `silent_pain` (meal refusals → nutrition + oral-pain assessment), `post_seizure` (the one true cross-table join: epilepsy profile ⋈ seizure incident → clinical monitoring), `abandonment` (negative mood logs → social worker, an isolation/abandonment early-warning), `weight_loss` (windowed weight-drop → clinical/nutrition), and `institutional_fatigue` (staff burnout + open alerts → staff-wellbeing). نبض is the **V4 reactor template** — extend it from alert to genuine interlock where safety demands (see [[basira-v4-cross-service-triggers]]).

- **مروءة (muruaa, chivalry/burnout-aware staff matching) — REAL algorithm, DEAD in V3.** A Maslach-grounded acuity + burnout engine (computes burnout from shifts/overtime/ratio; treats *staff burnout → beneficiary under-care* as a SAFETY trigger). The algorithm genuinely exists in `muruah-engine.service.ts`, but it is **never enqueued — zero `.add` calls** — so it does nothing in production. In V2 it ran only on hardcoded `WARD_PRESETS`. This is the second piece of LOGIC worth porting.

- **خوارزمية الإحسان (ihsan) → ملف الكرامة — DESIGN doctrine; thin CRUD live.** A Compliance→Empowerment scoring doctrine (`if meal_served && choice_respected && autonomy_exercised` → Autonomy Score; data-humanization → Wellbeing Score; proactive compassion). The doctrine is proven design (Drive); only thin preference CRUD is live; the **scoring is unbuilt**. Naming is RESOLVED and not to be re-litigated: **ملف الكرامة** (the Dignity File) is the user-facing name; *إحسان* is the internal engine name underneath — do not claim إحسان as a separate user-facing engine.

- **كرامة (karama, dignity) — REAL/LIVE thin CRUD.** This is the humanisation file itself (the Dignity File: preferred-name, how-to-engage, sensory tolerances, سجل الحسنات / merit ledger). The rich scoring loop on top of it is DEMO/aspirational; the CRUD beneath is real.

- **البوصلة (bawsala, the Compass / Leadership Compass) — DESIGN.** A 7-tab decision instrument (decisions ledger, honest mirror, 12-month trends, scenario simulation, policy horizon) with decision-permanence and barrier-linkage as non-negotiable principles. It existed as a seed-fed instrument in V2; **V3 lost it (kept a dead ~739-LoC stub)**. Restore the design, not the seed.

- **حسّة (hessa, risk-sensing) — REAL keyword-logic in V2, reduced to CRUD in V3.** Arabic-keyword extraction (بلع/انفعال/عدوان → score) + Morse factors → seizure + behavioural-crisis early-warning. The proactive logic existed in V2 and was hollowed into a CRUD surface in V3.

- **Wellbeing index — REAL but two-headed.** A weighted composite (V1 SQL view-chain; Drive scorecard variant). Real but inconsistent across versions (V1 had a silent demo fallback, colour drift, `activity` hardcoded to 70); V3 dropped the pattern.

- **Predictive Engine — DESIGN only.** The Drive doctrine of fusing weak signals into a ~48h-ahead prediction. نبض is its partial code realization; the predictive engine proper does not exist.

**Engines NOT to claim (anti-fabrication, load-bearing):** the **SROI "engine" is fabricated** — the NotebookLM-described "SROI / triangulation / Launch-Gate engine" does not exist in code; `SroiTab` is a **slider calculator**, not an engine. The 1:4.2 SROI ratio is a real *parameterised calculation* (deadweight 25% / attribution 30% / displacement 5%) and is the pitch number; ≥3.5 is the aspirational national target — never swap them. Also do not claim **governance auto-CAPA** as built (Drive Governance Engine design; ABSENT in code), and do not resurrect the NOT-ADOPTED **"Social-Impact Digital Twin"** simulation (same fabrication class as the phantom SROI engine — keep its four impact-KPI dimensions as measured fields, drop the crystal ball).

### What to port from V3 — LOGIC, not plumbing

The two pieces worth carrying forward are **مروءة's burnout-aware matching** and **نبض's early-warning rule reactor**. Port the **LOGIC as pure library / engine functions**, NOT the V3 NestJS/BullMQ/Redis plumbing. The Terminal-C best-practices arm of the gather phase reached the same conclusion: keep Next.js full-stack, drive interlocks through ONE transactional trigger-dispatcher, and implement engines as pure lib functions rather than re-importing the framework ceremony that hollowed V3. Each ported engine ships as a real, characterization-tested loop (firing case AND the negative case where the guard blocks it) or it is not claimed.

## The Source Corpus — navigational map

The gather phase harvested roughly **88 Drive documents** into traceable extracts. The raw per-file extracts live under `Desktop/Basira-REBUILD/harvest/` (files `01…13`); the two thematic syntheses are `12-CORPUS-SYNTHESIS.md` and `13-CORPUS-BATCH2-SYNTHESIS.md`. The traceable requirements rows distilled from all of it land in [[basira-v4-requirements-ledger]]. See [[drive-catalog]] and [[drive-folders-master-index]] for the broader Drive inventory.

**Batch-1 — the 62-file operations corpus (`harvest/12-a … 12-h`).** Thematic coverage:

- `12-a` — improvement / excellence / strategy: the canonical ministry **WHY** (medical→rights), the Golden Thread anti-drift gate, the DMAIC/SIPOC/CTQ toolset.
- `12-c` — quality / QMS / standards: the **127-process / 25-department owner registry**, the standards-KPI scorecard schema, the consolidated center KPI table.
- `12-d` — infection control: the 18-category national IPC audit form, the CAPA tracker, the 3-tier committee + real roster, isolation→fan-out triggers, the BICSL 2-year staff certification.
- `12-e` — catering (الإعاشة, beneficiary food provisioning): the GFM-FS-TP-PR-6003 food-safety forms, FIFO inventory, contractor-governance → entitlement% → financial extract.
- `12-f` — operations / forms / org / emergency / maintenance: the **4-division org chart + 8-level authority ladder**, the social-services Forms 12/14, the ~52 GFM-ZM maintenance forms, the ICS emergency model.
- `12-g` — beneficiary voice / satisfaction / gap analysis: the strongest single **WHY** (the 5-gap diagnosis vs UN-CRPD), the activity→impact KPI pivot, the صوت المستفيد (beneficiary voice) methodology.
- `12-h` — Basira system / platform docs: Ahmad's real ops-guide forms and the alert-tags-as-directive-emitters table (the proven KNOW→SERVE seed).

**12-b — the empowerment theme (KNOWN GAP, HIGH severity).** The تمكين / رؤية 2030 / الدمج المجتمعي (empowerment / community-integration) theme — 10 files including the مشروع الدمج المجتمعي guide v1.3, the vocational rehab/employment doctrine, the new disability table (جدول الإعاقات), and the رؤية 2030 empowerment vision — was **never synthesized into a finished extract**. This is the compass-core theme; its content is only partially cross-referenced elsewhere (the 8-category integration table via `12-f §7b`). See [[empowerment-thesis-corpus]] and [[empowerment-vocabulary]] for the adjacent already-mapped material, and [[community-integration-project]] and [[999-disability-care-empowerment-strategy]] for the policy frame this gap was meant to capture.

**Batch-2 — the WHY-and-narrative batch (`harvest/13-a … 13-e`).** Batch-2 heavily re-covers batch-1 terrain; it is *not* a new-capability batch. Its load-bearing contributions: (1) the **medical-gateway barrier** (البوابة الطبية) — the sharpest diagnosis in the whole corpus; (2) the richest **NOT-ADOPTED** haul (radar/LiDAR room sensors, an "IHSAN-Score" engine, wearables, emotion-AI, the Digital Twin, SROI/SIB finance, a سري self-classification header — each a re-confirmation of an already-settled ban); and (3) ministry-credible pitch language + real national KPIs. Its few clean new build-rows: the self-care task-analysis skill tracker, the NCR / quality-loop form, Dignity-File sensory-preference fields, the round-trip referral pattern, the outbreak-mode facility state machine, and the emergency-readiness checklist + functional-state-derived evacuation priority.

### Spine truths the corpus established

These are the externally-validated facts the corpus locks in, beyond any single capability:

- **The ministry's OWN national report validates the social frame.** It measures **Outputs, not Outcomes** — *وهم الإنجاز* (the illusion of achievement), where activity KPIs (sessions counted, paper plans completed) become a defense mechanism that masks the absence of real impact. V4's north-star inverts this: *functional-independence delta per beneficiary per quarter*, not service volume.

- **The medical gateway forces the medical model.** The only entry to any service is "خدمة تقييم الإعاقة" (disability-assessment service), which mandatorily demands "أصل تقرير طبي" (an original medical report) to set disability type/degree. From contact-point one the whole منظومة (system) is locked into "ما تشخيصك؟" (what is your diagnosis?) instead of "ما أهدافك؟" (what are your goals?). This is the concrete mechanism V4's KNOW surface must invert — **start from goals + barriers + function, not diagnosis.** Disability is social/functional, never a ceiling.

- **A 27-procedure (batch-2: 30-procedure) RACI operational layer sits above the intake forms.** Standardized procedures in three categories (اجتماعية نفسية / دعم المستفيدين / تقديم الرعاية), each with a goal + RACI executors + governing regulations + named forms — the workflow backbone V3 never modeled. The catalogue's referral loops (e.g. the PT → medical round-trip on استمارة تحويل) are all **alert + human-action, never auto-block** — primary evidence for the "alert vs hard-block" open design call.

- **A 5-year weighted-BSC KPI history grounds V4's numbers.** Real numerators (2026 health-KPI collection fields, national outcomes) plus Balanced-Scorecard targets (which are *aspirational* design values, NOT achieved actuals — preserve that flag) and a cumulative quarterly model (Q1 51% / Q2 66% / Q3 83% / Q4 100%). This anchors V4 KPIs in real center history so the numbers are grounded, not fabricated — consistent with [[mhrsd-kpi-landscape-2024-2026]] and [[999-zero-paper-master]].

- **The celebrated "engines" honesty truth** (restated as a spine fact): they were never built in any version, so V4 builds real loops or claims nothing — and the dental-extraction → soft-diet wire that V4 proved end-to-end has a **real paper origin** (the استمارة تبليغ مطبخ بالحالة, the kitchen-notification form), so it is a port of proven behavior, not an invention.

For the org/role layer the corpus filled, see [[basira-v4-org-roles-rbac]]; for the disability/empowerment classification work, [[basira-v4-disability-empowerment-model]]; for the architecture decision, [[0003-basira-v4-architecture]]. The vault's own structure rules are in [[0001-vault-architecture]].
