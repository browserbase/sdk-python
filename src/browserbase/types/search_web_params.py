# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union
from datetime import datetime
from typing_extensions import Literal, Required, Annotated, TypeAlias, TypedDict

from .._types import SequenceNotStr
from .._utils import PropertyInfo

__all__ = ["SearchWebParams", "Variant0", "Variant1", "Variant2"]


class Variant0(TypedDict, total=False):
    provider: Required[Literal["parallel"]]
    """Search provider to serve this request.

    Defaults to `parallel`, which uses `advanced` mode unless `mode` is set.
    """

    query: Required[str]
    """The search query string"""

    category: Literal["company", "publication", "news", "personal site", "financial report", "people"]
    """Focus the search on a category of content"""

    end_published_date: Annotated[Union[str, datetime], PropertyInfo(alias="endPublishedDate", format="iso8601")]
    """Only return results published before this date (ISO 8601).

    Not supported with the company or people categories.
    """

    excerpts: bool
    """Return the passages of each page most relevant to the query. Defaults to false."""

    exclude_domains: Annotated[SequenceNotStr[str], PropertyInfo(alias="excludeDomains")]
    """Never return results from these domains.

    Accepts the same entry formats as includeDomains. Not supported with the people
    category.
    """

    include_domains: Annotated[SequenceNotStr[str], PropertyInfo(alias="includeDomains")]
    """Only return results from these domains.

    Entries can be a hostname (example.com), a hostname with a path prefix
    (example.com/docs), or a wildcard subdomain (\\**.example.com).
    """

    max_age_hours: Annotated[int, PropertyInfo(alias="maxAgeHours")]
    """Refetch a page when the cached copy is older than this many hours.

    Omit to use the provider default. A provider can return an older cached copy
    when a live fetch fails.
    """

    mode: Literal["fast", "advanced"]
    """The search mode used by the underlying provider.

    Defaults to `advanced` for `parallel` and `fast` for `exa`. See the
    [Search docs](https://docs.browserbase.com/platform/search/overview) for the
    available modes.
    """

    moderation: bool
    """Filter unsafe content from the results. Defaults to false."""

    num_results: Annotated[int, PropertyInfo(alias="numResults")]
    """Number of results to return"""

    objective: str
    """The task intent and soft preferences for the search, in natural language.

    Adds context to query without replacing it.
    """

    start_published_date: Annotated[Union[str, datetime], PropertyInfo(alias="startPublishedDate", format="iso8601")]
    """Only return results published after this date (ISO 8601).

    Not supported with the company or people categories.
    """

    user_location: Annotated[str, PropertyInfo(alias="userLocation")]
    """Two-letter ISO 3166-1 country code of the end user, used to localize results.

    This localizes ranking and does not restrict results to sources from that
    country.
    """


class Variant1(TypedDict, total=False):
    provider: Required[Literal["exa"]]
    """Search provider to serve this request.

    Defaults to `parallel`, which uses `advanced` mode unless `mode` is set.
    """

    query: Required[str]
    """The search query string"""

    category: Literal["company", "publication", "news", "personal site", "financial report", "people"]
    """Focus the search on a category of content"""

    end_published_date: Annotated[Union[str, datetime], PropertyInfo(alias="endPublishedDate", format="iso8601")]
    """Only return results published before this date (ISO 8601).

    Not supported with the company or people categories.
    """

    excerpts: bool
    """Return the passages of each page most relevant to the query. Defaults to false."""

    exclude_domains: Annotated[SequenceNotStr[str], PropertyInfo(alias="excludeDomains")]
    """Never return results from these domains.

    Accepts the same entry formats as includeDomains. Not supported with the people
    category.
    """

    include_domains: Annotated[SequenceNotStr[str], PropertyInfo(alias="includeDomains")]
    """Only return results from these domains.

    Entries can be a hostname (example.com), a hostname with a path prefix
    (example.com/docs), or a wildcard subdomain (\\**.example.com).
    """

    max_age_hours: Annotated[int, PropertyInfo(alias="maxAgeHours")]
    """Refetch a page when the cached copy is older than this many hours.

    Omit to use the provider default. A provider can return an older cached copy
    when a live fetch fails.
    """

    mode: Literal["fast", "deep-lite", "deep"]
    """The search mode used by the underlying provider.

    Defaults to `advanced` for `parallel` and `fast` for `exa`. See the
    [Search docs](https://docs.browserbase.com/platform/search/overview) for the
    available modes.
    """

    moderation: bool
    """Filter unsafe content from the results. Defaults to false."""

    num_results: Annotated[int, PropertyInfo(alias="numResults")]
    """Number of results to return"""

    objective: str
    """The task intent and soft preferences for the search, in natural language.

    Adds context to query without replacing it.
    """

    start_published_date: Annotated[Union[str, datetime], PropertyInfo(alias="startPublishedDate", format="iso8601")]
    """Only return results published after this date (ISO 8601).

    Not supported with the company or people categories.
    """

    user_location: Annotated[str, PropertyInfo(alias="userLocation")]
    """Two-letter ISO 3166-1 country code of the end user, used to localize results.

    This localizes ranking and does not restrict results to sources from that
    country.
    """


class Variant2(TypedDict, total=False):
    query: Required[str]
    """The search query string"""

    category: Literal["company", "publication", "news", "personal site", "financial report", "people"]
    """Focus the search on a category of content"""

    end_published_date: Annotated[Union[str, datetime], PropertyInfo(alias="endPublishedDate", format="iso8601")]
    """Only return results published before this date (ISO 8601).

    Not supported with the company or people categories.
    """

    excerpts: bool
    """Return the passages of each page most relevant to the query. Defaults to false."""

    exclude_domains: Annotated[SequenceNotStr[str], PropertyInfo(alias="excludeDomains")]
    """Never return results from these domains.

    Accepts the same entry formats as includeDomains. Not supported with the people
    category.
    """

    include_domains: Annotated[SequenceNotStr[str], PropertyInfo(alias="includeDomains")]
    """Only return results from these domains.

    Entries can be a hostname (example.com), a hostname with a path prefix
    (example.com/docs), or a wildcard subdomain (\\**.example.com).
    """

    max_age_hours: Annotated[int, PropertyInfo(alias="maxAgeHours")]
    """Refetch a page when the cached copy is older than this many hours.

    Omit to use the provider default. A provider can return an older cached copy
    when a live fetch fails.
    """

    moderation: bool
    """Filter unsafe content from the results. Defaults to false."""

    num_results: Annotated[int, PropertyInfo(alias="numResults")]
    """Number of results to return"""

    objective: str
    """The task intent and soft preferences for the search, in natural language.

    Adds context to query without replacing it.
    """

    start_published_date: Annotated[Union[str, datetime], PropertyInfo(alias="startPublishedDate", format="iso8601")]
    """Only return results published after this date (ISO 8601).

    Not supported with the company or people categories.
    """

    user_location: Annotated[str, PropertyInfo(alias="userLocation")]
    """Two-letter ISO 3166-1 country code of the end user, used to localize results.

    This localizes ranking and does not restrict results to sources from that
    country.
    """


SearchWebParams: TypeAlias = Union[Variant0, Variant1, Variant2]
