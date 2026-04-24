---
id: pst-mailbox-hrsd-snapshot-d3
title: PST Mailbox Snapshot D3 — subset of PST-A (no unique content)
type: source
status: active
aliases:
  - pst-d3
  - pst-archive-d3
tags:
  - pst
  - mailbox
  - hrsd-email
  - subset-snapshot
  - provenance-only
created: 2026-04-25
updated: 2026-04-25
valid_from: 2023-10-12
learned_at: 2026-04-25
confidence: high
source: local:D:\My_Files\rename document library\أرشيف\أرشيف سطح المكتب\backup.pst
related:
  - "[[pst-mailbox-hrsd-snapshot-a]]"
  - "[[pst-mailbox-hrsd-merged]]"
summary: >-
  Fourth PST archive extracted 2026-04-25 (888 MB, 1,846 messages) — confirmed
  strict subset of pst-mailbox-hrsd-snapshot-a. Zero unique content
  contributed to the merged archive. Retained in vault for provenance only;
  indicates this was the earlier-in-time snapshot that PST-A grew from.
---

# PST Mailbox Snapshot D3 — subset of PST-A

Extracted 2026-04-25 from `D:\My_Files\rename document library\أرشيف\أرشيف سطح المكتب\backup.pst` (888 MB, 1,846 raw messages). Three identical copies exist locally (same md5 `f040d030...`):

- `أرشيف Google Drive\aass112001@gmail.com - Google Drive\email backup\backup.pst`
- `أرشيف Google Drive\...\سطح مكتب\Create Prompt _ Google AI Studio_files\email backup\backup.pst`
- `أرشيف سطح المكتب\backup.pst` (extracted)

## Why this note exists

For provenance only. The 4-way merge revealed PST-D3 is a strict subset of [[pst-mailbox-hrsd-snapshot-a]]:

| Folder | D3 count | Unique added to merged |
|---|---|---|
| inbox | 1,554 | 0 |
| sent | 85 | 0 |
| drafts | 202 | 0 |
| sync-issues | 5 | 0 |
| **total** | **1,846** | **0** |

Every PST-D3 message had an identical (date + sender + subject) fingerprint already in PST-A. Date windows match PST-A exactly (inbox 2023-11-13 → 2024-10-13; sent 2023-11-14 → 2024-11-12; drafts 2015-10-19 → 2024-11-07). PST-D3 is the earlier-in-time snapshot that PST-A grew out of.

## Data on disk (for reference)

```
D:\pst-archive-d3\
├── extract.log
├── index.log
└── raw\
    ├── _index.txt
    ├── inbox.mbox     (1,554 msgs, ~)
    ├── sent.mbox      (85 msgs)
    ├── drafts.mbox    (202 msgs)
    └── sync-issues.mbox (5 msgs)
D:\pst-archive-d3\search\messages.sqlite  (18.6 MB, queryable but redundant)
```

## Action recommendation

Leave on disk for provenance but there's no need to query D3 directly — every row is in the merged archive tagged with `source_archive = 'PST-A'`. If disk space becomes a concern, D3 can be safely deleted.

## Provenance

Written 2026-04-25 after discovering and processing all four locally-extractable PSTs.
