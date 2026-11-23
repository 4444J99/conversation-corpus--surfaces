# Web search (H2, planned)

Ring 1 web prototype for read-only conversation search over a CCE corpus.

Planned shape:

- Consume `INTERFACE_CONTRACT` from `packages/interface-contracts/`.
- Call the CCE MCP tools (`cce_search`, `cce_list_corpora`) through a host that
  owns the corpus path; never accept a corpus root from an untrusted client.
- Return cited answers only. No billing, auth, or seat logic belongs here —
  that is `conversation-corpus--product` (ORGAN-III).
