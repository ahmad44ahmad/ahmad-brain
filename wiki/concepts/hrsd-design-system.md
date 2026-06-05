---
id: hrsd-design-system
title: HRSD Design System (verified extraction)
type: concept
status: active
aliases: ["HRSD brand identity", "ministry design system", "hawiyat al-wizara"]
tags: [hrsd, design-system, brand-identity, basira]
created: 2026-06-05
updated: 2026-06-05
summary: >-
  The verified, page-cited extraction of MHRSD's 132-page brand book into a reusable design system at
  C:\dev\hrsd-design-system. Canonical home for the strategic foundation/voice, colour, type, logo,
  icons, patterns, sonic and a VERIFICATION-LEDGER that separates brand-book canon from derived product tokens.
related:
  - "[[0004-hrsd-design-system-canonical-home]]"
  - "[[0001-vault-architecture]]"
  - "[[basira-v4-rebuild]]"
  - "[[hrsd-work]]"
source: session:517d5e0a-32d8-47b2-97b1-ef3caec73170
confidence: high
---

# HRSD Design System (verified extraction)

The Ministry of Human Resources and Social Development (MHRSD / HRSD) publishes a 132-page brand book
(`HRSD guideline -employee.pdf`, © 2023, InDesign 2024-09). On 2026-06-05 that book was re-extracted
**page-by-page, visually** into a single reusable design system so that any ministry-grade deliverable —
the Basira V4 app, decks, reports, certificates, recognition cards — is on-brand by construction rather
than by guesswork.

## Where it lives

- **Canonical home:** `C:\dev\hrsd-design-system\` — self-contained: `tokens/` (CSS + typed TS),
  `docs/01..09` (one per brand dimension) + `10-application-rules.md`, `assets/` (fonts, logo lockups,
  icon PNGs, characters), and the `VERIFICATION-LEDGER.md` trust spine.
- **Desktop mirror:** `C:\Users\aass1\Desktop\HRSD-Design-System\` (always-accessible copy).
- **Basira V4 hook:** `C:\dev\basira-v4\lib\design\hrsd-tokens.ts` + `docs/HRSD-DESIGN-SYSTEM.md`.
- **Memory digest:** `reference_hrsd_brand_identity.md` (+ `feedback_hrsd_brand_compliance.md`).

## The method that makes it trustworthy

Every factual value carries an inline **brand-book page cite** or is tagged **`[DERIVED]`** (a computed or
product-design value with no brand-book basis). The `VERIFICATION-LEDGER.md` is the spine: each claim is
marked VERIFIED / CORRECTED / DERIVED / OPEN. Verification was **visual** — pages were rasterised and read
as images, because a hex value, a filled-vs-outline icon, or a layout cannot be trusted from a text layer.
The page-cite convention: the printed footer page = PDF index − 2 (TOC-verified).

This discipline caught real errors a text pass had missed (see "What the visual pass corrected").

## Strategic foundation & voice (the identity behind the visuals, p.1 / p.3)

The brand book opens with the ministry's "who we are" front matter — the **strategy** the visual system
serves (verified visually from p.1 / p.3; `docs/01-strategic-foundation-and-voice.md`):

- **Vision (الرؤية):** «مجتمع حيوي ممكّن، وبيئة عمل متميزة نحو سوق عمل جاذب» — *"A dynamic and enabled society, and an exception[sic] work environment towards an attractive labor market."* (the book prints "exception"; intended *exceptional* — preserved verbatim).
- **Mission (الرسالة):** empower the individual / society / institutions, instil social responsibility, raise labour-market efficiency through policy + legislation, and enable ministry employees to deliver a distinctive beneficiary experience.
- **Values (قيمنا):** التركيز على المستفيدين (Customer centricity) · المسؤولية المجتمعية (Social responsibility) · المشاركة · التعاون (Cooperation) · التميز (Excellence). ⚠️ **Book-internal mismatch — do NOT harmonise:** the Arabic value **المشاركة (Participation)** is printed in English as **"Inclusion."** Quote whichever language you publish in.
- **Strategic axes (المحاور):** سوق عمل واحد (One Labor Market) · حياة كريمة للجميع (Decent Living For All) · اقتصاد عالي الإنتاجية (High Productivity Economy) · التميز المؤسسي المستدام (Sustainable Corporate Excellence — book prints "Sustalnable … Excence"[sic]).
- **Identity-inspiration concepts (p.3):** تمكين (Empowerment) · مستقبل (The future) · قوة (Strength) · مرونة (Flexibility) — the four abstract concepts the **pattern system + characters** are built from (one shared brand-concept vocabulary).
- **Colour-personality (p.3, distinct from the Values):** each palette colour carries a psychological meaning — Teal = تميز/Excellence · Yellow = حيوي/Dynamic · Orange = ممكّن/Enabled · Cool-Gray = متعاون/Cooperative · Blue = مسؤول/Responsible · Green = مجتمع/Society. This explains *why each colour was chosen* — a six-item set distinct from the five Values; never substitute one for the other.
- **No voice / tone-of-voice chapter (load-bearing).** The brand book governs **visual identity only** — it has no verbal-identity, tone-of-voice, messaging, or content section. Any tone-of-voice or microcopy rule applied to an HRSD/Basira deliverable is a **product addition** that must be tagged `[DERIVED]`, never cited to the brand book (the prior "4.8" build's "content fundamentals" section was invented).

## Core verified facts

- **Colour.** Primary: HRSD Blue `#0F3144` (Pantone 2189 C) and White. Secondary: Orange `#F7941D`
  (2011 C / 2012 U), Yellow `#FCB614` (7409 C / 128 U), Teal `#269798` (2235 C), Green `#2BB574` (2414 C),
  Cool Gray `#7A7A7A` (**Cool Gray 9**, not "423 C"). Tints are defined at 20/40/60/80/100 % but the book
  prints **only the % labels — no per-step hexes**, so every concrete tint hex is `[DERIVED]`.
- **Typography.** Custom typeface **HRSD Gov**: roster = 1 display (Title) + 4 content
  (SemiBold/Medium/Regular/Light); Thin and Bold ship as files but are off-roster. Heading:body ratio
  3:2 (anchor 27/18/12 pt); bilingual sizing 1:1; body text is gray/white only.
- **Logo.** Sunrise + national emblem (palm & crossed swords). Construction unit X = brand-mark width.
  Arabic logo top-right, English top-left. Colour-version ↔ background is binding: the positive (colour)
  mark is **wrong on a secondary-colour background** — use the white mark there. Never add branch/region
  text, never recolour/effect, black version is print-only.
- **Icons.** Built on a **4×4** grid with a **5 pt** stroke, round corners, filled or outline (never
  mixed). The book itself notes the icons are "downloadable from most websites" — a generic library, so
  licence-check before reuse. Default level = secondary palette (gray excluded); Formal = primary only.
- **Patterns.** Five patterns crossed by a curved line; colour by the larger area, never blue/navy,
  never gray at Default level; 20 % pattern-fill transparency vs the separate 60/40 layout proportion.
- **Sonic & video.** Five sonic styles (Ambience / Formal / Empowering / Impactful / Coverage); the
  animated-logo video outro uses ministry-licensed music only.

## What the visual pass corrected

- Icon construction is **4×4 grid / 5 pt stroke**, NOT the previously-recorded "4×45 pt / 23 px / −11°"
  (that was a text-layer artifact; no rotation angle exists on the page).
- **Cool Gray Pantone is "Cool Gray 9"**, not "423 C" (the 423 C error lived in an unverified prior
  "Design System 4.8" candidate build).
- **`www.hrsd.gov.sa` is not in the brand book** — the letterhead prints only the postal block
  (P.O. Box 21110, Riyadh 11475). The URL is real but `[DERIVED]` relative to this document.
- Two book typos preserved verbatim (Vision EN "an exception[sic]"; Axis-4 "Sustalnable[sic]"); the
  Arabic value "المشاركة (Participation)" is rendered "Inclusion" in English — a book-internal mismatch.

## Open questions

- **Font licensing.** HRSD Gov is © 2020 Zan Agency, all rights reserved; the files' embed bits are a
  document/print flag, **not a webfont licence** → keep web apps (Basira V4) on the current production
  font (Tajawal); HRSD Gov is design/print-time only until written permission.
- **Icon source/licence** (generic library) and the full ~1,235-icon official set (only a 40/41 sample
  extracted) remain to confirm.

## How to use it

For product code, import `hrsd-tokens.ts` (canonical values, page-cited) and follow the hard rules in
`10-application-rules.md`. For decks/PPTX, the `hrsd-brand-identity` Claude skill carries the official
templates, the ~1,235-icon library, and a generator — it is the asset/generator half; this knowledge base
is the verified rule/value half. See [[0004-hrsd-design-system-canonical-home]] for why a single home.
