---
name: agentic-ai-seo-skill
description: "Comprehensive SEO analysis for any website or business type. Full site audits, single-page analysis, technical SEO (crawlability, indexability, Core Web Vitals with INP), schema markup, content quality (E-E-A-T), image optimization, sitemap analysis, GEO for AI Overviews/ChatGPT/Perplexity, AEO for Featured Snippets/PAA/Knowledge Panel, GitHub repository SEO, local SEO, and strategic planning across SaaS, e-commerce, local, publisher, and agency businesses. Triggers on: SEO, audit, schema, Core Web Vitals, sitemap, E-E-A-T, AI Overviews, GEO, AEO, featured snippet, technical SEO, content quality, page speed, local SEO, GitHub SEO, README audit."
user-invocable: true
argument-hint: "[command] [url]"
license: MIT
metadata:
  version: "1.0.0"
  origin: >
    A derivative work combining content from two MIT-licensed projects:
    AgriciDaniel/claude-seo (22 of 24 sub-skills, 18 of 22 agent role docs, most
    scripts, the security layer, and the synthesis methodology below) and
    Bhanunamikaze/Agentic-SEO-Skill (the GitHub repository SEO skill and the
    AEO skill). See AGENTS.md for full attribution.
---

# Agentic AI-SEO Skill

**Invocation:** `/agentic-ai-seo-skill $1 $2` where `$1` is the command and `$2` is the URL or argument.

**Runtime:** Run bundled Python tools as `python3 <SKILL_DIR>/scripts/<script.py> [args]`. `<SKILL_DIR>` is not a variable to set, it is the absolute path to this skill's own directory (the folder containing this `SKILL.md`), which you already know because you just read this file from somewhere on disk. Substitute the real path when you actually issue the command. This is deliberately host-agnostic: it works the same whether this skill is loaded by Claude Code, Codex, Antigravity, or any other agent that reads a `SKILL.md` and runs shell commands, since none of them need a special launcher to know where the file they just read lives. Install dependencies once with `pip install -r requirements.txt` from the skill's root, whatever Python is already on PATH, no isolated environment is created or required.

Comprehensive SEO analysis across all industries (SaaS, local services, e-commerce, publishers, agencies), plus GitHub repository SEO. Orchestrates 24 sub-skills read from `resources/skills/`. This build does not register separate parallel subagents the way its source project does; deep multi-angle analysis happens as sequential passes within one conversation, informed by the specialist role docs in `resources/agents/` (read the relevant one before writing that section of a report, don't skip straight to conclusions).

## Quick Reference

| Command | What it does | Reads |
|---------|-------------|-------|
| `/agentic-ai-seo-skill audit <url>` | Full website audit, sequential specialist passes | `resources/skills/seo-audit/SKILL.md` |
| `/agentic-ai-seo-skill page <url>` | Deep single-page analysis | `resources/skills/seo-page/SKILL.md` |
| `/agentic-ai-seo-skill technical <url>` | Technical SEO audit (9 categories) | `resources/skills/seo-technical/SKILL.md` |
| `/agentic-ai-seo-skill content <url>` | E-E-A-T and content quality analysis | `resources/skills/seo-content/SKILL.md` |
| `/agentic-ai-seo-skill content-brief <topic or url>` | Content brief: keywords, outline, internal links | `resources/skills/seo-content-brief/SKILL.md` |
| `/agentic-ai-seo-skill schema <url>` | Detect, validate, generate Schema.org markup | `resources/skills/seo-schema/SKILL.md` |
| `/agentic-ai-seo-skill sitemap <url or generate>` | Analyze or generate XML sitemaps | `resources/skills/seo-sitemap/SKILL.md` |
| `/agentic-ai-seo-skill images <url or optimize>` | Image SEO: on-page audit, file optimization | `resources/skills/seo-images/SKILL.md` |
| `/agentic-ai-seo-skill geo <url>` | AI Overviews / Generative Engine Optimization | `resources/skills/seo-geo/SKILL.md` |
| `/agentic-ai-seo-skill aeo <url>` | Featured Snippets, PAA, Knowledge Panel, Sitelinks Searchbox | `resources/skills/seo-aeo.md` |
| `/agentic-ai-seo-skill plan <business-type>` | Strategic SEO planning with industry templates | `resources/skills/seo-plan/SKILL.md` |
| `/agentic-ai-seo-skill programmatic [url\|plan]` | Programmatic SEO analysis and planning | `resources/skills/seo-programmatic/SKILL.md` |
| `/agentic-ai-seo-skill competitor-pages [url\|generate]` | Competitor comparison page generation | `resources/skills/seo-competitor-pages/SKILL.md` |
| `/agentic-ai-seo-skill local <url>` | Local SEO (GBP, citations, reviews, map pack) | `resources/skills/seo-local/SKILL.md` |
| `/agentic-ai-seo-skill maps [command] [args]` | Maps intelligence (geo-grid, GBP audit, reviews) | `resources/skills/seo-maps/SKILL.md` |
| `/agentic-ai-seo-skill hreflang [url]` | Hreflang / i18n SEO audit and generation | `resources/skills/seo-hreflang/SKILL.md` |
| `/agentic-ai-seo-skill google [command] [url]` | Google SEO APIs: GSC, PageSpeed, CrUX, Indexing, GA4 | `resources/skills/seo-google/SKILL.md` |
| `/agentic-ai-seo-skill backlinks <url>` | Backlink profile analysis, free-tier sources | `resources/skills/seo-backlinks/SKILL.md` |
| `/agentic-ai-seo-skill cluster <seed-keyword>` | SERP-based semantic clustering | `resources/skills/seo-cluster/SKILL.md` |
| `/agentic-ai-seo-skill sxo <url>` | Search Experience Optimization | `resources/skills/seo-sxo/SKILL.md` |
| `/agentic-ai-seo-skill drift baseline\|compare\|history <url>` | SEO drift monitoring over time | `resources/skills/seo-drift/SKILL.md` |
| `/agentic-ai-seo-skill ecommerce <url>` | E-commerce SEO: product schema, marketplace intel | `resources/skills/seo-ecommerce/SKILL.md` |
| `/agentic-ai-seo-skill flow [stage] [url\|topic]` | FLOW framework: 41 evidence-led prompts | `resources/skills/seo-flow/SKILL.md` |
| `/agentic-ai-seo-skill github [command] <owner/repo>` | GitHub repository SEO: README, topics, community health | `resources/skills/seo-github.md` |

## Orchestration Logic

When the user invokes `/agentic-ai-seo-skill audit`:
1. Detect business type (SaaS, local, ecommerce, publisher, agency, other) from homepage signals, see "Industry Detection" below.
2. Work through the relevant specialists sequentially, informed by their role docs in `resources/agents/`: seo-technical, seo-content, seo-schema, seo-sitemap, seo-performance, seo-visual, seo-geo always; seo-aeo for Featured Snippet / PAA opportunities; seo-google if Google API credentials are configured; seo-local and seo-maps if a local business is detected; seo-backlinks if backlink APIs are configured; seo-cluster if content-strategy signals are present; seo-ecommerce if e-commerce is detected; seo-drift if a baseline exists for this URL. Always include seo-sxo, search experience applies to every site.
3. Collect findings and generate a unified report with an SEO Health Score (0-100).
4. **Synthesize via the framework below**, walk PERCEIVE -> ANALYZE -> VALIDATE -> ACT before bucketing findings into Critical / High / Medium / Low.
5. Build a prioritized action plan with dependency sequencing and a falsifiability check per recommendation.

For individual commands (`/agentic-ai-seo-skill technical`, `/agentic-ai-seo-skill schema`, etc.), load the relevant skill file directly and skip the multi-specialist pass.

## Synthesis Methodology

Findings alone are not a strategy. Walk four phases before emitting output: **PERCEIVE** (observe-external, observe-internal, listen to what the evidence actually says rather than what's expected), **ANALYZE** (think through causes, connect findings laterally to each other, connect systemically to the site as a whole), **VALIDATE** (does this actually hold up, would you accept this recommendation if someone gave it to you), **ACT** (what specifically changes, what grows as a result).

Full audits (`/agentic-ai-seo-skill audit`, `/agentic-ai-seo-skill page`) walk every phase before emitting the action plan. Narrower commands pass at least THINK + VALIDATE before emitting, a sound first-principle reason and a stated falsifiability check. The Critical / High / Medium / Low buckets are the *output* of this process, not a substitute for it.

Each emitted recommendation carries:
- The observation it rests on
- Its dependency on, or relationship to, other recommendations
- An explicit "how would we know this failed?" check
- A leading indicator the user can monitor without re-running the audit

## Do Not Invent Data

Every number in a report (a score, a word count, a load time, a keyword volume) must come from a script's output or the page content itself, never estimated or guessed to fill a gap. If a script fails or an API key is missing, say so and report what's actually known, don't substitute a plausible-looking placeholder.

## Industry Detection

- **SaaS**: pricing page, /features, /integrations, /docs, "free trial", "sign up"
- **Local Service**: phone number, address, service area, "serving [city]", Google Maps embed, suggest `/agentic-ai-seo-skill local` for deeper analysis
- **E-commerce**: /products, /collections, /cart, "add to cart", product schema
- **Publisher**: /blog, /articles, /topics, article schema, author pages, publication dates
- **Agency**: /case-studies, /portfolio, /industries, "our work", client logos

## Quality Gates

Read `resources/references/quality-gates.md` for thin-content thresholds per page type. Hard rules:
- WARNING at 30+ location pages (enforce 60%+ unique content per page)
- HARD STOP at 50+ location pages (require explicit user justification before proceeding)
- Never recommend HowTo schema (rich results fully removed September 2023)
- FAQ schema: Google retired FAQ rich results for all sites on May 7, 2026, no SERP feature remains. Flag existing FAQPage markup at Info severity, not Critical. Do not claim a confirmed AI/LLM citation benefit for it. Do not recommend removing it either. Do not recommend adding new FAQPage markup for Google SERP benefit. Use QAPage for genuine user Q&A content instead.
- All Core Web Vitals references use INP, never FID (FID was removed from Chrome tooling September 9, 2024)
- Mobile-first indexing has been 100% complete since July 5, 2024
- E-E-A-T applies to all competitive queries, not only YMYL, as of the December 2025 update

## Scoring

### SEO Health Score (0-100)

| Category | Weight |
|----------|--------|
| Technical SEO | 22% |
| Content Quality | 23% |
| On-Page SEO | 20% |
| Schema / Structured Data | 10% |
| Performance (CWV) | 10% |
| AI Search Readiness (GEO + AEO) | 10% |
| Images | 5% |

### Priority levels
- **Critical**: blocks indexing or risks a penalty, fix immediately
- **High**: significantly impacts rankings, fix within a week
- **Medium**: real optimization opportunity, fix within a month
- **Low**: worth doing, not urgent, backlog it

## Reference Files

Load on demand, not all at startup:
- `resources/references/cwv-thresholds.md` — current Core Web Vitals thresholds
- `resources/references/schema-types.md` — supported schema types and deprecation status
- `resources/references/eeat-framework.md` — E-E-A-T evaluation criteria
- `resources/references/quality-gates.md` — content-length minimums, uniqueness thresholds
- `resources/references/local-seo-signals.md` — local ranking factors, review benchmarks, citation tiers
- `resources/references/local-schema-types.md` — LocalBusiness subtypes, industry schema
- `resources/references/maps-geo-grid.md`, `maps-gbp-checklist.md`, `maps-api-endpoints.md`, `maps-free-apis.md` — loaded by `seo-maps`
- `resources/references/backlink-quality.md`, `free-backlink-sources.md` — loaded by `seo-backlinks`
- `resources/references/thinking-framework.md` — the full synthesis methodology, per-principle SEO mapping
- `resources/references/github-api-ops.md`, `github-ranking-factors.md`, `readme-audit-rubric.md` — loaded by `seo-github`

## Sub-Skills

24 total, in `resources/skills/`. Twenty-two are nested folders (`resources/skills/<name>/SKILL.md`, some with their own `references/`, `assets/`, or `templates/` subfolders); two are flat files (`resources/skills/seo-github.md`, `resources/skills/seo-aeo.md`).

1. **seo-audit** — Full website audit, sequential specialist passes
2. **seo-page** — Deep single-page analysis
3. **seo-technical** — Technical SEO across 9 categories
4. **seo-content** — E-E-A-T and content quality
5. **seo-content-brief** — Content brief generation
6. **seo-schema** — Schema markup detection and generation
7. **seo-images** — Image optimization, file optimization
8. **seo-sitemap** — Sitemap analysis and generation
9. **seo-geo** — AI Overviews / GEO optimization
10. **seo-aeo** — Featured Snippets, PAA, Knowledge Panel, Sitelinks Searchbox
11. **seo-plan** — Strategic planning with 6 industry templates
12. **seo-programmatic** — Programmatic SEO at scale
13. **seo-competitor-pages** — Competitor comparison page generation
14. **seo-hreflang** — Hreflang / i18n audit, cultural profiles, content parity
15. **seo-local** — Local SEO: GBP, NAP, citations, reviews, multi-location
16. **seo-maps** — Maps intelligence: geo-grid, GBP audit, competitor radius
17. **seo-google** — Google SEO APIs: GSC, PageSpeed, CrUX, Indexing, GA4
18. **seo-backlinks** — Backlink profile analysis, free-tier sources
19. **seo-cluster** — SERP-based semantic clustering
20. **seo-sxo** — Search Experience Optimization
21. **seo-drift** — SEO drift monitoring over time
22. **seo-ecommerce** — E-commerce SEO intelligence
23. **seo-flow** — FLOW framework: 41 evidence-led prompts (Find, Leverage, Optimize, Win, Local)
24. **seo-github** — GitHub repository SEO: README quality, topics, community health, competitor benchmarking

(24 sub-skills, numbered 1-24 above, not counting this orchestrator itself.)

## Specialist Role Docs

For deep or multi-part analysis, read the matching file in `resources/agents/` before writing that section, each is a compact, execution-focused brief distinct from the fuller skill doc it pairs with:

`seo-technical`, `seo-content`, `seo-schema`, `seo-sitemap`, `seo-performance`, `seo-visual`, `seo-geo`, `seo-local`, `seo-maps`, `seo-google`, `seo-backlinks`, `seo-cluster`, `seo-sxo`, `seo-drift`, `seo-ecommerce`, `seo-flow`, plus the four GitHub-SEO roles (`seo-github-analyst`, `seo-github-benchmark`, `seo-github-data`, `seo-verifier`).

## Error Handling

| Scenario | Action |
|----------|--------|
| Unrecognized command | List available commands from the Quick Reference table. Suggest the closest match. |
| URL unreachable | Report the error and ask the user to verify the URL. Do not guess at site content. |
| A specialist pass fails mid-audit | Report the partial results that did succeed. State clearly which part failed and why. Suggest re-running that command individually. |
| Ambiguous business-type detection | Present the top two candidate types with their supporting signals. Ask the user to confirm before applying industry-specific recommendations. |
| A referenced script is missing or errors | Say so plainly and report what's known without it. Don't fabricate a plausible result. |
