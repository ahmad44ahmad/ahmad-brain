---
id: pst-mailbox-hrsd-merged
title: PST Mailbox — Merged Archive (primary search surface, 2015-2026)
type: source
status: active
aliases:
  - pst-merged
  - pst-archive-merged
  - unified-email-archive
tags:
  - pst
  - mailbox
  - hrsd-email
  - merged
  - primary-query-surface
  - deduplicated
created: 2026-04-25
updated: 2026-04-25
valid_from: 2015-10-19
learned_at: 2026-04-25
confidence: high
source: merged:D:\pst-archive\ + D:\pst-archive-a\
related:
  - "[[pst-mailbox-hrsd]]"
  - "[[pst-mailbox-hrsd-snapshot-a]]"
  - "[[sent-mbox-hrsd]]"
  - "[[ahmad-career-arc]]"
  - "[[hrsd-work]]"
summary: >-
  Unified FTS5 search surface across both local HRSD PST snapshots. 4,479
  deduplicated messages spanning 2015-2026. Primary archive to query.
  Built 2026-04-25 after exhaustive local-drive scan confirmed only two
  distinct PST content sets exist — PST-A (2023-11 → 2025-01 + 2015-2022
  drafts) and PST-C (2025-03 → 2026-03). Pre-2023 = drafts/deleted only.
---

# PST Mailbox — Merged Archive (2015–2026)

## The full local picture

Exhaustive scan of the D: and C: drives on 2026-04-25 (following Ahmad's directive to re-search) confirmed that only two distinct PST content sets exist on this machine:

- **PST-A** — 2025-06-15 snapshot, present as three near-duplicate copies in `999 15 6 2025/backup.pst`, `999 27-10-2025/backup.pst`, `999 27-10-2025/backup (2).pst`.
- **PST-C** — primary working backup `backup22222 (1).pst` (hardlinked to `backup-clean.pst`).

There is **no hidden "main PST"** elsewhere — no other local PSTs, no .ost for HRSD (only a Hotmail .ost in AppData), no File History, no Windows Image Backup. Material pre-dating 2023-11 survives only as drafts and deleted items.

Both archives have been extracted, indexed, and now merged:

- `D:\pst-archive\` — PST-C, 2,582 raw messages ([[pst-mailbox-hrsd]]).
- `D:\pst-archive-a\` — PST-A, 3,659 raw messages ([[pst-mailbox-hrsd-snapshot-a]]).
- **`D:\pst-archive-merged\`** — unified deduplicated index: **4,479 unique messages**.

## Merged DB stats

Deduplication removed 1,762 items — mostly Outlook's auto-saved draft versions of the same (date + sender + subject).

### Per-archive contribution

| Source | Added unique | Duplicates skipped |
|---|---|---|
| PST-A | 2,149 | 1,510 |
| PST-C | 2,330 | 252 |

### Year distribution (combined)

| Year | Messages | Nature |
|---|---|---|
| 2015 | 2 | MOSA-era drafts (Ahmad, `23200@mosa.gov.sa`) |
| 2016 | 18 | drafts |
| 2017 | 1 | drafts |
| 2018 | 1 | drafts |
| 2019 | 23 | drafts + 1 MLSD-era deleted (`TABS@mlsd.gov.sa`) |
| 2020 | 22 | drafts + deleted |
| 2021 | 57 | drafts |
| 2022 | 38 | drafts + 2022 deleted |
| 2023 | 371 | first real inbox (starts 2023-11-13) |
| 2024 | 1,634 | active |
| 2025 | 1,975 | two snapshots cover 2025-01 and 2025-03 onward |
| 2026 | 337 | through 2026-03 |

### Per-folder coverage within each source

| Source | Folder | Count | Window |
|---|---|---|---|
| PST-A | inbox | 1,827 | 2023-11-13 → 2025-01-09 |
| PST-A | sent | 108 | 2023-11-14 → 2025-01-05 |
| PST-A | drafts | 208 | **2015-10-19** → 2025-01-09 |
| PST-A | deleted | 1 | 2024-12-04 |
| PST-A | sync-issues | 5 | 2023-10-12 → 2023-11-26 |
| PST-C | inbox | 2,125 | 2025-03-02 → 2026-03-01 |
| PST-C | sent | 51 | 2025-03-03 → 2026-02-23 |
| PST-C | drafts | 35 | 2025-10-01 → 2026-03-01 |
| PST-C | deleted | 119 | 2019-04-25 → 2026-02-21 |

(Counts are post-dedup unique per source; raw per-archive counts are in the individual archive notes.)

## Ahmad-authored messages (sender = Ahmad)

Across both archives before dedup, ~784 messages are authored by Ahmad himself (sender matches `23200` or `alshahri015`). The drafts track — written by Ahmad and saved rather than sent — is the **10-year archive of his own voice**, spanning 2015-10-19 to 2026-03-01.

## Primary search surface

Query `D:\pst-archive-merged\search\messages.sqlite` via `D:\pst-archive-merged\search\search.py`. Same FTS5 Arabic-aware tokenizer as the source archives. Example queries in the README at `D:\pst-archive-merged\README.md`.

The merged DB adds two columns not present in source DBs:

- `source_archive` — `'PST-A'` or `'PST-C'` (traces each row to origin).
- `fingerprint` — MD5 of `date|sender|subject` (enables dedup + cross-archive diffs).

## Gaps (confirmed, not hypothetical)

1. **Active inbox/sent traffic pre-2023-11 is not in any local PST.** It either never survived Outlook's online sync or lives in the OneDrive files that are currently cloud-only placeholders (Google Takeout mbox, 4.2 GB; two `backupahmad.pst` files, 1 GB each).
2. **No contacts / calendar folders in the merged DB** — the extraction captured the 5 mail folders only. To add contacts/calendar, re-run extraction with a walker that includes `IPF.Appointment` and `IPF.Contact` container classes.
3. **Attachment bodies not indexed** — only attachment filenames are in FTS. Content of PDFs/DOCX/XLSX attachments is not searchable; extraction into a text index is a separate job.

## Retrieval rules

- **Default to this archive** for any email-history question. Sibling archives ([[pst-mailbox-hrsd]], [[pst-mailbox-hrsd-snapshot-a]]) remain documented and separately searchable, but the merged DB is the single point of entry.
- When a result's `source_archive` matters (e.g., for provenance in a formal document), include it in the citation.
- For MOSA/MLSD-era context (pre-2020), remember that what survives is **what Ahmad wrote** (drafts), not what he received. Inbound MOSA/MLSD traffic is missing.

## Provenance

Built 2026-04-25 after Ahmad's directive to re-search the local drives for backup email. Three custom tools produced in `C:\Users\aass1\.claude\plans\`:

- `pst_recon.py` — fast structure/date recon without body extraction.
- `pst_archive_diff.py` — fingerprint-level cross-archive diff.
- `pst_archive_merge.py` — build the merged FTS5 DB.

All three are re-runnable. See external README at `D:\pst-archive-merged\README.md` for rebuild steps.
