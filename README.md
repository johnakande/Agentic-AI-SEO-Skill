# SEO Skill

![MIT license](https://img.shields.io/badge/license-MIT-blue.svg)
![Free only](https://img.shields.io/badge/dependencies-free%20only-brightgreen.svg)

SEO Skill is a free, open-source, LLM-first SEO analysis skill. One orchestrator, `/seo-skill`, routes to 23 sub-skills covering technical SEO, schema markup, content quality (E-E-A-T), AI search optimization (GEO and AEO), local SEO, and GitHub repository SEO. It's plain Markdown with YAML frontmatter, no host-specific installer or launcher, so it works the same whether it's loaded by Claude Code, Codex, Antigravity, or any other agent that reads a `SKILL.md` and runs shell commands. Confirmed working install paths below cover Claude Code and OpenCode; if you install it into another host's skills directory, the skill content itself doesn't need to change.

It's a derivative work combining the strongest parts of two separately MIT-licensed projects rather than a from-scratch build: most of the depth and the security-hardened script layer come from [claude-seo](https://github.com/AgriciDaniel/claude-seo), and GitHub repository SEO plus Answer Engine Optimization come from [Agentic-SEO-Skill](https://github.com/Bhanunamikaze/Agentic-SEO-Skill). Full attribution, including both original license texts, lives in [THIRD_PARTY_NOTICES.md](THIRD_PARTY_NOTICES.md).

## Free only, on purpose

Every script here runs without a paid account, a paid API tier, or an active-ad-spend gate. Extensions that need one (Ahrefs, DataForSEO, SE Ranking, Profound, paid Bing/Firecrawl tiers) were left out entirely rather than bundled-but-broken. One script, `keyword_planner.py` (Google Ads Keyword Planner), was removed for the same reason: without ad spend on the account, it only returns bucketed volume ranges, not real numbers, so it doesn't actually work for free.

## How it works

For a full audit, the orchestrator detects the business type (SaaS, local service, e-commerce, publisher, agency) from homepage signals, works through the relevant specialists sequentially, and synthesizes findings through a PERCEIVE → ANALYZE → VALIDATE → ACT framework before emitting a prioritized action plan. Every recommendation carries the observation it rests on, its relationship to other recommendations, an explicit falsifiability check, and a leading indicator to monitor without re-running the audit. Full methodology in `resources/references/thinking-framework.md`.

Individual commands (`/seo-skill technical`, `/seo-skill schema`, etc.) skip straight to the relevant sub-skill instead of the full multi-pass audit.

Bundled scripts are invoked as `python3 <SKILL_DIR>/scripts/<script>.py`, where `<SKILL_DIR>` isn't an environment variable, it's the absolute path to wherever this skill actually lives, which whatever agent is running it already knows, since it just read this file from there. No launcher, no PATH installer, no hardcoded assumption about which host installed it.

## Usage

```
/seo-skill audit https://example.com
/seo-skill technical https://example.com
/seo-skill schema https://example.com
/seo-skill geo https://example.com
/seo-skill aeo https://example.com
/seo-skill github johnakande/seo-skill
```

Or ask in plain language, "audit example.com's technical SEO" works the same way.

## Commands

| Command | What it does |
|---------|-------------|
| `/seo-skill audit <url>` | Full site audit, sequential specialist passes, SEO Health Score |
| `/seo-skill page <url>` | Deep single-page analysis |
| `/seo-skill technical <url>` | Technical SEO across 9 categories |
| `/seo-skill content <url>` | E-E-A-T and content quality |
| `/seo-skill content-brief <topic or url>` | Content brief: keywords, outline, internal links |
| `/seo-skill schema <url>` | Detect, validate, generate Schema.org markup |
| `/seo-skill sitemap <url or generate>` | Analyze or generate XML sitemaps |
| `/seo-skill images <url or optimize>` | Image SEO and file optimization |
| `/seo-skill geo <url>` | AI Overviews / Generative Engine Optimization |
| `/seo-skill aeo <url>` | Featured Snippets, PAA, Knowledge Panel |
| `/seo-skill plan <business-type>` | Strategic planning, 6 industry templates |
| `/seo-skill programmatic [url\|plan]` | Programmatic SEO at scale |
| `/seo-skill competitor-pages [url\|generate]` | Competitor comparison pages |
| `/seo-skill local <url>` | Local SEO: GBP, NAP, citations, reviews |
| `/seo-skill maps [command]` | Maps intelligence: geo-grid, GBP audit |
| `/seo-skill hreflang [url]` | Hreflang / i18n audit and generation |
| `/seo-skill google [command] [url]` | Google APIs: GSC, PageSpeed, CrUX, Indexing, GA4 |
| `/seo-skill backlinks <url>` | Backlink profile, free-tier sources only |
| `/seo-skill cluster <seed-keyword>` | SERP-based semantic clustering |
| `/seo-skill sxo <url>` | Search Experience Optimization |
| `/seo-skill drift baseline\|compare\|history <url>` | SEO drift monitoring over time |
| `/seo-skill ecommerce <url>` | E-commerce SEO and marketplace intel |
| `/seo-skill flow [stage] [url\|topic]` | FLOW framework, 41 evidence-led prompts |
| `/seo-skill github [command] <owner/repo>` | GitHub repository SEO |

Full detail on every command lives in its own file under `resources/skills/`.

## Testing

354 tests: 201 ported from claude-seo's suite adapted to this repo's layout, plus 153 new structure/consistency checks specific to this build (every routing-table path, every reference-file path, every script reference under `resources/`, version sync across `SKILL.md`/`plugin.json`/README, and a guard against `keyword_planner.py` quietly coming back). Run them with `python3 -m pytest tests/ -v`. Four are correctly skipped on Windows (they assert POSIX file-permission bits `os.chmod` can't produce on NTFS); everything else passes. CI runs the same suite on every push and pull request.

## Sources

- [AgriciDaniel/claude-seo](https://github.com/AgriciDaniel/claude-seo) — orchestration methodology, 21 of 23 sub-skills, 18 of 22 role docs, shared references, most of `scripts/`, including the SSRF-safe HTTP layer.
- [Bhanunamikaze/Agentic-SEO-Skill](https://github.com/Bhanunamikaze/Agentic-SEO-Skill) — the GitHub repository SEO skill and the AEO skill.
- Full attribution and both original MIT license texts: [THIRD_PARTY_NOTICES.md](THIRD_PARTY_NOTICES.md).

## Version history

<details>
<summary>Show release notes</summary>

- **1.0.0** — Initial release. Forked from claude-seo v2.2.5 and Agentic-SEO-Skill, restructured into one orchestrator with a nested `resources/` tree instead of 25 separate top-level Claude Code skills. Scripts invoke via the host-agnostic `python3 <SKILL_DIR>/scripts/<script>.py` convention (same one Agentic-SEO-Skill uses), no launcher binary, no isolated venv, no hardcoded install path, so it works the same across Claude Code, Codex, Antigravity, or any other agent that reads a `SKILL.md`. Fixed a real Windows file-locking gap (`fcntl` silently no-op'd on Windows in two scripts) with a tested cross-platform replacement. Removed all paid-vendor-dependent code paths, including `keyword_planner.py` (Google Ads). 354 tests passing (201 ported, 153 new structure checks), 4 correctly platform-skipped.

</details>

## License

MIT for the original and combining work in this repository. See [THIRD_PARTY_NOTICES.md](THIRD_PARTY_NOTICES.md) for the two source projects' own MIT license texts, both preserved in full as required.

## Installation

Install with the Skills CLI:

```bash
npx skills add johnakande/seo-skill --global
```

Leave off `--global` to install only in the current project.

Claude Code 2.1.142 or newer can install the plugin instead:

```
/plugin marketplace add johnakande/seo-skill
/plugin install seo-skill@seo-skill
```

The plugin command is `/seo-skill:seo-skill`.

### Manual install (Claude Code)

```bash
mkdir -p ~/.claude/skills
git clone https://github.com/johnakande/seo-skill.git ~/.claude/skills/seo-skill
cd ~/.claude/skills/seo-skill
pip install -r requirements.txt
```

### Manual install (OpenCode)

```bash
mkdir -p ~/.config/opencode/skills
git clone https://github.com/johnakande/seo-skill.git ~/.config/opencode/skills/seo-skill
cd ~/.config/opencode/skills/seo-skill
pip install -r requirements.txt
```

### Other hosts (Codex, Antigravity, etc.)

The skill content works the same regardless of install path, `SKILL.md` and everything under `resources/` and `scripts/` don't reference a fixed location. Clone the repo into whatever skills directory your host reads from, `pip install -r requirements.txt` inside it, done. This README doesn't list exact paths for every host since those change and aren't independently confirmed here, check your host's own skills documentation for its install directory.

No isolated environment, no Chromium download, just the scripts and whatever Python you already have (3.10+).
