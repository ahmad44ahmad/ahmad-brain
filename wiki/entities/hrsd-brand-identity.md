---
id: hrsd-brand-identity
title: "HRSD Brand Identity — 2026-04-30 summary (superseded)"
type: entity
status: superseded
aliases:
  - hrsd-brand
  - ministry-brand-identity-summary
tags:
  - hrsd
  - brand-identity
  - design-system
  - superseded
created: 2026-04-30
updated: 2026-06-05
summary: >-
  The 2026-04-30 prose summary of MHRSD's brand identity — the first vault
  capture from the 132-page guideline PDF. SUPERSEDED by the verified, page-cited
  [[hrsd-design-system]] (2026-06-05) + ADR-0004. Kept for history; this older
  page carries some pre-verification values (4×45pt icon grid since corrected to
  4×4/5pt; F7931D/FCB613 hexes vs the brand-book F7941D/FCB614). Cite hrsd-design-system.
related:
  - "[[hrsd-design-system]]"
  - "[[hrsd-brand-identity-skill]]"
  - "[[basira]]"
  - "[[mhrsd-leadership]]"
---

# HRSD brand identity

> ⚠️ **Superseded (2026-06-05) by the verified [[hrsd-design-system]]** (+ ADR-0004 `0004-hrsd-design-system-canonical-home`). This 2026-04-30 prose summary was the first vault capture from the 132-page guideline; the page-cited `hrsd-design-system` is now canonical. Two known pre-verification drifts on this page: the icon grid here reads **"4×45pt"** but the visual re-extraction corrected it to **4×4 grid / 5pt stroke**; and the hexes here (`#F7931D`/`#FCB613`, from the template XML) differ from the brand-book values (`#F7941D`/`#FCB614`) the verified note carries. Cite [[hrsd-design-system]] for current values; this is kept for history.

The Ministry of Human Resources and Social Development (وزارة الموارد البشرية والتنمية الاجتماعية, "HRSD") publishes a 132-page brand guideline ("HRSD Brand Guidelines", v1.0, designed in InDesign in September 2024). The PDF lives at `C:\Users\aass1\Desktop\HRSD guideline -employee.pdf`. This entry is the LLM-consumable summary; the canonical detail-level reference for an LLM working on Ahmad's machine is `~/.claude/projects/C--Users-aass1/memory/reference_hrsd_brand_identity.md`. When the two disagree, the memory file wins because it stays in sync with the PDF.

The brand has two appearance levels. The **formal level** is for press releases, ministerial speeches, and any artifact a deputy minister will sign — it strips down to gray plus a limited primary palette and locks icons to blue and white. The **default level** is for everything else, including Basira, dashboards, internal training docs, and most stationery — it uses the full secondary palette except gray. Most of Ahmad's work is default level. Treating Basira as formal-level by accident causes the design to collapse to grayscale, which feels government but violates the rule the other direction.

## Logo

The logo is sovereign and unaltered. It carries three layers of meaning: the sunrise above the wordmark stands for Saudi Arabia's civilizational growth, the joining of icon and wordmark stands for cooperation, and the overall composition evokes the country's two swords and palm tree. Versions exist for Arabic primary, English primary, icon-only (default for social media), positive (light backgrounds), reversed (dark backgrounds, except secondary-color backgrounds), white (on secondary colors and dark photos), and black (print-only — never appears in ministry digital designs).

Minimum size is 1 cm in print or 20 px on screen. In RTL Arabic content the logo defaults to the top-right corner; in English content it defaults to top-left; on social-media tiles the icon-only version sits bottom-right. There is a vertical version with proper proportions available on request from the brand team — do not invent one by rotating the horizontal logo.

The misuse list is long, but the rule that gets violated most is **"do not add a regional or branch name to the logo"**. The brand book is explicit: «لا تقم بإضافة أي نص للشعار مثل: إضافة اسم الفرع». The Al-Baha center is not a sub-brand of HRSD; it is HRSD operating in Al-Baha. The center identity goes in body text or a separate header element, not bolted onto the official mark. Other forbidden modifications: no recoloring, no gradients, no shadow or drop-shadow, no stretching, no cropping, no use as a watermark, no decorative-element use, no filling with photography. The black version exists for B&W print only and must never appear in a digital ministry design.

## Color system

The primary palette is two colors: dark blue `#0F3144` (Pantone 2189C, used for dark-mode backgrounds) and white `#FFFFFF` (used for light-mode backgrounds). The secondary palette is five colors: orange `#F7931D` (PMS 2011C), yellow/gold `#FCB613` (PMS 7409C), teal `#269798` (PMS 2235C), green `#2BB574` (PMS 2414C), and cool gray `#7A7A7A` (PMS Cool Gray 9). All seven colors support tints and shades from 20% to 100%, but tints are reserved for illustrations, characters, and charts — not for body text and not for buttons.

> **Hex correction (2026-05-08):** Earlier prose on this page listed `#FCB614` and `#F7941D` for gold and orange. Direct extraction from the official template `theme1.xml` (during the [[hrsd-brand-identity-skill]] build) confirmed the true values are `#FCB613` and `#F7931D` — both off by one digit in earlier transcriptions. Treat the values above as authoritative and update any downstream copies (Basira CSS, decks, references) accordingly.

Two rules govern usage. The first is the 60/40 proportion: backgrounds should occupy roughly 60% of the design and other elements roughly 40%. The second is the maximum-three-colors rule: no design uses more than three colors at once except illustrations and charts. The body-text color rule is even stricter — body paragraphs are always gray or white, never secondary colors. Headlines may use any palette color. Coloured paragraph text reads as marketing material, not as government communication, and will be flagged on review.

In Basira specifically, the existing `src/styles/hrsd-theme.css` contains slightly wrong RGB values for every secondary color and fabricated Pantone numbers ("Pantone 1375 C", "Pantone 1235 C", "Pantone 3025 C", etc.) that don't match the actual ministry guidelines. Fixing those tokens to the values above is item one of the brand-compliance change-plan.

## Typography

The ministry developed its own typeface, **HRSD Gov**, which it claims is the first government typeface in Saudi Arabia. The font is inspired by the geometric features of the logo combined with elements of the Naskh calligraphy style, supports Arabic and English, and ships in five weights: HRSD Gov Title (the headline weight), SemiBold, Medium, Regular, and Light. Body text uses Medium and Regular as the two main weights. Text settings are leading auto, tracking 0, kerning optical.

The Arabic-to-English headline ratio is 3:2 when one language stands alone (Arabic larger) and 1:1 when both languages appear together (equal sizes for parity). This matters in bilingual decks where a single headline pairs Arabic and English on the same line — they must be the same size, not visually balanced by eye.

Ahmad's directive on 2026-04-30 is that Basira keeps its current production font (Tajawal or IBM Plex Sans Arabic, depending on the surface) until HRSD Gov is properly licensed and embedded. Don't switch the font on a whim — only switch when the official font files are in the repo.

## Patterns, icons, characters, charts

There are five main flexible patterns plus an optional curved-line accent. Pattern coloring follows the formal/default rule: gray-only at the formal level, full secondary palette at the default level. The curved line is colored based on the larger color region it crosses — and specifically forbidden from being blue (reserved) or gray at the default level.

Icons have round corners only (no sharp edges), one of two styles (filled or outline, never mixed in the same icon), and live on a 4×45pt grid. Formal-level icons are blue and white only. Default-level icons can be a single color (outline) or two colors combining primary and secondary (filled). Tints, shades, and any kind of effect (shadow, glow, etc.) are forbidden.

Characters are drawn in a 600×600 px square with 1-px stroke lines, realistic body proportions, and **no facial features** — no eyes, no wrinkles. A simplified-features "custom version" exists for animation only. Each character uses two primary colors plus two shadow colors. Pre-made illustrations from external libraries can be partially recolored (keep three of the original colors, add two or three brand colors) for cases where the meaning depends on color, or fully recolored to brand palette otherwise. Characters never appear standalone — they integrate with patterns and typography.

Charts use HRSD Title font for titles and HRSD body font for labels, with headline colors for titles and gray/white body colors for labels. Pie charts have hard rules: largest slice at 12 o'clock, slices ordered clockwise from largest to smallest, maximum five slices (otherwise convert to a bar chart). 3D effects, shadow effects, similar-tint adjacencies in a single chart, external colors, and external fonts are all forbidden.

## Sonic identity

Five sonic styles cover the ministry's video and multimedia work. **Ambience** is for ministry facilities, forums, and events as background. **Formal** is for news, decisions, and official interviews. **Empowering** is for achievements and "what we made possible" videos. **Impactful** is for emotional and humanitarian content. **Coverage** is for event and activity coverage. The ministry licenses its own music for the animated logo outro; commercial music is forbidden in any video that uses the official logo motion.

## Strategic foundation (verbatim, for pitch decks)

Vision: «مجتمع حيوي ممكن، وبيئة عمل متميزة نحو سوق عمل جاذب». Mission: «تمكين الفرد والمجتمع والمؤسسات في السعودية، وتعزيز المسؤولية المجتمعية، والارتقاء بسوق العمل من خلال تطوير السياسات والتشريعات، وتمكين منسوبي الوزارة من تقديم تجربة مميزة للمستفيدين». Values: customer-centricity, social responsibility, cooperation, inclusion, excellence. Strategic axes: one labor market, decent living for all, high productivity economy, sustainable corporate excellence.

Identity inspiration words: flexibility, strength, the future, empowerment. Color personality: society, excellence, responsible, cooperative, enabled, dynamic. These are the words to reach for in body copy when describing what the ministry does — the brand book essentially provides the controlled vocabulary.

## Official contact

P.O. Box 21110, Riyadh 11475, Kingdom of Saudi Arabia. Web: `www.hrsd.gov.sa`. Social: `@hrsd_sa` on Twitter/X, `hrsd.sa` on Instagram, `hrsdsa` elsewhere.

## Application to Basira

Basira is default-level, light-mode-first, RTL Arabic. Logo goes top-right. Body text is gray or white. Buttons and accents use the secondary palette but no more than two or three colors per screen. The five sonic styles map to walkthrough video voiceover work — Empowering for the achievements walkthrough, Impactful for the cup-of-water Karama scene, Formal for the auditor demo. Charts in the Pulse Dashboard and Smart Alerts panels need to drop any 3D effects and switch to the rule-set above.

Related: the [[basira]] project hub captures what the system is and how it builds. The [[mhrsd-leadership]] entity captures the people who consume HRSD-branded artifacts.
