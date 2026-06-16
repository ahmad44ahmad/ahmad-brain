---
id: architecture-first-knowledge-retrieval
title: "Architecture-First Knowledge Retrieval — Walk the Shelf, Don't Funnel by Keyword"
type: synthesis
status: active
aliases:
  - architecture-first-retrieval
  - module-shelf-walk
  - coverage-map-method
  - read-extract-library-vault
tags:
  - synthesis
  - method
  - knowledge-management
  - retrieval
  - ai-markdown-pipeline
created: 2026-06-16
updated: 2026-06-16
learned_at: 2026-06-16
confidence: high
source: local:C:\Users\aass1\Desktop\PHASE-2R-architecture-first-method.md
related:
  - "[[prompt-forge]]"
  - "[[vault-operating-manual]]"
  - "[[basira-v4-rebuild]]"
  - "[[ai-model-routing-and-governance]]"
summary: >-
  Ahmad's standing retrieval method: invert the keyword-funnel. Instead of
  searching a corpus by query terms (which silently discards whatever the query
  didn't name), enumerate the system's modules, walk each module's corpus shelf
  top-to-bottom (the shelf is the filter — no ambient discard), emit a per-module
  coverage row, and extract to English AI-markdown. The read→extract→library→
  vault pipeline. Project-agnostic; pairs with prompt-forge as a second standing
  method.
---

# Architecture-First Knowledge Retrieval

## The diagnosis

Keyword-funnel retrieval — search a corpus by query terms, read the hits — has a silent failure mode: **it discards whatever the query didn't name.** You can't find a gap you didn't think to search for, and "ambient" documents that don't match any query term vanish without ever being counted. For a knowledge-foundation task ("what do we have, and what's missing?"), that is exactly the wrong tool — it confirms what you expected and hides what you didn't.

## The method (invert it)

Drive retrieval from the **architecture**, not the query:

1. **Enumerate the modules** — list the capabilities/units the system must cover (the architecture is the index).
2. **Walk each module's corpus shelf top-to-bottom** — read every document on the shelf, in order. **The shelf is the filter**; there is no "ambient" discard, because every item is either on a module's shelf (read it) or not (out of scope, explicitly).
3. **Emit a per-module coverage row** — for each capability: is the source present? is it wired? This produces a coverage map (e.g. "154 required · 127 present · 18 wired") instead of a pile of search hits.
4. **Extract to English AI-markdown** — distill each read source into clean, structured markdown.

The output is a coverage map with named blindspots, not a search-result list — and blindspots are the whole point.

## The read→extract→library→vault pipeline

The retrieval method feeds a standing pipeline (the durable upgrade of the `feedback_ai_markdown_library_pipeline` memory note):

**read → extract English AI-markdown → Desktop working folder → Drive knowledge library → ahmad-brain vault.**

Retrieval at query time then runs architecture-first too: go module → shelf, not keyword → funnel. Memory stays a pointer; the vault holds the distilled knowledge.

## The honest autonomous-vs-blocked split

A load-bearing discipline: when walking a shelf, separate what was **actually read** from what was **blocked** (access-denied, classifier-refused, PHI-gated) — and `log()` the blocked set rather than letting a silent truncation read as "covered everything." A coverage map that hides its own gaps is worse than no map. (This is the same anti-`وهم الإنجاز` discipline the vault enforces on every note.)

## Why this is in the vault

It is project-agnostic and reusable — Ahmad's **second standing method** alongside [[prompt-forge]] (intake/forge) and the model-routing doctrine ([[ai-model-routing-and-governance]]). It is the method behind the Basira V4 coverage audit (the "12% wired / 82% present" headline, [[basira-v4-rebuild]]) and behind this very harvest→vault integration. The [[vault-operating-manual]]'s own retrieval pattern (module → `type:`/`tags:` → `related:` edges) is the in-vault instance of the same principle.

## Provenance

- **Source:** the Desktop `PHASE-2R-architecture-first-method.md` — the general method (§0 diagnosis, §1 method, §4 pipeline, §5 autonomous-vs-blocked split), not the Basira-specific folder→module table (that is project state, kept on Desktop/in-repo).
- **Method:** distilled 2026-06-16; upgrades the memory-pointer `feedback_ai_markdown_library_pipeline` into a durable concept.
