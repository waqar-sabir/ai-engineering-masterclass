# Lab 01 — Vector-record and collection contract worksheet

[Phase home](../../../../../README.md) · [Module](../README.md)

## Objectives and prerequisites

Translate the Phase 2 embedding manifest into collection, point, and payload contracts. Complete the owning module lectures and carry forward relevant Phase 1–2 contracts. Guided allocation: 75 minutes. Material status: In Review; all execution and implementation: Planned.

## Tools, dependencies, and setup

Python standard library; Qdrant documentation; no running service.

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

1. Define a two-dimensional toy-vector collection separately from the later real encoder collection.
2. Design payload fields: doc_id, source_version, chunk_id, source_locator, text, chunk_policy, and encoder_contract.
3. Derive a supported deterministic point ID from the source/chunk identity. Keep arbitrary user-facing IDs in payload.
4. Compare a toy exact-neighbor list and a candidate ANN list. Compute neighbor overlap separately from human relevance.
5. Specify type, dimension, finite-number, identity, and collection-compatibility checks. Submit the record contract and one failure case.

## Educational example

```python
from uuid import NAMESPACE_URL, uuid5

identity = "source-v1|parser-v1|chunker-v1|chunk-0001"
point_id = str(uuid5(NAMESPACE_URL, identity))
assert point_id == str(uuid5(NAMESPACE_URL, identity))
# Policy changes produce a different generation/identity, not mixed old vectors.
```

This fragment illustrates the mechanism; it is not a bundled project implementation.

## Commands and test plan

After the learner creates the experiment and tests in their own workspace:

```sh
python experiments/lab_01.py
python -m pytest tests/test_lab_01.py -q
```

These files are future learner tasks, not files shipped here. Lab 10 can use only the capacity example as its Python fragment; its main submission is the design document.

## Expected output

A supported stable UUID, a vector/payload schema, and a hand-checked neighbor-overlap calculation. No database operation is claimed.

## Common errors and troubleshooting

Use a valid arbitrary payload ID but an invalid point-ID shape to distinguish the two contracts. Test wrong vector width and incompatible encoder revision even when numeric widths match.

## Acceptance criteria

- [ ] Numbered tasks have reviewable artifacts and an independent counterexample.
- [ ] Correct behavior and failure behavior are specified separately.
- [ ] Any later run records actual versions, inputs, and observed output; no invented result.
- [ ] No credentials, private documents, destructive shared-collection operations, or unreviewed downloads.
- [ ] Limitations are explicit; pending implementation is not marked complete.

## Assignment and assessment

Submit the artifact and one original failure example, then attempt the [module assessment](../assessments/knowledge-check.md). Carry the contract into the [Enterprise Knowledge Assistant specification](../../../../../project/README.md).
