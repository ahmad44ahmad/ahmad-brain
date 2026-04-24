---
type: meta
status: active
track: personal
lang: en
created: 2026-04-24
updated: 2026-04-24
tags: [master-index, entity-registry]
---

# Master Entity Index

Canonical list of every named entity in this vault. Regenerate when adding/removing entities. Grep this file to check if an entity already exists before creating a new one.

## People (`50-People/`)

| File | Entity | Role (short) | Track |
|---|---|---|---|
| `ali-alqarni` | Ali Awad Al-Qarni (علي عوض القرني) | Former Al-Baha center manager | hrsd |
| `hamed-alruwaili` | Hamed Al-Ruwaili (حامد الرويلي) | HRSD HR-in-Regions forum lead | hrsd |
| `ismail-alghamdi` | Ismail Al-Ghamdi (إسماعيل الغامدي) | Assistant Minister Shared Services, Basira patron | hrsd |
| `khalid-alzahrani` | Khalid bin Saleh Al-Zahrani (خالد بن صالح الزهراني / أبو فيصل) | Al-Baha Regional GM + Dev Sector Assistant | hrsd |
| `khalid-mutr` | Khalid Mutr (خالد مطر) | NEW Al-Baha center director (2026-04) | hrsd |
| `nasser-alqahtani` | Dr. Nasser Al-Qahtani (د. ناصر القحطاني) | Current وكيل التأهيل والتوجيه الاجتماعي | hrsd |
| `nuwaira` | Nuwaira / Umm Abdulmalik (نوير / أم عبدالملك) | مديرة الإشراف الاجتماعي Al-Baha regional | hrsd |

## Projects (`10-Projects/`)

| Path | Project | Status |
|---|---|---|
| `10-Projects/basira/` | Basira (بصيرة) digital transformation system | active |
| `10-Projects/habibi-tts/` | Habibi-TTS (F5-TTS Saudi Arabic) | active |
| `10-Projects/pt-modeling/` | PT services modeling (36 MHRSD centers) | active |
| `10-Projects/hrsd-work/` | HRSD supervisor duties (Al-Baha PT supervision) | active |

## Areas (`20-Areas/`)

| Path | Domain | Status |
|---|---|---|
| `20-Areas/career/` | Career arc, nominations, achievements timeline | active |
| `20-Areas/pt-practice/` | PT clinical practice (credential-level) | active |
| `20-Areas/quality-excellence/` | Quality + institutional-excellence supervisor | active |
| `20-Areas/personal/` | Personal / non-work | active |
| `20-Areas/personal/ahmad-brain-foundation/` | Ahmad-brain thinking-system foundation docs | active |

## External sources (`30-Resources/`)

| File | Purpose |
|---|---|
| `30-Resources/drive-catalog.md` | Index of Ahmad's Google Drive (admin@albahah.app) |
| `30-Resources/999-docs-catalog.md` | High-density "999"-prefixed research archive (70-100+ docs) |
| `30-Resources/ai-models/PROMPT-FORGE.md` | Prompt-engineering intake template |

## Career + HRSD anchors

| File | Purpose |
|---|---|
| `20-Areas/career/formal-assignments.md` | Ahmad's 6 formal ministry assignments (Quality, Strategic Partnerships, CSR, Home Healthcare, Disability, Non-gov Rehab Committee) |
| `20-Areas/career/ministry-era-timeline.md` | Ministry evolution MOSA → MLSD → HRSD + Majid Al-Qasabi inflection |
| `20-Areas/career/employment-archive.md` | **Priority-1 Drive folder** — career archive 26 files: admin-court overtime case, civil-service regs, Power Platform achievements |
| `20-Areas/career/research-initiatives-portfolio.md` | **Priority-3 Drive folder** — 37 files: أمان مستدام (6.26M SAR), مبادرة تمكين, رضا المستفيدين, الإحسان قبل المعيار. Also = 999-docs hub. |
| `10-Projects/hrsd-work/sources/pst-analysis-2026-04-21.md` | PST mailbox analysis — 2,172 inbox + 606 contacts + themes |
| `10-Projects/hrsd-work/sources/sent-mbox-analysis-2026-04-24.md` | Sent mailbox analysis — 51 unique messages 2025-03→2026-02, confirmed emails, thematic clusters |
| `10-Projects/hrsd-work/sources/center-policies-digest.md` | **Priority-2 Drive folder** — 24 files: nurse/psych/speech/PT/dental department modeling, admission forms 2024, org chart |
| `30-Resources/drive-folders-master-index.md` | Master index of 68 Drive folders (Gemini-summarized) — retrieval map |

## Meta (`90-Meta/`)

| File | Purpose |
|---|---|
| `90-Meta/CLAUDE.md` | Vault operating manual (LLM-first) |
| `90-Meta/rules.md` | Capture/review/never rules |
| `90-Meta/queries.md` | Reusable Dataview queries |
| `90-Meta/index.md` | This file |
| `90-Meta/templates/` | Project/person/daily/decision templates |

## Maintenance

- When adding an entity: append a row here.
- When archiving: move row to a "Archived" section below and set `status: archived` in the file's frontmatter.
- When two notes describe the same entity: merge, then update this index + `supersedes:` field.
