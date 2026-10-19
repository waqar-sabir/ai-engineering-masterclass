# Lab 04 — Chunk-policy comparison and token-budget audit

[Phase home](../../../../../README.md) · [Module](../README.md)

## Objectives and prerequisites

Compare fixed, sentence-aware, and recursive boundaries on one source. Complete the owning module lectures and carry forward relevant Phase 1–2 contracts. Guided allocation: 75 minutes. Material status: In Review; all execution and implementation: Planned.

## Tools, dependencies, and setup

Later: langchain-text-splitters, the pinned encoder tokenizer, pytest; paper boundary work needs no packages.

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

1. Prepare a synthetic policy containing a heading, a rule, an exception, and an oversized paragraph.
2. Mark fixed-size and sentence-grouped chunks manually. Then specify a recursive-splitter alternative with explicit size units.
3. Compare two overlap values while keeping the source and question labels fixed. Explain duplicated evidence and storage effects.
4. Count actual final encoder tokens including any heading prefix. Reject or visibly split over-budget inputs.
5. Version every boundary/normalization/heading decision. Define tests for empty text, a single long sentence, overlap ≥ size, and an exception crossing a boundary.
6. Submit a policy comparison, not a universal “best chunk size” claim.

## Educational example

```python
from langchain_text_splitters import RecursiveCharacterTextSplitter

splitter = RecursiveCharacterTextSplitter(
    chunk_size=200, chunk_overlap=40, length_function=len)
chunks = splitter.split_text("Synthetic policy. " * 40)
assert all(len(text) <= 200 for text in chunks)
# These are character limits. Validate encoder-token limits separately.
```

This fragment illustrates the mechanism; it is not a bundled project implementation.

## Commands and test plan

After the learner creates the experiment and tests in their own workspace:

```sh
python experiments/lab_04.py
python -m pytest tests/test_lab_04.py -q
```

These files are future learner tasks, not files shipped here. Lab 10 can use only the capacity example as its Python fragment; its main submission is the design document.

## Expected output

A boundary worksheet, versioned policy, and proposed tests. For a sliding 1000-unit sequence with size 200/overlap 40, the estimated chunk count is 6; actual recursive counts depend on boundaries.

## Common errors and troubleshooting

Do not interpret len as token count. Increasing overlap may increase duplicates without adding unique evidence. Separate fixed-window arithmetic from observed recursive-splitter output.

## Acceptance criteria

- [ ] Numbered tasks have reviewable artifacts and an independent counterexample.
- [ ] Correct behavior and failure behavior are specified separately.
- [ ] Any later run records actual versions, inputs, and observed output; no invented result.
- [ ] No credentials, private documents, destructive shared-collection operations, or unreviewed downloads.
- [ ] Limitations are explicit; pending implementation is not marked complete.

## Assignment and assessment

Submit the artifact and one original failure example, then attempt the [module assessment](../assessments/knowledge-check.md). Carry the contract into the [Enterprise Knowledge Assistant specification](../../../../../project/README.md).
