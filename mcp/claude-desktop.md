# Claude Desktop / MCP host setup

CCE's MCP server is read-only and speaks stdio. Install the engine with its
`mcp` extra, then point your host at `cce-mcp`:

```bash
pipx install "conversation-corpus-engine[mcp] @ git+https://github.com/4444J99/conversation-corpus-engine.git@v0.3.1"
```

```json
{
  "mcpServers": {
    "conversation-corpus-engine": {
      "command": "cce-mcp",
      "args": ["--project-root", "/path/to/project"]
    }
  }
}
```

Tools advertised today:

| Tool | Purpose |
| --- | --- |
| `cce_search` | Search a registered corpus and return grounded, cited answers |
| `cce_list_corpora` | List corpora registered for the project |
| `cce_surface_context` | Build the MCP-facing project context payload |

The corpus root is host configuration, never a tool argument. Archive/library
search tools are only advertised when the server is started with the matching
`--archive-root` / `--library-store-root` flags.
