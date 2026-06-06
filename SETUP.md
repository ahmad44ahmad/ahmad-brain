# ahmad-brain — AI & Google Bridge: SETUP

> **For any future Claude Code session:** this file documents how the vault is wired to Git/GitHub,
> to AI agents (MCP), and to Google Drive / NotebookLM. Built 2026-06-06. Idempotent — safe to re-run.

This vault (`C:\dev\ahmad-brain`) is an English-first "second brain" (LLM-oriented; Arabic source
material lives only under `raw/`). It is exposed to AI tools through **three independent channels**,
all kept current automatically.

---

## 1. Architecture at a glance

```
                         C:\dev\ahmad-brain  (the vault — source of truth)
                                   |
         +-------------------------+--------------------------+
         |                         |                          |
   [A] Git / GitHub          [B] MCP server            [C] Google Drive mirror
   private repo +            @bitbonsai/mcpvault        rclone sync (hourly)
   15-min auto-push          (read-only) for            -> gdrive-albahah:ObsidianVault
   (version history +        Claude Code / any                |
    cloud backup)            MCP AI client                    +-- whole vault (for Gemini)
                                                              +-- _export/ahmad-brain-combined.md      (distilled)
                                                              +-- _export/ahmad-brain-combined-full.md (incl. raw/)
```

Automation scripts live **outside** the vault at `C:\dev\ahmad-brain-bridge\` so they are never
committed into the vault or synced to Drive.

---

## 2. Components & paths

| Component | Path |
|---|---|
| Vault | `C:\dev\ahmad-brain` |
| Bridge scripts | `C:\dev\ahmad-brain-bridge\` |
| Logs | `C:\dev\ahmad-brain-bridge\logs\` |
| Backups (zips) | `C:\Users\aass1\backups\ahmad-brain\` |
| Combined exports (NotebookLM) | `_export\ahmad-brain-combined.md` (distilled) + `_export\ahmad-brain-combined-full.md` (incl. `raw/`); both gitignored |
| GitHub repo | `https://github.com/ahmad44ahmad/ahmad-brain` (**private**) |
| Drive folder | `gdrive-albahah:ObsidianVault` (Google account `admin@albahah.app`) |

Absolute tool paths used by the scheduled scripts (so they work outside an interactive shell):
- git: `C:\Program Files\Git\mingw64\bin\git.exe`
- rclone: `C:\Users\aass1\AppData\Local\Microsoft\WinGet\Links\rclone.exe`
- python: `C:\Users\aass1\scoop\apps\python312\current\python.exe`

---

## 3. The three channels — how to use each

### [A] Claude Code / Git history
Just edit notes. Every 15 minutes a hidden task commits and pushes any changes.
Manual sync anytime: `powershell -File C:\dev\ahmad-brain-bridge\git-autosync.ps1`

### [B] Claude Code (or any MCP AI) reading the vault — `ahmad_brain` MCP server
Registered in `~/.claude.json` (user scope). In a **new** Claude Code session, the tools
`mcp__ahmad_brain__read_note`, `search_notes`, `list_directory`, `read_multiple_notes`,
`get_frontmatter`, `get_notes_info`, `get_vault_stats`, `list_all_tags` are available.
Example: ask Claude "search my ahmad-brain vault for the Basira compass."

**Read-only by design.** The 7 mutating tools (`write_note`, `patch_note`, `delete_note`,
`move_note`, `move_file`, `update_frontmatter`, `manage_tags`) are blocked via
`permissions.deny` in `~/.claude\settings.json`. To enable writing later, remove those entries.

### [C] Gemini (browser) & NotebookLM — via Google Drive
Hourly, the vault is mirrored to `gdrive-albahah:ObsidianVault` and TWO combined Markdown files
are regenerated into `_export/`:
- `ahmad-brain-combined.md` — **distilled** (English-first: wiki/decisions/index/log, ~1.2 MB).
- `ahmad-brain-combined-full.md` — **full**, also includes `raw/` Arabic sources (~3 MB).

- **Gemini in the browser:** it sees the whole vault under Drive › `ObsidianVault` (signed in as
  `admin@albahah.app`). Use "@" / Drive context to reference notes.
- **NotebookLM:** *Add source → Upload* whichever fits the notebook — the local files at
  `C:\dev\ahmad-brain\_export\ahmad-brain-combined*.md` (NotebookLM accepts Markdown). Use the
  distilled file for focused Q&A; the full file when you need the Arabic source material too.
  For Drive-native import (Docs/PDF only), see §7 to add a PDF.

---

## 4. Scheduled tasks (Windows Task Scheduler, current user, hidden)

| Task name | Every | Action |
|---|---|---|
| `AhmadBrain GitAutoSync` | 15 min | commit + push if the vault changed |
| `AhmadBrain DriveSync` | 60 min | rebuild combined.md + rclone sync vault → Drive |

Each runs a `.vbs` launcher (`*-hidden.vbs`) so no console window appears.
Inspect / run manually:
```
schtasks /Query /TN "AhmadBrain GitAutoSync" /V /FO LIST
schtasks /Run   /TN "AhmadBrain DriveSync"
```
Disable / remove:
```
schtasks /Change /TN "AhmadBrain DriveSync" /DISABLE
schtasks /Delete /TN "AhmadBrain DriveSync" /F
```

---

## 5. Google Drive remote

Remote `gdrive-albahah:` (rclone, full `drive` scope, account `admin@albahah.app`).
Re-create the OAuth if it ever expires:
```
rclone config reconnect gdrive-albahah:
```
The sync excludes `.git`, `.obsidian`, `.trash`, and secret patterns (`.env*`, `*.key`, `*.pem`,
`*.pfx`, Office lock files) so nothing sensitive leaves the machine.

> **Note:** a separate, older `gdrive:` remote also exists (holds Basira backups etc.). This bridge
> deliberately uses its own `gdrive-albahah:` remote and does not touch `gdrive:`.

---

## 6. Backups

A full compressed snapshot was taken before setup at
`C:\Users\aass1\backups\ahmad-brain\ahmad-brain-backup-<timestamp>.tgz`.
Make a fresh one anytime:
```
tar -czf "C:/Users/aass1/backups/ahmad-brain/ahmad-brain-backup-$(date +%Y%m%d-%H%M%S).tgz" -C /c/dev ahmad-brain
```
(Git/GitHub is the live version history; these zips are belt-and-suspenders.)

---

## 7. Optional: PDF for NotebookLM Drive-import

No PDF engine is installed (Markdown upload covers NotebookLM). To add PDF generation later:
```
winget install --id wkhtmltopdf.wkhtmltopdf
pandoc "C:\dev\ahmad-brain\_export\ahmad-brain-combined.md" -o "C:\dev\ahmad-brain\_export\ahmad-brain-combined.pdf"
```
(pandoc 3.9 is already installed.) Then the PDF mirrors to Drive on the next hourly sync.

---

## 8. Verify everything (health check)

```powershell
# A — git pushed & clean
& 'C:\Program Files\Git\mingw64\bin\git.exe' -C C:\dev\ahmad-brain status -s
& 'C:\Program Files\Git\mingw64\bin\git.exe' -C C:\dev\ahmad-brain rev-list --count origin/main..main   # expect 0

# B — MCP reads (standalone probe)
node C:\dev\ahmad-brain-bridge\mcp-probe.mjs C:\dev\ahmad-brain

# C — Drive folder reachable + combined present
rclone lsf gdrive-albahah:ObsidianVault/_export/

# tasks
schtasks /Query | findstr AhmadBrain
```

---

## 9. Troubleshooting

- **Scheduled push not happening:** check `logs\git-autosync.log`. Credential helper is `gh`
  (`gh auth status` must be logged in). Re-run `gh auth setup-git` if needed.
- **Drive sync failing:** check `logs\drive-sync.log`. Re-auth with `rclone config reconnect gdrive-albahah:`.
- **MCP tools missing in Claude Code:** they only load at session start — restart the session.
  Confirm with `claude mcp list` (should show `ahmad_brain ... ✓ Connected`).
- **A console window flashes:** ensure the task action is `wscript.exe "...-hidden.vbs"`, not
  `powershell ...` directly.
