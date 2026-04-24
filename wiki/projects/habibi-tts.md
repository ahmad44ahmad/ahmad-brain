---
id: habibi-tts
title: Habibi-TTS — F5-TTS Saudi Arabic Voice Model
type: project
status: active
aliases:
  - habibi
  - habibi-tts-sau
  - f5-tts-saudi
tags:
  - project
  - tts
  - f5-tts
  - saudi-arabic
  - modal
  - diacritization
  - tashkeel
created: 2026-04-24
updated: 2026-04-24
source: local-repo:C:\Users\aass1\habibi-tts-project\
related:
  - "[[ahmad-brain-foundation]]"
summary: >-
  Ahmad's TTS project. F5-TTS v1 Base architecture fine-tuned on Saudi Arabic
  with Ahmad's own voice (speaker 65721). Training on Modal A100 GPUs with
  fully diacritized text. Round history through R8 documented with the seven
  golden rules (diacritization, digit normalisation, Saudi-dialect sukun,
  lam-shamsiyya shadda, no dropped shadda, clean-slate protocol, inference
  expectations). Skill `tts-round-runner` governs every new round.
---

# Habibi-TTS (F5-TTS Saudi Arabic)

## Project snapshot

- **Model:** Habibi-TTS SAU — F5-TTS v1 Base architecture, fine-tuned for Saudi Arabic.
- **Speaker:** Ahmad (speaker ID 65721), HyperX QuadCast 2 S microphone, 24 kHz / 16-bit / mono target.
- **Training compute:** Modal cloud, A100 GPU. F5-TTS trainer with a patched checkpoint loader.
- **Datasets (cumulative as of R8):** v3_pro (273 clips) + v4 (225 clips) + v5 (300 clips) = **798 total clips, ~79 min**.
- **Project directory:** `C:\Users\aass1\habibi-tts-project\`.
- **Evaluation partner:** Gemini Deep Think 3.1 — analyses audio output and returns linguistic feedback (wrong-pronunciation / correct-pronunciation pairs).
- **Skill:** `tts-round-runner` under `~/.claude/skills/`.
- **Slash command:** `/tts-round` — prepares a new round and checks the golden rules before training.

## The seven golden rules (never violate)

Hard-won across R1–R8. Every rule traces to a failed experiment.

### 1. All training text must be fully diacritized (تشكيل)

Use `metadata_diacritized.csv`, never `metadata.csv` or `metadata_clean.csv`. Without diacritics the model cannot distinguish e.g. `سَمِعْتُ` (I heard) from `سَمِعَتْ` (she heard). Diacritization tool: `tashkeel_gemini.py` (Gemini 2.0 Flash API). **Do not use CAMeL Tools BERT** — it has a `LFUCache` bug as of 2026-03-26.

### 2. Never put raw digits in training text

The model reads *"1445"* as *"واحد، أربعة، أربعة، خمسة"* (digit by digit). Convert all numbers to fully diacritized Arabic words (تفقيط) before training — e.g. `25748 ريال` → `خَمْسَةٌ وَعِشْرُونَ أَلْفًا وَسَبْعُمِائَةٍ وَثَمَانِيَةٌ وَأَرْبَعِينَ رِيَالًا`. Run `fix_digits.py` to sweep and replace anything missed.

### 3. At inference, provide diacritized text

R8+ models are trained with diacritics and expect diacritized input at inference. `inference_eval.py` strips tashkeel only for R6–R7 (legacy). For production use, diacritize user input with the Gemini API before sending to the model.

### 4. Saudi dialect gets SUKUN at word endings

Colloquial words should not carry formal إعراب (case endings). Correct: `يَا أَخُويْ` / `خَلَاصْ` / `وَاللَّهِ`. Wrong: `يَا أَخُوِيُّ` / `خَلَاصٌ` (over-formalised). Gemini handles this correctly when prompted for Saudi register.

### 5. Lam Shamsiyya must have شدة on the following letter

Sun letters: `ت ث د ذ ر ز س ش ص ض ط ظ ل ن`. Correct: `الشَّمْس` / `النَّاس` / `الصَّبْر` / `الرَّجُل`. Wrong: `اَلْشَمْس` / `اَلْنَاس` (treats lam as qamariyya). Misses here teach the model the wrong assimilation and are expensive to retrain out.

### 6. Shadda (التضعيف) must never be dropped

The model's failure mode is to drop shadda, which changes meaning outright:

- `حَمَّلَ` (downloaded) ≠ `حَمَلَ` (carried)
- `عَلَّمَ` (taught) ≠ `عَلِمَ` (knew)
- `مُعَلِّم` (teacher) ≠ `مُعَلِم` (malformed)

Review every metadata row for intact shadda before training.

### 7. Clean-slate protocol for strategy changes

When fundamentally changing the training approach (e.g. adding diacritics), start from the SAU base model — do not build on contaminated checkpoints. Rounds that started clean: **R1, R5, R8**. Hyperparameters:

- **Clean-slate rounds:** 60 epochs, `lr = 1e-5`.
- **Continuation rounds:** 40 epochs, `lr = 5e-6`.

## Data pipeline

### Recording a new group

1. Write the script in markdown with numbered sentences.
2. Each line is one WAV, numbered `Recording (N).wav`.
3. The first file may be `Recording.wav` without a number — handle that edge case in the prep script.
4. Record at 48 kHz stereo (microphone default); convert to 24 kHz mono during prep.

### Processing new recordings

1. `prepare_vN.py` — converts WAV (48 kHz stereo → 24 kHz mono), parses the script, generates `metadata.csv`.
2. `tashkeel_gemini.py` — diacritises every metadata file → `metadata_diacritized.csv`.
3. `fix_digits.py` — converts any remaining raw digits to Arabic words.
4. Verify: `wc -l` on all metadata files; check no digits remain with `grep '[0-9]'`.

### Training

1. Edit `train_modal.py`: add the new dataset directory, update `data_sources`, update the round docstring.
2. Run `python -m modal run train_modal.py --round N`.
3. Monitor at `https://modal.com/apps/admin-62589/main`.

### Evaluation

1. Update `round_num` in `inference_eval.py`.
2. Run `python -m modal run inference_eval.py`.
3. Output: 10 WAV files in the `output/` folder.
4. Send the audio to Gemini Deep Think for linguistic analysis.
5. Gemini returns, per clip, the wrong pronunciation (النطق الخاطئ) versus correct pronunciation (النطق الصحيح).

## Evaluation test suite (10 standard clips)

| # | Focus |
|---|---|
| eval_01 | Emphatic consonants (ص vs س, ض vs د) |
| eval_02 | Similar letters (ض/د, ظ/ذ, ط/ت) |
| eval_03 | Throat sounds (ع/أ, غ/خ, ح/هـ) |
| eval_04 | Hamza positions — beginning, middle, end |
| eval_05 | Shadda + tanween |
| eval_06 | Numbers and dates |
| eval_07 | Saudi colloquial (عامية) |
| eval_08 | Intonation — questions, exclamations |
| eval_09 | Long flowing sentence — breath, rhythm |
| eval_10 | Technical and foreign words |

## Round history

State as of the 2026-03 memory capture. Current round state may have advanced — verify with Ahmad before citing as live.

| Round | Strategy | Result | Lesson |
|---|---|---|---|
| R1–R4 | Incremental data, original (undiacritized) text | Voice timbre OK, pronunciation poor | Mixed-quality data hurts more than it helps. |
| R5 | Clean data (v3_pro + v4), SAU base | Better timbre, same pronunciation errors | Data quality beats quantity. |
| R6 | Strip all tashkeel | Slight improvement, core issues persisted | Stripping removes the disambiguation signal entirely. |
| R7 | Added Group 5 targeted recordings | No improvement on core issues | Targeted data alone is insufficient without diacritics. |
| R8 | **Full diacritisation, SAU clean slate** | Pending evaluation (at memory capture) | The correct approach — give the model explicit pronunciation guidance. |

## Key files

- `train_modal.py` — main training script (Modal A100).
- `inference_eval.py` — evaluation inference (Modal T4).
- `tashkeel_gemini.py` — Gemini-based diacritisation (API key in the script).
- `fix_digits.py` — converts raw digits to Arabic words.
- `prepare_v5.py` — Group 5 data preparation.
- `prepare_v4.py` — Group 4 data preparation.
- `datasets/group5_recording_script.md` — Group 5 recording script (300 sentences).

## Why this guide exists

Eight rounds of failed experiments produced these seven rules. Every rule traces to a specific failure mode observed on the eval set. Following the guide prevents repeating past mistakes — skipping it restarts the eight-round debt. Before any training-related task, read this hub. Before adding new data, ensure it follows every golden rule. Before running inference, ensure the input text is diacritized.

## Gaps

- Current round beyond R8 — memory capture is from 2026-03; ask Ahmad or inspect `train_modal.py` for the latest `--round` value.
- R8 evaluation result — not yet captured at memory time.
- Drive docs related to TTS training-text generation — should be cross-linked from `drive-catalog` once identified.
- Whether any round has incorporated a second speaker / reference audio — all rounds so far are Ahmad-only.

## Provenance

Hub rewritten 2026-04-24 from memory file `tts-training-guide.md` (captured ~2026-03, flagged as 28 days old at migration time). The memory file is the sole source; the local repo has not been re-inspected during this migration, so *current* round state may differ from what is documented here. Phase D migration task from [[log-2026-04-24]]; upstream memory file retained as a one-line pointer.
