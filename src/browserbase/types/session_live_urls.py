# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List

from pydantic import Field as FieldInfo

from .._models import BaseModel

__all__ = ["SessionLiveURLs", "Page"]


class Page(BaseModel):
    id: str

    debugger_fullscreen_url: str = FieldInfo(alias="debuggerFullscreenUrl")

    debugger_url: str = FieldInfo(alias="debuggerUrl")

    favicon_url: str = FieldInfo(alias="faviconUrl")

    title: str

    url: str


class SessionLiveURLs(BaseModel):
    debugger_fullscreen_url: str = FieldInfo(alias="debuggerFullscreenUrl")

    debugger_url: str = FieldInfo(alias="debuggerUrl")

    pages: List[Page]

    ws_url: str = FieldInfo(alias="wsUrl")
