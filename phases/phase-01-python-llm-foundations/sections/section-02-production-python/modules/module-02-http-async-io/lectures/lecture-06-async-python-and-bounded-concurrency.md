# Lecture 06 — Async Python and bounded concurrency

[Phase home](../../../../../README.md) · [Module](../README.md)

## Lecture metadata

ID: P01-L06 · Duration: 75 minutes · Material status: In Review · Learner completion: Planned.

## Learning objectives

Explain coroutines and the event loop; run independent I/O concurrently; bound pressure on downstream services.

## Prerequisites

Complete Lecture 5 and its knowledge checks.

## Detailed theory

- `async`/`await` improves throughput for waiting-heavy I/O; it does not make CPU-bound work faster.
- A coroutine must be awaited. `asyncio.gather` runs awaitables concurrently but needs an error policy.
- A semaphore or worker queue limits concurrency. Provider rate limits, connection pools, memory, and downstream SLOs determine the bound.
- Cancellation and timeouts are normal control paths. Clean up clients using `async with` and do not swallow `CancelledError`.
- Avoid creating a new async client in each request; retain it for the application lifecycle.

### Demonstration

```python
import asyncio
import httpx

async def fetch(client: httpx.AsyncClient, url: str, gate: asyncio.Semaphore) -> str:
    async with gate:
        response = await client.get(url)
        response.raise_for_status()
        return response.text
```

## Technical explanations

Trace the semaphore example below: acquisition, awaited network operation, and release on success or exception. Note that asyncio does not parallelize CPU-heavy work.

## Real-world example

Three independent company pages can be fetched while waiting for I/O, but only two should occupy downstream connections at once.

## Code walkthrough

In the fetch coroutine, async with gate acquires one slot before the network wait. Awaiting client.get allows another task to run; raise_for_status exposes failure, and the context manager releases the slot even if it raises. Wrap the shared AsyncClient around the whole batch rather than around each task. This is a teaching walkthrough; implementation is deferred.

## Learning resources

[Required and optional resources](../../../../../resources/README.md#lectures-5-6-resources) (Lecture 6 grouping). Read required selections alongside the lecture; optional resources close specific gaps.

## Hands-on exercise

Trace three tasks with a concurrency bound of two, including one failure. Specify cancellation and client-cleanup behavior.

## Knowledge checks

1. Why can unlimited `gather` reduce reliability?
2. Which work belongs in a process pool rather than the event loop?
3. What resource does `async with` protect?

## Completion criteria

You can fetch three URLs concurrently with a bound of two and correctly surface one failing request.

## Next lecture

[Previous lecture](lecture-05-http-client-engineering.md) · [Next lecture](../../../../section-03-llm-apis-contracts-prompts/modules/module-01-provider-boundaries-streaming/lectures/lecture-07-llm-apis-and-provider-abstraction.md)
