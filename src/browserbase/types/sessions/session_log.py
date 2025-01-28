# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, Optional

from pydantic import Field as FieldInfo

from ..._models import BaseModel

__all__ = ["SessionLog", "Request", "Response"]


class Request(BaseModel):
    params: Dict[str, object]

    raw_body: str = FieldInfo(alias="rawBody")

    timestamp: Optional[int] = None
    """milliseconds that have elapsed since the UNIX epoch"""


class Response(BaseModel):
    raw_body: str = FieldInfo(alias="rawBody")

    result: Dict[str, object]

    timestamp: Optional[int] = None
    """milliseconds that have elapsed since the UNIX epoch"""


class SessionLog(BaseModel):
    method: str

    page_id: int = FieldInfo(alias="pageId")

    session_id: str = FieldInfo(alias="sessionId")

    frame_id: Optional[str] = FieldInfo(alias="frameId", default=None)

    loader_id: Optional[str] = FieldInfo(alias="loaderId", default=None)

    request: Optional[Request] = None

    response: Optional[Response] = None

    timestamp: Optional[int] = None
    """milliseconds that have elapsed since the UNIX epoch"""
