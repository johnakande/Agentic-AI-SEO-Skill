"""Structure and consistency checks for this repo's actual layout.

Unlike the tests ported from claude-seo, these check things specific to
this build: the orchestrator/plugin.json/README version stay in sync, every
routing-table entry and reference-file path in SKILL.md resolves on disk,
and no .md file anywhere under resources/ names a script that doesn't
exist in scripts/. These three things were checked by hand repeatedly
during the build; this turns those checks into a real regression test
instead of leaving them as a one-time manual pass.
"""

from __future__ import annotations

import json
import re
from pathlib import Path

import pytest

REPO = Path(__file__).resolve().parents[1]
SKILL_MD = (REPO / "SKILL.md").read_text(encoding="utf-8")
README = (REPO / "README.md").read_text(encoding="utf-8")
PLUGIN = json.loads((REPO / ".claude-plugin" / "plugin.json").read_text(encoding="utf-8"))


def test_skill_md_has_valid_yaml_frontmatter():
    match = re.match(r"\A---\n(.*?)\n---\n", SKILL_MD, re.DOTALL)
    assert match, "SKILL.md must start with a --- delimited YAML block"
    import yaml

    data = yaml.safe_load(match.group(1))
    assert data["name"] == "agentic-ai-seo-skill"
    assert "description" in data
    assert data["metadata"]["version"]


def test_version_matches_across_skill_plugin_and_readme():
    skill_version = re.search(r'version:\s*"([^"]+)"', SKILL_MD).group(1)
    plugin_version = PLUGIN["version"]
    readme_version = re.search(r"- \*\*([0-9]+\.[0-9]+\.[0-9]+)\*\*", README).group(1)
    assert skill_version == plugin_version == readme_version, (
        skill_version,
        plugin_version,
        readme_version,
    )


def test_no_top_level_version_field_in_skill_md():
    frontmatter = re.match(r"\A---\n(.*?)\n---\n", SKILL_MD, re.DOTALL).group(1)
    assert not re.search(r"(?m)^version:", frontmatter), (
        "version belongs under metadata:, not as a top-level frontmatter field"
    )


def test_every_routing_table_skill_path_exists():
    # Pull every `resources/skills/...` path referenced anywhere in SKILL.md.
    paths = set(re.findall(r"resources/skills/[\w\-./]+\.md", SKILL_MD))
    assert len(paths) == 24, f"expected exactly 24 skill paths, found {len(paths)}"
    missing = [p for p in paths if not (REPO / p).is_file()]
    assert not missing, f"SKILL.md references missing skill files: {missing}"


def test_every_reference_file_path_exists():
    paths = set(re.findall(r"resources/references/[\w\-./]+\.md", SKILL_MD))
    assert paths, "expected at least one reference file path in SKILL.md"
    missing = [p for p in paths if not (REPO / p).is_file()]
    assert not missing, f"SKILL.md references missing reference files: {missing}"


def test_every_agent_doc_named_in_skill_md_exists():
    section = SKILL_MD.split("## Specialist Role Docs")[1].split("## Error Handling")[0]
    names = re.findall(r"`([a-z0-9-]+)`", section)
    assert names, "expected agent names in the Specialist Role Docs section"
    missing = [n for n in names if not (REPO / "resources" / "agents" / f"{n}.md").is_file()]
    assert not missing, f"SKILL.md names agents with no matching file: {missing}"


@pytest.mark.parametrize(
    "md_file",
    sorted((REPO / "resources").rglob("*.md")),
    ids=lambda p: str(p.relative_to(REPO)),
)
def test_no_dangling_script_references(md_file: Path):
    text = md_file.read_text(encoding="utf-8")
    scripts_dir = REPO / "scripts"
    for script in sorted(set(re.findall(r"\b([a-zA-Z_][a-zA-Z0-9_]*\.py)\b", text))):
        assert (scripts_dir / script).is_file(), (
            f"{md_file.relative_to(REPO)} references {script}, "
            f"which does not exist in scripts/"
        )


def test_no_paid_launcher_scripts_remain():
    # keyword_planner.py was removed for needing an active-ad-spend Google
    # Ads account to return real data. Guard against it quietly coming back.
    assert not (REPO / "scripts" / "keyword_planner.py").exists()
    assert "keyword_planner" not in SKILL_MD
