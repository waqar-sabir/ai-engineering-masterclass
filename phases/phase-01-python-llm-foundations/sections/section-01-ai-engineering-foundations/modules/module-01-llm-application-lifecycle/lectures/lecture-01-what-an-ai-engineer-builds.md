# Lecture 01 — What an AI engineer builds

[Phase home](../../../../../README.md) · [Module](../README.md)

## Lecture metadata

ID: P01-L01 · Duration: 60 minutes · Material status: Approved · Learner completion: Planned.

## Learning objectives

Distinguish AI, ML, deep learning, and generative AI; map the AI engineer’s work to software, data, model, evaluation, and operations boundaries.

## Prerequisites

Course prerequisites and the phase overview.

## Detailed theory

- Classical software maps explicit rules to outputs. ML learns a predictive function from data. Deep learning uses layered neural networks. Generative models produce new content by modeling distributions over sequences or other modalities.
- An AI engineer usually does not train a frontier model. The job is to turn probabilistic model capability into a reliable product: input contracts, context assembly, provider calls, validation, tool/data access, evaluation, security, observability, and cost control.
- Separate four layers from the start:
  1. **Product layer:** user intent, UI, permissions, acceptance criteria.
  2. **Application layer:** orchestration, prompts, schemas, business rules.
  3. **Model layer:** provider/model selection, inference parameters, limits.
  4. **Operations layer:** telemetry, evaluation, deployment, incident response.
- A model response is not a database fact or executed action. It is untrusted generated data until the application validates and authorizes it.

**Practical demonstration:** Sketch the lifecycle for “generate a company brief”: CLI input → validation → prompt assembly → model API → schema validation → evidence checks → rendered report → logs/metrics.

## Technical explanations

Trace CLI input → prompt builder → provider adapter → validator → renderer. Mark each boundary where an exception or invalid result must stop success.

## Real-world example

A company-brief product can return fluent but unsupported competitor claims. Put a contract, source review, and an evaluation boundary between generation and the user.

## Code walkthrough

Use the lifecycle sketch as the worked example. (1) Validate the company name. (2) assemble instructions and explicitly approved source text. (3) call the provider. (4) validate the response contract and references. (5) render only the validated result. Explain which component owns each step and how a failure propagates. This is a teaching walkthrough; implementation is deferred.

## Learning resources

[Required and optional resources](../../../../../resources/README.md#lecture-1-resources) (Lecture 1 grouping). Read required selections alongside the lecture; optional resources close specific gaps.

## Hands-on exercise

Draw the company-brief lifecycle and label the four responsibility layers. List three failures that a model alone cannot prevent.

## Knowledge checks

1. Which responsibilities remain with the application even if the model follows instructions well?
2. Why is an LLM output closer to untrusted API input than to a deterministic function return?
3. Name one evaluation metric for product quality and one for operations.

## Completion criteria

You can explain the four layers and identify where validation, authorization, and evaluation belong.

## Next lecture

[Start here](../../../../../README.md) · [Next lecture](lecture-02-llm-request-lifecycle-tokens-and-model-access.md)
