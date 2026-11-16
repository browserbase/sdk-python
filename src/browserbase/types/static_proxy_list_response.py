# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from pydantic import Field as FieldInfo

from .._models import BaseModel

__all__ = ["StaticProxyListResponse"]


class StaticProxyListResponse(BaseModel):
    data: List[str]
    """IDs of enabled static proxies. Use as proxyId when creating a session."""

    limit: int

    next_cursor: Optional[str] = FieldInfo(alias="nextCursor", default=None)
    """Pass as cursor for the next page; null on the last page."""
