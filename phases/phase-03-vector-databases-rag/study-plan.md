# Phase 3 study plan

Target: 3.5 hours/day across Days 15–24, or 35 hours total. These allocations describe the eventual learner journey, not executed work. Resource catalog durations are selected-study estimates; do not add every optional resource to this budget.

## Daily allocations

- Days 15–22, each: 80 min lecture notes/examples + 30 min selected resources + 75 min lab/independent artifact + 25 min review/project contribution = 210 min.
- Day 23: 60 min lecture notes/examples + 30 min selected resources + 75 min retrieval-variants lab + 45 min project integration/module review = 210 min.
- Day 24: 40 min lecture notes/examples + 15 min selected resources + 45 min architecture lab + 50 min project integration + 60 min final assessment/review = 210 min.

Total: 740 min guided notes/examples + 285 min external reading/video + 720 min labs/assignments + 295 min review/project integration + 60 min final assessment = 2,100 min = 35 hours. Lab components become project components rather than being rebuilt independently. The final assessment can reuse lab/project artifacts; extend the calendar if actual implementation or review needs more time, rather than claiming unperformed acceptance criteria are satisfied.

## Materials-only use now

Read, inspect sources, do hand calculations, and review lab/project/assessment instructions. The user has deferred every implementation until the whole course’s materials are ready. No runtime, parser model, collection, or provider integration is created by this material-authoring task.

## Daily navigation

- Day 15: [Vector store and identity contracts](sections/section-01-vector-databases/modules/module-01-vector-contracts/README.md) · [Lab 1](sections/section-01-vector-databases/modules/module-01-vector-contracts/labs/lab-01.md)
- Day 16: [Qdrant lifecycle and querying](sections/section-01-vector-databases/modules/module-02-qdrant-lifecycle/README.md) · [Lab 2](sections/section-01-vector-databases/modules/module-02-qdrant-lifecycle/labs/lab-02.md)
- Day 17: [Manual RAG and evidence contracts](sections/section-02-manual-rag-chunking/modules/module-01-manual-rag/README.md) · [Lab 3](sections/section-02-manual-rag-chunking/modules/module-01-manual-rag/labs/lab-03.md)
- Day 18: [Chunk boundaries and token budgets](sections/section-02-manual-rag-chunking/modules/module-02-chunking/README.md) · [Lab 4](sections/section-02-manual-rag-chunking/modules/module-02-chunking/labs/lab-04.md)
- Day 19: [Provenance and ingestion lifecycle](sections/section-02-manual-rag-chunking/modules/module-03-provenance-lifecycle/README.md) · [Lab 5](sections/section-02-manual-rag-chunking/modules/module-03-provenance-lifecycle/labs/lab-05.md)
- Day 20: [LangChain components and model boundaries](sections/section-03-langchain-rag/modules/module-01-components/README.md) · [Lab 6](sections/section-03-langchain-rag/modules/module-01-components/labs/lab-06.md)
- Day 21: [LangChain RAG and parity checks](sections/section-03-langchain-rag/modules/module-02-integration-parity/README.md) · [Lab 7](sections/section-03-langchain-rag/modules/module-02-integration-parity/labs/lab-07.md)
- Day 22: [Docling and multi-format parsing](sections/section-04-document-parsing-retrieval/modules/module-01-docling-formats/README.md) · [Lab 8](sections/section-04-document-parsing-retrieval/modules/module-01-docling-formats/labs/lab-08.md)
- Day 23: [Filtering, rewriting, fusion, and reranking](sections/section-04-document-parsing-retrieval/modules/module-02-retrieval-orientation/README.md) · [Lab 9](sections/section-04-document-parsing-retrieval/modules/module-02-retrieval-orientation/labs/lab-09.md)
- Day 24: [Knowledge assistant architecture and review](sections/section-05-system-design-project/modules/module-01-architecture/README.md) · [Lab 10](sections/section-05-system-design-project/modules/module-01-architecture/labs/lab-10.md)

## Study and resource order

Use lecture notes → required publisher excerpt → worked example/lab → independent counterexample → module assessment. Optional videos replace optional reading, not the core material. Familiar Python/API/testing concepts need not be relearned from scratch. Keep manual RAG before LangChain; Day 23 variants are orientation, and Phase 4 owns their depth/tuning.

## Implementation prerequisites for later

When implementation is requested, create a separate learner workspace with a reviewed environment/lockfile, local synthetic/licensed corpus, pinned encoder/parser versions, and an isolated Qdrant sandbox. Choose any live generator/provider and review its official capabilities/credentials/cost then. Prior-phase project implementations are Planned, so either build their components first or use the specified fakes/contracts until they exist.
