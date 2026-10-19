# Lecture 06 — Evidence labels, citations, context budgets, and abstention

[Phase home](../../../../../README.md) · [Module](../README.md)

## Lecture metadata

ID: P03-L06 · Day 17 · Guided notes/example: 40 minutes · Difficulty: Intermediate.

Material status: In Review. Learner completion and implementation: Planned. Selected external reading has a separate allocation in the study plan.

## Learning objectives and syllabus

- Explain and demonstrate: What does citation integrity verify?
- Explain and demonstrate: Why do generator and encoder budgets differ?
- Explain and demonstrate: Can delimiters guarantee injection resistance?
- Trace the worked example, identify a failure boundary, and carry the invariant into the module lab.

## Prerequisites

Phase 1 typed interfaces, validation, prompting, and provider errors; Phase 2 encoder compatibility, exact search, similarity, and evaluation. Complete the preceding Phase 3 lecture.

## Core learning material

Assign context-local labels such as C1 and C2 to retrieved chunks, and retain a deterministic mapping to source document/version and locator. The model may reference only supplied labels. After generation, reject unknown labels and statements that fail the declared claim/citation contract. Label validity is a structural check; human or separate semantic review still evaluates whether evidence actually supports a claim.

Budget instructions, question, labeled context, and output separately with the actual generator tokenizer. The embedding encoder’s limit is a different contract. Rank, deduplicate, and trim whole evidence units without silently dropping citation locators. Adding more text can add noise, duplicates, and contradictory versions rather than improving the answer.

Retrieved text is untrusted. A page saying “ignore prior instructions” does not acquire authority because it was retrieved. Keep policies outside source text, avoid tool authority in this phase, and expose uncertainty. Empty evidence, inadequate coverage, and conflicting sources should remain visible rather than turning into apparent certainty.

## Practical example and walkthrough

Context includes C1 and C2; output cites C7. Reject the citation deterministically. If output cites C1 but misstates it, a separate support check is still required.

Trace inputs, intermediate evidence/metadata, outputs, and the earliest point where a failed invariant can be detected. The module lab adds a small educational code fragment or worked calculation; no application is bundled.

## Learning resources

Required selections (free to read; choose excerpts within the daily budget):

- [Lost in the Middle: How Language Models Use Long Contexts](https://arxiv.org/abs/2307.03172) — Original research paper, free to read; selected abstract and reported position effects; 15 min study estimate. Motivates context inspection; not a claim about every current model.
- [OWASP LLM Prompt Injection Prevention Cheat Sheet](https://cheatsheetseries.owasp.org/cheatsheets/LLM_Prompt_Injection_Prevention_Cheat_Sheet.html) — Official security guidance, free to read; selected indirect prompt injection and layered controls; 20 min study estimate. Supports a clear trust boundary; delimiters alone do not establish security.

Optional supplements/fallbacks:

- [Retrieval-Augmented Generation for Knowledge-Intensive NLP Tasks](https://arxiv.org/abs/2005.11401) — Original research paper, free to read; selected abstract and retrieval/generation architecture; 20 min study estimate. Historical conceptual grounding; the course uses an application pipeline, not training the paper’s model.

Video alternative: [Qdrant Essentials](https://qdrant.tech/course/essentials/) for storage/search concepts, or the introductory video playlist linked in [LangChain RAG from Scratch](https://github.com/langchain-ai/rag-from-scratch) for retrieval/generation concepts. For parsing/provenance, official Docling text is primary; the RAG videos are background only. Optional 15–20 minute selections replace other optional study, not additional mandatory hours. Historical notebook APIs must be checked against current component docs.

## Independent assignment

Design a cited-answer schema and rules for insufficient evidence and conflicting source versions. Include one original counterexample, the invariant it violates, and the expected safe behavior. Complete [the module lab](../labs/lab-03.md) as the practical follow-through.

## Debugging scenario

Every citation label is valid but the answer is wrong. Which validation was missing?

## Knowledge check

1. What does citation integrity verify?
2. Why do generator and encoder budgets differ?
3. Can delimiters guarantee injection resistance?

## Completion criteria

- [ ] Explain the mechanism and its prerequisites in your own words.
- [ ] Submit the worked example, independent counterexample, and failure analysis.
- [ ] Attempt the [module assessment](../assessments/knowledge-check.md) before its separate solution guide.
- [ ] Label proposed behavior separately from any later executed result.

## Next lecture

[Previous](lecture-05-manual-rag-retrieval-context-assembly-and-generation.md) · [Next](../../module-02-chunking/lectures/lecture-07-fixed-sentence-and-recursive-chunking.md)
