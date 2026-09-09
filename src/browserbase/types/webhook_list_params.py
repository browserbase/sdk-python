# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import TypedDict

__all__ = ["WebhookListParams"]


class WebhookListParams(TypedDict, total=False):
    cursor: str
    """Cursor from a previous response's `nextCursor`. Omit for the first page."""

    limit: int
    """Maximum number of results to return."""
