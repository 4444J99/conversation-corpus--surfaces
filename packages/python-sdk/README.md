# cce-surfaces (scaffold)

A thin wrapper over the `cce surface` CLI. It deliberately contains no
corpus, retrieval, or policy logic — those stay in
[conversation-corpus-engine](https://github.com/4444J99/conversation-corpus-engine).

```python
from pathlib import Path
from cce_surfaces import surface_bundle

bundle = surface_bundle(Path("/path/to/project"))
print(bundle["contract_version"] if "contract_version" in bundle else bundle.keys())
```

Functions:

- `surface_manifest(project_root, source_drop_root=None)` — `cce surface manifest`
- `mcp_context(project_root, source_drop_root=None)` — `cce surface context`
- `surface_bundle(project_root, source_drop_root=None)` — `cce surface bundle`

Each returns the JSON payload printed by the CLI. A non-zero CLI exit raises
`CCEError`. The `cce` executable must be installed (for example with the
engine's `mcp` extra).
