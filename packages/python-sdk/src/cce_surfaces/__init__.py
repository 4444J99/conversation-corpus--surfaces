"""Thin Python wrappers over CCE surface CLI commands."""

from __future__ import annotations

import json
import subprocess
from pathlib import Path
from typing import Any

__all__ = ["CCEError", "mcp_context", "surface_bundle", "surface_manifest"]


class CCEError(RuntimeError):
    """Raised when the CCE CLI fails or emits unreadable JSON."""


def _run_surface(action: str, project_root: Path, source_drop_root: Path | None) -> dict[str, Any]:
    command = ["cce", "surface", action, "--project-root", str(project_root)]
    if source_drop_root is not None:
        command.extend(["--source-drop-root", str(source_drop_root)])
    result = subprocess.run(command, capture_output=True, text=True, check=False)
    if result.returncode != 0:
        raise CCEError(f"cce surface {action} failed: {result.stderr.strip()}")
    try:
        payload = json.loads(result.stdout)
    except json.JSONDecodeError as exc:
        raise CCEError(f"cce surface {action} did not emit JSON") from exc
    if not isinstance(payload, dict):
        raise CCEError(f"cce surface {action} emitted a non-object payload")
    return payload


def surface_manifest(
    project_root: Path, source_drop_root: Path | None = None
) -> dict[str, Any]:
    """Return the engine-facing externalization manifest."""
    return _run_surface("manifest", project_root, source_drop_root)


def mcp_context(
    project_root: Path, source_drop_root: Path | None = None
) -> dict[str, Any]:
    """Return the MCP-facing context payload."""
    return _run_surface("context", project_root, source_drop_root)


def surface_bundle(
    project_root: Path, source_drop_root: Path | None = None
) -> dict[str, Any]:
    """Return both exported surfaces plus their validation results."""
    return _run_surface("bundle", project_root, source_drop_root)
