# AGENTS.md

Guidance for AI coding agents working in this repository.

## What this repo is

A **Claude Code skill**, one orchestrator (`SKILL.md`) that routes to 23 sub-skills, 22 specialist role docs, and roughly 44 Python scripts, all under `resources/` and `scripts/`. It is a derivative work built from two separately MIT-licensed projects; read `THIRD_PARTY_NOTICES.md` before assuming any given file is original to this repo.

This is a **free-only build**. No script here should require a paid API, a paid account, or an active-ad-spend gate to produce real output. `keyword_planner.py` (Google Ads, bucketed volume ranges without ad spend) was removed for exactly this reason. If you're tempted to add something from claude-seo's paid extensions (Ahrefs, DataForSEO, SE Ranking, Profound, Bing Webmaster paid tiers, Firecrawl beyond its free tier), don't, unless the user explicitly asks and understands the cost.

## Key files

- `SKILL.md` — the orchestrator. Routing table, synthesis methodology, quality gates, current-fact rules. **Source of truth for what commands exist.**
- `resources/skills/` — 23 sub-skills. 21 are nested folders (`<name>/SKILL.md`, some with their own `references/`, `assets/`, `templates/`), 2 are flat files (`seo-github.md`, `seo-aeo.md`).
- `resources/agents/` — 22 specialist role docs, read on demand, not registered as separate Claude Code subagents (that would collide with a locally-installed claude-seo; see "Why no real subagents" below).
- `resources/references/` — 16 shared reference files (quality gates, CWV thresholds, schema types, E-E-A-T, local/maps signals, GitHub ranking factors, etc.), loaded on demand by whichever skill cites them.
- `scripts/` — ~44 Python scripts, real working tooling, not stubs. `scripts/lib/` holds shared helpers (`safe_http.py`, `file_lock.py`).
- `bin/seo-skill` — the launcher. `run <script.py> [args]` resolves the script path relative to itself, so it works regardless of the caller's cwd. This is deliberately thinner than claude-seo's `runtime.py`, no isolated venv, no Chromium auto-install, just `python3` on whatever's already on PATH.
- `tests/` — 11 ported test files (201 tests) plus `test_gsc_query.py`'s path already fixed for this layout, and `test_url_safety.py` has 4 tests correctly `skipif`'d on Windows (POSIX chmod semantics don't translate).
- `THIRD_PARTY_NOTICES.md` — required reading before removing or relicensing anything ported from either source project.

## Why no real subagents

claude-seo spawns up to 15 parallel Claude Code subagents during a full audit, registered globally in `~/.claude/agents/`. This build deliberately does not do that: registering 22 agent names globally would collide with a machine that also has claude-seo installed (exactly the situation this repo was built alongside). The role docs are preserved as content, read on demand for sequential deep passes, not wired to the Agent tool. Re-adding real parallel delegation is a reasonable v2 change, but do it with prefixed names (e.g. `seo-skill-technical`) to stay collision-safe, don't just copy claude-seo's agent filenames verbatim into `~/.claude/agents/`.

## The maintenance contract

- **Routing table:** `SKILL.md`'s Quick Reference table, the numbered Sub-Skills list, and the actual folders in `resources/skills/` must all agree. Adding, removing, or renaming a skill means updating all three plus `resources/skills/<name>/SKILL.md`'s own content.
- **Script references:** every `.py` filename mentioned anywhere under `resources/` must exist in `scripts/`. This was hand-verified during the build (`grep -oE '[a-zA-Z_][a-zA-Z0-9_]*\.py'` across every `.md` file, checked against `scripts/`), but there's no automated check for it yet, see "Known gaps" below.
- **The launcher path:** scripts are invoked as `"$HOME/.claude/skills/seo-skill/bin/seo-skill" run <script>.py`, not `seo-skill run` bare (there's no PATH installer) and not `python3 scripts/<script>.py` directly (breaks if the caller's cwd isn't the skill root). If you add a new script reference anywhere, use the full form.
- **Version:** lives in `SKILL.md`'s `metadata.version`, `.claude-plugin/plugin.json`'s `version`, and README's first "Version History" entry. Bump all three together.
- **Free-only:** see the note at the top of this file. Don't reintroduce a paid dependency without flagging it loudly to the user first.
- **Attribution:** if you port more content from either source project, add it to `THIRD_PARTY_NOTICES.md`'s file lists in the same change, don't let that file drift out of sync with what's actually here.

## Known gaps (honest, not hidden)

- No automated structure/consistency test yet (the equivalent of claude-seo's `test_manifest_consistency.py` or this session's own `validate-package.py` pattern from a different skill). The routing table, script references, and reference-file paths were verified by hand during the build; a real regression test for this is the next thing worth adding.
- CI runs `pytest`, but nothing yet re-verifies the hand-checked path consistency on every change.
- `resources/skills/seo-flow`'s `/seo-skill flow sync` command is intentionally non-functional (see that skill's own error-handling table), it was tied to a `gh`-CLI-based upstream sync mechanic (`sync_flow.py`) that didn't fit this simpler build. The 41 prompts are a static, complete snapshot; they just don't auto-update.

## Editing SKILL.md or any resources/skills/ file

- Preserve valid YAML frontmatter where present.
- Ground any new before/after examples or claims in something checkable (a real Google doc, a real changelog date), the whole reason this build's content is trustworthy is that it was read and verified against primary sources during construction, not paraphrased from memory.
- Keep `SKILL.md` itself reasonably scannable; the deep content belongs in `resources/`, not duplicated into the orchestrator.
