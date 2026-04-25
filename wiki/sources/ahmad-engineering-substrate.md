---
id: ahmad-engineering-substrate
title: "Ahmad's Engineering Substrate — Pre-Basira Digital-Transformation Track Record"
type: source
status: active
aliases:
  - engineering-substrate
  - pre-basira-engineering
  - ahmad-appsheet-portfolio
  - ahmad-prompt-rubrics
  - prior-art
tags:
  - engineering
  - digital-transformation
  - appsheet
  - gemini
  - prompt-engineering
  - basira-prior-art
  - drive-source
created: 2026-04-25
updated: 2026-04-25
valid_from: 2024-01-01
learned_at: 2026-04-25
confidence: medium
source: drive-folder-jsonl:#56+#59+#60+#61+#62
related:
  - "[[basira]]"
  - "[[ahmad-career-arc]]"
  - "[[ahmad-2025-achievements]]"
  - "[[hrsd-work]]"
  - "[[albaha-center-org]]"
  - "[[three-tracks]]"
  - "[[overtime-grievance-case]]"
  - "[[drive-folders-master-index]]"
  - "[[drive-vault-coverage-audit]]"
summary: >-
  English distillation of Ahmad's pre-Basira engineering credentials —
  AppSheet apps in production (Catering Mgmt System, Tamkeen Vision 2030
  copy), Google AI Studio applet portfolio (Dictation App, Video Analyzer,
  Gemini Co-Drawing), self-taught Python+VS Code track, and the prompt-
  engineering rubric library targeting MVVM/DDD/Hexagonal architectures with
  OWASP/CI-CD/Core-Web-Vitals discipline. Anchors the prior-art evidence the
  Basira pitch leans on, alongside flags for grievance-folder mixing and
  out-of-scope agricultural feasibility content surfaced from the same Drive
  folders.
---

# Ahmad's Engineering Substrate

## What this source is

Five Drive folders catalogued in `~/ahmad-brain-import/drive-folders-gemini.jsonl` documenting Ahmad's engineering activity in the **two years before [[basira]] reached its v2 codebase**:

| JSONL # | Folder | Size | Slot |
|---|---|---|---|
| #56 | `appsheet` | 20 files | AppSheet platform usage + (mixed) admin-grievance dossier |
| #59 | `Google AI Studio` (small) | 2 files | Gemini model-version archive — strict subset of #61 |
| #60 | `Google AI Studio` (medium) | 70+ files | Gemini API setup + Python learning plan + applets + system info + IC training |
| #61 | `Google AI Studio` (largest) | 250+ files | Internal HRSD applets + AI testing + Sarat Blossoms feasibility study (out-of-scope) |
| #62 | `prompts أوامر تلقين` | 5 files | Advanced prompt-engineering rubric library |

**Authorship:** Ahmad-authored / Ahmad-curated. Unlike F-5.1 and F-5.3, this is not a Gemini-narrated synthesis but a working-evidence folder (apps, code, prompts, system reports). The Gemini summaries used here are *folder-listings*, not authored content; the underlying artefacts are Ahmad's.

**Position in the stack.** This note **does not** document Basira itself — Basira lives at [[basira]] with its own technical state. What this note does is provide the **prior-art audit trail**: documented engineering activity *before* Basira's v2 codebase, evidence that the engineering depth Basira draws on was earned over years of practice rather than emerging fully-formed at one point.

## AppSheet apps in production

[[ahmad-2025-achievements]] item #3 — *تحويل حوكمة الإعاشة إلى تطبيق* (digitising food-service governance, 2025-02-11 → 2025-09-09) — is a **production AppSheet deployment**. JSONL #61 confirms the application's name and scope:

> **«نظام إدارة خدمات الإعاشة والمستفيدين»** (Catering Management System) — *a core application based on HRSD's catering governance guide.*

This is the most institutionally-anchored item in the substrate. Approved by [[ali-alqarni]] on 2025-11-25 as a 5★ achievement, registered in the MHRSD performance system, and deployed at مركز التأهيل الشامل بالباحة. **Documentary status before Basira's pitch arc started.**

Other applets in the access history:

- **«Copy of Tamkeen Vision 2030»** — strategic empowerment app. The "Copy of" prefix indicates it's a copy of an external initiative-template, not Ahmad-authored from scratch. Verify whether the deployed instance was customised or kept as imported.
- **Dictation App** — Gemini-powered audio→transcript pipeline used for meetings/audits. Pre-figures the workflow that now sits inside the [[habibi-tts]] training pipeline (different model, different direction, but same problem framing).
- **Video Analyzer** — Gemini-powered video summarisation + text extraction.
- **Gemini Co-Drawing** — collaborative AI illustration. Less load-bearing; recreational.

**JSONL #60 + #61 also document:**

- **Gemini API integration** — concrete API key + client-bootstrap code in Python and Bash (export `GOOGLE_API_KEY`, `client = genai.Client(...)`). Files #182, #183 of the source folder.
- **System info reports** — HUAWEI laptop, **Intel Core Ultra 9 185H**, **32 GB RAM**, two snapshots (2025-02-17 / 2025-05-08). Capable development hardware, removes the "amateur on a low-spec machine" objection if it ever arose.
- **4-week Python + VS Code learning plan** (file #189) — beginner-level, organised by week. Documents the *learning curve* Ahmad followed, not present-state competence. Worth flagging as historical artefact rather than current credential.

## Prompt-engineering rubric library (JSONL #62)

A library of 5 prompt-engineering rubrics targeting **mid-to-advanced web application generation via LLMs**. Explicit positioning: *targeting developers at diploma-level and above, not beginners.* Goal: helping Gemini understand the architecture/performance/security depth required by professional environments.

**Architecture vocabulary the rubrics demand from the model:**

| Layer | Standards invoked |
|---|---|
| Architecture patterns | **MVVM, Hexagonal, Domain-Driven Design (DDD)** |
| Build tooling | Webpack, **Vite**, Parcel; Module Federation; CI/CD; lazy loading; code splitting |
| Security | **OWASP Top 10**, OWASP Web Security Standards, CSP (Content Security Policy), penetration testing, end-to-end encryption |
| Performance | HTTP/3, Resource Hints, Preloading, **Core Web Vitals**, Web Workers |
| Frontend | TypeScript, Virtual DOM, ARIA Live Regions, Animation API + Physics-based Animations, Design Systems, i18n with **RTL/LTR support**, WebGL/Three.js/WebGPU |
| Testing | Unit / Integration / E2E (Jest, Vitest); Mocking + Stubbing |
| Backend | JAMstack (Next.js / Nuxt.js), **Micro-frontend, Micro-services, Docker, Kubernetes**, GraphQL+Apollo, SSR/SSG, WebAssembly, A/B testing + Feature Flags, Event-Driven Architecture (Redis/Kafka), CQRS, Redux Toolkit/MobX |
| Auth | OAuth 2.0 + JWT |

**The 5 rubrics generate prompts for:**

1. Educational presentation (TS, MVC/MVVM, PWA, WebGL/Three.js, RTL/LTR i18n)
2. Industry-grade product showcase (JAMstack, Micro-frontend, GraphQL, SSR/SSG, WebAssembly)
3. Data-analytics platform (Micro-services, Docker, Kubernetes, D3.js, WebGL/WebGPU, OWASP)
4. Events / conference platform (OAuth+JWT, WebRTC, Event-Driven Architecture, E2E encryption, OWASP Top 10)
5. Project-management system (DDD, Redux Toolkit/MobX, CQRS, Gantt-Charts via Web Components, DevOps + CI/CD)

**Cross-walk with [[basira]]'s actual stack.** Basira v2 uses Vite 6 (build-tool match), TypeScript-with-React (frontend match), and the 11-document compliance packet maps to NCA ECC-2:2024 + CSCC-1:2019 — a Saudi-regulatory analogue of the OWASP-class rigour these rubrics demand. The rubrics show Ahmad **knew what professional-grade looked like** before he started building Basira, which is the rhetorical anchor for "this isn't an amateur side project."

## Cross-references to Basira evidence

For Basira's pitch arc, the engineering substrate provides three load-bearing claims:

1. **"Ahmad ships, not just plans"** — the Catering Management System is in production at the center, registered in the MHRSD performance system, approved by Al-Qarni. AppSheet shipping pre-dates Basira's pitch arc by 2+ years.
2. **"Ahmad knows what professional-grade looks like"** — the prompt-engineering library targets DDD / OWASP / Core Web Vitals discipline. Not amateur vocabulary.
3. **"Ahmad's hardware + AI substrate is real"** — Core Ultra 9 + 32 GB RAM + Gemini API + applet portfolio. Not a "PowerPoint engineer."

Pair these three claims with [[basira]]'s seven-pillar evidence stack when senior-leadership audiences ask *"who is this person and why should we trust the codebase?"*

## What is NOT engineering substrate (out-of-scope material in same folders)

Two clusters of mixed content live in the same folders and **must not be folded into this note's evidence claims**:

### Admin-grievance overlap (JSONL #56)

JSONL #56's folder bundles legal/admin-grievance documents — *"استعمال السلطة الإدارية والتعسف"*, *"اللائحة التنفيذية لنظام الخدمة المدنية"*, *"عدم الاختصاص الجسيم"*, references to *ديوان المظالم* and *نزاهة* — alongside the AppSheet artefacts. **Do not double-count this content with [[overtime-grievance-case]]** (F-4.1), which already canonicalises the legal arc with verbatim source attribution. The folder co-mingling reflects how Ahmad organises his Drive (operational-by-folder rather than by-domain), not a content overlap that needs vault-side reconciliation.

### Sarat Blossoms feasibility study (JSONL #61)

JSONL #61 contains a complete economic feasibility study for *«أزهار السراة للمنتجات العطرية»* (Sarat Blossoms for Aromatic Products) — a 1,000 m² lavender + rosemary cultivation project in Baljurashi, prepared for **Saleh Ahmed Al-Ghamdi** (a citizen, not an Ahmad project), aligned with the Reef Program + Vision 2030. SAR 54,000 total investment, 79.6% margin by Year 3, 12-month implementation plan.

**This is out-of-scope for the engineering substrate.** It looks like Ahmad-as-consultant work for a third party (likely a relative or community member named Al-Ghamdi), prepared via Gemini-assisted authoring. The mere presence in the AI-Studio folder reflects that Ahmad uses Gemini as a general-purpose authoring tool, not that the feasibility study is part of his engineering portfolio. **Do not link this from [[basira]] or [[ahmad-career-arc]] as engineering evidence.** Could plausibly warrant its own future note under `wiki/sources/` if Ahmad asks; for now, recorded here as scoped-out flag.

### Other co-mingled material in #60

Three documents in #60 are clearly out-of-scope for the engineering substrate but on-scope for other vault notes:

- **BICSL-RC infection-control trainer manual** — covered by Phase F-7's planned `al-baha-ic-archive` (note not yet authored; will resolve as a wikilink after F-7).
- **Center org chart** — anchors [[albaha-center-org]] (already authored, F-1).
- **Supervisory-visits governance manual** — anchors a future Phase F-8 note `mhrsd-supervisory-visit-instruments` from audit §F-8.2 (not yet authored; will resolve as a wikilink after F-8).

These three should each migrate to their proper home rather than being treated as engineering evidence.

## Honest flagging

1. **Mixed Drive folders.** All five JSONL entries describe folders with operational-by-folder organisation. Do not infer that everything in folder *X* belongs to vault topic *Y* — verify file-by-file when claims are load-bearing.
2. **JSONL #59 ⊂ #61.** Don't double-count the Gemini-version archive when citing model-testing activity.
3. **"Copy of Tamkeen Vision 2030"** — verify whether Ahmad customised it or kept the imported template. Affects whether it counts as Ahmad-authored output.
4. **Beginner Python plan** is a learning-curve artefact, not a current-competence claim. The current state is what's in `C:\dev\basira` (66k lines TS/TSX), not what was in a 4-week beginner plan.
5. **API key in plaintext.** JSONL #60 file #182 documents an *AIzaSyC...* Google API key. **Operational security action item** — rotate that key if still active. Not vault material; flagging here for follow-up.
6. **Saleh Al-Ghamdi feasibility study** is third-party consulting work, not Ahmad's institutional output. Don't conflate.
7. **No timestamps on most artefacts.** The Gemini-folder summaries don't preserve creation dates for individual files. Treat this note as a *catalog* of substrate, not a chronology — when chronology matters, route to [[ahmad-career-arc]] or PST evidence.

## Open questions

1. **AppSheet app inventory completeness.** JSONL #61 names three applets (Catering, Tamkeen, Dictation) plus implies "several internal applications." Are there more? Particularly any additional production deployments at the center beyond the Catering MGMT system? Verify with Ahmad.
2. **Tamkeen Vision 2030 customisation.** Pure import or modified instance?
3. **API key rotation status.** Plaintext key in Drive — still active? Operational action item.

## Provenance

- **Source:** JSONL #56 (`appsheet`) + #59 (`Google AI Studio` 2-file) + #60 (`Google AI Studio` 70+ files) + #61 (`Google AI Studio` 250+ files) + #62 (`prompts أوامر تلقين`) in `~/ahmad-brain-import/drive-folders-gemini.jsonl`.
- **Method:** Phase F-6 of [[drive-vault-coverage-audit]]. Direct main-context distillation (no >50 kB threshold trigger; total summary text ~20 kB).
- **Authority:** the Gemini summaries describe folder *contents*, not Gemini-authored claims about Ahmad. The underlying artefacts (applets, prompts, code) are Ahmad's working output.
- **Re-run trigger:** when Ahmad ships a new AppSheet app or extends the prompt-rubric library, append rather than re-derive.
