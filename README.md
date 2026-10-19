# Agentic AI SEO Skill

Free, open source SEO audits that run inside your AI coding agent. One command, 24 specialist checks, one prioritized fix list.

![MIT license](https://img.shields.io/badge/license-MIT-blue.svg)

Works with Claude Code and OpenCode. It covers technical SEO, schema, E-E-A-T content quality, GEO and AEO (AI search), local SEO, and GitHub repo SEO. Plain Markdown, no launcher, no paid API needed.

## Quick start

```bash
npx skills add johnakande/agentic-ai-seo-skill --global
```

Then, in your agent:

```
/agentic-ai-seo-skill audit https://example.com
```

Or just ask: "audit example.com's technical SEO."

## What you get

A full audit gives you an SEO Health Score and a prioritized action plan. Every recommendation comes with:

- the observation it rests on
- how it connects to the other fixes
- a falsifiability check, so you know when it's wrong
- a leading indicator to watch, so you don't re-run the audit to see if it worked

The skill detects your business type first (SaaS, local service, ecommerce, publisher, agency), then runs only the specialists that matter for it.

## Commands

**Audits**

| Command | What it does |
|---|---|
| `audit <url>` | Full site audit with SEO Health Score |
| `page <url>` | Deep single page analysis |
| `technical <url>` | Technical SEO across 9 categories |
| `content <url>` | E-E-A-T and content quality |
| `sxo <url>` | Search Experience Optimization |
| `drift baseline\|compare\|history <url>` | Track SEO changes over time |

**AI search and content**

| Command | What it does |
|---|---|
| `geo <url>` | Generative Engine Optimization (AI Overviews, AI answers) |
| `aeo <url>` | Featured Snippets, People Also Ask, Knowledge Panel |
| `schema <url>` | Detect, validate and generate Schema.org markup |
| `content-brief <topic or url>` | Keywords, outline, internal links |
| `cluster <seed-keyword>` | SERP based semantic keyword clustering |

**Local, ecommerce and international**

| Command | What it does |
|---|---|
| `local <url>` | GBP, NAP, citations, reviews |
| `maps [command]` | Geo-grid and GBP audit |
| `ecommerce <url>` | Ecommerce SEO and marketplace intel |
| `hreflang [url]` | Hreflang and i18n audit and generation |

**Data and links**

| Command | What it does |
|---|---|
| `google [command] [url]` | Search Console, PageSpeed, CrUX, Indexing, GA4 |
| `backlinks <url>` | Backlink profile using free tier sources only |
| `sitemap <url or generate>` | Analyze or generate XML sitemaps |
| `images <url or optimize>` | Image SEO and file optimization |

**Strategy**

| Command | What it does |
|---|---|
| `plan <business-type>` | Strategic plan, 6 industry templates |
| `programmatic [url\|plan]` | Programmatic SEO at scale |
| `competitor-pages [url\|generate]` | Competitor comparison pages |
| `flow [stage] [url\|topic]` | FLOW framework, 41 evidence led prompts |

**Repositories**

| Command | What it does |
|---|---|
| `github [command] <owner/repo>` | GitHub repository SEO |

Prefix every command with `/agentic-ai-seo-skill`. Each one has its own file in `resources/skills/`.

## Install

**Skills CLI (any supported agent)**

```bash
npx skills add johnakande/agentic-ai-seo-skill --global
```

Drop `--global` to install for the current project only.

**Claude Code plugin** (2.1.142 or newer)

```
/plugin marketplace add johnakande/agentic-ai-seo-skill
/plugin install agentic-ai-seo-skill@agentic-ai-seo-skill
```

The plugin command is `/agentic-ai-seo-skill:agentic-ai-seo-skill`.

**Manual, Claude Code**

```bash
mkdir -p ~/.claude/skills
git clone https://github.com/johnakande/agentic-ai-seo-skill.git ~/.claude/skills/agentic-ai-seo-skill
cd ~/.claude/skills/agentic-ai-seo-skill
pip install -r requirements.txt
```

**Manual, OpenCode**

```bash
mkdir -p ~/.config/opencode/skills
git clone https://github.com/johnakande/agentic-ai-seo-skill.git ~/.config/opencode/skills/agentic-ai-seo-skill
cd ~/.config/opencode/skills/agentic-ai-seo-skill
pip install -r requirements.txt
```

You need Python 3.10 or newer. No isolated environment, no Chromium download.

## Compatibility

| Host | Install location | Status |
|---|---|---|
| Claude Code | `~/.claude/skills/agentic-ai-seo-skill/` | Tested and working |
| OpenCode | `~/.config/opencode/skills/agentic-ai-seo-skill/` | Tested and working |
| Antigravity IDE | `<project>/.agent/skills/agentic-ai-seo-skill/` | Reads `SKILL.md` natively, not tested yet |

Cursor, Windsurf, Continue.dev, GitHub Copilot and Cline use their own rule formats, so `SKILL.md` needs converting for them. I haven't done that work. If you do, send a pull request.

Any other agent that reads a `SKILL.md` folder and runs shell commands should work. Clone the repo, run `pip install -r requirements.txt`, and point your agent at the folder.

## How it works

For a full audit, the orchestrator detects your business type from homepage signals and runs the relevant specialists one after another. It then passes the findings through a four step framework: PERCEIVE, ANALYZE, VALIDATE, ACT. Full method in `resources/references/thinking-framework.md`.

Bundled scripts run as `python3 <SKILL_DIR>/scripts/<script>.py`. `<SKILL_DIR>` is wherever the skill lives on your machine, and your agent already knows that path. Nothing to configure.

## Built by

John Akande, SEO and GTM engineer at Zozzah Technologies. I build technical SEO, GEO and CRM automation systems for service businesses, ecommerce and SaaS.

- Site: [johnakande.com](https://johnakande.com)
- YouTube: [@thejohnakande](https://www.youtube.com/@thejohnakande/)
- Want a human to run the audit? [Free audit](https://johnakande.com/#audit)

Found a bug or want a new sub-skill? Open an issue.

## License

MIT
