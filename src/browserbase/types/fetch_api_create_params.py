# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict
from typing_extensions import Literal, Required, Annotated, TypedDict

from .._utils import PropertyInfo

__all__ = ["FetchAPICreateParams"]


class FetchAPICreateParams(TypedDict, total=False):
    url: Required[str]
    """The URL to fetch"""

    allow_insecure_ssl: Annotated[bool, PropertyInfo(alias="allowInsecureSsl")]
    """Whether to bypass TLS certificate verification"""

    allow_redirects: Annotated[bool, PropertyInfo(alias="allowRedirects")]
    """Whether to follow HTTP redirects"""

    format: Literal["raw", "json", "markdown"]
    """Output format for the response content.

    `raw` (default) returns the response body unchanged; `json` returns structured
    data (requires `schema`); `markdown` returns the page as markdown.
    """

    proxies: bool
    """Whether to enable proxy support for the request"""

    schema: Dict[str, object]
    """JSON Schema describing the desired structure of the response.

    Only used when `format` is `json`.
    """
