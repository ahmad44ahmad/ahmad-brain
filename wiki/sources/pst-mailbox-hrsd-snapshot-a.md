---
id: pst-mailbox-hrsd-snapshot-a
title: PST Mailbox Snapshot A — 2025-06-15 (covers 2023-11 → 2025-01)
type: source
status: active
aliases:
  - pst-a
  - pst-archive-a
  - pst-mailbox-2025-06
tags:
  - pst
  - exchange
  - mailbox
  - hrsd-email
  - mosa-era
  - mlsd-era
  - full-extraction
created: 2026-04-24
updated: 2026-04-24
valid_from: 2023-10-12
learned_at: 2026-04-24
confidence: high
source: local:D:\My_Files\01_Documents\999 15 6 2025\backup.pst
related:
  - "[[pst-mailbox-hrsd]]"
  - "[[pst-mailbox-hrsd-merged]]"
  - "[[pst-archive-2023-2026]]"
  - "[[sent-mbox-hrsd]]"
  - "[[ahmad-career-arc]]"
  - "[[mhrsd-era-timeline]]"
summary: >-
  Second PST archive of Ahmad's HRSD mailbox, extracted 2026-04-24 from a
  2025-06-15 Outlook snapshot. 3,659 messages across 5 folders. Dovetails
  with (not overlaps) pst-mailbox-hrsd. Drafts folder reaches back to
  2015-10-19 (MOSA era, 23200@mosa.gov.sa — Ahmad's own employee ID).
  Full FTS5 index at D:\pst-archive-a\search\messages.sqlite. Superseded
  as primary query surface by [[pst-mailbox-hrsd-merged]].
---

# PST Mailbox Snapshot A — 2025-06-15

## Provenance

- **Raw PST:** `D:\My_Files\01_Documents\999 15 6 2025\backup.pst` (1.9 GB). Duplicate at `D:\My_Files\01_Documents\999 27-10-2025\backup.pst` (identical md5). A near-duplicate at `D:\My_Files\01_Documents\999 27-10-2025\backup (2).pst` has a different md5 but identical folder-level stats (3,659 messages, same per-folder counts, same date ranges to the millisecond) — treated as content-equivalent.
- **Extracted:** 2026-04-24 via `C:\Users\aass1\.claude\plans\pst_export_mbox.py` (Aspose.Email, licensed).
- **Indexed:** `D:\pst-archive-a\search\messages.sqlite` (32 MB, FTS5 with Arabic-aware tokenizer).
- **README:** `D:\pst-archive-a\README.md`.

## Why this matters

Resolves Ahmad's long-standing claim that his mailbox contains "7–8 years of email history" that the earlier PST-C analysis did not reflect. Two rolling snapshots of the same mailbox dovetail to give continuous coverage of the active work period, and the Drafts + Deleted folders in both snapshots reach back significantly further than the Inbox.

## Coverage (per folder)

| Folder | Count | Earliest | Latest |
|---|---|---|---|
| inbox | 3,073 | 2023-11-13 | 2025-01-09 |
| sent | 165 | 2023-11-14 | 2025-01-05 |
| drafts | **410** | **2015-10-19** | 2025-01-09 |
| deleted | 1 | 2024-12-04 | 2024-12-04 |
| sync-issues | 10 | 2023-10-12 | 2023-11-26 |

## Relationship to [[pst-mailbox-hrsd]] (PST-C)

| Archive | Inbox window | Sent window | Drafts window | Deleted window |
|---|---|---|---|---|
| PST-A (this) | 2023-11-13 → 2025-01-09 | 2023-11-14 → 2025-01-05 | 2015-10-19 → 2025-01-09 | 2024-12-04 |
| PST-C (existing) | 2025-03-02 → 2026-03-01 | 2025-03-03 → 2026-02-23 | 2025-10-01 → 2026-03-01 | 2019-04-25 → 2026-02-21 |

**The two snapshots dovetail.** Inbox windows do not overlap (PST-A ends 2025-01-09; PST-C starts 2025-03-02 — a ~7-week gap where the mailbox was presumably archived and started fresh). Fingerprint overlap between the two DBs is **5 messages** — the five sync-issue items common to both.

Combined coverage: active inbox/sent from 2023-11 → 2026-03 (≈ 28 months), plus fragmentary older history in Drafts and Deleted.

## Pre-2023 content (MOSA/MLSD era — partial verification)

Year-by-year distribution of pre-2023 messages in PST-A Drafts:

| Year | Drafts | Note |
|---|---|---|
| 2015 | 4 | **MOSA era.** Forwards from `23200@mosa.gov.sa` re الرعاية النهارية (elderly daycare). Earliest: 2015-10-19. |
| 2016 | 36 | |
| 2017 | 2 | |
| 2018 | 2 | |
| 2019 | 42 | **MLSD era.** Includes MLSD-domain traffic (see PST-C deleted for MLSD inbox items). |
| 2020 | 40 | |
| 2021 | 112 | |
| 2022 | 34 | Pre-cutover to the PST-C window. |

PST-C's Deleted folder also contains pre-2023 items: 2 in 2019 (earliest `TABS@mlsd.gov.sa` forward 2019-04-25), 2 in 2020, 1 in 2021, 21 in 2022.

**What this means.** Ahmad's mailbox history pre-2023 exists but is **fragmentary** in the local PSTs — it survives as drafts (items he composed or forwarded to himself) and in the Deleted folder, not as the full inbox/sent traffic. The 2020 event Ahmad remembers (Kingdom-level PT Services Supervisor meeting) might exist as a draft in PST-A; worth a targeted search. Full pre-2023 inbox/sent is more likely in the Google Takeout mbox (4.2 GB, currently OneDrive cloud-only).

## Search examples

```bash
# MOSA-era drafts (2015-2016)
python D:/pst-archive/search/search.py --db D:/pst-archive-a/search/messages.sqlite \
    --folder drafts --since 2015-01-01 --until 2016-12-31 --show-body

# Anything from mlsd.gov.sa domain
python D:/pst-archive/search/search.py --db D:/pst-archive-a/search/messages.sqlite \
    "sender_email:mlsd"
```

## Cross-archive diff

`C:\Users\aass1\.claude\plans\pst_archive_diff.py` compares fingerprints (date + sender + subject) between any two archive DBs. For PST-A vs PST-C:

- Unique to PST-A: 2,144 fingerprints (inbox 1,827; drafts 208; sent 108; deleted 1).
- Unique to PST-C: 2,330 fingerprints (inbox 2,125; deleted 119; sent 51; drafts 35).
- Overlap: 5 (the sync-issues).

## Action items surfaced

- [ ] Targeted search for the 2020 Kingdom-level PT Supervisor meeting in PST-A drafts (Ahmad's memory anchor, previously "not recoverable").
- [ ] Signature extraction from pre-2023 drafts — could populate titles/emails for people from the MOSA/MLSD era not yet in the [[hrsd-work]] people orbit.
- [ ] Cross-reference MOSA-era `23200@mosa.gov.sa` to identify the sender persona (a person or a shared ministry account?).
- [ ] Once OneDrive Takeout mbox is synced to disk (4.2 GB, currently cloud-only), parse directly with Python `mailbox` module — no Aspose required — and merge fingerprints to see whether it fills the pre-2023 inbox/sent gap.

## Gaps

- No Calendar or Contacts folders captured in this extraction (the PST recon showed only the 5 mail folders were populated at recon time; no IPF.Appointment or IPF.Contact folders were enumerated).
- Attachments preserved inside MBOX (base64). Individual extraction into `D:\pst-archive-a\attachments\` is on-demand.

## Provenance of this note

Written 2026-04-24 after the PST-A extraction + index + diff analysis. Upstream memory: none (this is native vault content, not migrated from a memory stub).
