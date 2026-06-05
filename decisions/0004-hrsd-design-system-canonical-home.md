---
id: 0004-hrsd-design-system-canonical-home
title: "ADR 0004: Canonical home for the verified HRSD design system"
type: decision
status: active
tags: [hrsd, design-system, brand-identity, adr]
created: 2026-06-05
updated: 2026-06-05
summary: >-
  Establish C:\dev\hrsd-design-system as the single verified, page-cited home for MHRSD's brand identity,
  built by a visual page-by-page re-extraction of the 132-page brand book; memory, Basira V4 and the
  Desktop mirror carry derived pointers, and every value is tagged brand-canon vs DERIVED.
related:
  - "[[hrsd-design-system]]"
  - "[[0003-basira-v4-architecture]]"
deciders: [ahmad, claude]
---

# ADR 0004: Canonical home for the verified HRSD design system

## Context

HRSD brand knowledge was scattered and partly wrong across three places: the always-loaded memory files
(`reference_hrsd_brand_identity.md`, `feedback_hrsd_brand_compliance.md`), an unverified prior "Design
System 4.8" extraction (a coded token/component bundle that carried at least three fabricated values —
e.g. Pantone "423 C", a "20→80 %" tint range, computed tint hexes presented as canon), and assorted
Basira CSS that had operated on guessed values since inception. Ahmad asked for one precise, exhaustive,
English design system so that building any feature, deck, report or card is on-brand from the first line —
not only colours and a font, but logo placement, icons, patterns, illustrations, sonic identity and voice.

The same official 132-page brand book underlay all of them; the "new 2026" folders turned out to be that
same book plus a fuller font family and the unverified 4.8 build — i.e. a **verify-and-consolidate** job,
not a fresh read.

## Decision

1. **One canonical home:** `C:\dev\hrsd-design-system\` holds the verified knowledge base — `tokens/`
   (CSS + typed TS), `docs/01..10`, `assets/`, and the `VERIFICATION-LEDGER.md` trust spine. All other
   homes are **derived pointers**: the Desktop mirror, Basira V4's `lib/design/hrsd-tokens.ts`, the memory
   digest, and this vault note.
2. **Verify against the PDF, visually.** The 4.8 extraction is treated as a *candidate to confirm*, never
   a base to promote. Pages are rasterised and read as images; every value gets a page cite or a
   `[DERIVED]` tag (computed/product value with no brand-book basis). The ledger marks each claim
   VERIFIED / CORRECTED / DERIVED / OPEN.
3. **One skill, not two.** The mature `hrsd-brand-identity` Claude skill (official PPTX templates, the
   ~1,235-icon library, the RTL-aware generator) is kept and pointed at this home for its rule/value half;
   the 4.8 `hrsd-design` skill is not installed and is retired into this knowledge base.
4. **Memory shrinks to corrections + a pointer**, per the memory→vault boundary — it is the hot-cache
   digest; this home is the on-demand spine.

## Consequences

- A new ministry deliverable starts from page-cited values, so "is this from the brand book or did we
  invent it?" is always answerable. The drift that let "423 C" and phantom tint hexes circulate is closed.
- The visual method already paid for itself: it corrected the icon construction spec to **4×4 grid / 5 pt
  stroke** (the recorded "4×45 pt / 23 px / −11°" was a text-layer artifact), resolved the Cool Gray
  Pantone to "Cool Gray 9", and flagged that `www.hrsd.gov.sa` is not in the book.
- Two genuinely open items are surfaced rather than buried: **font webfont-licensing** (HRSD Gov is
  © Zan Agency, not webfont-licensed → Basira V4 stays on Tajawal for the web) and the **icon
  source/licence**.
- Cost: ~1.8 M subagent tokens across two multi-agent passes; an acceptable one-time price for a
  permanent, trustworthy foundation.

## Alternatives considered

- **Promote the 4.8 build as-is** (fast) — rejected: it would have propagated its fabricated values into
  four homes.
- **Canonical inside Basira V4** — rejected: the design system outlives and is broader than one app
  (decks, reports, cards), and the project-registry rule places new shared work under `C:\dev\<name>\`.
- **Keep it only in memory** — rejected: the always-loaded memory must stay small; an exhaustive,
  page-cited corpus belongs in an on-demand home with the digest pointing to it.
