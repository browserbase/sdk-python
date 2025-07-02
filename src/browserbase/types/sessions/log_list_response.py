# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, List, Optional
from typing_extensions import TypeAlias

from pydantic import Field as FieldInfo

from ..._models import BaseModel

__all__ = ["LogListResponse", "LogListResponseItem", "LogListResponseItemRequest", "LogListResponseItemResponse"]


class LogListResponseItemRequest(BaseModel):
    params: Dict[str, object]

    raw_body: str = FieldInfo(alias="rawBody")

    timestamp: Optional[int] = None
    """milliseconds that have elapsed since the UNIX epoch"""


class LogListResponseItemResponse(BaseModel):
    raw_body: str = FieldInfo(alias="rawBody")

    result: Dict[str, object]

    timestamp: Optional[int] = None
    """milliseconds that have elapsed since the UNIX epoch"""


class LogListResponseItem(BaseModel):
    method: str

    page_id: int = FieldInfo(alias="pageId")

    session_id: str = FieldInfo(alias="sessionId")

    frame_id: Optional[str] = FieldInfo(alias="frameId", default=None)

    loader_id: Optional[str] = FieldInfo(alias="loaderId", default=None)

    request: Optional[LogListResponseItemRequest] = None

    response: Optional[LogListResponseItemResponse] = None

    timestamp: Optional[int] = None
    """milliseconds that have elapsed since the UNIX epoch"""


LogListResponse: TypeAlias = List[LogListResponseItem]
