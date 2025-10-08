"""Parse CHANGELOG.md and pyproject.toml, generate RELEASE_NOTES.md and version."""

import os
import re
import sys
import tomllib
from pathlib import Path

with Path("CHANGELOG.md").open("r", encoding="utf-8") as changelog:
    content = changelog.read()
    match = re.search(
        r"^## \[(\d+\.\d+\.\d+)\] - (\d{4}-\d{2}-\d{2})$", content, re.MULTILINE
    )

    if not match:
        print("::error file=CHANGELOG.md::No version header found at top")

        sys.exit(1)

    changelog_version = match.group(1)

    start = match.end()
    top_section = re.search(r"^## \[", content[start:], re.MULTILINE)
    body = content[
        start : start  # noqa: E203, RUF100
        + (top_section.start() if top_section else len(content[start:]))
    ]

    if not re.search(r"^\s*-\s", body, re.MULTILINE):
        print("::error file=CHANGELOG.md::Latest entry is empty")

        sys.exit(1)

    print("::group::Release Notes")
    print(body.strip() + "\n")
    print("::endgroup::")

with Path("pyproject.toml").open("rb") as pyproject:
    data = tomllib.load(pyproject)

project_version = (data.get("project") or {}).get("version")

if not project_version:
    print("::error file=pyproject.toml::Missing [project].version")

    sys.exit(1)

print(f"Changelog version: {changelog_version}")
print(f"Project version: {project_version}")

if project_version != changelog_version:
    print(
        f"::error::Version mismatch: CHANGELOG.md has {changelog_version}, "
        f"but pyproject.toml has {project_version}"
    )

    sys.exit(1)

with Path("RELEASE_NOTES.md").open("w", encoding="utf-8") as release_notes:
    release_notes.write(body.strip() + "\n")

github_output_path = os.environ.get("GITHUB_OUTPUT")

if not github_output_path:
    print("::error::GITHUB_OUTPUT environment variable not set")

    sys.exit(1)

with Path(github_output_path).open("a", encoding="utf-8") as github_output:
    github_output.write(f"version={project_version}")
