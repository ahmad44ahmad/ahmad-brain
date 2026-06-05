---
id: pst-mailbox-hrsd-snapshot-d2
title: PST Mailbox Snapshot D2 — the gap-closer (2025-01-09 → 2025-03-05 inbox)
type: source
status: active
aliases:
  - pst-d2
  - pst-archive-d2
  - backupahmad-pst
tags:
  - pst
  - mailbox
  - hrsd-email
  - gap-closer
  - full-extraction
created: 2026-04-25
updated: 2026-04-25
valid_from: 2024-05-13
learned_at: 2026-04-25
confidence: high
source: local:D:\My_Files\rename document library\أرشيف\أرشيف Google Drive\aass112001@gmail.com - Google Drive\backupahmad.pst
related:
  - "[[pst-mailbox-hrsd]]"
  - "[[pst-mailbox-hrsd-snapshot-a]]"
  - "[[pst-mailbox-hrsd-merged]]"
  - "[[pst-archive-2023-2026]]"
summary: >-
  Third PST archive of Ahmad's HRSD mailbox, extracted 2026-04-25 from a
  Google Drive backup that had been archived locally under
  rename document library/أرشيف/. 1,732 messages across inbox + drafts only
  (no sent folder). Inbox 2024-05-13 → 2025-04-10 — critically fills the
  7-week gap between PST-A (ends 2025-01-09) and PST-C (starts 2025-03-02).
  Contributed 337 unique messages to the merged archive.
---

# PST Mailbox Snapshot D2 — the gap-closer

## Provenance

- **Raw PST:** `D:\My_Files\rename document library\أرشيف\أرشيف Google Drive\aass112001@gmail.com - Google Drive\backupahmad.pst` (1.07 GB). Identical copy at `.../متفرقات/backupahmad.pst` (same md5).
- **Extracted:** 2026-04-25 via `pst_export_mbox.py`.
- **Indexed:** `D:\pst-archive-d2\search\messages.sqlite` (12 MB, FTS5 Arabic-aware).
- **README:** `D:\pst-archive-d2\README.md` (not written — uses the parent pattern).
- **Merged into:** [[pst-mailbox-hrsd-merged]].

## Why this matters

Prior to this extraction, the merged archive had a visible gap: PST-A's inbox ended 2025-01-09, PST-C's inbox started 2025-03-02, leaving a ~7-week hole during which Ahmad's email traffic was unrepresented. PST-D2 closed exactly that gap:

- **Inbox window: 2024-05-13 → 2025-04-10** (1,505 raw; 322 unique added after dedup).
- **Drafts: 2024-01-03 → 2025-02-27** (227 raw; 15 unique added).

Most of PST-D2 overlaps PST-A — but the post-2025-01-09 portion is unique and bridges cleanly into PST-C's 2025-03 start.

## Structure

Only 2 folders populated (unusual — no sent, no deleted):

| Folder | Count | Earliest | Latest |
|---|---|---|---|
| inbox | 1,505 | 2024-05-13 | 2025-04-10 |
| drafts | 227 | 2015-10-19 | 2025-03-19 |

No sent folder in this snapshot — Ahmad's outgoing traffic from Jan-April 2025 still has no local source (PST-A's sent ends 2025-01-05; PST-C's sent starts 2025-03-03).

## Relationship to siblings

| Archive | Inbox window | Gap closed? |
|---|---|---|
| PST-A | 2023-11-13 → 2025-01-09 | no |
| PST-D2 | 2024-05-13 → 2025-04-10 | **yes — fills PST-A → PST-C gap** |
| PST-C | 2025-03-02 → 2026-03-01 | no |

Combined inbox coverage across all three: **2023-11-13 → 2026-03-01, continuous**.

## Where the file was hiding

The archive directory tree `D:\My_Files\rename document library\أرشيف\أرشيف Google Drive\aass112001@gmail.com - Google Drive\` mirrors Ahmad's old Google Drive backup taken before OneDrive use (date shows copy operation, not original). The `backupahmad.pst` naming suggests it's a deliberate manual backup. Confirmed by Ahmad on 2026-04-25: he backs up with Windows monthly, which explains the dated snapshots in `999 *` folders and the archive mirror in `rename document library/أرشيف/`.

My earlier vault claim that "only two distinct PST content sets exist locally" was wrong — this and [[pst-mailbox-hrsd-snapshot-d3]] were hiding in the deeper archive tree and the background find that enumerated them completed silently.

## Ahmad-authored messages

Across PST-D2 raw:

- Inbox: not all are Ahmad-sender (this folder reflects received items).
- Drafts: 227 drafts, many Ahmad-authored as `A.A.Alshahri015@hrsd.gov.sa`. The 2015-10-19 draft is the same earliest-draft anchor seen in PST-A (Ahmad as `23200@mosa.gov.sa`).

## Search

Either query PST-D2 directly or use the merged archive (recommended):

```bash
# Query merged archive filtered to PST-D2 rows
python -c "
import sqlite3
db = sqlite3.connect(r'D:\pst-archive-merged\search\messages.sqlite')
for r in db.execute(\"SELECT date, folder, sender_email, subject FROM messages WHERE source_archive='PST-D2' ORDER BY date LIMIT 20\").fetchall():
    print(r)
"

# Or direct against D2 only
python D:/pst-archive/search/search.py "$@" \
    # (copy the search.py pattern to /d/pst-archive-d2/search/ for direct D2 queries)
```

## Provenance of this note

Written 2026-04-25 after discovering the deeper archive tree. Superseded as primary query surface by [[pst-mailbox-hrsd-merged]].
