# Lab 07 — Embedding-search architecture review

[Phase home](../../../../../README.md) · [Module](../README.md)

## Metadata and objectives

Guided allocation: 45 minutes. Material status: Approved; execution: Planned.

Focus: Snapshot compatibility, capacity, privacy, and failure isolation. Submit the specified artifacts and explain the failure cases.

## Prerequisites and dependencies

Complete the owning module lectures and previous lab contracts where used. Tools/dependencies: Markdown editor, calculator, and the phase case study. No service or infrastructure deployment.

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

1. Draw separate build and query paths using the case study. Label text, vector, manifest, and output boundaries.
2. Estimate raw float32 vector storage for 10,000 documents at dimension 384. List omitted memory components and propose a warm-query timing procedure.
3. Model an interrupted build, incompatible query model, corrupt snapshot, and deletion request. Explain fail-closed behavior and rollback.
4. Specify how a local single-user project differs from a multi-user service. Authorization and tenant isolation are future controls, not an achieved property of the MVP.
5. Write a decision record explaining when exact search is sufficient and what measurements would motivate Phase 3 infrastructure.

## Teaching example

```python
documents, dimensions, bytes_per_value = 10_000, 384, 4
raw_bytes = documents * dimensions * bytes_per_value
print(raw_bytes)  # 15360000
print(round(raw_bytes / 1024**2, 2))  # 14.65 MiB
# This excludes model weights, text, metadata, and scratch arrays.
```

These are small explanatory fragments, not a bundled project implementation.

## Commands and testing steps

After the learner creates an experiment and its tests in the proposed workspace:

```sh
python experiments/lab_07.py
python -m pytest tests/test_lab_07.py -q
```

For Lab 7, the Python file may contain only the capacity calculation; the substantive submission is the design document. The commands are future learner tasks and do not refer to files shipped in this repository.

## Expected output

One Mermaid diagram, one capacity calculation, a four-case failure table, a deletion/retention policy, and a short exact-search trade-off record.

## Common errors and troubleshooting

If a design claims latency from operation count, replace it with a measurement plan. If a rebuild overwrites active files in place, design immutable generations and atomic activation instead. A manifest is not an access-control mechanism.

## Acceptance criteria

- [ ] All numbered tasks have reviewable evidence.
- [ ] Mathematical expectations and boundary/failure cases are specified.
- [ ] Any real run is labeled with package/model versions and its actual measured result.
- [ ] Synthetic data used; no credentials or private documents submitted.
- [ ] Limitations and incomplete work remain explicit.

## Assignment and project connection

Submit the worksheet or artifact specification plus one independent failure example not copied from the worked example. Add its invariant to the [Document Semantic Search project plan](../../../../../project/README.md). Complete the [module assessment](../assessments/knowledge-check.md) before consulting solutions.
