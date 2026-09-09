# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from pydantic import Field as FieldInfo

from .webhook import Webhook
from .._models import BaseModel

__all__ = ["WebhookListResponse"]


class WebhookListResponse(BaseModel):
    """A page of webhooks. Signing secrets are not included."""

    data: List[Webhook]
    """The page of webhooks, newest first."""

    limit: int
    """The maximum number of results returned in this page."""

    next_cursor: Optional[str] = FieldInfo(alias="nextCursor", default=None)
    """Cursor for the next page.

    Pass it back as `cursor` to continue paging. null when there are no more
    results.
    """
