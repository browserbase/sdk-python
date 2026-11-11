# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import httpx

from ..types import label_list_params, label_create_params, label_update_params
from .._types import Body, Omit, Query, Headers, NoneType, NotGiven, omit, not_given
from .._utils import path_template, maybe_transform, async_maybe_transform
from .._compat import cached_property
from .._resource import SyncAPIResource, AsyncAPIResource
from .._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ..types.label import Label
from .._base_client import make_request_options
from ..types.label_list_response import LabelListResponse

__all__ = ["LabelsResource", "AsyncLabelsResource"]


class LabelsResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> LabelsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/browserbase/sdk-python#accessing-raw-response-data-eg-headers
        """
        return LabelsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> LabelsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/browserbase/sdk-python#with_streaming_response
        """
        return LabelsResourceWithStreamingResponse(self)

    def create(
        self,
        *,
        name: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Label:
        """Create a project-owned label.

        Args:
          name: Label name.

        Browserbase trims surrounding Unicode whitespace and preserves
              display capitalization. The trimmed name must contain 1–128 Unicode characters
              and no NUL characters. Names are unique ignoring case within the project.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/v1/labels",
            body=maybe_transform({"name": name}, label_create_params.LabelCreateParams),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=Label,
        )

    def update(
        self,
        label_id: str,
        *,
        name: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Label:
        """
        Rename a label, preserving its ID, creation time, and session assignments.

        Args:
          name: Label name. Browserbase trims surrounding Unicode whitespace and preserves
              display capitalization. The trimmed name must contain 1–128 Unicode characters
              and no NUL characters. Names are unique ignoring case within the project.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not label_id:
            raise ValueError(f"Expected a non-empty value for `label_id` but received {label_id!r}")
        return self._patch(
            path_template("/v1/labels/{label_id}", label_id=label_id),
            body=maybe_transform({"name": name}, label_update_params.LabelUpdateParams),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=Label,
        )

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
    ) -> LabelListResponse:
        """List the project's labels, newest first.

        Page by passing the previous response's
        `nextCursor` as `cursor`; a null `nextCursor` means there are no further pages.

        Args:
          cursor: Pagination cursor. Pass the nextCursor from the previous response to fetch the
              next page. Omit to start from the first page.

          limit: Maximum number of results to return.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            "/v1/labels",
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
                    label_list_params.LabelListParams,
                ),
            ),
            cast_to=LabelListResponse,
        )

    def delete(
        self,
        label_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> None:
        """Delete a label and its session assignments, preserving the sessions.

        Missing and
        other-project labels are successful no-ops.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not label_id:
            raise ValueError(f"Expected a non-empty value for `label_id` but received {label_id!r}")
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return self._delete(
            path_template("/v1/labels/{label_id}", label_id=label_id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )


class AsyncLabelsResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncLabelsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/browserbase/sdk-python#accessing-raw-response-data-eg-headers
        """
        return AsyncLabelsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncLabelsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/browserbase/sdk-python#with_streaming_response
        """
        return AsyncLabelsResourceWithStreamingResponse(self)

    async def create(
        self,
        *,
        name: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Label:
        """Create a project-owned label.

        Args:
          name: Label name.

        Browserbase trims surrounding Unicode whitespace and preserves
              display capitalization. The trimmed name must contain 1–128 Unicode characters
              and no NUL characters. Names are unique ignoring case within the project.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/v1/labels",
            body=await async_maybe_transform({"name": name}, label_create_params.LabelCreateParams),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=Label,
        )

    async def update(
        self,
        label_id: str,
        *,
        name: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Label:
        """
        Rename a label, preserving its ID, creation time, and session assignments.

        Args:
          name: Label name. Browserbase trims surrounding Unicode whitespace and preserves
              display capitalization. The trimmed name must contain 1–128 Unicode characters
              and no NUL characters. Names are unique ignoring case within the project.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not label_id:
            raise ValueError(f"Expected a non-empty value for `label_id` but received {label_id!r}")
        return await self._patch(
            path_template("/v1/labels/{label_id}", label_id=label_id),
            body=await async_maybe_transform({"name": name}, label_update_params.LabelUpdateParams),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=Label,
        )

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
    ) -> LabelListResponse:
        """List the project's labels, newest first.

        Page by passing the previous response's
        `nextCursor` as `cursor`; a null `nextCursor` means there are no further pages.

        Args:
          cursor: Pagination cursor. Pass the nextCursor from the previous response to fetch the
              next page. Omit to start from the first page.

          limit: Maximum number of results to return.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            "/v1/labels",
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
                    label_list_params.LabelListParams,
                ),
            ),
            cast_to=LabelListResponse,
        )

    async def delete(
        self,
        label_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> None:
        """Delete a label and its session assignments, preserving the sessions.

        Missing and
        other-project labels are successful no-ops.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not label_id:
            raise ValueError(f"Expected a non-empty value for `label_id` but received {label_id!r}")
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return await self._delete(
            path_template("/v1/labels/{label_id}", label_id=label_id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )


class LabelsResourceWithRawResponse:
    def __init__(self, labels: LabelsResource) -> None:
        self._labels = labels

        self.create = to_raw_response_wrapper(
            labels.create,
        )
        self.update = to_raw_response_wrapper(
            labels.update,
        )
        self.list = to_raw_response_wrapper(
            labels.list,
        )
        self.delete = to_raw_response_wrapper(
            labels.delete,
        )


class AsyncLabelsResourceWithRawResponse:
    def __init__(self, labels: AsyncLabelsResource) -> None:
        self._labels = labels

        self.create = async_to_raw_response_wrapper(
            labels.create,
        )
        self.update = async_to_raw_response_wrapper(
            labels.update,
        )
        self.list = async_to_raw_response_wrapper(
            labels.list,
        )
        self.delete = async_to_raw_response_wrapper(
            labels.delete,
        )


class LabelsResourceWithStreamingResponse:
    def __init__(self, labels: LabelsResource) -> None:
        self._labels = labels

        self.create = to_streamed_response_wrapper(
            labels.create,
        )
        self.update = to_streamed_response_wrapper(
            labels.update,
        )
        self.list = to_streamed_response_wrapper(
            labels.list,
        )
        self.delete = to_streamed_response_wrapper(
            labels.delete,
        )


class AsyncLabelsResourceWithStreamingResponse:
    def __init__(self, labels: AsyncLabelsResource) -> None:
        self._labels = labels

        self.create = async_to_streamed_response_wrapper(
            labels.create,
        )
        self.update = async_to_streamed_response_wrapper(
            labels.update,
        )
        self.list = async_to_streamed_response_wrapper(
            labels.list,
        )
        self.delete = async_to_streamed_response_wrapper(
            labels.delete,
        )
