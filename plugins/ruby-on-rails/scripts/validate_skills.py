#!/usr/bin/env python3
import re
import sys
from pathlib import Path


NAME_RE = re.compile(r"^[a-z0-9-]{1,64}$")
LINK_RE = re.compile(r"\[[^\]]+\]\(([^)]+)\)")


def parse_frontmatter(text: str):
    lines = text.splitlines()
    if not lines or lines[0].strip() != "---":
        return None, "missing frontmatter start"
    try:
        end = lines.index("---", 1)
    except ValueError:
        return None, "missing frontmatter end"
    front = lines[1:end]
    data = {}
    for line in front:
        if not line.strip() or line.lstrip().startswith("#"):
            continue
        if ":" not in line:
            continue
        key, value = line.split(":", 1)
        data[key.strip()] = value.strip().strip("\"'")  # simple scalar parsing
    return data, None


def iter_relative_links(text: str):
    for raw in LINK_RE.findall(text):
        target = raw.strip()
        if not target or target.startswith(("#", "http://", "https://", "mailto:", "tel:", "//")):
            continue
        target = target.split()[0]
        target = target.split("#", 1)[0]
        if not target:
            continue
        yield target


def main():
    repo_root = Path(__file__).resolve().parents[1]
    skills_dir = repo_root / "skills"
    errors = []
    seen_names = {}

    if not skills_dir.is_dir():
        errors.append("skills/ directory not found")
    else:
        for skill_dir in sorted(p for p in skills_dir.iterdir() if p.is_dir()):
            skill_md = skill_dir / "SKILL.md"
            if not skill_md.exists():
                errors.append(f"{skill_md}: missing SKILL.md")
                continue
            text = skill_md.read_text(encoding="utf-8")
            meta, err = parse_frontmatter(text)
            if err:
                errors.append(f"{skill_md}: {err}")
                continue

            name = (meta or {}).get("name", "")
            if not name:
                errors.append(f"{skill_md}: missing name in frontmatter")
            else:
                if name != skill_dir.name:
                    errors.append(f"{skill_md}: name '{name}' does not match folder '{skill_dir.name}'")
                if not NAME_RE.match(name):
                    errors.append(f"{skill_md}: name '{name}' must match {NAME_RE.pattern}")
                if name in seen_names:
                    errors.append(f"{skill_md}: duplicate name '{name}' also in {seen_names[name]}")
                else:
                    seen_names[name] = str(skill_md)

            for link in iter_relative_links(text):
                target_path = (skill_dir / link).resolve()
                try:
                    target_path.relative_to(skill_dir.resolve())
                except ValueError:
                    errors.append(f"{skill_md}: link escapes skill dir: {link}")
                    continue
                if not target_path.exists():
                    errors.append(f"{skill_md}: missing link target: {link}")

    if errors:
        print("Skill validation failed:")
        for err in errors:
            print(f"- {err}")
        return 1

    print("Skill validation passed.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
