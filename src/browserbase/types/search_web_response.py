# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from datetime import datetime

from pydantic import Field as FieldInfo

from .._models import BaseModel

__all__ = ["SearchWebResponse", "Result"]


class Result(BaseModel):
    id: str
    """Unique identifier for the result"""

    title: str
    """The title of the search result"""

    url: str
    """The URL of the search result"""

    author: Optional[str] = None
    """Author of the content if available"""

    favicon: Optional[str] = None
    """Favicon URL"""

    image: Optional[str] = None
    """Image URL if available"""

    published_date: Optional[datetime] = FieldInfo(alias="publishedDate", default=None)
    """Publication date in ISO 8601 format"""


class SearchWebResponse(BaseModel):
    """Response body for web search"""

    query: str
    """The search query that was executed"""

    request_id: str = FieldInfo(alias="requestId")
    """Unique identifier for the request"""

    results: List[Result]
    """List of search results"""
