# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union
from typing_extensions import Literal, Required, Annotated, TypeAlias, TypedDict

from .._utils import PropertyInfo

__all__ = ["SearchWebParams", "Variant0", "Variant1"]


class Variant0(TypedDict, total=False):
    provider: Required[Literal["parallel"]]
    """Search provider to serve this request.

    Omit to use the default provider for your project.
    """

    query: Required[str]
    """The search query string"""

    mode: Literal["fast", "advanced"]
    """The search mode used by the underlying provider.

    [Search docs](https://docs.browserbase.com/platform/search/overview) for the
    available modes and defaults.
    """

    num_results: Annotated[int, PropertyInfo(alias="numResults")]
    """Number of results to return (1-25)"""


class Variant1(TypedDict, total=False):
    query: Required[str]
    """The search query string"""

    num_results: Annotated[int, PropertyInfo(alias="numResults")]
    """Number of results to return (1-25)"""

    provider: Literal["exa"]
    """Search provider to serve this request.

    Omit to use the default provider for your project.
    """


SearchWebParams: TypeAlias = Union[Variant0, Variant1]
