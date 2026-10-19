# Lab 07 — Manual versus LangChain RAG parity audit

[Phase home](../../../../../README.md) · [Module](../README.md)

## Objectives and prerequisites

Hold data/model contracts fixed while replacing only integration wiring. Complete the owning module lectures and carry forward relevant Phase 1–2 contracts. Guided allocation: 75 minutes. Material status: In Review; all execution and implementation: Planned.

## Tools, dependencies, and setup

Later: langchain-qdrant and reviewed embedding/model adapters; fake or hand-vector fixtures first.

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

1. Freeze corpus, chunker, encoder revision, collection generation, query set, and answer schema from the manual baseline.
2. Write down the direct Qdrant payload keys and the integration’s expected text/metadata schema. Specify an explicit mapping or use a separately built compatible collection.
3. Compare retrieved IDs, original text, locators, filters, and error behavior before comparing generated prose.
4. Feed both evidence paths to the same fake generator and output validator. Require unknown-label and empty-evidence behavior to match.
5. Plan one later real generation comparison with the same frozen questions and documented settings; outputs need not match word for word.
6. Submit a parity report template with actual-result fields left blank until execution.

## Educational example

```python
direct = {"doc_id": "a", "chunk_id": "a-1", "text": "Notice required."}
adapted = {"page_content": direct["text"],
           "metadata": {"doc_id": direct["doc_id"], "chunk_id": direct["chunk_id"]}}
assert adapted["metadata"]["chunk_id"] == direct["chunk_id"]
# Match the installed integration’s configured payload keys explicitly.
```

This fragment illustrates the mechanism; it is not a bundled project implementation.

## Commands and test plan

After the learner creates the experiment and tests in their own workspace:

```sh
python experiments/lab_07.py
python -m pytest tests/test_lab_07.py -q
```

These files are future learner tasks, not files shipped here. Lab 10 can use only the capacity example as its Python fragment; its main submission is the design document.

## Expected output

An adapter mapping, fixed-fixture parity matrix, and stage-by-stage failure report. Framework use alone is not an improved-quality result.

## Common errors and troubleshooting

Blank framework documents can come from payload-key mismatch. Different hits may come from filters, embedding roles, search parameters, or collection selection; inspect these before changing prompts.

## Acceptance criteria

- [ ] Numbered tasks have reviewable artifacts and an independent counterexample.
- [ ] Correct behavior and failure behavior are specified separately.
- [ ] Any later run records actual versions, inputs, and observed output; no invented result.
- [ ] No credentials, private documents, destructive shared-collection operations, or unreviewed downloads.
- [ ] Limitations are explicit; pending implementation is not marked complete.

## Assignment and assessment

Submit the artifact and one original failure example, then attempt the [module assessment](../assessments/knowledge-check.md). Carry the contract into the [Enterprise Knowledge Assistant specification](../../../../../project/README.md).
