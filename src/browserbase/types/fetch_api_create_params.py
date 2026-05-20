# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, Annotated, TypedDict

from .._utils import PropertyInfo

__all__ = ["FetchAPICreateParams"]


class FetchAPICreateParams(TypedDict, total=False):
    url: Required[str]
    """The URL to fetch"""

    allow_insecure_ssl: Annotated[bool, PropertyInfo(alias="allowInsecureSsl")]
    """Whether to bypass TLS certificate verification"""

    allow_redirects: Annotated[bool, PropertyInfo(alias="allowRedirects")]
    """Whether to follow HTTP redirects"""

    proxies: bool
    """Whether to enable proxy support for the request"""
