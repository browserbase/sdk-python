# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union
from datetime import datetime
from typing_extensions import Required, Annotated, TypedDict

from .._utils import PropertyInfo

__all__ = ["DownloadListParams"]


class DownloadListParams(TypedDict, total=False):
    session_id: Required[Annotated[str, PropertyInfo(alias="sessionId")]]
    """Filter downloads by session ID (required)."""

    created_after: Annotated[Union[str, datetime], PropertyInfo(alias="createdAfter", format="iso8601")]
    """Filter downloads created on or after this timestamp."""

    created_before: Annotated[Union[str, datetime], PropertyInfo(alias="createdBefore", format="iso8601")]
    """Filter downloads created on or before this timestamp."""

    filename: str
    """Filter by exact filename match."""

    limit: int
    """Maximum number of results to return."""

    max_size: Annotated[float, PropertyInfo(alias="maxSize")]
    """Maximum file size in bytes."""

    mime_type: Annotated[str, PropertyInfo(alias="mimeType")]
    """Filter by MIME type."""

    min_size: Annotated[float, PropertyInfo(alias="minSize")]
    """Minimum file size in bytes."""

    offset: int
    """Number of results to skip for pagination."""
