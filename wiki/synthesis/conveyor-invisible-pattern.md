---
id: conveyor-invisible-pattern
title: "Conveyor-Invisible Pattern — Specced-but-Unrowed (and Rowed-but-Unsequenced) Gets Silently Skipped"
type: synthesis
status: active
aliases:
  - conveyor-invisible
  - specced-but-no-row
  - rowed-but-unsequenced
  - reconcile-into-the-ledger
tags:
  - synthesis
  - method
  - build-discipline
  - anti-drift
  - basira-v4
created: 2026-06-16
updated: 2026-06-16
learned_at: 2026-06-16
confidence: high
source: local:C:\dev\basira-v4\docs\PLAN-v4-R3.md
summary: >-
  In a ledger-driven build a capability is built only if it is a row, and
  reached only if its row has a slot in the ordered sequence — so
  specced-but-unrowed and rowed-but-unsequenced items get silently skipped, and
  the failure recurs self-similarly across layers (spec→row→sequence). The fix
  (reconcile-into-the-ledger): mint a row for everything including conscious
  drops, give the order a complete topological tail, encode the DAG. The
  build-side cousin of architecture-first retrieval.
related:
  - "[[architecture-first-knowledge-retrieval]]"
  - "[[basira-v4-requirements-ledger]]"
  - "[[basira-v4-rebuild]]"
  - "[[prompt-forge]]"
---

# Conveyor-Invisible Pattern

## The pattern

In a ledger-driven build (a gap-ledger of `G-###` capability rows worked through an ordered sequence), a capability is built **only if it is a row**, and reached **only if its row has a slot in the ordered build sequence**. That creates two silent-skip failure modes — the capability is real and specced, but the conveyor never carries it to the build:

1. **Specced-but-no-row.** A capability described in the source corpus or a spec, but never minted as a ledger row. The conveyor never sees it. *(V4 instance: the "I23 vocational chain" named in the harvest never survived as any G-row — see [[two-doors-empowerment-model]].)*
2. **Rowed-but-unsequenced.** A row that exists (has a batch home) but is absent from the ordered build sequence the session actually walks. A build following the order literally **never reaches it**. *(V4 instance: `G-047`/`G-049`/`G-050` were minted into the Batch-4 cell-blob but listed in NEITHER explicit build order. Worst stranded: `G-049` case-shifting — the population-level de-dilution that operationalizes «close the custodial center», the literal North Star, invisible to a build that walks the §0 order.)*

The failure is silent because nothing errors — a missing row or a missing slot simply produces no work, and the gap reads as "covered" because every *listed* item got done.

## The self-similar recursion (the load-bearing observation)

The §7 reconciliation pass of the ledger was minted to fix failure-mode #1 (specced-but-unrowed). The plan review found the **same failure recurring one layer up**: the rows §7 had captured were now rowed-but-unsequenced. **The pattern is self-similar across layers** — fixing it at the spec→row layer does not fix it at the row→sequence layer. A completeness check must run at *every* hand-off: spec → row → sequence → built.

## The fix — reconcile-into-the-ledger (reusable method)

1. **Mint a row for everything — including conscious drops and defers.** A capability that is deliberately NOT built (e.g. a Scenario Simulator, an IoT vitals feed) still gets a row whose fix-class is "dropped/deferred, with rationale." This converts a *silent gap* into a *recorded decision* — the conveyor proves the call was conscious, not forgotten.
2. **Give the ordered sequence a complete topological tail.** Every row gets an explicit slot; no undifferentiated "rides alongside" cloud that the walk skips. (V4 fix: extend the §0 order from a 6-item head to the full sequence, inserting the stranded rows at their true dependency slots.)
3. **Encode the dependency DAG explicitly** so a reader can *see* the order is correct — which row feeds which (e.g. case-shifting routes into the catalogue and pairs the ledger, so it sequences after both).

The principle in one line: **a ledger protects only against the gaps it can SEE — if it's not a row, the build is blind to it; if it's a row without a slot, the build skips it anyway.**

## Cousin: the retrieval side

This is the **build-side analogue of [[architecture-first-knowledge-retrieval]]**. There, the coverage-map makes *knowledge* gaps visible (walk every module's shelf; an un-walked shelf is a blind spot). Here, the gap-ledger makes *build* gaps visible (mint every capability as a row; an un-rowed or un-sequenced capability is a blind spot). Same doctrine — **make the invisible visible via an explicit, exhaustive ledger** — applied once to retrieval and once to the build conveyor. Both pair with [[prompt-forge]] as Ahmad's standing anti-drift methods; the V4 ledger instance is [[basira-v4-requirements-ledger]] / [[basira-v4-rebuild]].

## Provenance

- **Source:** the 2026-06-16 Basira V4 plan-review (`C:\dev\basira-v4\docs\PLAN-v4-R3.md`; the stranded-row finding R-S1 in `…\scratch\v4-plan-review-2026-06-16\C-FINDINGS-PACKAGE.md §3A` + `C-critique-integrity.md §1.2`). Memory-as-pointer — the specific G-row slots live in R3, not here.
- **Method:** distilled 2026-06-16 as a reusable method; the V4-specific row IDs are illustrations of the general pattern.
