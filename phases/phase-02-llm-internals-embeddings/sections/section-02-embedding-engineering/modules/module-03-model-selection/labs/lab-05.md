# Lab 05 — Model-card review and controlled comparison

[Phase home](../../../../../README.md) · [Module](../README.md)

## Metadata and objectives

Guided allocation: 75 minutes. Material status: Approved; execution: Planned.

Focus: Model constraints, evaluation splits, and migration. Submit the specified artifacts and explain the failure cases.

## Prerequisites and dependencies

Complete the owning module lectures and previous lab contracts where used. Tools/dependencies: Documentation access; optional later encoding environment from Lab 4.

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

1. Review the baseline card and select one alternative candidate through a publisher’s model card. Record actual limits, intended task, language, license, revision, role/prompt policy, and CPU requirements. Do not assume access to a private/gated model.
2. Create six development queries with human relevance labels over the same 12-document corpus. Include paraphrases and exact identifiers. Define six held-out answerable queries plus two no-relevant queries before tuning.
3. Write a comparison protocol: same corpus and labels, same preprocessing where compatible, separate thresholds per model if needed, and explicit cold/warm timing methods.
4. Predict likely failure slices as hypotheses. Leave result fields blank until measured; a model card is not a benchmark result on your corpus.
5. Plan a complete re-encoding and rollback if the model changes. Baseline-only execution is mandatory for the later MVP; running the second model is an optional extension.

## Teaching example

```python
# Proposed comparison-record shape, not measured values.
record = {
    "model_revision": "reviewed-commit-required",
    "corpus_digest": "digest-of-frozen-corpus",
    "split": "development",
    "recall_at_3": None,
    "mrr": None,
    "warm_query_ms": None,
}
assert record["mrr"] is None  # No results have been measured here.
```

These are small explanatory fragments, not a bundled project implementation.

## Commands and testing steps

After the learner creates an experiment and its tests in the proposed workspace:

```sh
python experiments/lab_05.py
python -m pytest tests/test_lab_05.py -q
```

For Lab 7, the Python file may contain only the capacity calculation; the substantive submission is the design document. The commands are future learner tasks and do not refer to files shipped in this repository.

## Expected output

Two model-review records, a fixed query-split plan, a comparison protocol, and a migration/rollback decision. No winning model or achieved metric is asserted.

## Common errors and troubleshooting

Check that a query service cannot switch to the candidate while the old corpus remains active. If all queries are tuned repeatedly, relabel them development and create fresh held-out queries. Keep no-relevant cases separate from recall averages.

## Acceptance criteria

- [ ] All numbered tasks have reviewable evidence.
- [ ] Mathematical expectations and boundary/failure cases are specified.
- [ ] Any real run is labeled with package/model versions and its actual measured result.
- [ ] Synthetic data used; no credentials or private documents submitted.
- [ ] Limitations and incomplete work remain explicit.

## Assignment and project connection

Submit the worksheet or artifact specification plus one independent failure example not copied from the worked example. Add its invariant to the [Document Semantic Search project plan](../../../../../project/README.md). Complete the [module assessment](../assessments/knowledge-check.md) before consulting solutions.
