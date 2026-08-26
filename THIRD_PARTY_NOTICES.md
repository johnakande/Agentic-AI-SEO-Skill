# Third-party notices

SEO Skill is a derivative work combining substantial content from two
separately MIT-licensed projects. MIT requires their original copyright
notices and permission text to be preserved in any substantial portion of
their code carried into a new work, that's what this file does.

## AgriciDaniel/claude-seo

Source of most of this build: the orchestration and synthesis methodology in
`SKILL.md`, 21 of the 24 sub-skills in `resources/skills/`, 18 of the 22 role
docs in `resources/agents/`, the shared reference files in
`resources/references/`, and most of the scripts in `scripts/`, including the
SSRF/DNS-rebinding defense in `scripts/url_safety.py`.

https://github.com/AgriciDaniel/claude-seo

```
MIT License

Copyright (c) 2026 agricidaniel

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
```

Individual sub-skill folders ported from this project each carry their own
`LICENSE.txt` pointer to this notice, unchanged from upstream.

Several sub-skills credit community contributors distinct from the primary
maintainer, preserved as-is in the ported files: `seo-content-brief`
(puneetindersingh), `seo-cluster` (Lutfiya Miller), `seo-sxo` (Florian
Schmitz), `seo-drift` (Dan Colta), `seo-ecommerce` (Matej Marjanovic).

`scripts/content_quality.py`'s AI-phrasing-pattern list is itself attributed
upstream to Wikipedia's "Signs of AI writing" (WikiProject AI Cleanup),
CC BY-SA 4.0.

`resources/skills/seo-flow/` bundles a static snapshot of the FLOW framework
and its 41 prompts:

```
Framework and prompts © Daniel Agrici, CC BY 4.0: github.com/AgriciDaniel/flow
```

## Bhanunamikaze/Agentic-SEO-Skill

Source of the GitHub repository SEO skill (`resources/skills/seo-github.md`,
its 4 agent docs, `github_api.py`, `github_repo_audit.py`,
`github_readme_lint.py`, `github_community_health.py`,
`github_search_benchmark.py`, `github_competitor_research.py`,
`github_traffic_archiver.py`, `github_seo_report.py`, `finding_verifier.py`,
`env_loader.py`, `scripts/lib/safe_http.py`, and 3 reference docs), and the
AEO skill (`resources/skills/seo-aeo.md` and its dependency
`entity_checker.py`).

https://github.com/Bhanunamikaze/Agentic-SEO-Skill

```
MIT License

Copyright (c) 2026 Bhanu Namikaze
Copyright (c) 2026 agricidaniel

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
```

## What's original to this repository

The orchestrator's routing table adaptation, the cross-platform file-locking
fix (`scripts/lib/file_lock.py`, applied to `dataforseo_costs.py` and
`moz_api.py`), removal of paid-vendor-only code paths, the restructuring from
claude-seo's many-top-level-skills layout into one orchestrator with a nested
`resources/` tree, and this notices file. The `<SKILL_DIR>` script-invocation
convention itself is not original to this repository, it's carried over
directly from Bhanunamikaze/Agentic-SEO-Skill's own `SKILL.md`.
