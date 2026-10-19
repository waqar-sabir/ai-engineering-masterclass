# Lab 06 — Exact search and retrieval-metric audit

[Phase home](../../../../../README.md) · [Module](../README.md)

## Metadata and objectives

Guided allocation: 75 minutes. Material status: Approved; execution: Planned.

Focus: Stable top-k, relevance judgments, and a lexical baseline. Submit the specified artifacts and explain the failure cases.

## Prerequisites and dependencies

Complete the owning module lectures and previous lab contracts where used. Tools/dependencies: Python standard library for fixtures; NumPy and the Lab 4 encoder only for later implementation.

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

1. Specify exact search over the immutable corpus. Validate blank queries and k; choose to clamp k to corpus size and record the actual returned count.
2. Define descending cosine ranking with document ID ascending for ties. Ensure every hit returns the correct text, ID, score, snapshot, and encoder version.
3. Compute Recall@1, Recall@3, and MRR by hand on at least three fixed rankings before writing code. Declare precision denominator as actual returned positions if you report it.
4. Define a simple token-overlap lexical baseline on the same corpus. Fix tokenization/tie rules; do not label it BM25.
5. Plan the frozen held-out evaluation and two no-relevant cases. Do not tune a threshold on held-out labels.
6. Add tests for score direction, ties, invalid vectors, metadata alignment, empty corpus, and a relevant document ranked second.

## Teaching example

```python
relevant = {"d1", "d3"}
ranking = ["d2", "d3", "d1"]
recall_at_2 = len(set(ranking[:2]) & relevant) / len(relevant)
rr = next((1/r for r, doc in enumerate(ranking, 1) if doc in relevant), 0)
print(recall_at_2, rr)  # 0.5 0.5
# No-relevant queries are reported separately, not divided by zero.
```

These are small explanatory fragments, not a bundled project implementation.

## Commands and testing steps

After the learner creates an experiment and its tests in the proposed workspace:

```sh
python experiments/lab_06.py
python -m pytest tests/test_lab_06.py -q
```

For Lab 7, the Python file may contain only the capacity calculation; the substantive submission is the design document. The commands are future learner tasks and do not refer to files shipped in this repository.

## Expected output

An exact-ranking contract, hand-checked metric examples, lexical-baseline specification, and a report outline with no invented results. Search returns retrieved documents, not generated answers.

## Common errors and troubleshooting

If top hits are least related, check score direction. If IDs are correct but snippets are wrong, audit row alignment. Deduplicate returned IDs before computing recall; fail evaluation when a relevant ID is absent from the declared corpus.

## Acceptance criteria

- [ ] All numbered tasks have reviewable evidence.
- [ ] Mathematical expectations and boundary/failure cases are specified.
- [ ] Any real run is labeled with package/model versions and its actual measured result.
- [ ] Synthetic data used; no credentials or private documents submitted.
- [ ] Limitations and incomplete work remain explicit.

## Assignment and project connection

Submit the worksheet or artifact specification plus one independent failure example not copied from the worked example. Add its invariant to the [Document Semantic Search project plan](../../../../../project/README.md). Complete the [module assessment](../assessments/knowledge-check.md) before consulting solutions.
