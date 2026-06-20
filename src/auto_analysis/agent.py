"""Agent Core (Person A, ``core`` branch).

STAGE 0: this is a *stub*. ``run_analysis`` returns a canned ``AnalysisResult``
so the CLI <-> core seam can be exercised end-to-end before any real agent loop
exists. Stage 1 (tasks 4-5) replaces the body with a real ``claude-agent-sdk``
loop + the ``run_python`` tool.
"""

from __future__ import annotations

from .contracts import (
    AnalysisResult,
    AskUserCallback,
    CodeStep,
    ProgressCallback,
    ProgressEvent,
)


def run_analysis(
    goal: str,
    data_paths: list[str],
    ask_user: AskUserCallback,
    on_progress: ProgressCallback,
) -> AnalysisResult:
    """Stage 0 walking-seam placeholder.

    Real implementation (Stage 1): build the agent loop on ``claude-opus-4-8``
    (adaptive thinking, effort high), wire the ``run_python`` and ``ask_user``
    tools, inject the ``DataProfile``, and return the agent's findings.
    """
    on_progress(
        ProgressEvent("status", f"(stub) received goal {goal!r} over {data_paths}")
    )
    return AnalysisResult(
        answer=(
            "(stub) Analysis is not implemented yet -- this is the Stage 0 "
            "walking-seam placeholder proving the CLI can call the core and "
            "render a result."
        ),
        method_notes="stub: no method chosen yet",
        code_trace=[CodeStep(code="# no analysis code has run yet", ok=True)],
        chart_paths=[],
    )
