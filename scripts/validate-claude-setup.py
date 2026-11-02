#!/usr/bin/env python3
"""Validate local Claude metadata and references; does not run the application."""
from __future__ import annotations

import json
from pathlib import Path
import re
import sys

ROOT = Path(__file__).resolve().parents[1]


def frontmatter(path: Path) -> tuple[dict[str, str], list[str]]:
    text = path.read_text(encoding="utf-8")
    if not text.startswith("---\n"):
        return {}, []
    parts = text.split("---", 2)
    if len(parts) != 3:
        raise ValueError(f"Unclosed frontmatter: {path.relative_to(ROOT)}")
    values: dict[str, str] = {}
    paths: list[str] = []
    for line in parts[1].splitlines():
        match = re.fullmatch(r'\s*-\s+"([^"]+)"\s*', line)
        if match:
            paths.append(match.group(1))
        elif line and not line[0].isspace() and ":" in line:
            key, value = line.split(":", 1)
            values[key] = value.strip().strip('"').strip("'")
    return values, paths


def matches(pattern: str, path: str) -> bool:
    """Small matcher for this setup's *, **, ? and brace alternatives."""
    brace = re.search(r"\{([^{}]+)\}", pattern)
    if brace:
        return any(matches(pattern[:brace.start()] + item + pattern[brace.end():], path)
                   for item in brace.group(1).split(","))
    pieces: list[str] = []
    i = 0
    while i < len(pattern):
        if pattern[i:i + 3] == "**/":
            pieces.append("(?:.*/)?")
            i += 3
        elif pattern[i:i + 2] == "**":
            pieces.append(".*")
            i += 2
        elif pattern[i] == "*":
            pieces.append("[^/]*")
            i += 1
        elif pattern[i] == "?":
            pieces.append("[^/]")
            i += 1
        else:
            pieces.append(re.escape(pattern[i]))
            i += 1
    return re.fullmatch("".join(pieces), path) is not None


def main() -> int:
    errors: list[str] = []
    skills = sorted((ROOT / ".claude/skills").glob("*/SKILL.md"))
    rules = sorted((ROOT / ".claude/rules").rglob("*.md"))
    names: set[str] = set()
    for path in skills:
        meta, _ = frontmatter(path)
        name = meta.get("name", "")
        if not re.fullmatch(r"[a-z0-9]+(?:-[a-z0-9]+)*", name):
            errors.append(f"Invalid skill name: {path.relative_to(ROOT)}")
        if name != path.parent.name or name in names:
            errors.append(f"Duplicate/mismatched skill: {name}")
        if not meta.get("description"):
            errors.append(f"Missing description: {path.relative_to(ROOT)}")
        names.add(name)
    for path in rules:
        meta, paths = frontmatter(path)
        if "paths" in meta and not paths:
            errors.append(f"Empty or unsupported path scope: {path.relative_to(ROOT)}")
        for pattern in paths:
            if pattern.startswith("/") or ".." in pattern.split("/"):
                errors.append(f"Non-relative path scope: {pattern}")
    command_file = ROOT / "CLAUDE.md"
    root_text = command_file.read_text(encoding="utf-8")
    for name in re.findall(r"(?<![\w.])\/([a-z][a-z0-9-]+)", root_text):
        if name not in names:
            errors.append(f"Unknown slash skill in CLAUDE.md: /{name}")
    if any(token in root_text for token in ["[describe", "[exact command]", "[Business invariant]"]):
        errors.append("Unfilled root template")
    documents = [command_file, ROOT / "docs/claude-setup.md", *skills, *rules]
    for path in documents:
        text = path.read_text(encoding="utf-8")
        if text.count("```") % 2:
            errors.append(f"Unbalanced Markdown fences: {path.relative_to(ROOT)}")
        if any(line.rstrip() != line for line in text.splitlines()):
            errors.append(f"Trailing whitespace: {path.relative_to(ROOT)}")
        for target in re.findall(r"(?<![\w./])(?:\.claude|docs)/[A-Za-z0-9_./-]+", text):
            if not (ROOT / target.rstrip(".,;")).exists():
                errors.append(f"Missing reference {target} in {path.relative_to(ROOT)}")
    manifest = json.loads((ROOT / ".claude/manifest.json").read_text(encoding="utf-8"))
    for relative, examples in manifest["scope_examples"].items():
        _, patterns = frontmatter(ROOT / relative)
        for example in examples:
            if not any(matches(pattern, example) for pattern in patterns):
                errors.append(f"Rule scope misses {example}: {relative}")
    if not (ROOT / ".claude/UPSTREAM-LICENSE.txt").is_file():
        errors.append("Missing upstream attribution license")
    if not skills or not rules:
        errors.append("No skills or rules found")
    if errors:
        print("\n".join("ERROR: " + error for error in errors), file=sys.stderr)
        return 1
    print(f"PASS: {len(skills)} skills, {len(rules)} rules, references and representative path scopes.")
    print("Application build/tests and live Claude /memory loading are not checked by this script.")
    return 0


if __name__ == "__main__":
    try:
        raise SystemExit(main())
    except (OSError, ValueError, KeyError) as error:
        print(f"ERROR: {error}", file=sys.stderr)
        raise SystemExit(1)
