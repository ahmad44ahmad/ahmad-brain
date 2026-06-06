# Vault Write-Protection Policy

**Status:** active · **Established:** 2026-06-06 · **Scope (chosen by Ahmad):** root files + `raw/` are read-only; `wiki/ decisions/ log/ index/` stay writable (Option A).

## Why this exists

The vault is LLM-only (see `_CLAUDE.md` / [[0001-vault-architecture]]). A write-protection test on 2026-06-06 found that while the `ahmad_brain` MCP server (read-only — exposes no write tools, and its hypothetical write tool-names are pre-denied in `~/.claude/settings.json`) and the home-scoped `filesystem` MCP server both **refuse** to write here, the agent's **built-in `Write` tool** could create an arbitrary file at the vault root (`_write_test.md`) with no guard. That is the leak this policy closes. The pre-existing root litter (`Untitled*.canvas`, `SETUP.md.bak.*`) is evidence the same class of stray write had landed before.

## What is protected, and how

Two mechanisms, because a permission deny-glob can only block a **whole subtree**, not "root files only":

1. **`raw/` — deny-glob (fail-closed).** `permissions.deny` blocks `Write/Edit/MultiEdit/NotebookEdit(//c/dev/ahmad-brain/raw/**)`. `raw/` is immutable by the vault contract ("Raw is immutable" — `_CLAUDE.md`). Robust because it does not depend on a script.
2. **Vault root — `PreToolUse` hook `vault-write-guard.js`.** Blocks the built-in edit tools from creating/editing files **directly at the vault root**, *except* the two files that legitimately live there: `_CLAUDE.md` and `README.md`. Subdirectories (`wiki/`, `decisions/`, `log/`, `index/`, `.claude/`, …) pass straight through, so legitimate enrichment is unaffected.

### Why root needs a hook, not a glob

Empirically verified on this Claude Code version (2026-06-06): a path deny like `Write(//c/dev/ahmad-brain/*)` matches the **entire subtree** — it blocked `wiki/` and `log/` writes, not just root files. So "root-only, with `_CLAUDE.md`/`README.md` exceptions" is **not expressible as a glob** and must be a hook. (`deny` also cannot be re-allowed by a child `allow` rule, so the "deny subtree then allow wiki" approach is impossible too.)

## What stays writable (by design)

`wiki/ decisions/ log/ index/` — the legitimate enrichment targets per the `_CLAUDE.md` "When to write where" contract. Option A deliberately does **not** freeze them. Editing `_CLAUDE.md` / `README.md` at root is also still allowed (allowlist).

## Where the rules live (two copies, different jobs)

| Copy | Path | Loaded when | Version-controlled? |
|---|---|---|---|
| **Enforcing** | `~/.claude/settings.json` (raw deny-glob) + `~/.claude/claude-hooks/vault-write-guard.js` (firing hook) | **Every** session, any cwd | settings.json: **No** (git-ignored on purpose — may hold MCP tokens; see `~/.claude/.gitignore`). Hook: yes, in the `~/.claude` git repo |
| **Record (this repo)** | `.claude/settings.json` + `.claude/hooks/vault-write-guard.js` (byte-identical to the firing hook) + this file | Only sessions whose cwd **is** the vault | **Yes** — tracked in the vault git repo |

Claude Code does **not** load permission rules or hooks from non-cwd / additional directories, so a copy living only inside the vault would **not** protect a session rooted elsewhere (e.g. `C:\Users\aass1`). The enforcing copy therefore has to live in `~/.claude`; the vault copy is the auditable, version-controlled record (and a redundant active guard for vault-rooted sessions, wired via `${CLAUDE_PROJECT_DIR}`). **Keep the hook copies and the raw deny-arrays in sync.**

## Residual gaps (not closed here)

- **`Bash`-based and subprocess writes** (`echo > file`, a Python/Node script's `open()`): the hook only sees the built-in edit tools, and `deny`-globs only extend to a few recognized Bash file-commands — not arbitrary subprocesses or every path spelling. Intentionally **not** papered over with a leaky Bash blocklist (false confidence). To close this at the OS level, add a sandbox filesystem write-deny for `//c/dev/ahmad-brain/**` — *verify the current key/syntax against Claude Code docs before enabling*, as it changes Bash sandbox behavior broadly.

## Verification (2026-06-06)

Hook unit-tested across all branches (root-junk → deny, `_CLAUDE.md`/`README.md` → allow, `wiki`/`decisions`/`.claude` → allow, `raw/**` → deny, gitbash `/c/..` paths → deny, outside-vault → allow, malformed input → fail-open). Live end-to-end through the real harness:

| Live built-in `Write` | Result |
|---|---|
| vault root `_write_test.md` | **denied** by the hook |
| `wiki/_probe_del.md` | **allowed** (then deleted) |
| `raw/_probe_del.md` | **denied** by the deny-glob |

A guard is only real if the previously-succeeding write now fails — demonstrated above. Permission rules + hooks load at session start; this session picked them up via hot-reload, but to re-confirm in a fresh session ask, from any cwd: *"Use your built-in Write tool to create `C:\dev\ahmad-brain\_write_test.md` with content test"* → expect **denied**.
