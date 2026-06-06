#!/usr/bin/env node
// PreToolUse hook — ahmad-brain vault write-protection (Option A, chosen by Ahmad 2026-06-06).
//
// Globs can only block a whole subtree, so "root files only, with exceptions" must be a hook.
// This blocks the built-in edit tools (Write/Edit/MultiEdit/NotebookEdit) from:
//   (1) creating/editing files directly at the vault ROOT — except _CLAUDE.md and README.md, and
//   (2) anything under raw/  (immutable sources; also covered by a deny-glob backstop in settings.json).
// Everything else under the vault (wiki/ decisions/ log/ index/ .claude/ ...) and every path OUTSIDE
// the vault passes straight through. Fails OPEN on error so a hook bug never bricks editing globally.
//
// Canonical source-of-record is version-controlled in the vault at .claude/hooks/vault-write-guard.js;
// this is the firing copy. Keep them in sync. See vault .claude/WRITE-PROTECTION.md.

let input = '';
process.stdin.on('data', (c) => { input += c; });
process.stdin.on('end', () => {
  try {
    const p = JSON.parse(input || '{}');
    const tool = p.tool_name || p.tool || '';
    if (!/^(Write|Edit|MultiEdit|NotebookEdit)$/.test(tool)) { process.exit(0); }

    const ti = p.tool_input || p.input || {};
    const fp = ti.file_path || ti.path || ti.notebook_path || '';
    if (!fp) { process.exit(0); }

    // Normalize to lowercase, forward-slash, drive-letter absolute form.
    let n = String(fp).replace(/\\/g, '/');
    n = n.replace(/^\/\/([a-zA-Z])\//, '$1:/').replace(/^\/([a-zA-Z])\//, '$1:/'); // //c/.. or /c/.. -> c:/..
    n = n.toLowerCase().replace(/\/+$/, '');

    const ROOT = 'c:/dev/ahmad-brain';
    if (n !== ROOT && !n.startsWith(ROOT + '/')) { process.exit(0); } // not in the vault

    const rel = n === ROOT ? '' : n.slice(ROOT.length + 1);
    const ALLOW_ROOT = ['_claude.md', 'readme.md'];

    // (2) raw/ is immutable
    if (rel === 'raw' || rel.startsWith('raw/')) {
      return block(`Vault write-protection: raw/ is immutable (sources are append-only via a deliberate action). Refused write to "${rel}".`);
    }
    // (1) direct root file (no "/" in rel): deny unless allowlisted; subdirs pass through
    if (rel.length > 0 && !rel.includes('/')) {
      if (ALLOW_ROOT.includes(rel)) { process.exit(0); }
      return block(`Vault write-protection: only _CLAUDE.md and README.md belong at the ahmad-brain vault root. Refused stray root write "${rel}". Put content under wiki/ , decisions/ , log/ or index/ instead. To override, lift the guard deliberately (see vault .claude/WRITE-PROTECTION.md).`);
    }
    process.exit(0); // subdir or vault dir itself -> allowed
  } catch (e) {
    process.stderr.write('vault-write-guard error (failing open): ' + e.message + '\n');
    process.exit(0);
  }
});

function block(msg) { process.stderr.write(msg + '\n'); process.exit(2); }
