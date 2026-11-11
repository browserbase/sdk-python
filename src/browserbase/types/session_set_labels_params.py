# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, TypedDict

from .._types import SequenceNotStr

__all__ = ["SessionSetLabelsParams"]


class SessionSetLabelsParams(TypedDict, total=False):
    labels: Required[SequenceNotStr[str]]
    """Complete replacement set of label names.

    Empty clears assignments; missing names create labels.
    """
