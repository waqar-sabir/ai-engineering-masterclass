# Lab 05 — Provenance, refresh, idempotency, and deletion ledger

[Phase home](../../../../../README.md) · [Module](../README.md)

## Objectives and prerequisites

Preserve source-to-chunk traceability across repeated and changed ingestion. Complete the owning module lectures and carry forward relevant Phase 1–2 contracts. Guided allocation: 75 minutes. Material status: In Review; all execution and implementation: Planned.

## Tools, dependencies, and setup

JSON/UUID/hashlib and a worksheet; later Qdrant operations from Lab 2.

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

1. Create locators for selectable-text PDF pages, DOCX heading/block paths, TXT line ranges, and CSV header/row identifiers.
2. Define source hash/version, parser options/version, chunk-policy version, and encoder manifest in a source ledger.
3. Simulate a source changing from five chunks to three. Identify which old points remain unless explicitly deactivated/deleted.
4. Specify unchanged-source reuse and changed-policy rebuild rules. Separate successful writes from whole-generation activation.
5. Design deletion of source text, derived chunks/vectors, local caches, and retained generations under a declared policy.
6. Submit a lifecycle state diagram and tests for duplicate ingestion, partial failure, stale tail chunks, and off-by-one locators.

## Educational example

```python
from hashlib import sha256

raw = b"Synthetic source version one"
source_version = sha256(raw).hexdigest()
ledger = {"doc_id": "policy-a", "source_version": source_version,
          "parser_version": "reviewed-version", "chunk_policy": "policy-v1",
          "status": "parsed"}
assert ledger["status"] != "active"  # Parsing is not corpus activation.
```

This fragment illustrates the mechanism; it is not a bundled project implementation.

## Commands and test plan

After the learner creates the experiment and tests in their own workspace:

```sh
python experiments/lab_05.py
python -m pytest tests/test_lab_05.py -q
```

These files are future learner tasks, not files shipped here. Lab 10 can use only the capacity example as its Python fragment; its main submission is the design document.

## Expected output

A source/version/locator ledger and explicit refresh/deletion plan. Unchanged ingestion reuses stable identity; source or policy changes produce a coherent new generation.

## Common errors and troubleshooting

A correct hash does not guarantee correct parsing or authorization. If a refreshed source still returns old passages, inspect active generation, collection selection, and stale-point cleanup.

## Acceptance criteria

- [ ] Numbered tasks have reviewable artifacts and an independent counterexample.
- [ ] Correct behavior and failure behavior are specified separately.
- [ ] Any later run records actual versions, inputs, and observed output; no invented result.
- [ ] No credentials, private documents, destructive shared-collection operations, or unreviewed downloads.
- [ ] Limitations are explicit; pending implementation is not marked complete.

## Assignment and assessment

Submit the artifact and one original failure example, then attempt the [module assessment](../assessments/knowledge-check.md). Carry the contract into the [Enterprise Knowledge Assistant specification](../../../../../project/README.md).
