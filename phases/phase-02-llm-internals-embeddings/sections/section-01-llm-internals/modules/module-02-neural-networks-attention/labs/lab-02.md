# Lab 02 — Attention and tensor-shape worksheet

[Phase home](../../../../../README.md) · [Module](../README.md)

## Metadata and objectives

Guided allocation: 75 minutes. Material status: Approved; execution: Planned.

Focus: Neural transformations, self-attention, and masks. Submit the specified artifacts and explain the failure cases.

## Prerequisites and dependencies

Complete the owning module lectures and previous lab contracts where used. Tools/dependencies: Python standard library and optionally NumPy; no model download.

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

1. Draw `[batch,tokens,hidden]` activations and `[hidden,output]` weights. Calculate output dimensions for a chosen small example.
2. Use two tokens with a two-dimensional query/key space. Compute QKᵀ and the sqrt(d_k) scaling by hand.
3. Compute row-wise softmax. Compare bidirectional attention with a causal mask on the first row.
4. Multiply weights by values. Explain why changing values changes the output without changing attention scores in this toy calculation.
5. Annotate residual paths, normalization, position information, and the feed-forward sublayer on a block diagram. Do not implement or train a Transformer.

## Teaching example

```python
from math import exp

logits = [0.0, 0.0]
shift = max(logits)
weights = [exp(x - shift) for x in logits]
weights = [x / sum(weights) for x in weights]
print(weights)  # [0.5, 0.5]
# A causal first row allows only its first position: [1.0, 0.0].
```

These are small explanatory fragments, not a bundled project implementation.

## Commands and testing steps

After the learner creates an experiment and its tests in the proposed workspace:

```sh
python experiments/lab_02.py
python -m pytest tests/test_lab_02.py -q
```

For Lab 7, the Python file may contain only the capacity calculation; the substantive submission is the design document. The commands are future learner tasks and do not refer to files shipped in this repository.

## Expected output

One complete two-token attention calculation, a causal-mask variant, and a labeled Transformer block diagram. Equal allowed logits yield equal weights; the causal first row selects only the first value.

## Common errors and troubleshooting

Check matrix axes, row sums near one, masked probabilities zero, and a deliberately wrong transpose. Explain why an all-masked row is invalid. If overflow occurs, subtract the largest allowed logit before exponentiating.

## Acceptance criteria

- [ ] All numbered tasks have reviewable evidence.
- [ ] Mathematical expectations and boundary/failure cases are specified.
- [ ] Any real run is labeled with package/model versions and its actual measured result.
- [ ] Synthetic data used; no credentials or private documents submitted.
- [ ] Limitations and incomplete work remain explicit.

## Assignment and project connection

Submit the worksheet or artifact specification plus one independent failure example not copied from the worked example. Add its invariant to the [Document Semantic Search project plan](../../../../../project/README.md). Complete the [module assessment](../assessments/knowledge-check.md) before consulting solutions.
