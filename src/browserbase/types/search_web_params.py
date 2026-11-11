# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union
from typing_extensions import Literal, Required, Annotated, TypeAlias, TypedDict

from .._utils import PropertyInfo

__all__ = [
    "SearchWebParams",
    "Variant0",
    "Variant0Excerpts",
    "Variant1",
    "Variant1Excerpts",
    "Variant2",
    "Variant2Excerpts",
]


class Variant0(TypedDict, total=False):
    provider: Required[Literal["parallel"]]
    """Search provider to serve this request.

    Defaults to `parallel`, which uses `advanced` mode unless `mode` is set.
    """

    query: Required[str]
    """The search query string"""

    excerpts: Variant0Excerpts
    """Return the passages of each page most relevant to the query.

    Omit to return no excerpts.
    """

    max_age_hours: Annotated[int, PropertyInfo(alias="maxAgeHours")]
    """Refetch a page when the cached copy is older than this many hours, from 1
    to 720.

    0 always fetches fresh content and -1 uses only cached content (exa provider
    only). Omit to use the provider default. This is a refresh threshold, not a
    strict maximum age: a provider can return an older cached copy when a live fetch
    fails.
    """

    mode: Literal["fast", "advanced"]
    """The search mode used by the underlying provider.

    Defaults to `advanced` for `parallel` and `fast` for `exa`. See the
    [Search docs](https://docs.browserbase.com/platform/search/overview) for the
    available modes.
    """

    num_results: Annotated[int, PropertyInfo(alias="numResults")]
    """Number of results to return (1-25)"""

    objective: str
    """The task intent and soft preferences for the search, in natural language.

    Adds context to query without replacing it.
    """


class Variant0Excerpts(TypedDict, total=False):
    """Return the passages of each page most relevant to the query.

    Omit to return no excerpts.
    """

    max_characters: Annotated[int, PropertyInfo(alias="maxCharacters")]
    """Maximum excerpt characters per result. Omit to use the provider default."""


class Variant1(TypedDict, total=False):
    provider: Required[Literal["exa"]]
    """Search provider to serve this request.

    Defaults to `parallel`, which uses `advanced` mode unless `mode` is set.
    """

    query: Required[str]
    """The search query string"""

    excerpts: Variant1Excerpts
    """Return the passages of each page most relevant to the query.

    Omit to return no excerpts.
    """

    max_age_hours: Annotated[int, PropertyInfo(alias="maxAgeHours")]
    """Refetch a page when the cached copy is older than this many hours, from 1
    to 720.

    0 always fetches fresh content and -1 uses only cached content (exa provider
    only). Omit to use the provider default. This is a refresh threshold, not a
    strict maximum age: a provider can return an older cached copy when a live fetch
    fails.
    """

    mode: Literal["fast", "deep-lite", "deep"]
    """The search mode used by the underlying provider.

    Defaults to `advanced` for `parallel` and `fast` for `exa`. See the
    [Search docs](https://docs.browserbase.com/platform/search/overview) for the
    available modes.
    """

    num_results: Annotated[int, PropertyInfo(alias="numResults")]
    """Number of results to return (1-25)"""

    objective: str
    """The task intent and soft preferences for the search, in natural language.

    Adds context to query without replacing it.
    """


class Variant1Excerpts(TypedDict, total=False):
    """Return the passages of each page most relevant to the query.

    Omit to return no excerpts.
    """

    max_characters: Annotated[int, PropertyInfo(alias="maxCharacters")]
    """Maximum excerpt characters per result. Omit to use the provider default."""


class Variant2(TypedDict, total=False):
    query: Required[str]
    """The search query string"""

    excerpts: Variant2Excerpts
    """Return the passages of each page most relevant to the query.

    Omit to return no excerpts.
    """

    max_age_hours: Annotated[int, PropertyInfo(alias="maxAgeHours")]
    """Refetch a page when the cached copy is older than this many hours, from 1
    to 720.

    0 always fetches fresh content and -1 uses only cached content (exa provider
    only). Omit to use the provider default. This is a refresh threshold, not a
    strict maximum age: a provider can return an older cached copy when a live fetch
    fails.
    """

    num_results: Annotated[int, PropertyInfo(alias="numResults")]
    """Number of results to return (1-25)"""

    objective: str
    """The task intent and soft preferences for the search, in natural language.

    Adds context to query without replacing it.
    """


class Variant2Excerpts(TypedDict, total=False):
    """Return the passages of each page most relevant to the query.

    Omit to return no excerpts.
    """

    max_characters: Annotated[int, PropertyInfo(alias="maxCharacters")]
    """Maximum excerpt characters per result. Omit to use the provider default."""


SearchWebParams: TypeAlias = Union[Variant0, Variant1, Variant2]
