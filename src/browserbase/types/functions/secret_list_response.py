# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from pydantic import Field as FieldInfo

from ..secret import Secret
from ..._models import BaseModel

__all__ = ["SecretListResponse"]


class SecretListResponse(BaseModel):
    """A page of secrets."""

    data: List[Secret]
    """The page of matching secrets."""

    limit: int
    """The maximum number of results returned in this page."""

    next_cursor: Optional[str] = FieldInfo(alias="nextCursor", default=None)
    """Cursor for the next page.

    Pass it back as `cursor` on the next request to continue paging. null when there
    are no more results.
    """
