# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict

from pydantic import Field as FieldInfo

from .._models import BaseModel

__all__ = ["FetchAPICreateResponse"]


class FetchAPICreateResponse(BaseModel):
    id: str
    """Unique identifier for the fetch request"""

    content: str
    """The response body content"""

    content_type: str = FieldInfo(alias="contentType")
    """The MIME type of the response"""

    encoding: str
    """The character encoding of the response"""

    headers: Dict[str, str]
    """Response headers as key-value pairs"""

    status_code: int = FieldInfo(alias="statusCode")
    """HTTP status code of the fetched response"""
