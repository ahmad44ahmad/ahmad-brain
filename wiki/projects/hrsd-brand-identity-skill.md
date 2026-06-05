---
id: hrsd-brand-identity-skill
title: HRSD Brand-Identity Skill — Claude Code PowerPoint Generator
type: project
status: active
aliases:
  - HRSD Skill
  - مهارة قوالب الوزارة
tags:
  - project
  - claude-code
  - hrsd
  - powerpoint
  - brand-identity
  - rtl
  - arabic
created: 2026-05-08
updated: 2026-06-05
source: local-skill:~/.claude/skills/hrsd-brand-identity/
related:
  - "[[basira]]"
  - "[[hrsd-work]]"
  - "[[pt-modeling]]"
  - "[[albaha-center-org]]"
  - "[[ahmad-2025-achievements]]"
summary: >-
  Claude Code skill that turns Word source content into MHRSD-branded PowerPoint
  decks (AR/EN, light/dark) with correct RTL flow, ministry palette, and a
  validate_output regression guard. Built 2026-05-08 in a single session from
  the four official ministry templates plus the 132-page brand guideline.
---

# HRSD Brand-Identity Skill

Single-session build (2026-05-08) that consolidates everything needed to produce ministry-grade slide decks from Claude Code: four official templates, ~1,235 ministry icons, a Python generator with twelve recipe kinds, and a `validate_output()` regression guard.

## Path

`~/.claude/skills/hrsd-brand-identity/` — 127 MB.

## What's bundled

| Asset | Count / size | Notes |
|---|---|---|
| Templates | 4 PPTX | AR/EN × light/dark. The fixed "© 2024 جميع الحقوق" footer was permanently removed from every layout (12 layouts × 4 templates = 48 layouts surgically cleaned). Both the skill copies and Ahmad's Desktop originals are clean. |
| Design catalogue | 102 slides | `templates/_specs/design_catalog.md` — every slide in `ar-light.pptx` indexed by kind and layout, ready for `clone_slide_from_catalog()`. |
| Icons | 1,235 PNGs | `light` (618) + `other` (617) extracted from the official ministry icon decks; visual grid in `icons/INDEX.md`. |
| References | 4 markdown + 190 PNGs | Verified palette + typography + logo rules + 132 PDF page thumbnails + 57 high-res key-page extracts. |
| Generator | `generate_hrsd_pptx.py` | 12 recipe kinds, JSON-driven CLI, four named helpers. |
| Tests | `test_generate.py` | 13 assertions; `validate_output()` is a separate regression guard. |
| Worked example | `_achievements_recipe.py` | Builds the 18-slide Al-Baha Centre achievements deck. |

## Verified colour palette (corrected from earlier memory)

| Role | HEX | Pantone |
|---|---|---|
| Dark Blue | `#0F3144` | 2189C |
| Turquoise | `#269798` | 2235C |
| Green | `#2BB574` | 2414C |
| Gold | `#FCB613` | 7409C |
| Orange | `#F7931D` | 2011C |
| Cool Gray | `#7A7A7A` | Cool Gray 9 |

Earlier memory had `#FCB614` and `#F7941D` — both off by one digit. Verified directly against `theme1.xml` of the official templates.

## Twelve recipe kinds

`cover` · `closing` · `agenda` · `bullet_list` · `section_divider` · `big_stat` · `stats_row` · `process_steps` · `grid_2x2` · `cards_3` · `spotlight` · `two_columns`.

All AR-side handlers auto-flip visual order so item 1 sits on the right (RTL flow). `agenda` and `bullet_list` use native PowerPoint bullets via `<a:buChar>` rather than inline characters, so bullets do not collide with bidi.

## Engineering learnings

1. **Templates lie about RTL.** Even the official Arabic templates contain hundreds of `rtl="0"` paragraphs (Google Slides export legacy). The generator must force `rtl="1"` on every Arabic paragraph regardless of source — `force_rtl(paragraph)` is mandatory.
2. **`font.name = 'Arial'` only writes `<a:latin>`.** Without an explicit `<a:cs typeface="Arial"/>`, Mac/Linux/PowerPoint-Online fall back to a generic shaper for Arabic and may render glyphs as boxes. The `_force_arial_cs(run)` helper writes both `<a:cs>` and `<a:ea>`.
3. **Inline bullet characters fight bidi.** A `◀` prepended to text collapses against the first word. Native PowerPoint bullets via `<a:buChar>` plus a hanging indent (`marR` + negative `indent`) render cleanly and look professional.
4. **Mixed numerals look broken.** `"50 من"` renders with awkward bidi spacing. Inside Arabic prose, use Arabic-Indic digits (`"٥٠ من"`); reserve Western digits for technical or financial tables and for isolated big-number callouts (`big_stat`, `stats_row`).
5. **Ministry brand-book hex codes were wrong in memory** — verified against `theme1.xml` and corrected (`#FCB613`, `#F7931D`).

## When to use

- Any HRSD-facing slide deck (vice minister, deputy, regional director, partners).
- Translating an English deck to Arabic via `mirror_layout_for_rtl()`.
- Brand-checking an existing artifact: open the `.pptx` and run `validate_output()`.

## When **not** to use

- Personal or creative artifacts.
- Non-MHRSD Saudi government bodies — different brand books.

## Standard invocation prompt (Arabic, verbatim)

Saved to `~/Desktop/تلقين - بناء عرض HRSD.txt` for quick paste-and-go. Embedded here as data:

```
استخدم مهارة hrsd-brand-identity لبناء عرض تقديمي من المستند المرفق.

📄 المصدر: «C:\Users\aass1\Desktop\اسم_الملف.docx»
🎨 القالب: «ar-dark» (الخيارات: ar-light · ar-dark · en-light · en-dark)
🎯 الجمهور: «معالي وكيل الوزارة»
📝 الطول المستهدف: «12-15 شريحة»
🗣️ اللهجة: حكومية رسمية، لا تشخصن، لا CBAHI

تعليمات التنفيذ:
1. اقرأ المستند بـ python-docx واستخرج كل الجداول والفقرات بحرفيتها.
2. صمّم بنية متنوعة بصرياً — لا تكرر نفس النمط أكثر من مرتين متتاليتين.
   استخدم على الأقل: cover + section_divider لكل محور + spotlight لقصة بارزة
   + stats_row للأرقام + cards_3 لقصص النجاح أو المذكرات + bullet_list
   للتفاصيل الداعمة + closing.
3. الأرقام داخل النصوص العربية: استخدم Arabic-Indic (٠-٩). الأرقام في
   stats_row و big_stat: لاتينية مقبولة.
4. تجنّب em-dash «—» داخل نص عربي — استخدم «·» أو «،».
5. احفظ على Desktop باسم وصفي عربي.
6. شغّل validate_output(out, 'ar') وتأكد أن النتيجة ✅. لا تُسلّم قبل ذلك.
7. ارندر 3-4 شرائح ممثلة كـPNG عبر PowerPoint COM وراجعها بصرياً.
8. ابدأ التنفيذ بدون طلب تأكيد.
```

## Worked example — Al-Baha Centre achievements deck

The same skill produced an 18-slide deck from a single-table Word document at `~/Desktop/الجدول التالي يوضح أبرز إنجازات مركز التأهيل الشامل بالباحة.docx`. Output landed at `~/Desktop/إنجازات مركز التأهيل الشامل بالباحة.pptx`. All 18 slides pass `validate_output()` with zero issues across: paragraph `rtl="1"` (83/83), Arabic run `<a:cs typeface="Arial">` (83/83), logo position, page-number position, and 16-pt minimum on body text.

## Related memory + vault references

- Memory pointer: `~/.claude/projects/C--Users-aass1/memory/skill_hrsd_brand_identity_pointer.md`.
- Brand-rule canonical reference: `~/.claude/projects/C--Users-aass1/memory/reference_hrsd_brand_identity.md`.
- Hard rules (rejected-by-review): `~/.claude/projects/C--Users-aass1/memory/feedback_hrsd_brand_compliance.md`.
- Source PDF: `~/Desktop/HRSD guideline -employee.pdf` (132 pages, Sept 2024).
