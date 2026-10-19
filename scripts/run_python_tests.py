"""Run pytest when tests exist; an unimplemented course is a valid scaffold."""
import subprocess
import sys
from pathlib import Path

roots = [Path("tests"), Path("projects"), Path("shared/python")]
tests = [p for root in roots if root.exists() for p in root.rglob("*.py")
         if p.name.startswith("test_") or p.name.endswith("_test.py")]
if tests:
    sys.exit(subprocess.call([sys.executable, "-m", "pytest"]))
print("No course Python tests yet; scaffold check passed.")
