# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union
from datetime import datetime
from typing_extensions import Literal, overload

import httpx

from ..types import search_web_params
from .._types import Body, Omit, Query, Headers, NotGiven, SequenceNotStr, omit, not_given
from .._utils import required_args, maybe_transform, async_maybe_transform
from .._compat import cached_property
from .._resource import SyncAPIResource, AsyncAPIResource
from .._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from .._base_client import make_request_options
from ..types.search_web_response import SearchWebResponse

__all__ = ["SearchResource", "AsyncSearchResource"]


class SearchResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> SearchResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/browserbase/sdk-python#accessing-raw-response-data-eg-headers
        """
        return SearchResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> SearchResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/browserbase/sdk-python#with_streaming_response
        """
        return SearchResourceWithStreamingResponse(self)

    @overload
    def web(
        self,
        *,
        provider: Literal["parallel"],
        query: str,
        category: Literal["company", "publication", "news", "personal site", "financial report", "people"]
        | Omit = omit,
        end_published_date: Union[str, datetime] | Omit = omit,
        excerpts: bool | Omit = omit,
        exclude_domains: SequenceNotStr[str] | Omit = omit,
        include_domains: SequenceNotStr[str] | Omit = omit,
        max_age_hours: int | Omit = omit,
        mode: Literal["fast", "advanced"] | Omit = omit,
        moderation: bool | Omit = omit,
        num_results: int | Omit = omit,
        objective: str | Omit = omit,
        start_published_date: Union[str, datetime] | Omit = omit,
        user_location: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SearchWebResponse:
        """
        Perform a web search and return structured results.

        Args:
          provider: Search provider to serve this request. Defaults to `parallel`, which uses
              `advanced` mode unless `mode` is set. If you omit it and `parallel` can't apply
              one of your filters, `exa` serves the request at `exa` pricing. The response
              `provider` field shows which one served it.

          query: The search query string

          category: Focus the search on a category of content. Only the `exa` provider supports this
              filter.

          end_published_date: Only return results published before this date-time (RFC 3339, for example
              2026-01-01T00:00:00Z). Only the `exa` provider supports this filter. Not
              supported with the company or people categories.

          excerpts: Return the passages of each page most relevant to the query. Defaults to false.

          exclude_domains: Never return results from these domains. Accepts the same entry formats as
              includeDomains. Not supported with the people category.

          include_domains: Only return results from these domains. Entries can be a hostname (example.com),
              a hostname with a path prefix (example.com/docs), or a wildcard subdomain
              (\\**.example.com). The `parallel` provider allows one list, not both, with at
              most 200 domains and no scheme, port, query string, or fragment.

          max_age_hours: Refetch a page when the cached copy is older than this many hours. Omit to use
              the provider default. A provider can return an older cached copy when a live
              fetch fails.

          mode: The search mode used by the underlying provider. Defaults to `advanced` for
              `parallel` and `fast` for `exa`. See the
              [Search docs](https://docs.browserbase.com/platform/search/overview) for the
              available modes.

          moderation: Filter unsafe content from the results. Defaults to `false`. Only the `exa`
              provider supports `true`.

          num_results: Number of results to return

          objective: The task intent and soft preferences for the search, in natural language. Adds
              context to query without replacing it.

          start_published_date: Only return results published after this date-time (RFC 3339, for example
              2026-01-01T00:00:00Z). The `parallel` provider rounds it up to a whole UTC day.
              Not supported with the company or people categories.

          user_location: Two-letter ISO 3166-1 country code of the end user. Localizes ranking without
              restricting results to sources from that country. The `parallel` provider
              supports only
              [some countries](https://docs.browserbase.com/platform/search/overview#appendix-supported-countries).

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        ...

    @overload
    def web(
        self,
        *,
        provider: Literal["exa"],
        query: str,
        category: Literal["company", "publication", "news", "personal site", "financial report", "people"]
        | Omit = omit,
        end_published_date: Union[str, datetime] | Omit = omit,
        excerpts: bool | Omit = omit,
        exclude_domains: SequenceNotStr[str] | Omit = omit,
        include_domains: SequenceNotStr[str] | Omit = omit,
        max_age_hours: int | Omit = omit,
        mode: Literal["fast", "deep-lite", "deep"] | Omit = omit,
        moderation: bool | Omit = omit,
        num_results: int | Omit = omit,
        objective: str | Omit = omit,
        start_published_date: Union[str, datetime] | Omit = omit,
        user_location: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SearchWebResponse:
        """
        Perform a web search and return structured results.

        Args:
          provider: Search provider to serve this request. Defaults to `parallel`, which uses
              `advanced` mode unless `mode` is set. If you omit it and `parallel` can't apply
              one of your filters, `exa` serves the request at `exa` pricing. The response
              `provider` field shows which one served it.

          query: The search query string

          category: Focus the search on a category of content. Only the `exa` provider supports this
              filter.

          end_published_date: Only return results published before this date-time (RFC 3339, for example
              2026-01-01T00:00:00Z). Only the `exa` provider supports this filter. Not
              supported with the company or people categories.

          excerpts: Return the passages of each page most relevant to the query. Defaults to false.

          exclude_domains: Never return results from these domains. Accepts the same entry formats as
              includeDomains. Not supported with the people category.

          include_domains: Only return results from these domains. Entries can be a hostname (example.com),
              a hostname with a path prefix (example.com/docs), or a wildcard subdomain
              (\\**.example.com). The `parallel` provider allows one list, not both, with at
              most 200 domains and no scheme, port, query string, or fragment.

          max_age_hours: Refetch a page when the cached copy is older than this many hours. Omit to use
              the provider default. A provider can return an older cached copy when a live
              fetch fails.

          mode: The search mode used by the underlying provider. Defaults to `advanced` for
              `parallel` and `fast` for `exa`. See the
              [Search docs](https://docs.browserbase.com/platform/search/overview) for the
              available modes.

          moderation: Filter unsafe content from the results. Defaults to `false`. Only the `exa`
              provider supports `true`.

          num_results: Number of results to return

          objective: The task intent and soft preferences for the search, in natural language. Adds
              context to query without replacing it.

          start_published_date: Only return results published after this date-time (RFC 3339, for example
              2026-01-01T00:00:00Z). The `parallel` provider rounds it up to a whole UTC day.
              Not supported with the company or people categories.

          user_location: Two-letter ISO 3166-1 country code of the end user. Localizes ranking without
              restricting results to sources from that country. The `parallel` provider
              supports only
              [some countries](https://docs.browserbase.com/platform/search/overview#appendix-supported-countries).

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        ...

    @overload
    def web(
        self,
        *,
        query: str,
        category: Literal["company", "publication", "news", "personal site", "financial report", "people"]
        | Omit = omit,
        end_published_date: Union[str, datetime] | Omit = omit,
        excerpts: bool | Omit = omit,
        exclude_domains: SequenceNotStr[str] | Omit = omit,
        include_domains: SequenceNotStr[str] | Omit = omit,
        max_age_hours: int | Omit = omit,
        moderation: bool | Omit = omit,
        num_results: int | Omit = omit,
        objective: str | Omit = omit,
        start_published_date: Union[str, datetime] | Omit = omit,
        user_location: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SearchWebResponse:
        """
        Perform a web search and return structured results.

        Args:
          query: The search query string

          category: Focus the search on a category of content. Only the `exa` provider supports this
              filter.

          end_published_date: Only return results published before this date-time (RFC 3339, for example
              2026-01-01T00:00:00Z). Only the `exa` provider supports this filter. Not
              supported with the company or people categories.

          excerpts: Return the passages of each page most relevant to the query. Defaults to false.

          exclude_domains: Never return results from these domains. Accepts the same entry formats as
              includeDomains. Not supported with the people category.

          include_domains: Only return results from these domains. Entries can be a hostname (example.com),
              a hostname with a path prefix (example.com/docs), or a wildcard subdomain
              (\\**.example.com). The `parallel` provider allows one list, not both, with at
              most 200 domains and no scheme, port, query string, or fragment.

          max_age_hours: Refetch a page when the cached copy is older than this many hours. Omit to use
              the provider default. A provider can return an older cached copy when a live
              fetch fails.

          moderation: Filter unsafe content from the results. Defaults to `false`. Only the `exa`
              provider supports `true`.

          num_results: Number of results to return

          objective: The task intent and soft preferences for the search, in natural language. Adds
              context to query without replacing it.

          start_published_date: Only return results published after this date-time (RFC 3339, for example
              2026-01-01T00:00:00Z). The `parallel` provider rounds it up to a whole UTC day.
              Not supported with the company or people categories.

          user_location: Two-letter ISO 3166-1 country code of the end user. Localizes ranking without
              restricting results to sources from that country. The `parallel` provider
              supports only
              [some countries](https://docs.browserbase.com/platform/search/overview#appendix-supported-countries).

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        ...

    @required_args(["provider", "query"], ["query"])
    def web(
        self,
        *,
        provider: Literal["parallel"] | Literal["exa"] | Omit = omit,
        query: str,
        category: Literal["company", "publication", "news", "personal site", "financial report", "people"]
        | Omit = omit,
        end_published_date: Union[str, datetime] | Omit = omit,
        excerpts: bool | Omit = omit,
        exclude_domains: SequenceNotStr[str] | Omit = omit,
        include_domains: SequenceNotStr[str] | Omit = omit,
        max_age_hours: int | Omit = omit,
        mode: Literal["fast", "advanced"] | Literal["fast", "deep-lite", "deep"] | Omit = omit,
        moderation: bool | Omit = omit,
        num_results: int | Omit = omit,
        objective: str | Omit = omit,
        start_published_date: Union[str, datetime] | Omit = omit,
        user_location: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SearchWebResponse:
        return self._post(
            "/v1/search",
            body=maybe_transform(
                {
                    "provider": provider,
                    "query": query,
                    "category": category,
                    "end_published_date": end_published_date,
                    "excerpts": excerpts,
                    "exclude_domains": exclude_domains,
                    "include_domains": include_domains,
                    "max_age_hours": max_age_hours,
                    "mode": mode,
                    "moderation": moderation,
                    "num_results": num_results,
                    "objective": objective,
                    "start_published_date": start_published_date,
                    "user_location": user_location,
                },
                search_web_params.SearchWebParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=SearchWebResponse,
        )


class AsyncSearchResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncSearchResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/browserbase/sdk-python#accessing-raw-response-data-eg-headers
        """
        return AsyncSearchResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncSearchResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/browserbase/sdk-python#with_streaming_response
        """
        return AsyncSearchResourceWithStreamingResponse(self)

    @overload
    async def web(
        self,
        *,
        provider: Literal["parallel"],
        query: str,
        category: Literal["company", "publication", "news", "personal site", "financial report", "people"]
        | Omit = omit,
        end_published_date: Union[str, datetime] | Omit = omit,
        excerpts: bool | Omit = omit,
        exclude_domains: SequenceNotStr[str] | Omit = omit,
        include_domains: SequenceNotStr[str] | Omit = omit,
        max_age_hours: int | Omit = omit,
        mode: Literal["fast", "advanced"] | Omit = omit,
        moderation: bool | Omit = omit,
        num_results: int | Omit = omit,
        objective: str | Omit = omit,
        start_published_date: Union[str, datetime] | Omit = omit,
        user_location: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SearchWebResponse:
        """
        Perform a web search and return structured results.

        Args:
          provider: Search provider to serve this request. Defaults to `parallel`, which uses
              `advanced` mode unless `mode` is set. If you omit it and `parallel` can't apply
              one of your filters, `exa` serves the request at `exa` pricing. The response
              `provider` field shows which one served it.

          query: The search query string

          category: Focus the search on a category of content. Only the `exa` provider supports this
              filter.

          end_published_date: Only return results published before this date-time (RFC 3339, for example
              2026-01-01T00:00:00Z). Only the `exa` provider supports this filter. Not
              supported with the company or people categories.

          excerpts: Return the passages of each page most relevant to the query. Defaults to false.

          exclude_domains: Never return results from these domains. Accepts the same entry formats as
              includeDomains. Not supported with the people category.

          include_domains: Only return results from these domains. Entries can be a hostname (example.com),
              a hostname with a path prefix (example.com/docs), or a wildcard subdomain
              (\\**.example.com). The `parallel` provider allows one list, not both, with at
              most 200 domains and no scheme, port, query string, or fragment.

          max_age_hours: Refetch a page when the cached copy is older than this many hours. Omit to use
              the provider default. A provider can return an older cached copy when a live
              fetch fails.

          mode: The search mode used by the underlying provider. Defaults to `advanced` for
              `parallel` and `fast` for `exa`. See the
              [Search docs](https://docs.browserbase.com/platform/search/overview) for the
              available modes.

          moderation: Filter unsafe content from the results. Defaults to `false`. Only the `exa`
              provider supports `true`.

          num_results: Number of results to return

          objective: The task intent and soft preferences for the search, in natural language. Adds
              context to query without replacing it.

          start_published_date: Only return results published after this date-time (RFC 3339, for example
              2026-01-01T00:00:00Z). The `parallel` provider rounds it up to a whole UTC day.
              Not supported with the company or people categories.

          user_location: Two-letter ISO 3166-1 country code of the end user. Localizes ranking without
              restricting results to sources from that country. The `parallel` provider
              supports only
              [some countries](https://docs.browserbase.com/platform/search/overview#appendix-supported-countries).

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        ...

    @overload
    async def web(
        self,
        *,
        provider: Literal["exa"],
        query: str,
        category: Literal["company", "publication", "news", "personal site", "financial report", "people"]
        | Omit = omit,
        end_published_date: Union[str, datetime] | Omit = omit,
        excerpts: bool | Omit = omit,
        exclude_domains: SequenceNotStr[str] | Omit = omit,
        include_domains: SequenceNotStr[str] | Omit = omit,
        max_age_hours: int | Omit = omit,
        mode: Literal["fast", "deep-lite", "deep"] | Omit = omit,
        moderation: bool | Omit = omit,
        num_results: int | Omit = omit,
        objective: str | Omit = omit,
        start_published_date: Union[str, datetime] | Omit = omit,
        user_location: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SearchWebResponse:
        """
        Perform a web search and return structured results.

        Args:
          provider: Search provider to serve this request. Defaults to `parallel`, which uses
              `advanced` mode unless `mode` is set. If you omit it and `parallel` can't apply
              one of your filters, `exa` serves the request at `exa` pricing. The response
              `provider` field shows which one served it.

          query: The search query string

          category: Focus the search on a category of content. Only the `exa` provider supports this
              filter.

          end_published_date: Only return results published before this date-time (RFC 3339, for example
              2026-01-01T00:00:00Z). Only the `exa` provider supports this filter. Not
              supported with the company or people categories.

          excerpts: Return the passages of each page most relevant to the query. Defaults to false.

          exclude_domains: Never return results from these domains. Accepts the same entry formats as
              includeDomains. Not supported with the people category.

          include_domains: Only return results from these domains. Entries can be a hostname (example.com),
              a hostname with a path prefix (example.com/docs), or a wildcard subdomain
              (\\**.example.com). The `parallel` provider allows one list, not both, with at
              most 200 domains and no scheme, port, query string, or fragment.

          max_age_hours: Refetch a page when the cached copy is older than this many hours. Omit to use
              the provider default. A provider can return an older cached copy when a live
              fetch fails.

          mode: The search mode used by the underlying provider. Defaults to `advanced` for
              `parallel` and `fast` for `exa`. See the
              [Search docs](https://docs.browserbase.com/platform/search/overview) for the
              available modes.

          moderation: Filter unsafe content from the results. Defaults to `false`. Only the `exa`
              provider supports `true`.

          num_results: Number of results to return

          objective: The task intent and soft preferences for the search, in natural language. Adds
              context to query without replacing it.

          start_published_date: Only return results published after this date-time (RFC 3339, for example
              2026-01-01T00:00:00Z). The `parallel` provider rounds it up to a whole UTC day.
              Not supported with the company or people categories.

          user_location: Two-letter ISO 3166-1 country code of the end user. Localizes ranking without
              restricting results to sources from that country. The `parallel` provider
              supports only
              [some countries](https://docs.browserbase.com/platform/search/overview#appendix-supported-countries).

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        ...

    @overload
    async def web(
        self,
        *,
        query: str,
        category: Literal["company", "publication", "news", "personal site", "financial report", "people"]
        | Omit = omit,
        end_published_date: Union[str, datetime] | Omit = omit,
        excerpts: bool | Omit = omit,
        exclude_domains: SequenceNotStr[str] | Omit = omit,
        include_domains: SequenceNotStr[str] | Omit = omit,
        max_age_hours: int | Omit = omit,
        moderation: bool | Omit = omit,
        num_results: int | Omit = omit,
        objective: str | Omit = omit,
        start_published_date: Union[str, datetime] | Omit = omit,
        user_location: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SearchWebResponse:
        """
        Perform a web search and return structured results.

        Args:
          query: The search query string

          category: Focus the search on a category of content. Only the `exa` provider supports this
              filter.

          end_published_date: Only return results published before this date-time (RFC 3339, for example
              2026-01-01T00:00:00Z). Only the `exa` provider supports this filter. Not
              supported with the company or people categories.

          excerpts: Return the passages of each page most relevant to the query. Defaults to false.

          exclude_domains: Never return results from these domains. Accepts the same entry formats as
              includeDomains. Not supported with the people category.

          include_domains: Only return results from these domains. Entries can be a hostname (example.com),
              a hostname with a path prefix (example.com/docs), or a wildcard subdomain
              (\\**.example.com). The `parallel` provider allows one list, not both, with at
              most 200 domains and no scheme, port, query string, or fragment.

          max_age_hours: Refetch a page when the cached copy is older than this many hours. Omit to use
              the provider default. A provider can return an older cached copy when a live
              fetch fails.

          moderation: Filter unsafe content from the results. Defaults to `false`. Only the `exa`
              provider supports `true`.

          num_results: Number of results to return

          objective: The task intent and soft preferences for the search, in natural language. Adds
              context to query without replacing it.

          start_published_date: Only return results published after this date-time (RFC 3339, for example
              2026-01-01T00:00:00Z). The `parallel` provider rounds it up to a whole UTC day.
              Not supported with the company or people categories.

          user_location: Two-letter ISO 3166-1 country code of the end user. Localizes ranking without
              restricting results to sources from that country. The `parallel` provider
              supports only
              [some countries](https://docs.browserbase.com/platform/search/overview#appendix-supported-countries).

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        ...

    @required_args(["provider", "query"], ["query"])
    async def web(
        self,
        *,
        provider: Literal["parallel"] | Literal["exa"] | Omit = omit,
        query: str,
        category: Literal["company", "publication", "news", "personal site", "financial report", "people"]
        | Omit = omit,
        end_published_date: Union[str, datetime] | Omit = omit,
        excerpts: bool | Omit = omit,
        exclude_domains: SequenceNotStr[str] | Omit = omit,
        include_domains: SequenceNotStr[str] | Omit = omit,
        max_age_hours: int | Omit = omit,
        mode: Literal["fast", "advanced"] | Literal["fast", "deep-lite", "deep"] | Omit = omit,
        moderation: bool | Omit = omit,
        num_results: int | Omit = omit,
        objective: str | Omit = omit,
        start_published_date: Union[str, datetime] | Omit = omit,
        user_location: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SearchWebResponse:
        return await self._post(
            "/v1/search",
            body=await async_maybe_transform(
                {
                    "provider": provider,
                    "query": query,
                    "category": category,
                    "end_published_date": end_published_date,
                    "excerpts": excerpts,
                    "exclude_domains": exclude_domains,
                    "include_domains": include_domains,
                    "max_age_hours": max_age_hours,
                    "mode": mode,
                    "moderation": moderation,
                    "num_results": num_results,
                    "objective": objective,
                    "start_published_date": start_published_date,
                    "user_location": user_location,
                },
                search_web_params.SearchWebParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=SearchWebResponse,
        )


class SearchResourceWithRawResponse:
    def __init__(self, search: SearchResource) -> None:
        self._search = search

        self.web = to_raw_response_wrapper(
            search.web,
        )


class AsyncSearchResourceWithRawResponse:
    def __init__(self, search: AsyncSearchResource) -> None:
        self._search = search

        self.web = async_to_raw_response_wrapper(
            search.web,
        )


class SearchResourceWithStreamingResponse:
    def __init__(self, search: SearchResource) -> None:
        self._search = search

        self.web = to_streamed_response_wrapper(
            search.web,
        )


class AsyncSearchResourceWithStreamingResponse:
    def __init__(self, search: AsyncSearchResource) -> None:
        self._search = search

        self.web = async_to_streamed_response_wrapper(
            search.web,
        )
