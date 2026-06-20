"""CLI entrypoint (Person B, ``interface`` branch).

STAGE 0: minimal but real — parses a goal + data paths, calls the (stubbed)
``run_analysis``, and renders the result. The ``_ask_user`` and ``_on_progress``
rendering here is deliberately bare; Stage 2 (task 10) makes the question
rendering nicer, and Stage 4 (task 18) polishes the report.
"""

from __future__ import annotations

import argparse
from typing import Optional

from .agent import run_analysis
from .contracts import ProgressEvent


def _ask_user(question: str, options: Optional[list[str]] = None) -> str:
    """Render an agent question in the terminal and block for the answer."""
    print(f"\n[agent asks] {question}")
    if options:
        for i, opt in enumerate(options, 1):
            print(f"  {i}. {opt}")
        print("(enter a number or type your own answer)")
    answer = input("> ").strip()
    if options and answer.isdigit():
        idx = int(answer) - 1
        if 0 <= idx < len(options):
            return options[idx]
    return answer


def _on_progress(event: ProgressEvent) -> None:
    print(f"... {event.message}")


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        prog="auto-analysis",
        description="An AI agent that analyzes your data and answers your question.",
    )
    parser.add_argument("goal", help="What you want to find out from the data.")
    parser.add_argument(
        "data", nargs="+", help="One or more data files (CSV/XLSX/JSON)."
    )
    parser.add_argument(
        "--show-code",
        action="store_true",
        help="Also print the analysis code the agent ran (technical drill-down).",
    )
    return parser


def main(argv: Optional[list[str]] = None) -> int:
    args = build_parser().parse_args(argv)

    result = run_analysis(args.goal, args.data, _ask_user, _on_progress)

    print("\n=== Answer ===")
    print(result.answer)

    if result.method_notes:
        print(f"\nMethod: {result.method_notes}")

    if result.chart_paths:
        print("\nCharts:")
        for path in result.chart_paths:
            print(f"  - {path}")

    if args.show_code and result.code_trace:
        print("\n=== Code ===")
        for step in result.code_trace:
            print(step.code)
            if step.stdout:
                print(f"# stdout:\n{step.stdout}")
            if step.stderr:
                print(f"# stderr:\n{step.stderr}")

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
