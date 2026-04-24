---
id: habibi-tts
title: Habibi-TTS — F5-TTS Saudi Arabic Voice Model
type: project
status: active
aliases: ["habibi", "f5-tts-saudi"]
tags: [project, tts, f5-tts, saudi-arabic, modal, diacritization]
created: 2026-04-24
updated: 2026-04-24
source: local-repo:C:\Users\aass1\habibi-tts-project\
related: [[ahmad-brain-foundation]]
summary: >-
  Ahmad's TTS project — F5-TTS fine-tuned on Saudi Arabic. Training on
  Modal with A100 GPUs. Uses diacritized (tashkeel) training text.
  Skill `tts-round-runner` governs training rounds. Stub pending full
  migration from memory/tts-training-guide.md.
---

# Habibi-TTS (F5-TTS Saudi)

## Local + infrastructure

- **Repo:** `C:\Users\aass1\habibi-tts-project\`
- **Model base:** F5-TTS
- **Target language:** Saudi Arabic (SAU)
- **Training compute:** Modal, A100 GPUs
- **Skill:** `tts-round-runner` (in `~/.claude/skills/`)
- **Slash command:** `/tts-round`

## Training pipeline (from memory, not yet fully migrated)

Key rules Ahmad has set (from `tts-training-guide.md` memory — pending migration):

- Training text must be **diacritized** (tashkeel) for correct pronunciation.
- Metadata files must use diacritized forms.
- `fix_digits` normalization applied.
- Named evaluation tests (e.g., `eval_XX`) used to score output.
- Rounds numbered (R[N]) with golden-rules compliance per round.

## Gaps — full hub still to populate

- [ ] Migrate memory file `tts-training-guide.md` in full.
- [ ] Document round history + current round status.
- [ ] Describe evaluation test set + thresholds.
- [ ] Link to any Drive docs related to TTS training text generation (see [[drive-catalog]] TTS section).

## Provenance

Stub created 2026-04-24 Phase B migration. Full content migration deferred until Ahmad next touches a training round.
