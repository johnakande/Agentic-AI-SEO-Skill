# Agentic AI-SEO Skill

![MIT license](https://img.shields.io/badge/license-MIT-blue.svg)

Agentic AI-SEO Skill is a free, open-source, LLM-first SEO analysis skill. One orchestrator, `/agentic-ai-seo-skill`, routes to 24 sub-skills covering technical SEO, schema markup, content quality (E-E-A-T), AI search optimization (GEO and AEO), local SEO, and GitHub repository SEO. It's plain Markdown with YAML frontmatter, no host-specific installer or launcher, so it works the same whether it's loaded by Claude Code, Codex, Antigravity, or any other agent that reads a `SKILL.md` and runs shell commands. Confirmed working install paths below cover Claude Code and OpenCode; if you install it into another host's skills directory, the skill content itself doesn't need to change.

## How it works

For a full audit, the orchestrator detects the business type (SaaS, local service, e-commerce, publisher, agency) from homepage signals, works through the relevant specialists sequentially, and synthesizes findings through a PERCEIVE → ANALYZE → VALIDATE → ACT framework before emitting a prioritized action plan. Every recommendation carries the observation it rests on, its relationship to other recommendations, an explicit falsifiability check, and a leading indicator to monitor without re-running the audit. Full methodology in `resources/references/thinking-framework.md`.

Individual commands (`/agentic-ai-seo-skill technical`, `/agentic-ai-seo-skill schema`, etc.) skip straight to the relevant sub-skill instead of the full multi-pass audit.

Bundled scripts are invoked as `python3 <SKILL_DIR>/scripts/<script>.py`, where `<SKILL_DIR>` isn't an environment variable — it's the absolute path to wherever this skill actually lives, which whatever agent is running it already knows, since it just read this file from there. No launcher, no PATH installer, no hardcoded assumption about which host installed it.

## Usage

```
/agentic-ai-seo-skill audit https://example.com
/agentic-ai-seo-skill technical https://example.com
/agentic-ai-seo-skill schema https://example.com
/agentic-ai-seo-skill geo https://example.com
/agentic-ai-seo-skill aeo https://example.com
/agentic-ai-seo-skill github johnakande/agentic-ai-seo-skill
```

Or ask in plain language — "audit example.com's technical SEO" works the same way.

## Commands

| Command | What it does |
|---|---|
| `/agentic-ai-seo-skill audit <url>` | Full site audit, sequential specialist passes, SEO Health Score |
| `/agentic-ai-seo-skill page <url>` | Deep single-page analysis |
| `/agentic-ai-seo-skill technical <url>` | Technical SEO across 9 categories |
| `/agentic-ai-seo-skill content <url>` | E-E-A-T and content quality |
| `/agentic-ai-seo-skill content-brief <topic or url>` | Content brief: keywords, outline, internal links |
| `/agentic-ai-seo-skill schema <url>` | Detect, validate, generate Schema.org markup |
| `/agentic-ai-seo-skill sitemap <url or generate>` | Analyze or generate XML sitemaps |
| `/agentic-ai-seo-skill images <url or optimize>` | Image SEO and file optimization |
| `/agentic-ai-seo-skill geo <url>` | AI Overviews / Generative Engine Optimization |
| `/agentic-ai-seo-skill aeo <url>` | Featured Snippets, PAA, Knowledge Panel |
| `/agentic-ai-seo-skill plan <business-type>` | Strategic planning, 6 industry templates |
| `/agentic-ai-seo-skill programmatic [url\|plan]` | Programmatic SEO at scale |
| `/agentic-ai-seo-skill competitor-pages [url\|generate]` | Competitor comparison pages |
| `/agentic-ai-seo-skill local <url>` | Local SEO: GBP, NAP, citations, reviews |
| `/agentic-ai-seo-skill maps [command]` | Maps intelligence: geo-grid, GBP audit |
| `/agentic-ai-seo-skill hreflang [url]` | Hreflang / i18n audit and generation |
| `/agentic-ai-seo-skill google [command] [url]` | Google APIs: GSC, PageSpeed, CrUX, Indexing, GA4 |
| `/agentic-ai-seo-skill backlinks <url>` | Backlink profile, free-tier sources only |
| `/agentic-ai-seo-skill cluster <seed-keyword>` | SERP-based semantic clustering |
| `/agentic-ai-seo-skill sxo <url>` | Search Experience Optimization |
| `/agentic-ai-seo-skill drift baseline\|compare\|history <url>` | SEO drift monitoring over time |
| `/agentic-ai-seo-skill ecommerce <url>` | E-commerce SEO and marketplace intel |
| `/agentic-ai-seo-skill flow [stage] [url\|topic]` | FLOW framework, 41 evidence-led prompts |
| `/agentic-ai-seo-skill github [command] <owner/repo>` | GitHub repository SEO |

Full detail on every command lives in its own file under `resources/skills/`.

## Installation

Install with the Skills CLI:

```bash
npx skills add johnakande/agentic-ai-seo-skill --global
```

Leave off `--global` to install only in the current project.

Claude Code 2.1.142 or newer can install the plugin instead:

```
/plugin marketplace add johnakande/agentic-ai-seo-skill
/plugin install agentic-ai-seo-skill@agentic-ai-seo-skill
```

The plugin command is `/agentic-ai-seo-skill:agentic-ai-seo-skill`.

### Manual install (Claude Code)

```bash
mkdir -p ~/.claude/skills
git clone https://github.com/johnakande/agentic-ai-seo-skill.git ~/.claude/skills/agentic-ai-seo-skill
cd ~/.claude/skills/agentic-ai-seo-skill
pip install -r requirements.txt
```

### Manual install (OpenCode)

```bash
mkdir -p ~/.config/opencode/skills
git clone https://github.com/johnakande/agentic-ai-seo-skill.git ~/.config/opencode/skills/agentic-ai-seo-skill
cd ~/.config/opencode/skills/agentic-ai-seo-skill
pip install -r requirements.txt
```

### IDE / host compatibility

`SKILL.md` and everything under `resources/` and `scripts/` don't reference a fixed install location — that's the whole point of the `<SKILL_DIR>` convention. Whether a given host can use it as-is or needs the content adapted into its own format depends on whether that host reads a `SKILL.md` folder natively:

| Host | Install location | Status |
|---|---|---|
| Claude Code | `~/.claude/skills/agentic-ai-seo-skill/` | Native skill folder. **Confirmed working** in this repo's own build and test process. |
| OpenCode | `~/.config/opencode/skills/agentic-ai-seo-skill/` | Native skill folder. **Confirmed working**, same as Claude Code above. |
| Antigravity IDE | `<project>/.agent/skills/agentic-ai-seo-skill/` | Native skill folder. Same sourcing caveat as Codex CLI above. |
| Cursor | `.cursor/rules/*.mdc` + `.cursor/skills/agentic-ai-seo-skill/` | **Different native format.** Cursor reads MDC rule files with their own frontmatter, not a straight copy of `SKILL.md` — real adaptation work, not done here. |
| Windsurf | `.windsurf/rules/*.md` + `.windsurf/skills/agentic-ai-seo-skill/` | Same caveat as Cursor: different native rule format, needs adaptation. |
| Continue.dev | `.continue/prompts/*.prompt` + `.continue/skills/agentic-ai-seo-skill/` | Same caveat: slash-command prompt format, needs adaptation. |
| GitHub Copilot | `.github/copilot-instructions.md` + `.github/skills/agentic-ai-seo-skill/` | Same caveat: repo-instructions format, needs adaptation. |
| Cline | `.clinerules` + `.cline/skills/agentic-ai-seo-skill/` | Same caveat: project-rules format, needs adaptation. |

For any host not listed, or the five above that need format adaptation: clone the repo, `pip install -r requirements.txt` inside it, and either point your host at the folder if it reads `SKILL.md` natively, or convert `SKILL.md`'s content into whatever rule/prompt format that host expects.

No isolated environment, no Chromium download — just the scripts and whatever Python you already have (3.10+).
