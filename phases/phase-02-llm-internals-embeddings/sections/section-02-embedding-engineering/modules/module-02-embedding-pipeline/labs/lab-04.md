# Lab 04 — Embedding snapshot contract and persistence plan

[Phase home](../../../../../README.md) · [Module](../README.md)

## Metadata and objectives

Guided allocation: 75 minutes. Material status: Approved; execution: Planned.

Focus: Text-to-embedding pipeline, roles, and stable document mapping. Submit the specified artifacts and explain the failure cases.

## Prerequisites and dependencies

Complete the owning module lectures and previous lab contracts where used. Tools/dependencies: For later model execution: sentence-transformers, numpy, pytest. Public model download and CPU memory required; no provider key.

The current repository contains materials only. Create files and run commands later in a separate learner workspace. Do not add exercise dependencies to this repository’s tooling configuration. GPU training and paid provider calls are not required.

## Setup and proposed folder structure

```text
learner-phase-02/
  notes/
  data/corpus.json
  data/queries.json
  experiments/
  tests/
  artifacts/
  reports/
```

For a later implementation session, create a local virtual environment and install only what this lab needs. Review publisher instructions and record resolved package/model versions; do not assume an unpinned environment is reproducible.

```sh
python3 -m venv .venv
# macOS/Linux; on Windows use the environment activation equivalent.
. .venv/bin/activate
python -m pip install pytest
# Add only the lab-specific packages listed above when required.
```

## Step-by-step instructions

1. Prepare 12 short synthetic documents with unique IDs and source labels. Reject duplicate IDs, empty text, and texts beyond the selected encoder budget.
2. Record a manifest: model/revision, tokenizer, role policy, dimension, pooling, normalization, dtype, preprocessing version, corpus hash, and ID order.
3. Plan batch encoding with a stable ID-to-row mapping. For a later live model exercise, encode documents and queries with the documented role-specific methods.
4. Specify numeric vectors.npy, documents.json, and manifest.json inside an immutable generation folder. Specify temporary writes, validation, and activation.
5. Define loader checks for `[N,d]`, matching ID count/order, digest compatibility, finite values, and nonzero norms. Reopen numeric arrays without pickle/object loading.
6. Submit a failure demonstration plan for an interrupted write and a query/corpus revision mismatch. Hand vectors can validate the contract, but are not a real embedding run.

## Teaching example

```python
# Future exercise fragment; MODEL_REVISION must be a reviewed commit.
import os
from sentence_transformers import SentenceTransformer

model = SentenceTransformer(
    "sentence-transformers/all-MiniLM-L6-v2",
    revision=os.environ["MODEL_REVISION"], trust_remote_code=False,
)
documents = ["Cancellation requires one day of notice.", "Invoices use USD."]
vectors = model.encode_document(documents, normalize_embeddings=True)
print(vectors.shape)  # (2, 384) for this documented model family.
# Persistence, validation, and source mapping are learner tasks.
```

These are small explanatory fragments, not a bundled project implementation.

## Commands and testing steps

After the learner creates an experiment and its tests in the proposed workspace:

```sh
python experiments/lab_04.py
python -m pytest tests/test_lab_04.py -q
```

For Lab 7, the Python file may contain only the capacity calculation; the substantive submission is the design document. The commands are future learner tasks and do not refer to files shipped in this repository.

## Expected output

An artifact specification and build/loader test plan. A later real run should produce one vector per accepted document. Never claim vector generation from a shape example alone.

## Common errors and troubleshooting

Test mismatched counts, swapped IDs, corrupt manifests, incompatible model revisions, empty texts, and invalid vectors. For memory errors reduce batch size; do not hide document failures by dropping rows without updating metadata.

## Acceptance criteria

- [ ] All numbered tasks have reviewable evidence.
- [ ] Mathematical expectations and boundary/failure cases are specified.
- [ ] Any real run is labeled with package/model versions and its actual measured result.
- [ ] Synthetic data used; no credentials or private documents submitted.
- [ ] Limitations and incomplete work remain explicit.

## Assignment and project connection

Submit the worksheet or artifact specification plus one independent failure example not copied from the worked example. Add its invariant to the [Document Semantic Search project plan](../../../../../project/README.md). Complete the [module assessment](../assessments/knowledge-check.md) before consulting solutions.
