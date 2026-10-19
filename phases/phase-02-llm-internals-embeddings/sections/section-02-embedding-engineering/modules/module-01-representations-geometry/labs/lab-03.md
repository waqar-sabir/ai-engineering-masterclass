# Lab 03 — Vector geometry and ranking invariants

[Phase home](../../../../../README.md) · [Module](../README.md)

## Metadata and objectives

Guided allocation: 75 minutes. Material status: Approved; execution: Planned.

Focus: Cosine, dot product, Euclidean distance, and normalization. Submit the specified artifacts and explain the failure cases.

## Prerequisites and dependencies

Complete the owning module lectures and previous lab contracts where used. Tools/dependencies: Python standard library; NumPy optional.

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

1. Use query `[1,0]` and documents `[1,0]`, `[3,0]`, `[0,1]`, and `[-1,0]` with stable IDs.
2. Calculate all three metrics by hand. Rank by descending similarity and ascending distance.
3. Normalize nonzero vectors and show that dot and cosine order now agree; define an ID-based tie rule.
4. Design a future scoring function that rejects dimension mismatch, zero norms, NaN, and infinity. Do not silently replace invalid vectors with zero.
5. Write the unit-test cases and expected mathematical values in your worksheet. These tests are specifications for later implementation.

## Teaching example

```python
from math import sqrt

a, b = [3.0, 4.0], [1.0, 0.0]
dot = sum(x*y for x, y in zip(a, b))
norm_a = sqrt(sum(x*x for x in a))
norm_b = sqrt(sum(x*x for x in b))
print(dot / (norm_a * norm_b))  # 0.6
# Validate dimensions and nonzero finite norms before generalizing.
```

These are small explanatory fragments, not a bundled project implementation.

## Commands and testing steps

After the learner creates an experiment and its tests in the proposed workspace:

```sh
python experiments/lab_03.py
python -m pytest tests/test_lab_03.py -q
```

For Lab 7, the Python file may contain only the capacity calculation; the substantive submission is the design document. The commands are future learner tasks and do not refer to files shipped in this repository.

## Expected output

Cosine scores for the four example documents: 1, 1, 0, -1. Raw dot scores: 1, 3, 0, -1. The first two cosine results tie and use the declared ID rule.

## Common errors and troubleshooting

Include identical, orthogonal, opposite, scaled, zero, mismatched-dimension, and non-finite examples. Check that distance sorting is ascending. A dot/cosine mismatch without normalization is expected, not an arithmetic bug.

## Acceptance criteria

- [ ] All numbered tasks have reviewable evidence.
- [ ] Mathematical expectations and boundary/failure cases are specified.
- [ ] Any real run is labeled with package/model versions and its actual measured result.
- [ ] Synthetic data used; no credentials or private documents submitted.
- [ ] Limitations and incomplete work remain explicit.

## Assignment and project connection

Submit the worksheet or artifact specification plus one independent failure example not copied from the worked example. Add its invariant to the [Document Semantic Search project plan](../../../../../project/README.md). Complete the [module assessment](../assessments/knowledge-check.md) before consulting solutions.
