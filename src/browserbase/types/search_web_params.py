# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, Annotated, TypedDict

from .._utils import PropertyInfo

__all__ = ["SearchWebParams"]


class SearchWebParams(TypedDict, total=False):
    query: Required[str]
    """The search query string"""

    num_results: Annotated[int, PropertyInfo(alias="numResults")]
    """Number of results to return (1-25)"""
