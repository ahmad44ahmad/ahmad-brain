---
id: drive-vault-coverage-audit
title: Drive ↔ Vault Coverage Audit + Phased Ingestion Plan
type: source
status: active
aliases:
  - coverage-audit
  - drive-audit-2026-04-25
  - vault-gap-analysis
  - ingestion-plan
tags:
  - audit
  - coverage
  - ingestion-plan
  - drive
  - vault-rules
  - meta
created: 2026-04-25
updated: 2026-04-25
valid_from: 2026-04-25
learned_at: 2026-04-25
confidence: high
source: synthesis:vault-frontmatter-scan + drive-folders-gemini.jsonl + 999HRSD-all-mcp-enum
related:
  - "[[drive-catalog]]"
  - "[[drive-folders-master-index]]"
  - "[[drive-999-docs]]"
  - "[[employment-archive]]"
  - "[[al-baha-center-policies]]"
  - "[[research-initiatives-portfolio]]"
  - "[[999-albaha-qms-bcp]]"
  - "[[999-disability-care-empowerment-strategy]]"
  - "[[0001-vault-architecture]]"
  - "[[0002-language-policy-and-sources-folder]]"
summary: >-
  Authoritative coverage audit run 2026-04-25 mapping the 45-note vault against
  68 Drive folders + indexed individual files. Surfaces 6 fragile asserted-no-source
  nodes, 11 Drive topic clusters, 17 skip-worthy folders, 10+ unrecorded coined
  Arabic phrases, and 3 cross-folder evidence chains. Output: a 9-phase ingestion
  plan ordered by leverage-per-effort with explicit anti-goals + decision log.
  Replaces the priority list in session_2026-04-25_phase-d-deep.md memory pointer.
---

# Drive ↔ Vault Coverage Audit + Phased Ingestion Plan

**Run date:** 2026-04-25 · **Methodology:** ADR-aligned, three-subagent parallel audit (vault frontmatter scan + Gemini-JSONL digest + Drive MCP enumeration of one folder).

**Why this exists.** Prior session priority lists drifted because they were derived from partial inventory. This audit re-derives ingestion order from a complete map of (a) what's in the vault, (b) what's on Drive that's worth ingesting, and (c) where each side has gaps the other can fill. Replaces the open-task list in `session_2026-04-25_phase-d-deep.md` memory file as the canonical source of "what to distill next".

## 1 — Vault state snapshot (2026-04-25 close of session 21)

| Bucket | Count | Notes |
|---|---|---|
| Total notes (wiki + decisions + log + root) | **45** | 8 people · 6 projects · 4 concepts · 4 entities · 14 sources · 4 synthesis · 2 ADRs · 2 logs · 1 root manual |
| Sourced (have `source:` frontmatter) | **34** (76%) | drive ×15 · pst ×7 · voice/other ×7 · local-repo ×5 |
| Fragile assertions (substantive content, no source) | **6** | The high-priority backfill targets |
| Stubs / drafts | **1** | bandar-alzahrani (status:draft) |
| Implied-but-missing target ids | **3** | Two real, one harmless legacy |

### 1.1 — Fragile asserted nodes (no `source:`)

Highest backfill priority. Substantive content currently unanchored to any verifiable external source — vulnerable to drift if Ahmad's memory shifts.

| id | type | what's asserted | best Drive anchor candidate |
|---|---|---|---|
| `albaha-center-org` | entity | Current heads of each dept at the Al-Baha Comprehensive Rehab Center, dictated 2026-04-23 | Drive fileId `1L3kGlLjaNZmU_scGDtW14rWky3x-XBZH63VwYy9Zaoc` (already in `drive-catalog`) + folders #16, #51 |
| `albaha-regional-admin` | entity | Org structure of HRSD GA at Al-Baha region | Drive fileId `1lo_3Qynf-v9-cqVi8_Z1H6CiuWISStaIpceqcCSmujI` (already catalogued, NOT yet linked) |
| `mhrsd-dev-sector-esystems` | entity | MHRSD Development Sector e-systems inventory | JSONL #10 (التحول في الوزارة, 200+ files) + #56 (appsheet) |
| `mhrsd-leadership` | entity | April 2026 ministry org map | JSONL #33 (سياسات المخاطر — names Ismail Al-Ghamdi as steering chair) + #54 (لائحة الخدمة الجديدة, delegation chains) |
| `ahmad-career-arc` | synthesis | 14-year MHRSD career arc with role progression | Aggregation node — anchored by employment-archive + PST + #19 + #26 (SCFHS license) + #37 |
| `three-tracks` | synthesis | Forward-facing portfolio (Basira / AI-H100 / ahmad-brain) | Pure synthesis; no single Drive doc anchors. JSONL #11 + #37 partial |

### 1.2 — Implied-but-missing wikilink targets

| missing target | referenced from | resolution |
|---|---|---|
| `50-People` | `log-2026-04-24` | Legacy PARA folder reference; harmless. |
| `999-albaha-qms-bcp-ar` | `log-2026-04-25` | The raw Arabic companion. Lint doesn't index `raw/`; documented open task — extend `lint.py:ROOTS` to `raw/drive/` so wikilinks resolve per ADR-0002 Amendment 3. |
| `albaha-regional-admin-org` | `nuwaira` person note | Likely typo for `albaha-regional-admin`. Fix during phase F-1. |

## 2 — Drive state snapshot

### 2.1 — Top-level structure

- **68 catalogued folders** (Gemini-narrated 324k chars, JSONL at `~/ahmad-brain-import/drive-folders-gemini.jsonl`).
- **5 confirmed empty** (#48, #64, #65, #66, #68) → skip.
- **3 already-distilled** (#19 → `employment-archive`, #22 → `al-baha-center-policies`, #3 → `research-initiatives-portfolio`).
- **~60 active folders remain** for evaluation.
- **Plus** ~25 high-signal individual files indexed in `drive-catalog` but not yet bound to source notes (Basira reference manuals, pitch docs, Gdocs not in any catalogued folder).

### 2.2 — Topic clusters (11)

Folders grouped by topic-domain for ingestion sequencing. Priority is leverage-per-effort, not raw signal.

| Cluster | Members (JSONL idx) | Already in vault | Ingestion priority |
|---|---|---|---|
| **C1 — Basira/digital-transformation/AI tooling** | #56, #59, #60, #61, #62, #67-partial | Partial — `basira` hub | **high** |
| **C2 — Basira evidentiary stack / CRPD pivot** | #3✓, #7, #11, #29, #44, #45, #55 | #3 only | **high** (rest) |
| **C3 — PT modeling / ministry templates** | #1, #36 (=#1), #22✓, #35, #51 | #22 only | **high** (rest) |
| **C4 — Quality / EFQM / ISO / KPIs** | #2, #46 (=#2), #5, #13, #30, #33, #42, #43, #53 | None directly | **high** |
| **C5 — Overtime court case** | #19✓, #20, #39, #49, #14, #56 | #19 only | **medium** (consolidate) |
| **C6 — Infection control + OSH + emergency** | #4, #12, #15, #16, #18, #23, #25, #34, #50 | None | **medium** |
| **C7 — HRSD ministerial transformation** | #10, #21, #54, #43 | Partial — `hrsd-work` | **medium** |
| **C8 — Career / personal credentials** | #19✓, #26, #37, #63 | #19 only | **low-medium** |
| **C9 — Innovation / authorship / IP** | #8 | None | **low** |
| **C10 — Personal library / non-work** | #6, #9, #17, #40, #41, #47 | None | **skip** |
| **C11 — Personal financial / sediment** | #24, #27, #28 (=#27), #32, #38, #57⚠, #58⚠, #67 | None | **skip** |

Plus operational sediment (#31, #38) at low priority and confirmed-empty folders skipped.

### 2.3 — Drive duplicates (verified by digest)

- `#1 ≈ #36` — "علاج طبيعي - هوية الوزارة" (treat as one source).
- `#2 ≈ #46` — "مشروع الجودة 2024" (treat as one source).
- `#3 ≈ #7?` — both 37 files; #7 carries denser strategic framing. Likely two snapshots of same folder; verify when distilling.
- `#27 = #28` — 2013 sports league.
- `#59-#61` — three "Google AI Studio" entries; #61 (largest) supersedes others.
- HRSD font-kit duplicated across `999HRSD-all` + 4 other locations — confirmed in 2026-04-25 audit.

### 2.4 — Disproved assumption

The catalog flagged `1emSX-om-05Brv3d8wYApzMqb4ocdlrHb` (`999HRSD-all`) as "secondary 999 doc hub, likely 20+ more docs". 2026-04-25 enumeration via Drive MCP shows: **19 font files, 0 documents, 0 overlap with the 7 known 999 Gdocs**. Reclassify as brand-asset duplicate; remove from any "research-doc hub" enumeration. Update `drive-999-docs` catalog accordingly during phase F-1.

### 2.5 — Drive MCP query limitation (operational note)

The `mcp__claude_ai_Google_Drive__search_files` tool **rejects** `parents in '<id>'`, `'<id>' in parents`, and `trashed = false` query fields. Future folder enumeration must use indirect strategies: file-extension queries (`.pdf`, `.ttf`) plus client-side `parentId` filtering, or `title contains` plus `parentId` filtering. Already wasted cycles in the 2026-04-25 audit; documenting here so future sessions don't repeat.

## 3 — Cross-walk: Drive surplus mapped to vault gaps

Each entry below maps a high-leverage Drive cluster or single folder to the vault node it would create or anchor. Effort estimates assume one main-context distillation pass for ≤50 KB Gdocs, subagent dispatch for >50 KB or folder enumerations.

### 3.1 — Folders with ZERO vault anchor that warrant new nodes

| Drive | Proposed vault node | Evidence in folder | Effort |
|---|---|---|---|
| #2/#46 (مشروع الجودة 2024, 110+ files) | `wiki/sources/al-baha-quality-project-2024.md` | The "الخيط الذهبي" QMS architecture · BSC · process inventory · governance escalation chain | **M** |
| #5 (2025 KPIs) | `wiki/sources/mhrsd-2025-kpi-portfolio.md` | تعميم 28597 (6/7/1446 H), official 2025 KPI weights + formulae per dept | **S** |
| #11 (التمكين المستقبلي) | `wiki/concepts/empowerment-maturity-model.md` | Three-tier maturity model (1.0 طبي → 2.0 حقوقي → 3.0 اقتصاد منصة) + coinages | **S** |
| #29 (رضا المستفيد / صوتك مسموع) | `wiki/sources/sawtuk-masmou-proposal.md` OR fold into existing `999-albaha-qms-bcp` evidence stack | IDD pictorial-survey design, القط العسيري visual identity, gender ethics | **S** |
| #18 + #23 + #42-fragments | `wiki/projects/aman-mustadam-initiative.md` | National PWD-emergency-mgmt initiative (CRPD Art. 11; 2-4× mortality stat) | **M** |
| #20 + #39 + #49 + #14 + #56 (legal slice) | `wiki/synthesis/overtime-grievance-case.md` | 8h-vs-7h dispute · إساءة سلطة · تزوير معنوي · case timeline | **M** |
| #4 (مكافحة العدوى, 275+ files) | `wiki/sources/al-baha-ic-archive.md` | Ahmad as IC trainer + IC committee secretary; BICSL-RC trained | **M** |
| #37 (علي القرني folder) | `wiki/sources/alqarni-leadership-thesis.md` | Ahmad-authored "leadership thesis" packaged FOR Al-Qarni | **S** |
| #51 (نماذج تقييم المركز) | `wiki/sources/mhrsd-supervisory-visit-instruments.md` | Official supervisory-visit instruments + control→partnership thesis | **S** |
| #56 + #59-#61 + #62 | `wiki/sources/ahmad-engineering-substrate.md` | AppSheet apps · prompt-engineering rubrics · pre-Basira tooling proof | **M** |
| #44 (الدمج المجتمعي) | `wiki/sources/community-integration-project.md` | Community-integration project artefacts | **S** |
| #45 (تطوير التدريب) | `wiki/sources/training-development-project.md` | Training-development project file | **S** |
| #55 (وثيقة حقوق المستفيدين) | `wiki/sources/beneficiary-rights-document.md` | Beneficiary-rights authoritative doc | **S** |
| #33 (سياسات المخاطر التميز الابتكار) | `wiki/sources/mhrsd-risk-excellence-policies-2025.md` | April 2025 ministerial risk/governance policies, signed by Ismail Al-Ghamdi | **S** |
| #1/#36 (هوية الوزارة, PT identity, 86+ files) | `wiki/sources/mhrsd-pt-identity-archive.md` | Pre-existing MHRSD PT modelling documentation | **M** |

### 3.2 — Existing Tier-1 individual Gdocs (still un-distilled)

Carried over from session_2026-04-25 priority list, validated against this audit:

| Drive fileId | title | size | vault target | status |
|---|---|---|---|---|
| `1sgdawDigC4wn_8FyfmTR21Xq_nnzu96VGKnqZ_aoBsw` | 999 تحقيق التميز المؤسسي والابتكار | 53 KB | `wiki/sources/999-institutional-excellence-innovation.md` | **active** |
| `1iC8AdwZStrwyGhGxzL-tujA-ws7hA3egIshgoioi5a4` | 999 إعادة بناء الرعاية الاجتماعية | 24 KB | `wiki/sources/999-rebuilding-social-care.md` | **active** (overlap-check first) |
| `1z4GxUGvvfpelVRFmqWS8vTB0aLQwWEj-B0yxKXuER_w` | 999 تنسيق Markdown — موضوع شامل | 272 KB | `wiki/sources/999-zero-paper-master.md` | **active** (subagent required) |
| `1W_NP1LIfK_hytOglryCy9aFTcaaij2GAZcAlQziMY3Q` | 999 منظومة رعاية وتمكين | 252 KB | `wiki/sources/999-disability-empowerment-system.md` | **probable-overlap with master 999** — verify before distill |
| `1oTXk7UBKrqgFDVl3_R7pg_58S665Y8-2xWszxxxAalY` | 999 تنمية المهارات لذوي الاحتياجات الخاصة | 319 KB | `wiki/sources/999-skills-development.md` | **deferred** until topic match emerges |

### 3.3 — Coined-vocabulary gap (concepts not yet noted)

The Drive digest surfaced 10+ Ahmad-orbit Arabic coinages. These cluster into three vocabulary domains, none of which has a concept-note in the vault yet:

**Critique vocabulary** (the medical-care model and its pathologies):
- «حلقة التبعية المغلقة» / «هندسة للتبعية» / «صناعة الاعتمادية»
- «مؤسسات كلية» (Total Institutions, Goffman)
- «إماتة الذات»
- «طغيان المؤشرات الكمية» / «صفر حوادث» (zero-incident anti-pattern)
- «هدر رأس المال البشري»
- «فصام استراتيجي» / «عبثية بيروقراطية» / «وهم الإنجاز»

**Vision vocabulary** (the empowerment-economy alternative):
- «اقتصاد المنصة للتمكين» (Platform Economy for Empowerment, Level 3.0)
- «الريادة السعودية» / «الريادة الاستباقية»
- «التمكين الاستباقي» vs «الرعاية التفاعلية»
- «نموذج أولي استراتيجي»
- «الدفع مقابل النجاح» (Pay for Success contracting)
- «التمويل الفردي»

**Procedural vocabulary** (governance shift + grievance):
- «الشراكة التكاملية والتفاعلية» vs «رقابة تقليدية»
- «اغتصاب صلاحية الوزير»
- «التزوير المعنوي» / «الإكراه الإداري»
- «نواة لتجربة رائدة قابلة للتعميم» (Al-Baha as scalable pilot nucleus)

Already in vault: «الخيط الذهبي», «صوتك مسموع», «أمان مستدام» (last two are partial — named but not concept-noted).

**Recommendation:** create `wiki/concepts/empowerment-vocabulary.md` as a single concept node holding all three vocabulary domains with provenance per phrase. Do NOT scatter across many tiny concept notes — kepano density rule.

## 4 — Phased ingestion plan

Sequencing principle: **anchor fragile assertions → saturate one project's evidence stack at a time → add cross-cutting syntheses → original Tier-1 docs → opportunistic enrichment → defer PST**.

Per-phase: each is one focused work unit, ~30-90 min. Phases F-1 through F-8 are vault-ingestion phases; F-9 is the deferred PST integration.

### Phase F-1 — Anchor fragile entities (effort: ~30 min)

**Goal:** add `source:` frontmatter to the 4 entity nodes + 1 typo fix + 1 catalog correction. No new content distillation; pure backfill.

1. `albaha-regional-admin` ← Drive fileId `1lo_3Qynf-v9-cqVi8_Z1H6CiuWISStaIpceqcCSmujI`.
2. `albaha-center-org` ← Drive fileId `1L3kGlLjaNZmU_scGDtW14rWky3x-XBZH63VwYy9Zaoc` (+ note older PDF org chart as `superseded:`).
3. `mhrsd-dev-sector-esystems` ← `drive-folder:<JSONL #10>` placeholder + JSONL #56 cross-ref.
4. `mhrsd-leadership` ← JSONL #33 + #54 (+ note that ministry org-chart is partly externally-researched).
5. Fix the `albaha-regional-admin-org` typo in `nuwaira`.
6. Update `drive-999-docs` catalog: reclassify `999HRSD-all` as font-kit duplicate, remove "secondary 999 hub" claim.
7. Extend `lint.py:ROOTS` to include `raw/drive/`. Re-instate the 3 plain-path references in `999-albaha-qms-bcp.md` as wikilinks to `[[999-albaha-qms-bcp-ar]]`.

**Stop-condition:** lint 0, reconcile 0, all entity nodes have `source:`. Single commit.

### Phase F-2 — Quality-stack saturation (effort: ~75 min, 2 distillations)

**Goal:** complete the Basira evidence stack started by `999-albaha-qms-bcp`. Two highest-leverage neighbours.

- F-2.1: JSONL #2/#46 (مشروع الجودة 2024, 110+ files) → `wiki/sources/al-baha-quality-project-2024.md`. Folder enumeration via Drive MCP + selective deep reads of the top 5-10 files. Subagent dispatch.
- F-2.2: JSONL #5 (2025 KPIs) → `wiki/sources/mhrsd-2025-kpi-portfolio.md`. Smaller, single-pass. Includes تعميم 28597 + per-dept formulae.

**Reciprocal edges:** both wire into `999-albaha-qms-bcp`, `basira-leadership-compass`, `ahmad-2025-achievements`, `albaha-center-org`, `hrsd-work`. Update sources index 14 → 16.

**Stop-condition:** Both notes lint-clean, evidence stack named in `basira-leadership-compass` references all three QMS sources by id.

### Phase F-3 — Empowerment thesis + vocabulary (effort: ~90 min, 1 distillation + 1 concept)

**Goal:** capture Ahmad's intellectual signature in proper concept-and-source form. This is the load-bearing original-voice content.

- F-3.1: JSONL #7 (denser variant of #3) + #11 (التمكين المستقبلي) → `wiki/sources/empowerment-thesis-corpus.md`. If #7 turns out to be a snapshot of #3, fold the delta into `research-initiatives-portfolio` instead. Verify with explicit overlap-check before distilling.
- F-3.2: harvest the 3 vocabulary domains from §3.3 → `wiki/concepts/empowerment-vocabulary.md`. Single concept note, three sub-sections, provenance per phrase.

**Reciprocal edges:** thesis-corpus → `basira`, `999-disability-care-empowerment-strategy`, `social-handicap-compass`. Vocabulary note → `social-handicap-compass`, `999-disability-care-empowerment-strategy`, `basira`.

### Phase F-4 — Cross-cutting syntheses (effort: ~60 min, 2 syntheses)

**Goal:** consolidate evidence chains that are currently scattered across multiple folders into single coherent vault notes.

- F-4.1: Overtime court case → `wiki/synthesis/overtime-grievance-case.md`. Spans #19 (already distilled), #20, #39, #49, #14 (legal-principles ref), #56 (mixed evidence). Names: عادل الغامدي, طامي العلياني, علي القرني (as endorser of disputed schedule), Ahmad as plaintiff. **Sensitivity flag: this is litigation material; treat with the same governance rigour as Basira-decisions material — see ADR-0001 "decisions are permanent".**
- F-4.2: أمان مستدام national initiative → `wiki/projects/aman-mustadam-initiative.md` (project type, since it's an active Ahmad-authored initiative not just a synthesis). Spans #18 (final), #23 (Stitch), #42 (fragments), #3/#7 (ideation roots).

**Reciprocal edges:** F-4.1 → `ali-alqarni`, `employment-archive`, `hrsd-work`, `ahmad-career-arc`. F-4.2 → `social-handicap-compass`, `basira`, `999-disability-care-empowerment-strategy`.

### Phase F-5 — Original Tier-1 individual Gdocs (effort: ~120-180 min, 2-3 distillations)

**Goal:** finish the original Tier-1 priority list, now validated against this audit. Order matters — overlap-checks gate distillations.

- F-5.1: `1sgdawDigC4wn_...` (53 KB, Institutional Excellence + Innovation) → `wiki/sources/999-institutional-excellence-innovation.md`. Pairs with `999-albaha-qms-bcp`. Single-pass, main context.
- F-5.2: `1iC8AdwZ_...` (24 KB, إعادة بناء الرعاية) → **overlap-check first** vs `999-disability-care-empowerment-strategy`. If distinct ≥30%, distill as `wiki/sources/999-rebuilding-social-care.md`. If subsumed, skip with a memo entry in the master 999 note.
- F-5.3: `1z4GxUGv_...` (272 KB, Zero-Paper master) → subagent dispatch (>50 KB threshold). Distill as `wiki/sources/999-zero-paper-master.md`. This is **Basira's narrative source** — high stakes; allocate full session.

### Phase F-6 — Engineering substrate (effort: ~45 min)

**Goal:** capture Ahmad's pre-Basira engineering credentials so the Basira pitch has documented prior art.

- JSONL #56 + #59-#61 + #62 → `wiki/sources/ahmad-engineering-substrate.md`. Includes the Catering Mgmt System, Dictation App, Video Analyzer, prompt-engineering rubrics targeting MVVM/DDD/OWASP.

**Reciprocal edges:** → `basira`, `ahmad-career-arc`, `hrsd-work`.

### Phase F-7 — Infection control + safety (effort: ~45 min)

**Goal:** anchor the IC-trainer credential that's currently asserted in user CLAUDE.md but not in vault.

- JSONL #4 (مكافحة العدوى, 275+ files) → `wiki/sources/al-baha-ic-archive.md`. Light treatment — focus on (a) Ahmad's role as IC trainer + committee secretary, (b) BICSL-RC training, (c) the 2023 standards file already in `drive-catalog`.

**Reciprocal edges:** → `hrsd-work`, `albaha-center-org`, `ahmad-career-arc`.

### Phase F-8 — Misc backfill / opportunistic (effort: ~60-90 min)

**Goal:** the smaller items that don't justify their own phase but together close meaningful gaps.

- F-8.1: JSONL #37 (علي القرني folder) → `wiki/sources/alqarni-leadership-thesis.md`. The Ahmad-authored leadership thesis packaged FOR Al-Qarni, with proactive-empowerment vs reactive-care framing.
- F-8.2: JSONL #51 (نماذج تقييم المركز) → `wiki/sources/mhrsd-supervisory-visit-instruments.md`. Official supervisory-visit instruments + control→partnership thesis.
- F-8.3: JSONL #33 (سياسات المخاطر) → `wiki/sources/mhrsd-risk-excellence-policies-2025.md`. April 2025 ministerial risk/governance policies, anchors `mhrsd-leadership` to Ismail Al-Ghamdi by name.
- F-8.4: JSONL #44, #45, #55 → three small source notes (community-integration, training-development, beneficiary-rights). Each ~30 min. Group commit.

### Phase F-9 — PST integration (deferred per session decision)

Not in scope this audit. The PST archive already has 5 vault source notes (the four snapshots + the merged DB). Future audit will derive vault-creation targets from PST searchable-content.

## 5 — Anti-goals (explicit DO-NOT-distill list)

These exist as Drive content but **must not** become vault notes. Documenting here so future sessions don't re-evaluate them.

| Drive | Reason |
|---|---|
| **JSONL #6, #9, #17, #40, #41, #47** | Personal reading library + genealogy + Islamic history. No load-bearing relevance to Ahmad's named projects. |
| **JSONL #24** | Rajhi 59 SAR transfer receipt. Sediment. |
| **JSONL #27, #28** | 2013 sports league archive. Sediment. |
| **JSONL #32** | BYD car purchase 2025. Personal financial. |
| **JSONL #38** | Winter clothing invoice mechanics. Operational sediment. |
| **JSONL #57** | ⚠️ **Plaintext credentials.** Contains Ahmad's HRSD email password used uniformly across 7 services (`@\#As100020003000`). **Security incident.** Action item — rotate password + purge from Drive. **Do NOT vault.** |
| **JSONL #58** | Unrelated criminal case (Ghamdi drug-dealing defendants). Why is this in Ahmad's Drive? Open question — possibly misfiled. Do NOT vault. |
| **JSONL #59 (small variant)** | Subset of #61, redundant. |
| **JSONL #63** | Two unread PDFs (transaction #428539). Personal financial. |
| **JSONL #67** | iPhone receipt + 2020 contractor letter. Sediment. |
| **JSONL #48, #52, #64, #65, #66, #68** | Empty (or near-empty for #52 audio — see open question). |
| **`999HRSD-all` (`1emSX-om-05Brv3d8wYApzMqb4ocdlrHb`)** | Font-kit duplicate. Confirmed by 2026-04-25 MCP enumeration. Reclassify in `drive-999-docs` catalog. |
| **HRSD font-kit duplicates** in 4 other locations | Already in `999HRSD-all` and 4 sibling locations. One canonical reference is enough — none in vault. |

## 6 — Open questions / red flags

1. **JSONL #1 vs #36** ("علاج طبيعي - هوية الوزارة") — same content? Verify on F-3 entry before distilling.
2. **JSONL #2 vs #46** — confirmed similar; treat as one source.
3. **JSONL #3 vs #7** — both 37 files, #7 denser. Two snapshots OR distinct? Verify on F-3.1.
4. **JSONL #52** ("نموذج صوتي", 46 audio files Gemini cannot read) — possibly Habibi-TTS source recordings. Cross-check with `wiki/projects/habibi-tts.md` round inventory before treating as void.
5. **JSONL #57** plaintext credentials — security action item; not vault material.
6. **JSONL #58** unrelated drug case — clarify with Ahmad why these docs are in his Drive.
7. **R8+ Habibi-TTS round state** — already flagged in memory; could be related to #52.
8. **Folder ID resolution** — JSONL stores summaries by `idx`, not Drive fileId. For Drive-MCP enumeration we need a separate `idx → fileId` lookup. Build in F-1 alongside the catalog updates.
9. **Drive MCP query limitation** — document in `context_tools.md` per §2.5.
10. **268 KB and larger Gdocs** — main-context vs subagent threshold tuning. Current heuristic: >50 KB → subagent. Reconsider after F-5.3 (272 KB Zero-Paper master) — that's the test case.

## 7 — Decision log (audit-time choices)

These are explicit choices made by this audit. Record so future-Claude doesn't second-guess.

1. **Do not distill the master 999 doc neighbours blindly.** F-5 ordering forces overlap-check before distilling — three of the five Tier-1 docs likely overlap each other or the master.
2. **One concept note for vocabulary, not many.** Per kepano density rule + ADR-0001 "medium-density wiki pages, 500-2000 words". Three vocabulary domains in one node is denser than 10 fragment notes.
3. **Overtime case as a single synthesis note, not 6 separate sources.** The legal narrative is one story; scattering it across 6 source notes loses the thread.
4. **أمان مستدام as a project, not synthesis.** It's an active Ahmad-authored initiative with its own outputs, not just retrospective analysis.
5. **PST deferred.** PST has 5 source notes already; creating people-from-PST or events-from-PST is a separate audit pass once Drive ingestion stabilises.
6. **Anti-goals are durable.** Items in §5 don't get re-evaluated unless Ahmad explicitly redirects.
7. **Engineering substrate (F-6) before infection control (F-7).** Engineering credibility is the harder claim to evidence; IC is well-supported elsewhere (BICSL-RC certification, training records). Order by signal strength.
8. **F-1 is unconditionally first.** Backfilling source frontmatter on existing nodes is cheaper than creating new nodes that reference unanchored ones.

## 8 — Estimated total effort + session sizing

| Phase | Effort | Notes |
|---|---|---|
| F-1 | ~30 min | Backfill + lint scope + catalog correction. Single commit. |
| F-2 | ~75 min | 2 distillations. Subagent for #2/#46. |
| F-3 | ~90 min | 1 distillation + 1 concept. Verify #3 vs #7 overlap first. |
| F-4 | ~60 min | 2 syntheses. F-4.1 sensitivity flag. |
| F-5 | ~120-180 min | 2-3 distillations. F-5.3 own session. |
| F-6 | ~45 min | 1 distillation. |
| F-7 | ~45 min | 1 distillation, light. |
| F-8 | ~60-90 min | 4 small distillations. Group commit. |
| **Total** | **~9-12 hours** | Across **5-7 focused sessions**. |

**Suggested session boundaries:**

- **Session A** = F-1 + F-2 (~105 min) — one commit per phase
- **Session B** = F-3 (~90 min)
- **Session C** = F-4 (~60 min)
- **Session D** = F-5.1 + F-5.2 (~75 min)
- **Session E** = F-5.3 (~120 min) — Zero-Paper master, dedicated
- **Session F** = F-6 + F-7 (~90 min)
- **Session G** = F-8 (~75 min)

Re-audit after Session G or whenever Ahmad's project mix changes substantially (new projects, new Drive uploads, PST work resuming).

## 9 — Provenance

- **Vault audit**: 2026-04-25 subagent dispatch, frontmatter-only scan of 45 notes.
- **Drive folder digest**: 2026-04-25 subagent dispatch reading `~/ahmad-brain-import/drive-folders-gemini.jsonl` (558 KB, 68 entries).
- **999HRSD-all enumeration**: 2026-04-25 subagent dispatch via Drive MCP — confirmed 19 fonts, 0 docs.
- **Cross-walk + plan**: synthesised in main context 2026-04-25.
- **Re-run trigger**: substantial Drive uploads, project pivot, or after completing Phases F-1 → F-8.
