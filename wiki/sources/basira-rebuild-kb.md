---
id: basira-rebuild-kb
title: "Basira V4 Rebuild Knowledge Base (Desktop) — the pull-don't-invent corpus"
type: source
status: active
aliases:
  - Basira-REBUILD
  - rebuild-kb
tags:
  - basira
  - basira-v4
  - rebuild
  - knowledge-base
  - source
created: 2026-06-04
updated: 2026-06-04
source: local-fs:C:\Users\aass1\Desktop\Basira-REBUILD\
summary: >-
  The single citable pointer from the vault to the Basira V4 rebuild knowledge
  base on Ahmad's Desktop — a 4-doc synthesis set (00-03 + 05) over ~30 harvest
  extracts (01-14) distilling the three old codebases, their live DBs, the
  vision/compass, HRSD design, the evolution/anti-patterns, the Drive corpus, and
  the ministry theoretical foundations. English, AI-facing, read-only. The vault
  POINTS here; this corpus HOLDS the row-level detail.
related:
  - "[[basira-v4-rebuild]]"
  - "[[basira-demo-vs-real-data]]"
  - "[[drive-catalog]]"
---

# Basira V4 Rebuild Knowledge Base (Desktop)

This note is the vault's **single citable pointer** to the Basira V4 rebuild knowledge base at
`C:\Users\aass1\Desktop\Basira-REBUILD\`. The KB is the "pull-don't-invent" corpus that fed the V4 cluster
([[basira-v4-rebuild]] and its facets); it is **English, AI-facing, and read-only** — never written from the
vault. The vault POINTS to this corpus and distils its conclusions; the row-level detail (field dumps, exact
form codes, KPI tables, code anchors) lives in the KB files this note names. When a V4 note cites
`(KB: harvest/NN §X)`, the target is here.

## The synthesis set (the map layer)

Read in this order for a cold start: **`02` (why) → `01` (what) → `03` (what's missing) → `00` (where it is).**

- **`00-MASTER-SOURCE-INVENTORY.md`** — the map of everything: the harvest extracts, the deep-analysis corpus, the three repos, the live DBs, the Drive reference, and the vault/memory.
- **`01-REQUIREMENTS-LEDGER.md`** — the traceable pull-don't-invent ledger (§A KNOW-the-human · §B cross-service triggers · §C engines real-vs-aspirational · §D governance · §E KPIs · §F medication safety · §G empowerment/rights · §H theoretical foundations · §I the 62-file corpus · §J corpus batch-2), every item barrier-tagged and marked REAL/DEMO/ABSENT.
- **`02-WHY-AND-ANTIPATTERNS.md`** — the authoritative "why": the compass, the V1→V4 evolution, the **settled security model** (every other doc points here for it), and the 11 named failure modes. The source of record for ADR [[0003-basira-v4-architecture]]'s context.
- **`03-GAPS-AND-DATA-ASK.md`** — what the harvest could not confirm without live access, plus the precise DB/Drive credentials and the ETL plan. Carries the S85 gap-fill update (org structure + disability table filled).
- **`05-MINISTRY-CONTEXT-AND-DECISIONS-S84.md`** — Ahmad's S84 ground-truth decisions: the مشاركة-submission stage, data residency (ministry's post-approval call), the demo-data model, the role list + delegation, and the single anti-stigma infectious-disease rule.

## The harvest extracts (the detail layer)

Under `harvest/`. The synthesis docs cite these as `NN §X`. **These ARE the deliverable; the synthesis only points.**

- **`01`-`03`** — the three codebases (V1 clean-backup · V2 pitch line · V3 active line): forms-persistence ledgers, the real-vs-aspirational engines, the anti-pattern catalogues.
- **`04`** vision/compass · **`05`** HRSD design system · **`06`/`10`** skills + from-scratch best-practices (DDD/hexagonal/persistence-by-construction; the strangler-vs-clean-rebuild evidence).
- **`07`** the evolution chronology + the settled security model + the failure modes · **`08`/`08b`** per-version data inventory + the live-DB pull findings (one real roster on one Supabase, schema diverged from every repo SQL).
- **`09`** the Drive read (Basira-as-Center-Operating-System manual + the بصيرة الإعاشة nutrition model = the kitchen half of dental→soft-diet) · **`11`** the 24 theoretical-foundations docs + 5-yr KPI history.
- **`12-a`...`12-h`** the 62-file ministry/center corpus (operations · quality/QMS · IPC · catering · org/forms/emergency · beneficiary-voice · platform) — synthesised in `12-CORPUS-SYNTHESIS.md`.
- **`13-a`...`13-e`** corpus batch-2 (the medical-gateway WHY · pitch narrative · the richest NOT-ADOPTED haul) — synthesised in `13-CORPUS-BATCH2-SYNTHESIS.md`.
- **`14-a`...`14-g` + `14-org`** (Track A, 2026-06-04) — the latest deep reads: `14-a` the CRPD de-institutionalisation guide (the §5 discharge-routing taxonomy + the طي القيد discharge-interlock); `14-b` the "999" national critique + 8-axis development roadmap; `14-c` the official KPI/quality-standards register + **real Al-Baha actuals** (73 staff, 2 beneficiaries employed) + the remote-partnership gap-strategy; `14-d` the ISO-9001 clause↔process↔KPI mapping; `14-e` the social-activities module form-set; `14-f` the beneficiary rights charter + the restraint-elimination PROTECT pillar; `14-g` the EHS/DR coded medical-forms manual (the admission intervention-dispatch matrix — the cleanest one-KNOW-event→N-SERVE pattern in the corpus); `14-org` the center org structure + the 6-group disability-classification table.

## Live data + Drive

The KB's data findings are distilled in [[basira-demo-vs-real-data]] (the one real roster, V3-prod-is-demo, the PDPL exposure, the mandatory `prisma db pull`). The Google Drive reference (owner `admin@albahah.app`, "almost everything is here") and its read-queue are catalogued in [[drive-catalog]].

## Honesty + anti-drift (one line)

The corpus enforces "pull, don't invent" and "honesty over green": it logs what is REAL vs DEMO vs ABSENT, and it keeps a NOT-ADOPTED register (radar/LiDAR sensors, an IHSAN-Score engine, wearables, affect-AI, Digital-Twin simulation, SROI/SIB finance, سري self-classification) so refused ideas cannot re-enter as "future features."
