# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union
from datetime import datetime
from typing_extensions import Literal, Required, Annotated, TypeAlias, TypedDict

from .._types import SequenceNotStr
from .._utils import PropertyInfo

__all__ = ["SearchWebParams", "ProviderParallel", "ProviderExa", "DefaultProvider"]


class ProviderParallel(TypedDict, total=False):
    provider: Required[Literal["parallel"]]
    """Search provider to serve this request.

    Defaults to `parallel`, which uses `advanced` mode unless `mode` is set. If you
    omit it and `parallel` can't apply one of your filters, `exa` serves the request
    at `exa` pricing. The response `provider` field shows which one served it.
    """

    query: Required[str]
    """The search query string"""

    category: Literal["company", "publication", "news", "personal site", "financial report", "people"]
    """Focus the search on a category of content.

    Only the `exa` provider supports this filter.
    """

    end_published_date: Annotated[Union[str, datetime], PropertyInfo(alias="endPublishedDate", format="iso8601")]
    """
    Only return results published before this date-time (RFC 3339, for example
    2026-01-01T00:00:00Z). Only the `exa` provider supports this filter. Not
    supported with the company or people categories.
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
    (example.com/docs), or a wildcard subdomain (\\**.example.com). The `parallel`
    provider allows one list, not both, with at most 200 domains and no scheme,
    port, query string, or fragment.
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
    """Filter unsafe content from the results.

    Defaults to `false`. Only the `exa` provider supports `true`.
    """

    num_results: Annotated[int, PropertyInfo(alias="numResults")]
    """Number of results to return"""

    objective: str
    """The task intent and soft preferences for the search, in natural language.

    Adds context to query without replacing it.
    """

    start_published_date: Annotated[Union[str, datetime], PropertyInfo(alias="startPublishedDate", format="iso8601")]
    """
    Only return results published after this date-time (RFC 3339, for example
    2026-01-01T00:00:00Z). The `parallel` provider rounds it up to a whole UTC day.
    Not supported with the company or people categories.
    """

    user_location: Annotated[str, PropertyInfo(alias="userLocation")]
    """Two-letter ISO 3166-1 country code of the end user.

    Localizes ranking without restricting results to sources from that country. The
    `parallel` provider supports only
    [some countries](https://docs.browserbase.com/platform/search/overview#appendix-supported-countries).
    """


class ProviderExa(TypedDict, total=False):
    provider: Required[Literal["exa"]]
    """Search provider to serve this request.

    Defaults to `parallel`, which uses `advanced` mode unless `mode` is set. If you
    omit it and `parallel` can't apply one of your filters, `exa` serves the request
    at `exa` pricing. The response `provider` field shows which one served it.
    """

    query: Required[str]
    """The search query string"""

    category: Literal["company", "publication", "news", "personal site", "financial report", "people"]
    """Focus the search on a category of content.

    Only the `exa` provider supports this filter.
    """

    end_published_date: Annotated[Union[str, datetime], PropertyInfo(alias="endPublishedDate", format="iso8601")]
    """
    Only return results published before this date-time (RFC 3339, for example
    2026-01-01T00:00:00Z). Only the `exa` provider supports this filter. Not
    supported with the company or people categories.
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
    (example.com/docs), or a wildcard subdomain (\\**.example.com). The `parallel`
    provider allows one list, not both, with at most 200 domains and no scheme,
    port, query string, or fragment.
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
    """Filter unsafe content from the results.

    Defaults to `false`. Only the `exa` provider supports `true`.
    """

    num_results: Annotated[int, PropertyInfo(alias="numResults")]
    """Number of results to return"""

    objective: str
    """The task intent and soft preferences for the search, in natural language.

    Adds context to query without replacing it.
    """

    start_published_date: Annotated[Union[str, datetime], PropertyInfo(alias="startPublishedDate", format="iso8601")]
    """
    Only return results published after this date-time (RFC 3339, for example
    2026-01-01T00:00:00Z). The `parallel` provider rounds it up to a whole UTC day.
    Not supported with the company or people categories.
    """

    user_location: Annotated[str, PropertyInfo(alias="userLocation")]
    """Two-letter ISO 3166-1 country code of the end user.

    Localizes ranking without restricting results to sources from that country. The
    `parallel` provider supports only
    [some countries](https://docs.browserbase.com/platform/search/overview#appendix-supported-countries).
    """


class DefaultProvider(TypedDict, total=False):
    query: Required[str]
    """The search query string"""

    category: Literal["company", "publication", "news", "personal site", "financial report", "people"]
    """Focus the search on a category of content.

    Only the `exa` provider supports this filter.
    """

    end_published_date: Annotated[Union[str, datetime], PropertyInfo(alias="endPublishedDate", format="iso8601")]
    """
    Only return results published before this date-time (RFC 3339, for example
    2026-01-01T00:00:00Z). Only the `exa` provider supports this filter. Not
    supported with the company or people categories.
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
    (example.com/docs), or a wildcard subdomain (\\**.example.com). The `parallel`
    provider allows one list, not both, with at most 200 domains and no scheme,
    port, query string, or fragment.
    """

    max_age_hours: Annotated[int, PropertyInfo(alias="maxAgeHours")]
    """Refetch a page when the cached copy is older than this many hours.

    Omit to use the provider default. A provider can return an older cached copy
    when a live fetch fails.
    """

    moderation: bool
    """Filter unsafe content from the results.

    Defaults to `false`. Only the `exa` provider supports `true`.
    """

    num_results: Annotated[int, PropertyInfo(alias="numResults")]
    """Number of results to return"""

    objective: str
    """The task intent and soft preferences for the search, in natural language.

    Adds context to query without replacing it.
    """

    start_published_date: Annotated[Union[str, datetime], PropertyInfo(alias="startPublishedDate", format="iso8601")]
    """
    Only return results published after this date-time (RFC 3339, for example
    2026-01-01T00:00:00Z). The `parallel` provider rounds it up to a whole UTC day.
    Not supported with the company or people categories.
    """

    user_location: Annotated[str, PropertyInfo(alias="userLocation")]
    """Two-letter ISO 3166-1 country code of the end user.

    Localizes ranking without restricting results to sources from that country. The
    `parallel` provider supports only
    [some countries](https://docs.browserbase.com/platform/search/overview#appendix-supported-countries).
    """


SearchWebParams: TypeAlias = Union[ProviderParallel, ProviderExa, DefaultProvider]
