"""The A<->B seam for Auto_Analysis.

This module is the *contract* between the two halves of the project:

- Person A (Agent Core) implements ``run_analysis`` and *invokes* ``AskUserCallback``
  / ``ProgressCallback``.
- Person B (Interface/Data/Output) *calls* ``run_analysis``, *implements* the two
  callbacks (terminal rendering), and *produces* ``DataProfile``.

Nothing here should import the Agent SDK, pandas, or the CLI — it is pure data
shapes and typing so both branches can develop against it independently.

⚠️  Any change to this file requires BOTH people to agree (it is the shared seam).
"""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Callable, Optional, Protocol


# --------------------------------------------------------------------------- #
# Data understanding (Person B produces, Person A injects into the prompt)
# --------------------------------------------------------------------------- #
@dataclass
class DataProfile:
    """A lightweight, grounding summary of one data file.

    Built by Person B's profiler (Stage 1, task 7) so the agent starts with a
    factual picture of the data instead of guessing at columns.
    """

    path: str
    n_rows: int
    n_cols: int
    columns: list[str] = field(default_factory=list)
    dtypes: dict[str, str] = field(default_factory=dict)          # column -> dtype name
    missing: dict[str, int] = field(default_factory=dict)         # column -> # missing
    sample_rows: list[dict] = field(default_factory=list)         # first few rows

    def as_prompt_block(self) -> str:
        """Render the profile as a compact text block to inject into the prompt."""
        lines = [
            f"File: {self.path}",
            f"Shape: {self.n_rows} rows x {self.n_cols} cols",
            "Columns:",
        ]
        for col in self.columns:
            dtype = self.dtypes.get(col, "?")
            miss = self.missing.get(col, 0)
            lines.append(f"  - {col} ({dtype}); missing={miss}")
        return "\n".join(lines)


# --------------------------------------------------------------------------- #
# The result that flows back from the agent to the CLI
# --------------------------------------------------------------------------- #
@dataclass
class CodeStep:
    """One unit of analysis code the agent ran, plus its captured output."""

    code: str
    stdout: str = ""
    stderr: str = ""
    ok: bool = True


@dataclass
class AnalysisResult:
    """The final payload Person A returns and Person B renders.

    ``answer`` is the plain-language result (shown to everyone). ``code_trace``
    and ``method_notes`` are the technical drill-down (shown on ``--show-code``).
    """

    answer: str
    method_notes: str = ""
    code_trace: list[CodeStep] = field(default_factory=list)
    chart_paths: list[str] = field(default_factory=list)


# --------------------------------------------------------------------------- #
# Live callbacks during a run
# --------------------------------------------------------------------------- #
@dataclass
class ProgressEvent:
    """An interim signal emitted by the agent core while it works."""

    kind: str        # "status" | "thinking" | "tool" | "text"
    message: str


# Person B implements (renders a question in the terminal, blocks, returns the
# user's answer). Person A invokes this from the ``ask_user`` tool.
#   args: (question, options_or_None) -> answer_string
AskUserCallback = Callable[[str, Optional[list[str]]], str]

# Person A emits these as it works; Person B renders them.
ProgressCallback = Callable[[ProgressEvent], None]


class AnalysisRunner(Protocol):
    """The single entrypoint Person A provides and Person B drives."""

    def __call__(
        self,
        goal: str,
        data_paths: list[str],
        ask_user: AskUserCallback,
        on_progress: ProgressCallback,
    ) -> AnalysisResult: ...
