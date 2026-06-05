---
id: pst-archive-2023-2026
title: PST Email Archive 2023–2026 — Full-Body Thematic Extract (the "jewel")
type: source
status: active
aliases:
  - pst-email-archive
  - pst-archive-deep
  - the-email-jewel
  - 2167-email-archive
tags:
  - pst
  - mailbox
  - hrsd-email
  - full-body
  - thematic-harvest
  - primary-content-surface
created: 2026-06-05
updated: 2026-06-05
valid_from: 2025-03-02
learned_at: 2026-06-05
confidence: high
source: local:C:\Users\aass1\Desktop\PST-Email-Archive\
related:
  - "[[pst-mailbox-hrsd-merged]]"
  - "[[pst-mailbox-hrsd]]"
  - "[[sent-mbox-hrsd]]"
  - "[[ahmad-mhrsd-arc-2023-2026]]"
  - "[[absence-deduction-dispute]]"
  - "[[ahmad-career-arc]]"
  - "[[hrsd-work]]"
summary: >-
  Full-body extract + 9-cluster thematic harvest + 11-thread synthesis of a
  2,167-email PST (PST-C working backup), 2026-06-05. Unlike the metadata-only
  [[pst-mailbox-hrsd-merged]], this one has decoded BODIES — the deep-content
  surface for the 2025-dense window. Real content window 2025-03 → 2026-03
  (zero 2024 = export boundary, not a quiet year). Local-only, redacted, never
  pushed. The source-of-record for the email→brain fold.
---

# PST Email Archive 2023–2026 — the deep-content surface

## What this is, and why it is not a duplicate of the merged archive

A fresh 2026-06-05 extraction of one PST (`D:\pst-export\ملف بيانات Outlook`, the PST-C working backup) into
**2,167 per-email text files + a manifest + a 9-cluster thematic harvest + an 11-thread synthesis**. Its
distinguishing property is **decoded message bodies** — the actual content of the threads, not just headers.

This is the complement of [[pst-mailbox-hrsd-merged]], not a replacement:

| | [[pst-mailbox-hrsd-merged]] | **this archive** |
|---|---|---|
| Shape | Metadata / FTS search index | Full bodies + thematic distillation |
| Window | **2015 → 2026** (broad envelope) | **2025-03 → 2026-03** (narrow, dense) |
| 2024 | **1,635 messages** (present) | **zero** (export boundary) |
| Pre-2023 | drafts back to 2015 (Ahmad's voice) | none |
| Best for | "did an email exist / when / from whom" | "what did the thread actually say / decide" |

**Retrieval rule:** for *content* of any 2025-03 → 2026-03 thread, use this archive. For *existence/date* of any
email 2015–2026 (especially 2024 and pre-2023), use the merged archive. Cite both when provenance matters.

## The zero-2024 export boundary (do not misread as a quiet year)

The manifest's year distribution is 2023-10 (1) · 2023-11 (4) · **hard gap** · 2025-03 → 2026-03 (continuous).
2024 is absent **because this single PST export does not contain it**, not because Ahmad was inactive — the merged
archive proves 1,635 messages in 2024 (his most active documented year). Any narrative built from this archive alone
must pull 2024 + pre-2023 from the merged note, or it encodes a false silence. See [[ahmad-mhrsd-arc-2023-2026]] for
the fused, source-labelled timeline.

## Corpus stats (from `00-INDEX.md`)

- **2,167 emails**, 0 parse errors. By folder: Inbox 1857 · Sent 142 · Drafts 102 · Deleted 61 · Sync 5.
- 1,704 emails carry 4,420 attachments (listed in manifest, **not extracted** — they remain inside the `.eml`).
- Also in the source folder, not processed: 606 contacts (.vcf) + 312 calendar (.ics).
- Owner-mailbox signature in-body: `a.a.alshahri015@hrsd.gov.sa` — *"أخصائي علاج طبيعي / مسؤول الجودة ومكافحة العدوى"*.

## The 9 clusters (workflow `wf_b1509b92-e76`)

SIGNAL: `01_sent` (142, Ahmad's outbound) · `02_drafts` (102, ~35 unique unsent — grievances, building-safety,
reform letters) · `03_inbox_human` (301, the real inbox) · `06_hrsd_broadcasts_regional` (197, ~16 directed tasks).
Noise: `04_ic_broadcasts` (970 all-staff) · `05_notifications` (383) · `07_bounces` (6, +1 misfiled OH&S proposal) ·
`08_deleted` (61, +2 private-venting do-NOT-circulate) · `09_sync` (5).

## The 11 threads (from `01-ARCHIVE-SYNTHESIS.md`)

The spine of the fold. In brief: §1 the **absence-deduction/fingerprint dispute** (dominant, OPEN →
[[absence-deduction-dispute]]) · §2 quality-dept leadership + the 2025 appraisal (155% → [[ahmad-2025-achievements]],
[[hrsd-pms]]) · §3 Zero-Paper/Basira's documented origin ([[basira]]) · §4 building/OH&S safety (the 23-observation
Civil-Defense escalation; the OH&S framework proposal) · §5 IPC trainer/assessor accreditation ([[al-baha-ic-archive]]) ·
§6 the 74-indicator disability-standards reporting · §7 HR grievances + reform letters · §8 finance/custody · §9 the
correspondents (now [[abdulaziz-alghamdi]], [[adel-alghamdi]], [[saeed-alghamdi]], [[tami-alelyani]],
[[nora-alqahtani]], [[awad-alshahri-safety]], plus [[ali-alqarni]], [[khalid-alzahrani]]) · §10 sensitive/private ·
§11 the dated open-items payload.

## Provenance + handling

- Raw PST: `D:\pst-export\ملف بيانات Outlook`. Extract + KB: `C:\Users\aass1\Desktop\PST-Email-Archive\`
  (`00-INDEX.md`, `01-ARCHIVE-SYNTHESIS.md`, `harvest\01..09_*.md`, `text\<folder>\<id>.txt`, `manifest.csv/json`).
- **Private, local-only, never committed/pushed.** Beneficiary names/IDs, national-IDs, medical specifics, and
  credentials are redacted in all summaries. Two Deleted-folder records (≈2025-04-16) are flagged
  *do-NOT-circulate* (personal venting); their substance is captured as self-context, their carrier is not surfaced.
- This vault note is the distillation; the redacted harvest files are the citable detail; the raw `text\` bodies
  are the immutable evidence layer (read, never quote third-party PHI out of them).

## Relationship to the older sampled PST notes

[[pst-mailbox-hrsd]] (50-item-per-folder sampled), [[pst-mailbox-hrsd-snapshot-a]], `-snapshot-d2`, `-snapshot-d3`
were the earlier *partial* reads. They retain provenance value (where the PSTs live on disk + the merge tooling) but
are **superseded as the primary content surface** by this archive. The **merged** note remains the primary *search*
surface. See [[ahmad-mhrsd-arc-2023-2026]] §sources for the full reconciliation.
