# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import httpx

from ..types import context_create_params
from .._types import NOT_GIVEN, Body, Query, Headers, NotGiven
from .._utils import (
    maybe_transform,
    async_maybe_transform,
)
from .._compat import cached_property
from .._resource import SyncAPIResource, AsyncAPIResource
from .._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from .._base_client import make_request_options
from ..types.context import Context
from ..types.context_create_response import ContextCreateResponse
from ..types.context_update_response import ContextUpdateResponse

__all__ = ["ContextsResource", "AsyncContextsResource"]


class ContextsResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> ContextsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/browserbase/sdk-python#accessing-raw-response-data-eg-headers
        """
        return ContextsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> ContextsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/browserbase/sdk-python#with_streaming_response
        """
        return ContextsResourceWithStreamingResponse(self)

    def create(
        self,
        *,
        project_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> ContextCreateResponse:
        """Create a Context

        Args:
          project_id: The Project ID.

        Can be found in
              [Settings](https://www.browserbase.com/settings).

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/v1/contexts",
            body=maybe_transform({"project_id": project_id}, context_create_params.ContextCreateParams),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ContextCreateResponse,
        )

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
    ) -> Context:
        """
        Context

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return self._get(
            f"/v1/contexts/{id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=Context,
        )

    def update(
        self,
        id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> ContextUpdateResponse:
        """
        Update Context

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return self._put(
            f"/v1/contexts/{id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ContextUpdateResponse,
        )


class AsyncContextsResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncContextsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/browserbase/sdk-python#accessing-raw-response-data-eg-headers
        """
        return AsyncContextsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncContextsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/browserbase/sdk-python#with_streaming_response
        """
        return AsyncContextsResourceWithStreamingResponse(self)

    async def create(
        self,
        *,
        project_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> ContextCreateResponse:
        """Create a Context

        Args:
          project_id: The Project ID.

        Can be found in
              [Settings](https://www.browserbase.com/settings).

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/v1/contexts",
            body=await async_maybe_transform({"project_id": project_id}, context_create_params.ContextCreateParams),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ContextCreateResponse,
        )

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
    ) -> Context:
        """
        Context

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return await self._get(
            f"/v1/contexts/{id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=Context,
        )

    async def update(
        self,
        id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> ContextUpdateResponse:
        """
        Update Context

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return await self._put(
            f"/v1/contexts/{id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ContextUpdateResponse,
        )


class ContextsResourceWithRawResponse:
    def __init__(self, contexts: ContextsResource) -> None:
        self._contexts = contexts

        self.create = to_raw_response_wrapper(
            contexts.create,
        )
        self.retrieve = to_raw_response_wrapper(
            contexts.retrieve,
        )
        self.update = to_raw_response_wrapper(
            contexts.update,
        )


class AsyncContextsResourceWithRawResponse:
    def __init__(self, contexts: AsyncContextsResource) -> None:
        self._contexts = contexts

        self.create = async_to_raw_response_wrapper(
            contexts.create,
        )
        self.retrieve = async_to_raw_response_wrapper(
            contexts.retrieve,
        )
        self.update = async_to_raw_response_wrapper(
            contexts.update,
        )


class ContextsResourceWithStreamingResponse:
    def __init__(self, contexts: ContextsResource) -> None:
        self._contexts = contexts

        self.create = to_streamed_response_wrapper(
            contexts.create,
        )
        self.retrieve = to_streamed_response_wrapper(
            contexts.retrieve,
        )
        self.update = to_streamed_response_wrapper(
            contexts.update,
        )


class AsyncContextsResourceWithStreamingResponse:
    def __init__(self, contexts: AsyncContextsResource) -> None:
        self._contexts = contexts

        self.create = async_to_streamed_response_wrapper(
            contexts.create,
        )
        self.retrieve = async_to_streamed_response_wrapper(
            contexts.retrieve,
        )
        self.update = async_to_streamed_response_wrapper(
            contexts.update,
        )
