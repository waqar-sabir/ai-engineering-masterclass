# LLM application architecture

Status: Approved (Phase 1 exercise). No application implementation is included.

[Phase 1](../../phases/phase-01-python-llm-foundations/README.md) · [Gateway case study](../02-inference-gateway/README.md)

## Exercise

Draw the Research Assistant across product, application, model, and operations layers. Mark input validation, secret handling, provider calls, output validation, evidence review, rendering, and telemetry. Draw both the successful path and one failure path.

## Review criteria

- Contracts identify trusted and untrusted inputs.
- Domain logic is separate from provider and terminal concerns.
- Invalid output cannot be rendered as a successful brief.
- Latency, usage, request IDs, and versions are observable without exposing secrets.
- Diagram explains hosted-vs-self-hosted trade-offs with explicit assumptions.

Submit the diagram and a short decision record. Use the gateway case study for the deeper scalability discussion.
