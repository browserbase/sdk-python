# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import httpx

from ..._types import NOT_GIVEN, Body, Query, Headers, NotGiven
from ..._compat import cached_property
from ..._resource import SyncAPIResource, AsyncAPIResource
from ..._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ..._base_client import make_request_options
from ...types.sessions.recording_retrieve_response import RecordingRetrieveResponse

__all__ = ["RecordingResource", "AsyncRecordingResource"]


class RecordingResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> RecordingResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return the
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/browserbase/sdk-python#accessing-raw-response-data-eg-headers
        """
        return RecordingResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> RecordingResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/browserbase/sdk-python#with_streaming_response
        """
        return RecordingResourceWithStreamingResponse(self)

    def retrieve(
        self,
        id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> RecordingRetrieveResponse:
        """
        Session Recording

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return self._get(
            f"/v1/sessions/{id}/recording",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=RecordingRetrieveResponse,
        )


class AsyncRecordingResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncRecordingResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return the
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/browserbase/sdk-python#accessing-raw-response-data-eg-headers
        """
        return AsyncRecordingResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncRecordingResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/browserbase/sdk-python#with_streaming_response
        """
        return AsyncRecordingResourceWithStreamingResponse(self)

    async def retrieve(
        self,
        id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> RecordingRetrieveResponse:
        """
        Session Recording

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return await self._get(
            f"/v1/sessions/{id}/recording",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=RecordingRetrieveResponse,
        )


class RecordingResourceWithRawResponse:
    def __init__(self, recording: RecordingResource) -> None:
        self._recording = recording

        self.retrieve = to_raw_response_wrapper(
            recording.retrieve,
        )


class AsyncRecordingResourceWithRawResponse:
    def __init__(self, recording: AsyncRecordingResource) -> None:
        self._recording = recording

        self.retrieve = async_to_raw_response_wrapper(
            recording.retrieve,
        )


class RecordingResourceWithStreamingResponse:
    def __init__(self, recording: RecordingResource) -> None:
        self._recording = recording

        self.retrieve = to_streamed_response_wrapper(
            recording.retrieve,
        )


class AsyncRecordingResourceWithStreamingResponse:
    def __init__(self, recording: AsyncRecordingResource) -> None:
        self._recording = recording

        self.retrieve = async_to_streamed_response_wrapper(
            recording.retrieve,
        )
