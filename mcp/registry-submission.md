# MCP registry submission (H2, planned)

Submission inputs are staged here; publishing is an owner-gated external action.

- Package: `conversation-corpus-engine[mcp]` (engine repo)
- Entry point: `cce-mcp --project-root /path/to/project`
- Transport: stdio
- Tools: `cce_search`, `cce_list_corpora`, `cce_surface_context`
- Privacy posture: read-only; corpus path is server configuration; no raw
  provider exports or credentials in the package.

Before submitting, verify the install command from a clean environment and
record the published package version and registry URL in issue #20.
