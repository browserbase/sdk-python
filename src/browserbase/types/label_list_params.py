# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import TypedDict

__all__ = ["LabelListParams"]


class LabelListParams(TypedDict, total=False):
    cursor: str
    """Pagination cursor.

    Pass the nextCursor from the previous response to fetch the next page. Omit to
    start from the first page.
    """

    limit: int
    """Maximum number of results to return."""
