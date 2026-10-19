# Lab 01 — Tokenization and request-budget notebook

[Phase home](../../../../../README.md) · [Module](../README.md)

## Metadata and objectives

Guided allocation: 75 minutes. Material status: Approved; execution: Planned.

Focus: Tokenization, special tokens, padding, and truncation. Submit the specified artifacts and explain the failure cases.

## Prerequisites and dependencies

Complete the owning module lectures and previous lab contracts where used. Tools/dependencies: transformers, pytest; a reviewed public tokenizer revision. No generative model or API key.

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

1. Select the tokenizer associated with the baseline model card and record the model revision. Create examples for English prose, an identifier, punctuation-heavy code, and mixed-language text.
2. Record character count, token IDs, special-token overhead, and the decoded result. Explain any whitespace/normalization differences; do not assert exact token IDs across revisions.
3. Add a document whose relevant statement is near the end. Compare explicit truncation with a reject-over-budget policy.
4. Plan a boundary test just below and just above the configured encoder budget. Distinguish tokenizer model_max_length from the actual embedding model’s input cap.
5. Submit a short explanation of why token IDs cannot be compared as semantic coordinates.

## Teaching example

```python
from transformers import AutoTokenizer
import os

tokenizer = AutoTokenizer.from_pretrained(
    "sentence-transformers/all-MiniLM-L6-v2",
    revision=os.environ["MODEL_REVISION"],
    trust_remote_code=False,
)
ids = tokenizer("refund policy", add_special_tokens=True)["input_ids"]
print(len(ids), tokenizer.decode(ids))
```

These are small explanatory fragments, not a bundled project implementation.

## Commands and testing steps

After the learner creates an experiment and its tests in the proposed workspace:

```sh
python experiments/lab_01.py
python -m pytest tests/test_lab_01.py -q
```

For Lab 7, the Python file may contain only the capacity calculation; the substantive submission is the design document. The commands are future learner tasks and do not refer to files shipped in this repository.

## Expected output

A small inspection record for four inputs, plus a visible accepted/rejected outcome at the selected token boundary. Exact token IDs and counts depend on the pinned tokenizer; do not copy invented output.

## Common errors and troubleshooting

Check empty text, added special tokens, Unicode round trips, and over-budget text. If padding appears in averages later, preserve the attention mask. If tokenizer download fails, complete a hand-worked subword example and mark the tokenizer exercise pending; do not call it verified.

## Acceptance criteria

- [ ] All numbered tasks have reviewable evidence.
- [ ] Mathematical expectations and boundary/failure cases are specified.
- [ ] Any real run is labeled with package/model versions and its actual measured result.
- [ ] Synthetic data used; no credentials or private documents submitted.
- [ ] Limitations and incomplete work remain explicit.

## Assignment and project connection

Submit the worksheet or artifact specification plus one independent failure example not copied from the worked example. Add its invariant to the [Document Semantic Search project plan](../../../../../project/README.md). Complete the [module assessment](../assessments/knowledge-check.md) before consulting solutions.
