"""auto_analysis — an autonomous data-analyst CLI agent."""

from .contracts import (
    AnalysisResult,
    AskUserCallback,
    CodeStep,
    DataProfile,
    ProgressCallback,
    ProgressEvent,
)

__all__ = [
    "AnalysisResult",
    "AskUserCallback",
    "CodeStep",
    "DataProfile",
    "ProgressCallback",
    "ProgressEvent",
]

__version__ = "0.0.0"
