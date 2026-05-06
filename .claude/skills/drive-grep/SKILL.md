---
name: drive-grep
description: Query the Drive catalog and the 68-folder Gemini summaries by pattern. Use when Ahmad asks about a specific Drive file/folder, when you need to locate a fileId from a partial title, or when surveying what's been catalogued without re-running expensive MCP searches.
---

# Drive-grep Skill

A small offline query tool over the vault's Drive sources:

- `wiki/sources/drive-catalog.md` — high-signal file index (~80 files + folders cataloged)
- `wiki/sources/drive-folders-master-index.md` — flat list of 68 Drive folders + idx
- `C:\Users\aass1\ahmad-brain-import\drive-folders-gemini.jsonl` — full Gemini summaries per folder (~324k chars across 68 entries)

Use this **before** running new Drive MCP searches — most of the time the answer is already in the catalog.

## Usage

```bash
python C:\dev\ahmad-brain\.claude\skills\drive-grep\drive_grep.py <subcommand> <pattern>
```

### Subcommands

- `catalog <pattern>` — grep the file titles in `drive-catalog.md` for a substring (case-insensitive). Returns matching rows with `fileId`.
- `folders <pattern>` — grep the 68 folder names in `drive-folders-master-index.md` for a substring. Returns folder name + idx number.
- `summary <idx>` — pull the full Gemini summary for a specific folder by idx number from the JSONL.
- `summary-grep <pattern>` — search the *content* of all 68 Gemini summaries for a pattern (slower, scans 324KB). Returns idx + folder name + matching line.
- `inventory <pattern>` — grep the full-inventory.tsv (filename + size + mtime catalog of ~833 Drive items, cached locally at `raw/drive/full-inventory.tsv`). Returns matching rows. Use to locate a specific filename across the entire surveyed Drive content.

### Examples

```bash
# Find KPI-related files in catalog
python drive_grep.py catalog kpi

# Find folder by partial Arabic name
python drive_grep.py folders 'مكافحة العدوى'

# Pull full Gemini summary for folder 4
python drive_grep.py summary 4

# Search all summaries for a topic
python drive_grep.py summary-grep 'سلامة المستفيدين'

# Find a specific file in the full-inventory catalog
python drive_grep.py inventory 'BICSL-RC'
python drive_grep.py inventory 'تعميم'
```

## When to fall back to Drive MCP

This skill is offline-first. Use Drive MCP (`search_files`, `read_file_content`) when:

- The pattern returns 0 hits across all three sources (file may not have been catalogued yet).
- You need to *read* a file's content, not just locate it.
- The user wants the latest state of a folder (catalog reflects last ingestion, not live Drive state).

## Maintenance

The catalog is updated by hand whenever new Drive files are ingested. The JSONL is a one-time export from a Gemini-narrated session and won't auto-refresh; if folder structure changes significantly, regenerate it via the procedure documented in [[drive-folders-master-index]].
