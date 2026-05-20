# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import httpx

from ..._types import Body, Query, Headers, NotGiven, not_given
from ..._utils import path_template
from ..._compat import cached_property
from ..._resource import SyncAPIResource, AsyncAPIResource
from ..._response import (
    BinaryAPIResponse,
    AsyncBinaryAPIResponse,
    StreamedBinaryAPIResponse,
    AsyncStreamedBinaryAPIResponse,
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    to_custom_raw_response_wrapper,
    async_to_streamed_response_wrapper,
    to_custom_streamed_response_wrapper,
    async_to_custom_raw_response_wrapper,
    async_to_custom_streamed_response_wrapper,
)
from ..._base_client import make_request_options
from ...types.sessions.replay_retrieve_response import ReplayRetrieveResponse

__all__ = ["ReplaysResource", "AsyncReplaysResource"]


class ReplaysResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> ReplaysResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/browserbase/sdk-python#accessing-raw-response-data-eg-headers
        """
        return ReplaysResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> ReplaysResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/browserbase/sdk-python#with_streaming_response
        """
        return ReplaysResourceWithStreamingResponse(self)

    def retrieve(
        self,
        id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ReplayRetrieveResponse:
        """
        Returns page metadata for a session replay, including timing information and the
        URL of each page's HLS playlist.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return self._get(
            path_template("/v1/sessions/{id}/replays", id=id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ReplayRetrieveResponse,
        )

    def retrieve_page(
        self,
        page_id: str,
        *,
        id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> BinaryAPIResponse:
        """
        Returns an HLS VOD media playlist (.m3u8) for a specific page of a session
        replay.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        if not page_id:
            raise ValueError(f"Expected a non-empty value for `page_id` but received {page_id!r}")
        extra_headers = {"Accept": "application/vnd.apple.mpegurl", **(extra_headers or {})}
        return self._get(
            path_template("/v1/sessions/{id}/replays/{page_id}", id=id, page_id=page_id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=BinaryAPIResponse,
        )


class AsyncReplaysResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncReplaysResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/browserbase/sdk-python#accessing-raw-response-data-eg-headers
        """
        return AsyncReplaysResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncReplaysResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/browserbase/sdk-python#with_streaming_response
        """
        return AsyncReplaysResourceWithStreamingResponse(self)

    async def retrieve(
        self,
        id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ReplayRetrieveResponse:
        """
        Returns page metadata for a session replay, including timing information and the
        URL of each page's HLS playlist.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return await self._get(
            path_template("/v1/sessions/{id}/replays", id=id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ReplayRetrieveResponse,
        )

    async def retrieve_page(
        self,
        page_id: str,
        *,
        id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AsyncBinaryAPIResponse:
        """
        Returns an HLS VOD media playlist (.m3u8) for a specific page of a session
        replay.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        if not page_id:
            raise ValueError(f"Expected a non-empty value for `page_id` but received {page_id!r}")
        extra_headers = {"Accept": "application/vnd.apple.mpegurl", **(extra_headers or {})}
        return await self._get(
            path_template("/v1/sessions/{id}/replays/{page_id}", id=id, page_id=page_id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=AsyncBinaryAPIResponse,
        )


class ReplaysResourceWithRawResponse:
    def __init__(self, replays: ReplaysResource) -> None:
        self._replays = replays

        self.retrieve = to_raw_response_wrapper(
            replays.retrieve,
        )
        self.retrieve_page = to_custom_raw_response_wrapper(
            replays.retrieve_page,
            BinaryAPIResponse,
        )


class AsyncReplaysResourceWithRawResponse:
    def __init__(self, replays: AsyncReplaysResource) -> None:
        self._replays = replays

        self.retrieve = async_to_raw_response_wrapper(
            replays.retrieve,
        )
        self.retrieve_page = async_to_custom_raw_response_wrapper(
            replays.retrieve_page,
            AsyncBinaryAPIResponse,
        )


class ReplaysResourceWithStreamingResponse:
    def __init__(self, replays: ReplaysResource) -> None:
        self._replays = replays

        self.retrieve = to_streamed_response_wrapper(
            replays.retrieve,
        )
        self.retrieve_page = to_custom_streamed_response_wrapper(
            replays.retrieve_page,
            StreamedBinaryAPIResponse,
        )


class AsyncReplaysResourceWithStreamingResponse:
    def __init__(self, replays: AsyncReplaysResource) -> None:
        self._replays = replays

        self.retrieve = async_to_streamed_response_wrapper(
            replays.retrieve,
        )
        self.retrieve_page = async_to_custom_streamed_response_wrapper(
            replays.retrieve_page,
            AsyncStreamedBinaryAPIResponse,
        )
