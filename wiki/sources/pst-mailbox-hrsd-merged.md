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
updated: 2026-06-05
valid_from: 2015-10-19
learned_at: 2026-04-25
confidence: high
source: merged:D:\pst-archive\ + D:\pst-archive-a\
related:
  - "[[pst-mailbox-hrsd]]"
  - "[[pst-archive-2023-2026]]"
  - "[[pst-mailbox-hrsd-snapshot-a]]"
  - "[[sent-mbox-hrsd]]"
  - "[[ahmad-career-arc]]"
  - "[[hrsd-work]]"
summary: >-
  Unified FTS5 search surface across ALL four locally-extractable HRSD PST
  snapshots. 4,816 deduplicated messages spanning 2015-2026. Primary archive
  to query. Updated 2026-04-25 after discovering two more PSTs (D2, D3) in
  the rename document library archive tree. PST-D2 critically closed the
  7-week inbox gap between PST-A and PST-C. Inbox coverage now continuous
  2023-11-13 → 2026-03-01. Pre-2023 = drafts only (MOSA/MLSD era).
---

# PST Mailbox — Merged Archive (2015–2026)

## The full local picture

A second-pass exhaustive scan on 2026-04-25 (following Ahmad's correction that I'd missed a deeper archive tree) surfaced **four distinct PST content sets** locally, not two:

- **PST-A** — 2025-06-15 snapshot, duplicated across three `999 *` folders and also present under `rename document library/أرشيف/أرشيف سطح المكتب/نسخة احتياطية بريد إلكتروني.pst`.
- **PST-C** — primary working backup `backup22222 (1).pst` (hardlinked to `backup-clean.pst`).
- **PST-D2** (new) — `rename document library/أرشيف/أرشيف Google Drive/.../backupahmad.pst` (1.07 GB, 1,732 messages). **Closes the 2025-01-09 → 2025-03-05 gap** between PST-A and PST-C. See [[pst-mailbox-hrsd-snapshot-d2]].
- **PST-D3** (new) — `rename document library/أرشيف/أرشيف سطح المكتب/backup.pst` (888 MB, 1,846 messages). Strict subset of PST-A; contributed zero unique content. See [[pst-mailbox-hrsd-snapshot-d3]].

Two 271 KB `Outlook*.pst` skeletons in the same archive tree are empty shells (0 messages), ignored.

No .ost for HRSD (only a Hotmail one in AppData). No File History. No Windows Image Backup. Material pre-dating 2023-11 survives only as drafts (Ahmad's own writing) and a handful of deleted items. OneDrive has PSTs that appear as placeholders but are unreachable with OneDrive sync off.

All four archives extracted, indexed, and merged:

- `D:\pst-archive\` — PST-C, 2,582 raw messages ([[pst-mailbox-hrsd]]).
- `D:\pst-archive-a\` — PST-A, 3,659 raw messages ([[pst-mailbox-hrsd-snapshot-a]]).
- `D:\pst-archive-d2\` — PST-D2, 1,732 raw messages ([[pst-mailbox-hrsd-snapshot-d2]]).
- `D:\pst-archive-d3\` — PST-D3, 1,846 raw messages ([[pst-mailbox-hrsd-snapshot-d3]]).
- **`D:\pst-archive-merged\`** — unified deduplicated index: **4,816 unique messages**.

## Merged DB stats

Deduplication across 9,819 raw input messages → **4,816 unique** (5,003 duplicates removed).

### Per-archive contribution

| Source | Added unique | Duplicates skipped |
|---|---|---|
| PST-A | 2,149 | 1,510 |
| PST-C | 2,330 | 252 |
| PST-D2 | **337** (the gap-closer) | 1,395 |
| PST-D3 | 0 (strict subset of PST-A) | 1,846 |

### Year distribution (combined, post-PST-D2 merge)

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
| 2024 | 1,635 | active |
| 2025 | **2,311** | now continuous across all months (PST-D2 closed the Jan-March gap) |
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

1. **Active inbox/sent traffic pre-2023-11 is not in any local PST.** The four extracted snapshots confirm this. Pre-2023 content = drafts + a few deleted items (Ahmad's own writing, not what he received). The OneDrive Takeout mbox (4.2 GB placeholder) remains the strongest candidate for pre-2023 inbox if OneDrive is ever re-synced.
2. **Sent items in 2025-01-05 → 2025-03-03 are missing.** PST-D2 has inbox + drafts only (no sent folder). PST-A sent ends 2025-01-05; PST-C sent starts 2025-03-03. A 2-month sent-folder gap remains.
3. **No contacts / calendar folders in the merged DB** — the extractions captured the 5 mail folders only. To add contacts/calendar, re-run extraction with a walker that includes `IPF.Appointment` and `IPF.Contact` container classes.
4. **Attachment bodies not indexed** — only attachment filenames are in FTS. Content of PDFs/DOCX/XLSX attachments is not searchable; extraction into a text index is a separate job.

## Retrieval rules

- **Default to this archive** for any email-history question. Sibling archives ([[pst-mailbox-hrsd]], [[pst-mailbox-hrsd-snapshot-a]]) remain documented and separately searchable, but the merged DB is the single point of entry.
- **This is the metadata/search surface; for full message *bodies* of the 2025-03 → 2026-03 window, defer to the deep-content archive [[pst-archive-2023-2026]]** (complementary shape — search here, read the thread content there). The two are not duplicates: this one alone holds the 2024 + pre-2023 envelope.
- When a result's `source_archive` matters (e.g., for provenance in a formal document), include it in the citation.
- For MOSA/MLSD-era context (pre-2020), remember that what survives is **what Ahmad wrote** (drafts), not what he received. Inbound MOSA/MLSD traffic is missing.

## Provenance

Built 2026-04-25 after Ahmad's directive to re-search the local drives for backup email. Updated later the same day after Ahmad pointed out I'd missed the deeper `rename document library/أرشيف/` archive tree — a second-pass scan surfaced PST-D2 (the gap-closer) and PST-D3 (redundant but kept for provenance). Four custom tools produced in `C:\Users\aass1\.claude\plans\`:

- `pst_recon.py` — fast structure/date recon without body extraction.
- `pst_archive_diff.py` — fingerprint-level cross-archive diff.
- `pst_archive_merge.py` — original pairwise merger.
- `pst_archive_merge_n.py` — N-way merger, preserves source_archive through chained merges.

All re-runnable. See external README at `D:\pst-archive-merged\README.md` for rebuild steps.
