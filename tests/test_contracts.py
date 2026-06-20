"""Stage 0 seam test — proves the CLI<->core contract round-trips.

Run with:  pytest -q
"""

from __future__ import annotations

from auto_analysis.agent import run_analysis
from auto_analysis.contracts import AnalysisResult, DataProfile, ProgressEvent


def test_run_analysis_stub_returns_analysis_result():
    events: list[ProgressEvent] = []
    answers = iter([])  # stub should not ask anything

    def ask_user(question, options=None):  # pragma: no cover - not hit by stub
        return next(answers)

    result = run_analysis(
        goal="What drives sales?",
        data_paths=["sample_data/sample.csv"],
        ask_user=ask_user,
        on_progress=events.append,
    )

    assert isinstance(result, AnalysisResult)
    assert result.answer
    assert events, "agent core should emit at least one progress event"


def test_data_profile_prompt_block_lists_columns():
    profile = DataProfile(
        path="sample.csv",
        n_rows=3,
        n_cols=2,
        columns=["x", "y"],
        dtypes={"x": "int64", "y": "float64"},
        missing={"x": 0, "y": 1},
    )
    block = profile.as_prompt_block()
    assert "sample.csv" in block
    assert "x (int64); missing=0" in block
    assert "y (float64); missing=1" in block
