# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import httpx

from ..types import fetch_api_create_params
from .._types import Body, Omit, Query, Headers, NotGiven, omit, not_given
from .._utils import maybe_transform, async_maybe_transform
from .._compat import cached_property
from .._resource import SyncAPIResource, AsyncAPIResource
from .._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from .._base_client import make_request_options
from ..types.fetch_api_create_response import FetchAPICreateResponse

__all__ = ["FetchAPIResource", "AsyncFetchAPIResource"]


class FetchAPIResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> FetchAPIResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/browserbase/sdk-python#accessing-raw-response-data-eg-headers
        """
        return FetchAPIResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> FetchAPIResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/browserbase/sdk-python#with_streaming_response
        """
        return FetchAPIResourceWithStreamingResponse(self)

    def create(
        self,
        *,
        url: str,
        allow_insecure_ssl: bool | Omit = omit,
        allow_redirects: bool | Omit = omit,
        proxies: bool | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> FetchAPICreateResponse:
        """
        Fetch a page and return its content, headers, and metadata.

        Args:
          url: The URL to fetch

          allow_insecure_ssl: Whether to bypass TLS certificate verification

          allow_redirects: Whether to follow HTTP redirects

          proxies: Whether to enable proxy support for the request

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/v1/fetch",
            body=maybe_transform(
                {
                    "url": url,
                    "allow_insecure_ssl": allow_insecure_ssl,
                    "allow_redirects": allow_redirects,
                    "proxies": proxies,
                },
                fetch_api_create_params.FetchAPICreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=FetchAPICreateResponse,
        )


class AsyncFetchAPIResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncFetchAPIResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/browserbase/sdk-python#accessing-raw-response-data-eg-headers
        """
        return AsyncFetchAPIResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncFetchAPIResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/browserbase/sdk-python#with_streaming_response
        """
        return AsyncFetchAPIResourceWithStreamingResponse(self)

    async def create(
        self,
        *,
        url: str,
        allow_insecure_ssl: bool | Omit = omit,
        allow_redirects: bool | Omit = omit,
        proxies: bool | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> FetchAPICreateResponse:
        """
        Fetch a page and return its content, headers, and metadata.

        Args:
          url: The URL to fetch

          allow_insecure_ssl: Whether to bypass TLS certificate verification

          allow_redirects: Whether to follow HTTP redirects

          proxies: Whether to enable proxy support for the request

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/v1/fetch",
            body=await async_maybe_transform(
                {
                    "url": url,
                    "allow_insecure_ssl": allow_insecure_ssl,
                    "allow_redirects": allow_redirects,
                    "proxies": proxies,
                },
                fetch_api_create_params.FetchAPICreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=FetchAPICreateResponse,
        )


class FetchAPIResourceWithRawResponse:
    def __init__(self, fetch_api: FetchAPIResource) -> None:
        self._fetch_api = fetch_api

        self.create = to_raw_response_wrapper(
            fetch_api.create,
        )


class AsyncFetchAPIResourceWithRawResponse:
    def __init__(self, fetch_api: AsyncFetchAPIResource) -> None:
        self._fetch_api = fetch_api

        self.create = async_to_raw_response_wrapper(
            fetch_api.create,
        )


class FetchAPIResourceWithStreamingResponse:
    def __init__(self, fetch_api: FetchAPIResource) -> None:
        self._fetch_api = fetch_api

        self.create = to_streamed_response_wrapper(
            fetch_api.create,
        )


class AsyncFetchAPIResourceWithStreamingResponse:
    def __init__(self, fetch_api: AsyncFetchAPIResource) -> None:
        self._fetch_api = fetch_api

        self.create = async_to_streamed_response_wrapper(
            fetch_api.create,
        )
