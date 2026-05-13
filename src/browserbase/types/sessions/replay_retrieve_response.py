# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List

from pydantic import Field as FieldInfo

from ..._models import BaseModel

__all__ = ["ReplayRetrieveResponse", "Page"]


class Page(BaseModel):
    end_time_ms: float = FieldInfo(alias="endTimeMs")

    page_id: str = FieldInfo(alias="pageId")

    start_time_ms: float = FieldInfo(alias="startTimeMs")

    url: str


class ReplayRetrieveResponse(BaseModel):
    page_count: int = FieldInfo(alias="pageCount")

    pages: List[Page]
