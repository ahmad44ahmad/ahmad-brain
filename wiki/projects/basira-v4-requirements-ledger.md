---
id: basira-v4-requirements-ledger
title: Basira V4 — Requirements Ledger (A–J Digest)
type: project
status: active
aliases: []
tags:
  - basira
  - basira-v4
  - requirements
  - ledger
  - project
created: 2026-06-04
updated: 2026-06-04
summary: >-
  Navigational map of the Basira V4 requirements ledger's ten sections (A KNOW-the-human, B cross-service triggers, C engines real-vs-aspirational, D governance, E KPIs/anti-falsification, F medication interlocks, G empowerment/rights, H theoretical-foundations, I 62-file corpus, J corpus batch-2), each with its load-bearing requirements and harvest pointers. The full 66KB ledger lives on Desktop.
related:
  - "[[basira-v4-rebuild]]"
  - "[[basira-v4-cross-service-triggers]]"
  - "[[basira-v4-org-roles-rbac]]"
  - "[[basira-v4-disability-empowerment-model]]"
  - "[[mhrsd-cyber-policy-library]]"
  - "[[mhrsd-rehab-center-forms]]"
  - "[[mhrsd-restraint-agitation-policy]]"
source: session:s85-basira-v4-gather
---

This is a navigational digest, not a re-transcription. The full requirements ledger — every capability row with its `what · source · why-it-exists · barrier · REAL/DEMO` cells and harvest pointers — is a 66KB document at `C:/Users/aass1/Desktop/Basira-REBUILD/01-REQUIREMENTS-LEDGER.md`. That file was built "pull, don't invent": each row is traceable to one of the harvest extracts (`harvest/01…13`) and preserves an honest REAL / DEMO / ABSENT / PARTIAL flag. Read this note to know which section holds what; read the ledger (or the named `harvest/NN §X` extract) for the field-level detail. The compass governing every section: KNOW the human (functional + dignity + safety) → SERVE across services → break the societal barrier. See [[basira-v4-rebuild]] for the rebuild's overall direction.

A recurring device is the **B1–B10 barrier dial** — a ten-type taxonomy of social-handicap codes (B1 physical/material … B10 religious dogma) pulled verbatim from V2's `sql/022_barrier_type_annotations.sql`. Each capability states which barrier it dissolves. The dial belongs to the [[social-handicap-compass]] frame.

## A — KNOW-the-human: models & forms (build FIRST)
The heart of V4: model the human richly enough that facts can flow to whoever serves or protects. The richest field knowledge is the MHRSD paper forms — re-author from those, not from any version's React. Load-bearing rows: A1 **ملف الكرامة** (the Dignity File — preferred name, what makes happy/upset, dreams, sensory tolerances, سجل الحسنات / Merit Ledger); A5 the PT 5-page clinical assessment (the crown jewel — bilateral per-joint/per-muscle graded grids; scanned-image only, re-author from scratch, no OCR); A7/A8 Social Form 12 (Social Study, 8–9pp) and Form 14 (IRP, 12pp — one plan, a sub-page per department); A10 the multi-actor shared-record model (section-level write ownership + role-scoped sections + multi-signature — the literal "مؤتمن signs تعهد + sees-all + accountable" model). Anti-invention flag: the 32-tooth odontogram was a V2 UX invention, **not** a ministry form — do not re-author it. Detail: `harvest/01 §1`, `02 §9`, `03 §2.4`.

## B — SERVE / cross-service impact triggers ★ (THE SOUL)
A care event in one service auto-causes a care action in another — the single capability whose absence most distinguishes real digital transformation from paper-to-keyboard. Honesty discipline here is non-negotiable, because overstating the soul *is* the fabrication anti-pattern. What is REAL today: the **نبض (Nabd)** rule engine (config-driven detection→alert, live in V3, the V4 reactor template), V1's fall-risk→facility-wide realtime alert (the only true event-driven interlock that ever shipped), and V2's vitals-breach early-warning pattern. The named soul-interlocks are **ABSENT in code** but have proven data hooks: dental-extraction → kitchen soft-diet (Ahmad's canonical proof, nutrition target model proven in Drive); epilepsy → outing-safety flag; glucose-measured → insulin interlock — but the **insulin** specifically carries a **provenance flag: it is unsourced in any Basira doc, a generic illustration; confirm against a real form before building** (the adjacent glucose→diabetic-diet edge is the design that is actually attested). V4 mandate: ship ONE interlock end-to-end first, each with a characterization test proving it fires and the negative case where the guard blocks it (soft-diet must expire after its time-box). Full interlock catalogue and field hooks: [[basira-v4-cross-service-triggers]]; ledger §B (`07 §5`, `08 §4.2`, `03 §2.2`).

## C — AI engines: real vs aspirational
Use only the **4 real engines** in deliverables; frame the rest as design language. The "7 AI engines" is marketing. Load-bearing honesty: **نبض (Nabd)** is REAL and live in V3; **مروءة (Muruah)** — staffing/burnout, staff under-care as a safety trigger — is a real algorithm but **DEAD in V3** (never enqueued); **حسّة (Hessa)** and **كرامة (Karama)** exist but were reduced to CRUD surfaces; **خوارزمية الإحسان (Ihsan)** is the internal engine name under the user-facing ملف الكرامة, with its compliance→empowerment scoring still unbuilt. Explicitly **fabricated** (do not claim): the NotebookLM "SROI/triangulation/Launch-Gate engine" — `SroiTab` is only a slider calculator. Engine inventory and corpus mapping: [[basira-v4-engines-and-corpus]]; ledger §C (`04 §5.1`, `03 §2.2`, `08 §4.1`).

## D — Governance & compliance (accountability-positive)
Frames governance as accountability, not restriction: the data FLOWS to serve; the human chain of trust plus the access ledger protect it. **NO field-masking, NO سري/مقيد classification tiers, NO PDPL-hedging-as-blocker** — re-importing those is re-importing the defect that ate V3. Load-bearing rows: D1 every authenticated user is a مؤتمن (trusted employee) who signs a تعهد and is fully accountable, every access logged; D2 the immutable `audit_logs` BEFORE-UPDATE/DELETE trigger (the one DB guard that works in V3) extended to all append-only tables, repurposed as the pledge's teeth not privacy machinery; D3 decisions are permanent (no DELETE on strategic_decisions, enforced at DB level). Role/RBAC detail: [[basira-v4-org-roles-rbac]]; ledger §D (`07 §3.1`, `03 §2.5`, `08 §7.4`).

## E — KPIs & anti-falsification
North-star metric: **functional-independence delta per beneficiary per quarter** — not service volume or satisfaction surveys (the inversion of the "zero incidents / quantitative-indicator tyranny" anti-pattern, the "وهم الإنجاز" / illusion-of-achievement critique). Load-bearing rows: E1 the 4-dimension Compass KPI (Autonomy · Active Contribution · Human Impact · Sustainability); E3 the **Honest Mirror** — deliberately surface uncomfortable structural patterns, never hide failures; E5 **SROI 1:4.2 is the pitch number, ≥3.5 is the aspirational national target — NEVER swap them**; E4 epistemic-humility labels (every trend tagged real / partial / modeled with declared confidence). Anchor numbers to real center history (E7), not fabrication. KPI-landscape context: [[mhrsd-kpi-landscape-2024-2026]]; ledger §E (`04 §3`, `04 §8`).

## F — Medication-safety interlocks
The eMAR backbone V3 left as a phantom. Load-bearing rows: F1 the missing `MedicationSchedule` model (`GET /medication-schedule` is a 404 with no backing table — must build); F2 `MedicationAdministration` made append-only plus `Prescription`; F3 the glucose → medication gate — the same brief-named insulin interlock, carrying the **same provenance caveat as B-T3: insulin specifically is unsourced; confirm against a real diabetes/medication form before building**; F5 the allergy + drug-restriction hard-block across medication and catering. The interlock-pattern detail lives with the triggers: [[basira-v4-cross-service-triggers]]; ledger §F (`08 §4.2`, `03 §4.3`, `01 §1.9`).

## G — Empowerment & rights expansion (V4's core mandate)
What V3 under-served. Framed as reviving stranded treasure, not new invention; compass = تمكين (empowerment), not رعاية (care); language discipline مريض→المستفيد, diagnosis→barrier-assessment. Load-bearing rows: G1 the empowerment cue-strip / "dark beneficiary" detector (V3's one alive product — diff roster vs rows-with-data, surface no-data beneficiaries as create-cards; fix the `limit=100` cap hiding 153 of 253); G3 the Leadership Compass 7-tab decision instrument with a no-delete Decision Ledger tracking 3/6/12-month outcomes (V3 lost it, kept a dead stub); G5 the B1–B10 barrier taxonomy as first-class `barrier_codes[]` plus the Dignity Index; G8 the accountability / evasion-pattern ledger (V1's crown jewel — instruments the institution's own failure to respond, with real Al-Baha quotes). Full model: [[basira-v4-disability-empowerment-model]]; ledger §G (`04 §4`, `02 §3.1`, `03 §3`).

## H — Theoretical-foundations additions (Drive: 24 conceptual docs)
The genuinely-new traceable items from Ahmad's theoretical-foundations harvest, nationally standardized (نظام 01 رعاية المعوقين + لائحة 02), so a sister-center provenance still applies to Al-Baha. Load-bearing rows: H1 the 27 standardized operational procedures (each with goal + RACI executors + governing regs + named forms — the workflow layer V3 never modeled); H2 the asset/maintenance forms set (the flagged DB gap); H7 real KPI numerators + BSC targets + the 2025 quarterly-cumulative model (Q1 51% · Q2 66% · Q3 83% · Q4 100% — REAL numerators, DESIGN targets). NOT-ADOPTED here (logged, never build-rows): field-classification, CCTV-radar, digital-twin simulation, SIB contracting. Anti-drift context: [[basira-v4-compass-and-anti-drift]]; ledger §H (`harvest/11 §A–G`, `11 §X`).

## I — Corpus (the 62-file Drive harvest)
Reframes V4 from "beneficiary-file + engines" to a **center operating system** and supplies the ministry-credible WHY for the مشاركة (participation/innovation) submission. 31 rows; anti-double-count rule means most only enrich an A–H row. Load-bearing rows: I1 the 127-process / 25-department owner registry (every screen serves an owned, measured process); I2 the org structure — 4-division chart + 8-level authority ladder, role name مسؤول الجودة not مدير الجودة (fills the S84 org-structure gap; see [[basira-v4-org-roles-rbac]]); I8 the 18-category national IPC audit form (Ahmad's actual quality role, default-OPEN); I13 isolation-precaution → multi-service fan-out (the IPC analogue of dental→soft-diet); I30 alert-tags-as-directive-emitters (a real ministry form validating the SafetyFact→cross-service-directive pattern — `صعوبة بلع` / swallowing-difficulty → pureed). Corpus map: [[basira-v4-engines-and-corpus]]; ledger §I (`harvest/12-a…12-h`, map in `12-CORPUS-SYNTHESIS.md`).

## J — Corpus batch-2 (the WHY + the NOT-ADOPTED haul)
Deliberately lean: batch-2 re-covers §§A–I ground, so its center of gravity is the **WHY**, the pitch narrative, and the corpus's richest NOT-ADOPTED haul — not new capability. Load-bearing new rows: J1 the **medical-gateway barrier** (the sharpest WHY — the only entry to any ministry service is disability-assessment requiring an original medical report, so the system asks "what is your diagnosis?" not "what is your dream?"; V4 inverts this — see [[community-integration-project]]); J6 the NCR form + RED-KPI→NCR→close loop (makes deviation→CAPA and the Honest Mirror buildable); J7 the self-care task-analysis skill tracker (the buildable shape of tracking empowerment as outcomes, not activity counts). The **NOT-ADOPTED** haul — refuse on sight: radar/LiDAR room sensors, the rolled-up "IHSAN Score" number (keep the 5 dimensions, drop the composite), wearables/biometrics, affect-detection AI, digital-twin, SROI/SIB finance, and the سري self-classification header. Positive finding: Al-Baha's own IPC docs independently validate the one anti-stigma rule. Anti-drift authority: [[basira-v4-compass-and-anti-drift]]; ledger §J (`harvest/13-a…13-e`, map in `13-CORPUS-BATCH2-SYNTHESIS.md §H`).

## The carry-forward, in one line
V4 = V3's engineering discipline + V2's product-philosophy + V1's domain-model, around the compass. V1's stranded treasure is data and domain-model (the accountability ledger, independence-economics, the two real engine patterns); V2's is product-philosophy (B1–B10, Dignity Index, Leadership Compass); V3's gain is engineering (the clean 114-model schema, the Nabd reactor, audit-immutability, the six live empowerment forms). The Drive corpus adds the center-operating-system doctrine and proven nutrition model; batch-2 tells V4 *why* it exists and *what surveillance/engine drift to refuse on sight* — المستفيد أولًا (the beneficiary first).
