# Lab 02 — Qdrant create, upsert, query, and persistence exercise

[Phase home](../../../../../README.md) · [Module](../README.md)

## Objectives and prerequisites

Plan and later execute a small Qdrant lifecycle without destructive recreation. Complete the owning module lectures and carry forward relevant Phase 1–2 contracts. Guided allocation: 75 minutes. Material status: In Review; all execution and implementation: Planned.

## Tools, dependencies, and setup

For later execution: qdrant-client and pytest; optional server/container only after choosing/pinning its version.

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

1. Choose in-memory or persistent client-local mode and state its limitations. Use a learner-owned sandbox name/path.
2. Create a collection only when absent. If present, inspect dimension/distance instead of blindly recreating it.
3. Upsert three toy points with supported stable IDs and provenance payloads. Rerun and check the active count does not grow unexpectedly.
4. Query with explicit payload return; compare exact-query mode against the hand-vector baseline.
5. Delete one sandbox point, query again, and document the expected identity changes. For persistent mode, close/reopen and verify data survives.
6. Test mismatched dimensions, missing payload, incompatible existing collections, and repeated ingestion.

## Educational example

```python
from qdrant_client import QdrantClient, models

client = QdrantClient(":memory:")  # New isolated teaching example only.
client.create_collection("toy", vectors_config=models.VectorParams(
    size=2, distance=models.Distance.COSINE))
client.upsert("toy", points=[models.PointStruct(
    id=1, vector=[1.0, 0.0], payload={"doc_id": "a", "text": "Refund policy"})])
result = client.query_points("toy", query=[1.0, 0.0], limit=1,
    with_payload=True, search_params=models.SearchParams(exact=True))
print(result.points[0].id)  # Expected 1 after a future successful toy run.
client.close()
```

This fragment illustrates the mechanism; it is not a bundled project implementation.

## Commands and test plan

After the learner creates the experiment and tests in their own workspace:

```sh
python experiments/lab_02.py
python -m pytest tests/test_lab_02.py -q
```

These files are future learner tasks, not files shipped here. Lab 10 can use only the capacity example as its Python fragment; its main submission is the design document.

## Expected output

A later successful run returns the inserted ID and its original payload. Repeated upsert does not add duplicate IDs. In-memory mode does not establish persistence or server performance.

## Common errors and troubleshooting

Check installed client/server versions and mode. Missing text may be an omitted payload or wrong key. Collection recreation must not be used to hide a compatibility mismatch.

## Acceptance criteria

- [ ] Numbered tasks have reviewable artifacts and an independent counterexample.
- [ ] Correct behavior and failure behavior are specified separately.
- [ ] Any later run records actual versions, inputs, and observed output; no invented result.
- [ ] No credentials, private documents, destructive shared-collection operations, or unreviewed downloads.
- [ ] Limitations are explicit; pending implementation is not marked complete.

## Assignment and assessment

Submit the artifact and one original failure example, then attempt the [module assessment](../assessments/knowledge-check.md). Carry the contract into the [Enterprise Knowledge Assistant specification](../../../../../project/README.md).
