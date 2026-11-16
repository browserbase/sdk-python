# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import httpx

from ..types import static_proxy_list_params
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
from ..types.static_proxy_list_response import StaticProxyListResponse

__all__ = ["StaticProxiesResource", "AsyncStaticProxiesResource"]


class StaticProxiesResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> StaticProxiesResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/browserbase/sdk-python#accessing-raw-response-data-eg-headers
        """
        return StaticProxiesResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> StaticProxiesResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/browserbase/sdk-python#with_streaming_response
        """
        return StaticProxiesResourceWithStreamingResponse(self)

    def list(
        self,
        *,
        cursor: str | Omit = omit,
        limit: int | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> StaticProxyListResponse:
        """
        List enabled static proxy IDs assigned to your organization, newest first.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            "/v1/static-proxies",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "cursor": cursor,
                        "limit": limit,
                    },
                    static_proxy_list_params.StaticProxyListParams,
                ),
            ),
            cast_to=StaticProxyListResponse,
        )


class AsyncStaticProxiesResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncStaticProxiesResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/browserbase/sdk-python#accessing-raw-response-data-eg-headers
        """
        return AsyncStaticProxiesResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncStaticProxiesResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/browserbase/sdk-python#with_streaming_response
        """
        return AsyncStaticProxiesResourceWithStreamingResponse(self)

    async def list(
        self,
        *,
        cursor: str | Omit = omit,
        limit: int | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> StaticProxyListResponse:
        """
        List enabled static proxy IDs assigned to your organization, newest first.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            "/v1/static-proxies",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "cursor": cursor,
                        "limit": limit,
                    },
                    static_proxy_list_params.StaticProxyListParams,
                ),
            ),
            cast_to=StaticProxyListResponse,
        )


class StaticProxiesResourceWithRawResponse:
    def __init__(self, static_proxies: StaticProxiesResource) -> None:
        self._static_proxies = static_proxies

        self.list = to_raw_response_wrapper(
            static_proxies.list,
        )


class AsyncStaticProxiesResourceWithRawResponse:
    def __init__(self, static_proxies: AsyncStaticProxiesResource) -> None:
        self._static_proxies = static_proxies

        self.list = async_to_raw_response_wrapper(
            static_proxies.list,
        )


class StaticProxiesResourceWithStreamingResponse:
    def __init__(self, static_proxies: StaticProxiesResource) -> None:
        self._static_proxies = static_proxies

        self.list = to_streamed_response_wrapper(
            static_proxies.list,
        )


class AsyncStaticProxiesResourceWithStreamingResponse:
    def __init__(self, static_proxies: AsyncStaticProxiesResource) -> None:
        self._static_proxies = static_proxies

        self.list = async_to_streamed_response_wrapper(
            static_proxies.list,
        )
