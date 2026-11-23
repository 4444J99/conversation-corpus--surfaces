# conversation-corpus--surfaces

[![Pages](https://github.com/4444J99/conversation-corpus--surfaces/actions/workflows/pages.yml/badge.svg)](https://github.com/4444J99/conversation-corpus--surfaces/actions/workflows/pages.yml)

The ORGAN-II bridge for [Conversation Corpus Engine](https://github.com/4444J99/conversation-corpus-engine) (CCE). This repo turns engine outputs into audience-facing and tool-facing interfaces without moving billing or product-state logic into the engine.

Landing page: https://4444j99.github.io/conversation-corpus--surfaces/

The waitlist form is intentionally inert until a submission sink is configured
and tested; see [`apps/landing/README.md`](apps/landing/README.md).

## Constitutional boundary

| Concern | Owner |
| --- | --- |
| Provider import, validation, federation, retrieval, source policy | `conversation-corpus-engine` (ORGAN-I) |
| Web app, SDK wrapper, MCP packaging docs, API gateway, interface contracts | **this repo** (ORGAN-II) |
| Stripe, pricing, licenses, seats, invoices, billing API | `conversation-corpus--product` (ORGAN-III) |

Signal contract:

```text
CCE engine
  consumes: ARCHIVE_PACKET
  emits: ANNOTATED_CORPUS, VALIDATION_RECORD, STATE_MODEL

conversation-corpus--surfaces
  consumes: STATE_MODEL, VALIDATION_RECORD
  emits: INTERFACE_CONTRACT

conversation-corpus--product
  consumes: INTERFACE_CONTRACT
  emits: STATE_MODEL (billing)
```

No ORGAN-I → ORGAN-III dependency is introduced; surfaces are the bridge.

## Layout

```text
apps/
  landing/                Static H1 landing page (GitHub Pages source)
  web-search/             H2 web search prototype (planned)
packages/
  python-sdk/             Thin wrapper over CCE surface CLI commands
  interface-contracts/    INTERFACE_CONTRACT v1 JSON schema
mcp/                      MCP host setup and registry submission notes
docs/                     Product brief, loop-1 memory, launch copy
```

## Quick start

```bash
# Install the CCE engine with its MCP extra from the tagged release.
pipx install "conversation-corpus-engine[mcp] @ git+https://github.com/4444J99/conversation-corpus-engine.git@v0.3.1"

# Build and inspect the engine's outward-facing artifacts.
cce surface bundle --project-root /path/to/project --source-drop-root /path/to/source-drop
cce-mcp --project-root /path/to/project
```

The Python SDK wrapper (H2) is scaffolded in `packages/python-sdk/` and delegates to the same CLI; it does not reimplement engine logic.

## Non-goals

- No Stripe integration, license checks, or seat management.
- No mutation of CCE registry state.
- No raw provider exports, browser profiles, or credentials in this repo.

## License

MIT — see [LICENSE](LICENSE).
