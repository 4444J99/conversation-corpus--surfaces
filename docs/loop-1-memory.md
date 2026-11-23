# Loop 1: memory

The first user loop is deliberately small:

1. A person has AI conversations spread across providers and wants to recall a decision.
2. They point CCE at their own exports; the engine builds a validated local corpus.
3. They ask a question through the CLI or an MCP host.
4. They get a cited answer, plus an explicit signal about source freshness and validation status.

Surfaces responsibilities in this loop: make the ask easy (landing page, MCP
setup docs), make the answer legible (future web search app), and publish the
interface contract. Everything about how the corpus is built stays in the
engine.

Success signal for Loop 1: an external user can complete steps 2–4 without
reading engine internals and can say whether they trust the answer.
