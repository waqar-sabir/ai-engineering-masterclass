"""Validate repository Markdown file targets and GitHub-style heading anchors."""
import re
import sys
from pathlib import Path
from urllib.parse import unquote

ROOT = Path(__file__).resolve().parents[1]
errors = []
files = [p for p in ROOT.rglob("*.md")
         if not any(x in p.parts for x in ("node_modules", ".venv", ".git"))]


def anchors(path):
    result = set()
    counts = {}
    for heading in re.findall(r"^#{1,6} (.+)$", path.read_text(), re.MULTILINE):
        slug = re.sub(r"[^\w\- ]", "", heading.lower()).replace(" ", "-")
        count = counts.get(slug, 0)
        counts[slug] = count + 1
        result.add(slug + (f"-{count}" if count else ""))
    return result


for path in files:
    for link in re.findall(r"\[[^\]]*\]\(([^)]+)\)", path.read_text()):
        if re.match(r"[a-zA-Z][a-zA-Z0-9+.-]*:", link):
            continue
        target, _, fragment = unquote(link).partition("#")
        dest = (path.parent / target).resolve() if target else path
        if not dest.exists():
            errors.append(f"{path.relative_to(ROOT)}: missing {link}")
        elif fragment and dest.suffix == ".md" and fragment not in anchors(dest):
            errors.append(f"{path.relative_to(ROOT)}: missing anchor {link}")
if errors:
    print("\n".join(errors))
    sys.exit(1)
print(f"Checked local links and anchors in {len(files)} Markdown files.")
