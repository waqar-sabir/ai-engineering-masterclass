# Lab 08 — PDF, DOCX, TXT, and CSV parsing review

[Phase home](../../../../../README.md) · [Module](../README.md)

## Objectives and prerequisites

Define and later test format-specific parsing without losing structure or provenance. Complete the owning module lectures and carry forward relevant Phase 1–2 contracts. Guided allocation: 75 minutes. Material status: In Review; all execution and implementation: Planned.

## Tools, dependencies, and setup

Later: docling and approved parser assets; Python pathlib/csv; synthetic local sources only.

These are future learner instructions. Do not add exercise dependencies or application files to the course repository during material preparation. No service, parser model, vector index, provider call, or app has been executed for this package. Create a separate learner workspace when implementation is explicitly requested.

```text
learner-phase-03/
  notes/
  data/sources/
  experiments/
  tests/
  artifacts/
  reports/
```

For a later local exercise, create a virtual environment and install only the named packages after reviewing current publisher requirements. Record resolved versions and model/parser revisions.

```sh
python3 -m venv .venv
. .venv/bin/activate
python -m pip install pytest
# Add only this lab's required packages during the later implementation pass.
```

## Step-by-step instructions

1. Prepare one small selectable-text PDF, one simple DOCX, one UTF-8 TXT, and one CSV with quoted commas and headers. Record expected excerpts/locators before parsing.
2. Check Docling’s installed format support and conversion status for PDF/DOCX. Record parser version/options/assets; avoid passing arbitrary remote URLs to the baseline converter.
3. Read TXT with explicit encoding and line references. Use csv.DictReader or a reviewed Docling CSV adapter, preserving header/row meaning.
4. Preserve structured document/provenance output needed for page/heading/table inspection, not only a flattened Markdown string.
5. Include negative fixtures: scanned/empty PDF, corrupt file, bad encoding, and malformed CSV. Mark explicit failures or needs-review outcomes.
6. Submit a parser-quality checklist and later output evidence; do not claim OCR/table perfection.

## Educational example

```python
from docling.document_converter import DocumentConverter
from pathlib import Path
import csv

result = DocumentConverter().convert("data/example.pdf")
print(result.status)  # Inspect status/warnings before using result.document.
text = Path("data/example.txt").read_text(encoding="utf-8")
with open("data/example.csv", encoding="utf-8", newline="") as handle:
    rows = list(csv.DictReader(handle))
# DOCX follows the reviewed converter path; preserve its heading/block locators.
```

This fragment illustrates the mechanism; it is not a bundled project implementation.

## Commands and test plan

After the learner creates the experiment and tests in their own workspace:

```sh
python experiments/lab_08.py
python -m pytest tests/test_lab_08.py -q
```

These files are future learner tasks, not files shipped here. Lab 10 can use only the capacity example as its Python fragment; its main submission is the design document.

## Expected output

A four-format adapter plan and gold-excerpt/locator checklist. A later successful run preserves actual source excerpts; unreadable/partial input never becomes an unexplained empty successful source.

## Common errors and troubleshooting

Scanned PDFs may require OCR outside the text-first baseline. CSV headers and embedded delimiters need a format-aware reader. A longer export can contain layout noise; compare reading order and source locators.

## Acceptance criteria

- [ ] Numbered tasks have reviewable artifacts and an independent counterexample.
- [ ] Correct behavior and failure behavior are specified separately.
- [ ] Any later run records actual versions, inputs, and observed output; no invented result.
- [ ] No credentials, private documents, destructive shared-collection operations, or unreviewed downloads.
- [ ] Limitations are explicit; pending implementation is not marked complete.

## Assignment and assessment

Submit the artifact and one original failure example, then attempt the [module assessment](../assessments/knowledge-check.md). Carry the contract into the [Enterprise Knowledge Assistant specification](../../../../../project/README.md).
