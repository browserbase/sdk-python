# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from datetime import datetime
from typing_extensions import Literal

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

    excerpts: Optional[List[str]] = None
    """Passages from the page most relevant to the query.

    Only set when the request asks for excerpts.
    """

    favicon: Optional[str] = None
    """Favicon URL"""

    image: Optional[str] = None
    """Image URL if available"""

    published_date: Optional[datetime] = FieldInfo(alias="publishedDate", default=None)
    """Publication date in RFC 3339 format"""


class SearchWebResponse(BaseModel):
    query: str
    """The search query that was executed"""

    request_id: str = FieldInfo(alias="requestId")
    """Unique identifier for the request"""

    results: List[Result]
    """List of search results"""

    mode: Optional[Literal["fast", "advanced", "deep-lite", "deep"]] = None
    """The search mode that served the request."""

    provider: Optional[Literal["parallel", "exa"]] = None
    """The search provider that served the request.

    Can differ from the documented default when the project or the filters select
    another provider.
    """
