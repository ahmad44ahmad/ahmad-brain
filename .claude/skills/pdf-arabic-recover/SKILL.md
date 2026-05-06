---
name: pdf-arabic-recover
description: Recover Arabic text from PDF text-exports that come back per-word character-reversed (RTL-as-LTR encoding bug). Apply to any Arabic PDF read via Drive MCP that returns mojibake'd output.
---

# PDF Arabic Reversal Recovery Skill

Some Arabic PDFs (especially older ministry forms) export text with **per-word character reversal**: the words appear in correct order but each word's characters are reversed. Example:

- Drive export: `يجارهزلا حلا نب دلاخ`
- Recovered: `الزهراني صالح بن خالد`

The reversal pattern is deterministic — apply per-word character reversal to recover.

## Usage

```bash
python C:\dev\ahmad-brain\.claude\skills\pdf-arabic-recover\recover.py < input.txt > output.txt
# or
echo "ةفاظنلا تامدخ" | python recover.py
```

The script reads stdin and writes the recovered text to stdout. Lines are processed independently; each word (whitespace-separated) gets its characters reversed.

## When to apply

Apply this recovery whenever:

1. A Drive PDF text export returns text where Arabic letter pairs look "off" (e.g., تامدخ instead of خدمات)
2. The known-good test phrase الزهراني does NOT appear in the output but يجارهزلا does — clear reversal signal
3. Section titles look syntactically valid but semantically nonsensical

## When NOT to apply

- Clean Drive exports (most modern Google Docs/Sheets/Slides) — no recovery needed
- Latin / English text — recovery will mangle it
- Mixed RTL/LTR text — apply only to RTL portions; the per-word approach handles space-aligned text but breaks on mixed runs

## Known limitations

- **Space-position artifacts** — sometimes Arabic words break on spaces incorrectly during the reversal, producing fragments that require manual reconstruction (e.g., `الح بن دلاخ` → recovery yields `الح ن خالد` instead of correct `بن صالح خالد`). Most data is recovered cleanly; fine-grained details may need verification.
- **Punctuation** — clings to the wrong side after reversal. Acceptable for distillation, not for direct citation.

## Cross-references

- First documented: 2026-05-06 in [[mhrsd-contractor-performance-scorecard-ar]] and [[mhrsd-2025-albaha-branch-quality-plan-ar]] (both PDF imports from old ministry forms).
- Recovery procedure verified against 3 known-good terms (الزهراني, الصيانة, النظافة).
