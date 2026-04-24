---
id: three-tracks
title: Ahmad's Three Parallel Tracks (+ Historical Track 0)
type: synthesis
status: active
aliases:
  - three-tracks
  - portfolio-tracks
  - ahmad-portfolio
  - integrated-systems-tracks
tags:
  - synthesis
  - portfolio
  - framing
  - career
  - integrated-systems
created: 2026-04-24
updated: 2026-04-24
related:
  - "[[basira]]"
  - "[[habibi-tts]]"
  - "[[hrsd-work]]"
  - "[[ahmad-brain-foundation]]"
  - "[[ahmad-career-arc]]"
  - "[[pt-modeling]]"
  - "[[social-handicap-compass]]"
summary: >-
  Ahmad's forward-facing work portfolio — three parallel tracks (Basira · AI
  models on H100 · Know-Ahmad / ahmad-brain) anchored in one unifying role:
  "integrated systems engineer for Saudi rehabilitation centres." Sits on a
  historical Track 0 of HRSD central-operations insider activity. Distinct
  from the ministry-assignment register (where pt-modeling lives). Five
  immutable principles govern all three. Framed against a four-layer
  integrated-systems model spanning hardware to intelligence.
---

# Ahmad's Three Parallel Tracks

## The unifying role

Ahmad frames himself as *"مهندس نظم متكاملة (Hardware + Software) لخدمة ذوي الإعاقة في مراكز التأهيل الشامل"* — an integrated-systems engineer (hardware + software) serving persons with disabilities in Saudi comprehensive rehabilitation centres. The three tracks below are not separate hobbies. They are facets of one long mission anchored in that role.

This framing matters because it determines how every deliverable is positioned. A proposal that reads as "Ahmad built an app" fails the frame. A proposal that reads as "an integrated-systems engineer is scaling validated institutional excellence to 36 centres via digital, intelligence, and knowledge layers" passes it.

## Track 0 — HRSD central operations (historical, 2023-10 → 2026-03)

Before and beneath the three forward-facing tracks, Ahmad is an active HRSD insider. Confirmed via PST backup analysis on 2026-04-21 (see [[pst-mailbox-hrsd]]):

- On the ministry-wide `مركز التواصل` distribution list — received invitations to meet ~16+ deputy ministers (وكلاء) across strategic affairs, human capital, social development, labour, rehabilitation, digital transformation, and the rest of the portfolio.
- Attended workshops on rehabilitation, elderly daycare, the social-monitor logbook, infection control, PT services, patient-escort training, and medical supplies in social-care homes.
- Exposure to institutional-excellence work (جائزة التميز المؤسسي), KPI documentation, annual operational plans, and risk maps.
- Regional attachment through the `التواصل الداخلي بمنطقة الباحة` distribution list.

This HQ-level context is why Ahmad speaks fluent HRSD process vocabulary (IQMS, PDCA, 36-centre modelling) and can frame initiatives in the language that deputy-minister offices already use. Track 0 is what makes Tracks 1–3 landable inside the ministry. See [[hrsd-work]] for the full institutional context and workshops catalogue.

## Track 1 — Basira (بصيرة)

- **Location:** `C:\dev\basira\` (flattened 2026-04-16 from a double-nested path).
- **What it is:** beneficiary-management and digital-transformation system for MHRSD comprehensive rehabilitation centres. Vite 6 + React + TypeScript, v2 branch, port 5175, ~66 kLoC.
- **Phase:** polish and possible dual AI-engine fusion → rebuild to <40 kLoC before final release. Decision pending.
- **Skill:** `basira-dev` (runs the dev server safely per the canonical-path rule).
- **Full hub:** [[basira]]. Facet notes: [[basira-leadership-compass]] and [[basira-sovereign-decks]].

Basira is the most externally-visible of the three tracks and the one that carries the forbidden-trinity (no budget, no staff, no one's time) moral floor.

## Track 2 — AI models (H100)

- **Location:** not yet located under `C:\dev\`.
- **What it is:** training AI models on H100-class hardware. Specific scope not yet shared by Ahmad.
- **Phase:** unknown.
- **Skill:** none yet.

Track 2 is deliberately under-specified in the vault because Ahmad has not yet surfaced the project. It is recorded here so future Claude does not confuse it with [[habibi-tts]].

**Important distinction — Habibi-TTS is not Track 2.** [[habibi-tts]] is Ahmad's F5-TTS Saudi Arabic voice model trained on Modal A100 — a personal project on commodity cloud compute. The "AI models on H100" track described in the 2026-04-21 memory is a separate, larger, as-yet-undocumented effort. Treat them as distinct until Ahmad says otherwise. If Ahmad later unifies them, update this note and add a `supersedes` ADR.

## Track 3 — Know-Ahmad / ahmad-brain

- **Location:** `C:\dev\ahmad-brain\` — the vault this synthesis note lives in.
- **What it is:** personalisation + knowledge base for Claude about Ahmad (personal) and his decade-plus of rehabilitation documentation (professional).
- **Framework:** Personalisation Maturity Model — currently Level 1 (Static) per the 2026-04-21 memory; target is Level 3 (Context-aware).
- **Architectural intent (pre-ADR-0001):** hybrid SQLite FTS5 (lexical Arabic) + Supabase pgvector (semantic), based on the proven pattern from the `bareed` repo.
- **Source-of-truth for docs:** Google Drive, 2020+ only; anything older is reference, not template.
- **Full hub:** [[ahmad-brain-foundation]]. Architectural decisions: [[0001-vault-architecture]] (LLM-only Karpathy-wiki layout) + [[0002-language-policy-and-sources-folder]] (English prose + Arabic as data + `wiki/sources/`).

Note that the Level 1 → Level 3 maturity target predates the 2026-04-24 architectural refactor. The current vault (LLM-only, English + markdown, MADR decisions) is a different architectural target; the maturity-model framing can be retired or re-anchored to the new structure in a future note.

## Cross-cutting frame — four-layer integrated-systems model

All three tracks map onto the same four layers:

| # | Layer | Scope | Medium |
|---|---|---|---|
| 1 | Beneficiary | assistive tech, monitoring | hardware |
| 2 | Facility & service | clinical + operational systems | software |
| 3 | Governance | quality, risk, compliance | policy + process |
| 4 | Intelligence | ML, GenAI, knowledge base | data + models |

The four-layer model is what earns Ahmad the "integrated-systems engineer" label — he can move vertically across all four, rather than specialising in one. Basira lives primarily at layers 2 + 3; the H100 track lives at layer 4; ahmad-brain is a layer-4 instrument for Ahmad's own productivity; Track 0 is layers 2 + 3 in the ministry's existing vocabulary. Full framing in [[ahmad-brain-foundation]].

## Immutable principles (stated by Ahmad)

Five rules that apply to every track:

1. **Beneficiary dignity first.** Technology serves it; dignity never serves technology.
2. **Sustainability beats innovation.** Five years running unattended wins over a dazzling-but-fragile release.
3. **Saudi government standard from 2020 onward only.** Pre-2020 documentation is reference material, not a template for new work.
4. **Do not rebuild what MHRSD or Google already solve.** Integrate. (This is the rule that makes [[basira]]'s NCA-alignment posture coherent — Basira meets existing policies rather than inventing parallel ones.)
5. **Hardware and software are co-designed, never patched separately.** The integrated-systems label fails the moment hardware and software are developed in isolation.

## What is not a track

The three tracks + Track 0 are Ahmad's **portfolio framing**. They are distinct from:

- **Ministry-assigned deliverables** — e.g. [[pt-modeling]], where Ahmad is producing a governmental operational manual for 36 centres. The PT manual is a formal MHRSD assignment on a different register (governmental Arabic, SOP format) and does not belong in any of the three tracks. Keeping the two categories separate is the rule that stops PT-modelling language from leaking into Basira pitches and vice versa.
- **Cross-cutting assignments** — the six formal assignments in [[ahmad-formal-assignments]] (Quality, Strategic Partnerships, CSR, Home Healthcare, PwD, Non-Gov Rehab Committee). Those are horizontal mandates inside HRSD, not forward-facing project tracks.
- **Recognitions and achievements** — [[ahmad-2025-achievements]], [[ahmad-career-arc]]. Those are evidence, not tracks.

## Retrieval rules

- When Ahmad says *"the three tracks"* or *"my projects"*, default to Basira + AI-models-H100 + ahmad-brain. Track 0 is invoked only when context is institutional-historical.
- When a new project appears, first ask which track it belongs to; if it belongs to none, check whether it is a ministry assignment or a cross-cutting mandate (different category) before forcing a fit.
- When a pitch or proposal is being drafted, open with the unifying role statement, not with a track name — the role is load-bearing; the tracks are instances of it.

## Gaps

- H100 AI-models track — specifics.
- Relation (if any) between H100 track and [[habibi-tts]] — to be clarified when Ahmad surfaces details.
- Re-anchoring of the Level 1 → Level 3 maturity-model framing against the post-2026-04-24 vault architecture.

## Provenance

Synthesis note built 2026-04-24 from memory file `project_ahmad_three_tracks.md` (captured 2026-04-21, 3 days old at migration time). Phase D migration task from [[log-2026-04-24]]; upstream memory file retained as a one-line pointer.
