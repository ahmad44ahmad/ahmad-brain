---
id: ai-model-routing-and-governance
title: "AI Model Routing & Governance — The Tier-by-Task Rule + the PHI/ZDR Gate"
type: synthesis
status: active
aliases:
  - model-routing
  - fable-opus-routing
  - phi-zdr-gate
  - model-governance
tags:
  - synthesis
  - ai-tooling
  - governance
  - pdpl
  - model-routing
  - basira-v4
created: 2026-06-16
updated: 2026-06-16
learned_at: 2026-06-16
confidence: high
source: local:C:\Users\aass1\Desktop\FABLE5-OPUS48-01-PORTFOLIO.md, FABLE5-OPUS48-05-GOVERNANCE-COST.md
related:
  - "[[basira-v4-rebuild]]"
  - "[[prompt-forge]]"
  - "[[mhrsd-cyber-policy-library]]"
  - "[[architecture-first-knowledge-retrieval]]"
summary: >-
  The durable, model-agnostic rule for routing work across AI model tiers: use a
  higher-ceiling model for long-horizon, ambiguous, architectural/design work;
  use a cheaper/ZDR-eligible model for incremental execution, verification, and
  sensitive content. Plus the hard PHI/ZDR governance gate — never route PHI
  through a model with mandatory retention / no ZDR; route refusal-category work
  (cyber/bio) to the ZDR lane; scrub reasoning-extraction prompts. Fable-specific
  facts are quarantined as date-stamped data.
---

# AI Model Routing & Governance

## The durable principle (model-agnostic)

The routing rule holds whatever the models are named:

- **Higher-ceiling model** → long-horizon, ambiguous, architectural / design / synthesis work where reasoning depth and recall pay for themselves (specs, hard plans, cross-codebase review).
- **Cheaper / ZDR-eligible model** → incremental execution, verification, mechanical edits, and **anything touching sensitive data**.

In the Basira V4 workflow this is the architect-vs-builder split: a design model drafts the spec, the executor model builds and verifies it. The principle is the durable assertion; the model names are data.

## The hard PHI / ZDR governance gate

Three non-negotiable rules, the most defensible part of the whole model-routing question and aligned with the PDPL posture in [[mhrsd-cyber-policy-library]]:

1. **Never route PHI through a model with mandatory retention / no ZDR.** Real beneficiary data only goes through a Zero-Data-Retention-eligible lane. A model that forces a 30-day retention window is disqualified for PHI by construction.
2. **Route refusal-category work to the ZDR/execution lane.** Cyber/ISMS and bio content hit the higher-ceiling model's refusal categories — route it to the executor model rather than fighting refusals.
3. **Scrub reasoning-extraction prompts.** "Show your full chain of thought" style asks can trip a `reasoning_extraction` refusal; phrase for the conclusion, not the raw reasoning dump.

## Fable-specific data (date-stamped — model facts move)

*As of 2026-06-13, per the cached Anthropic `claude-api` reference (cached 2026-06-04) and verified in the strategy-meta audit:*

- **Claude Fable 5 (`claude-fable-5`) is real** — in the current-models table. (An earlier "fabricated, no such model" note was the stale/wrong one; this records the resolution, not the confusion.)
- **Pricing $10 / $50 per 1M tokens** vs Opus 4.8's $5 / $25 = exactly **2× per-token**.
- **Same tokenizer as Opus 4.8** → effective cost ≈ **2× vs the Opus-4.8 baseline this work runs on** (NOT the "2.6×" an earlier report claimed; the ~30% tokenizer inflation only applies coming from Opus 4.6 / Sonnet / older).
- **30-day mandatory retention, NOT available under ZDR** (ZDR orgs get a `400` on every request) — this is the load-bearing fact behind gate rule #1.
- **Refusal categories: cyber / bio / reasoning_extraction** (the earlier "chemistry/distillation" phrasing was wrong).

Treat the prices and ceiling-claims as date-stamped data, not durable assertions; re-verify against `claude-api` before quoting. Do **not** enshrine benchmark numbers — those were `[REPORT]`-flagged (cited as official but unverified) in the source.

## Why this is in the vault

It pairs with [[prompt-forge]] (the intake method) and [[architecture-first-knowledge-retrieval]] (the retrieval method) as Ahmad's standing operating doctrine for working with AI, and it is the governance rule that keeps real PHI out of the wrong model lane — the same discipline as the GitHub/Supabase exposure posture.

## Provenance

- **Source:** the Desktop `FABLE5-OPUS48-01-PORTFOLIO.md` (routing principle) + `-05-GOVERNANCE-COST.md` (governance + cost), distilled — not the Arabic decision report. Model facts cross-checked against the `claude-api` skill reference.
- **Method:** distilled 2026-06-16; principle stated as durable, Fable-specifics quarantined as date-stamped data per the no-fabrication discipline the vault itself enforces.
