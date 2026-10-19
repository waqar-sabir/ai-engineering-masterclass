# Lab 06 — LangChain component and message-boundary exercise

[Phase home](../../../../../README.md) · [Module](../README.md)

## Objectives and prerequisites

Map the manual pipeline to explicit component interfaces without agents. Complete the owning module lectures and carry forward relevant Phase 1–2 contracts. Guided allocation: 75 minutes. Material status: In Review; all execution and implementation: Planned.

## Tools, dependencies, and setup

Later: langchain-core and selected integration packages; fake components suffice for contract tests.

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

1. Map Document, embedding function, vector store, retriever, message construction, chat model, and output validator to the manual pipeline.
2. Create an example Document carrying doc_id, source_version, chunk_id, and locator metadata. Verify no metadata is silently dropped.
3. Design separate system policy, user question, and labeled untrusted context. Do not let source content redefine policy.
4. Specify fake model outputs for success, malformed output, refusal, timeout, and unknown citations.
5. Record intended package/provider versions and identify provider-specific capabilities that require later tests.
6. Submit a component diagram and adapter contract; no tool loop, LangGraph, or autonomous agent is required.

## Educational example

```python
from langchain_core.documents import Document
from langchain_core.messages import HumanMessage, SystemMessage

doc = Document(page_content="One day of notice is required.",
               metadata={"doc_id": "policy-a", "chunk_id": "a-1"})
messages = [SystemMessage(content="Use only supplied evidence; do not guess."),
            HumanMessage(content=f"Question: Notice?\n[C1] {doc.page_content}")]
assert len(messages) == 2
# A later fake model receives these inputs; do not execute source instructions.
```

This fragment illustrates the mechanism; it is not a bundled project implementation.

## Commands and test plan

After the learner creates the experiment and tests in their own workspace:

```sh
python experiments/lab_06.py
python -m pytest tests/test_lab_06.py -q
```

These files are future learner tasks, not files shipped here. Lab 10 can use only the capacity example as its Python fragment; its main submission is the design document.

## Expected output

An explicit manual-to-framework component map, metadata-preserving document example, and fake-model test cases. No real model invocation is claimed.

## Common errors and troubleshooting

Old tutorial imports may refer to different package versions. Resolve through official component documentation, and test response-shape translation rather than assuming all provider wrappers are equivalent.

## Acceptance criteria

- [ ] Numbered tasks have reviewable artifacts and an independent counterexample.
- [ ] Correct behavior and failure behavior are specified separately.
- [ ] Any later run records actual versions, inputs, and observed output; no invented result.
- [ ] No credentials, private documents, destructive shared-collection operations, or unreviewed downloads.
- [ ] Limitations are explicit; pending implementation is not marked complete.

## Assignment and assessment

Submit the artifact and one original failure example, then attempt the [module assessment](../assessments/knowledge-check.md). Carry the contract into the [Enterprise Knowledge Assistant specification](../../../../../project/README.md).
