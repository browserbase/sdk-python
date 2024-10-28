# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal

import httpx

from .logs import (
    LogsResource,
    AsyncLogsResource,
    LogsResourceWithRawResponse,
    AsyncLogsResourceWithRawResponse,
    LogsResourceWithStreamingResponse,
    AsyncLogsResourceWithStreamingResponse,
)
from ...types import session_list_params, session_create_params, session_update_params
from .uploads import (
    UploadsResource,
    AsyncUploadsResource,
    UploadsResourceWithRawResponse,
    AsyncUploadsResourceWithRawResponse,
    UploadsResourceWithStreamingResponse,
    AsyncUploadsResourceWithStreamingResponse,
)
from ..._types import NOT_GIVEN, Body, Query, Headers, NotGiven
from ..._utils import (
    maybe_transform,
    async_maybe_transform,
)
from ..._compat import cached_property
from .downloads import (
    DownloadsResource,
    AsyncDownloadsResource,
    DownloadsResourceWithRawResponse,
    AsyncDownloadsResourceWithRawResponse,
    DownloadsResourceWithStreamingResponse,
    AsyncDownloadsResourceWithStreamingResponse,
)
from .recording import (
    RecordingResource,
    AsyncRecordingResource,
    RecordingResourceWithRawResponse,
    AsyncRecordingResourceWithRawResponse,
    RecordingResourceWithStreamingResponse,
    AsyncRecordingResourceWithStreamingResponse,
)
from ..._resource import SyncAPIResource, AsyncAPIResource
from ..._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ..._base_client import make_request_options
from ...types.session import Session
from ...types.session_live_urls import SessionLiveURLs
from ...types.session_list_response import SessionListResponse
from ...types.session_create_response import SessionCreateResponse

__all__ = ["SessionsResource", "AsyncSessionsResource"]


class SessionsResource(SyncAPIResource):
    @cached_property
    def downloads(self) -> DownloadsResource:
        return DownloadsResource(self._client)

    @cached_property
    def logs(self) -> LogsResource:
        return LogsResource(self._client)

    @cached_property
    def recording(self) -> RecordingResource:
        return RecordingResource(self._client)

    @cached_property
    def uploads(self) -> UploadsResource:
        return UploadsResource(self._client)

    @cached_property
    def with_raw_response(self) -> SessionsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return the
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/browserbase/sdk-python#accessing-raw-response-data-eg-headers
        """
        return SessionsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> SessionsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/browserbase/sdk-python#with_streaming_response
        """
        return SessionsResourceWithStreamingResponse(self)

    def create(
        self,
        *,
        project_id: str,
        browser_settings: session_create_params.BrowserSettings | NotGiven = NOT_GIVEN,
        extension_id: str | NotGiven = NOT_GIVEN,
        keep_alive: bool | NotGiven = NOT_GIVEN,
        proxies: object | NotGiven = NOT_GIVEN,
        region: Literal["us-west-2", "us-east-1", "eu-central-1", "ap-southeast-1"] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> SessionCreateResponse:
        """Create a Session

        Args:
          project_id: The Project ID.

        Can be found in
              [Settings](https://www.browserbase.com/settings).

          extension_id: The uploaded Extension ID. See
              [Upload Extension](/reference/api/upload-an-extension).

          keep_alive: Set to true to keep the session alive even after disconnections. This is
              available on the Startup plan only.

          proxies: Proxy configuration. Can be true for default proxy, or an array of proxy
              configurations.

          region: The region where the Session should run.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/v1/sessions",
            body=maybe_transform(
                {
                    "project_id": project_id,
                    "browser_settings": browser_settings,
                    "extension_id": extension_id,
                    "keep_alive": keep_alive,
                    "proxies": proxies,
                    "region": region,
                },
                session_create_params.SessionCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=SessionCreateResponse,
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
    ) -> Session:
        """
        Session

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return self._get(
            f"/v1/sessions/{id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=Session,
        )

    def update(
        self,
        id: str,
        *,
        project_id: str,
        status: Literal["REQUEST_RELEASE"],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Session:
        """Update Session

        Args:
          project_id: The Project ID.

        Can be found in
              [Settings](https://www.browserbase.com/settings).

          status: Set to `REQUEST_RELEASE` to request that the session complete. Use before
              session's timeout to avoid additional charges.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return self._post(
            f"/v1/sessions/{id}",
            body=maybe_transform(
                {
                    "project_id": project_id,
                    "status": status,
                },
                session_update_params.SessionUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=Session,
        )

    def list(
        self,
        *,
        status: Literal["RUNNING", "ERROR", "TIMED_OUT", "COMPLETED"] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> SessionListResponse:
        """
        List Sessions

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            "/v1/sessions",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform({"status": status}, session_list_params.SessionListParams),
            ),
            cast_to=SessionListResponse,
        )

    def debug(
        self,
        id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> SessionLiveURLs:
        """
        Session Live URLs

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return self._get(
            f"/v1/sessions/{id}/debug",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=SessionLiveURLs,
        )


class AsyncSessionsResource(AsyncAPIResource):
    @cached_property
    def downloads(self) -> AsyncDownloadsResource:
        return AsyncDownloadsResource(self._client)

    @cached_property
    def logs(self) -> AsyncLogsResource:
        return AsyncLogsResource(self._client)

    @cached_property
    def recording(self) -> AsyncRecordingResource:
        return AsyncRecordingResource(self._client)

    @cached_property
    def uploads(self) -> AsyncUploadsResource:
        return AsyncUploadsResource(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncSessionsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return the
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/browserbase/sdk-python#accessing-raw-response-data-eg-headers
        """
        return AsyncSessionsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncSessionsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/browserbase/sdk-python#with_streaming_response
        """
        return AsyncSessionsResourceWithStreamingResponse(self)

    async def create(
        self,
        *,
        project_id: str,
        browser_settings: session_create_params.BrowserSettings | NotGiven = NOT_GIVEN,
        extension_id: str | NotGiven = NOT_GIVEN,
        keep_alive: bool | NotGiven = NOT_GIVEN,
        proxies: object | NotGiven = NOT_GIVEN,
        region: Literal["us-west-2", "us-east-1", "eu-central-1", "ap-southeast-1"] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> SessionCreateResponse:
        """Create a Session

        Args:
          project_id: The Project ID.

        Can be found in
              [Settings](https://www.browserbase.com/settings).

          extension_id: The uploaded Extension ID. See
              [Upload Extension](/reference/api/upload-an-extension).

          keep_alive: Set to true to keep the session alive even after disconnections. This is
              available on the Startup plan only.

          proxies: Proxy configuration. Can be true for default proxy, or an array of proxy
              configurations.

          region: The region where the Session should run.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/v1/sessions",
            body=await async_maybe_transform(
                {
                    "project_id": project_id,
                    "browser_settings": browser_settings,
                    "extension_id": extension_id,
                    "keep_alive": keep_alive,
                    "proxies": proxies,
                    "region": region,
                },
                session_create_params.SessionCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=SessionCreateResponse,
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
    ) -> Session:
        """
        Session

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return await self._get(
            f"/v1/sessions/{id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=Session,
        )

    async def update(
        self,
        id: str,
        *,
        project_id: str,
        status: Literal["REQUEST_RELEASE"],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Session:
        """Update Session

        Args:
          project_id: The Project ID.

        Can be found in
              [Settings](https://www.browserbase.com/settings).

          status: Set to `REQUEST_RELEASE` to request that the session complete. Use before
              session's timeout to avoid additional charges.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return await self._post(
            f"/v1/sessions/{id}",
            body=await async_maybe_transform(
                {
                    "project_id": project_id,
                    "status": status,
                },
                session_update_params.SessionUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=Session,
        )

    async def list(
        self,
        *,
        status: Literal["RUNNING", "ERROR", "TIMED_OUT", "COMPLETED"] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> SessionListResponse:
        """
        List Sessions

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            "/v1/sessions",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform({"status": status}, session_list_params.SessionListParams),
            ),
            cast_to=SessionListResponse,
        )

    async def debug(
        self,
        id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> SessionLiveURLs:
        """
        Session Live URLs

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return await self._get(
            f"/v1/sessions/{id}/debug",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=SessionLiveURLs,
        )


class SessionsResourceWithRawResponse:
    def __init__(self, sessions: SessionsResource) -> None:
        self._sessions = sessions

        self.create = to_raw_response_wrapper(
            sessions.create,
        )
        self.retrieve = to_raw_response_wrapper(
            sessions.retrieve,
        )
        self.update = to_raw_response_wrapper(
            sessions.update,
        )
        self.list = to_raw_response_wrapper(
            sessions.list,
        )
        self.debug = to_raw_response_wrapper(
            sessions.debug,
        )

    @cached_property
    def downloads(self) -> DownloadsResourceWithRawResponse:
        return DownloadsResourceWithRawResponse(self._sessions.downloads)

    @cached_property
    def logs(self) -> LogsResourceWithRawResponse:
        return LogsResourceWithRawResponse(self._sessions.logs)

    @cached_property
    def recording(self) -> RecordingResourceWithRawResponse:
        return RecordingResourceWithRawResponse(self._sessions.recording)

    @cached_property
    def uploads(self) -> UploadsResourceWithRawResponse:
        return UploadsResourceWithRawResponse(self._sessions.uploads)


class AsyncSessionsResourceWithRawResponse:
    def __init__(self, sessions: AsyncSessionsResource) -> None:
        self._sessions = sessions

        self.create = async_to_raw_response_wrapper(
            sessions.create,
        )
        self.retrieve = async_to_raw_response_wrapper(
            sessions.retrieve,
        )
        self.update = async_to_raw_response_wrapper(
            sessions.update,
        )
        self.list = async_to_raw_response_wrapper(
            sessions.list,
        )
        self.debug = async_to_raw_response_wrapper(
            sessions.debug,
        )

    @cached_property
    def downloads(self) -> AsyncDownloadsResourceWithRawResponse:
        return AsyncDownloadsResourceWithRawResponse(self._sessions.downloads)

    @cached_property
    def logs(self) -> AsyncLogsResourceWithRawResponse:
        return AsyncLogsResourceWithRawResponse(self._sessions.logs)

    @cached_property
    def recording(self) -> AsyncRecordingResourceWithRawResponse:
        return AsyncRecordingResourceWithRawResponse(self._sessions.recording)

    @cached_property
    def uploads(self) -> AsyncUploadsResourceWithRawResponse:
        return AsyncUploadsResourceWithRawResponse(self._sessions.uploads)


class SessionsResourceWithStreamingResponse:
    def __init__(self, sessions: SessionsResource) -> None:
        self._sessions = sessions

        self.create = to_streamed_response_wrapper(
            sessions.create,
        )
        self.retrieve = to_streamed_response_wrapper(
            sessions.retrieve,
        )
        self.update = to_streamed_response_wrapper(
            sessions.update,
        )
        self.list = to_streamed_response_wrapper(
            sessions.list,
        )
        self.debug = to_streamed_response_wrapper(
            sessions.debug,
        )

    @cached_property
    def downloads(self) -> DownloadsResourceWithStreamingResponse:
        return DownloadsResourceWithStreamingResponse(self._sessions.downloads)

    @cached_property
    def logs(self) -> LogsResourceWithStreamingResponse:
        return LogsResourceWithStreamingResponse(self._sessions.logs)

    @cached_property
    def recording(self) -> RecordingResourceWithStreamingResponse:
        return RecordingResourceWithStreamingResponse(self._sessions.recording)

    @cached_property
    def uploads(self) -> UploadsResourceWithStreamingResponse:
        return UploadsResourceWithStreamingResponse(self._sessions.uploads)


class AsyncSessionsResourceWithStreamingResponse:
    def __init__(self, sessions: AsyncSessionsResource) -> None:
        self._sessions = sessions

        self.create = async_to_streamed_response_wrapper(
            sessions.create,
        )
        self.retrieve = async_to_streamed_response_wrapper(
            sessions.retrieve,
        )
        self.update = async_to_streamed_response_wrapper(
            sessions.update,
        )
        self.list = async_to_streamed_response_wrapper(
            sessions.list,
        )
        self.debug = async_to_streamed_response_wrapper(
            sessions.debug,
        )

    @cached_property
    def downloads(self) -> AsyncDownloadsResourceWithStreamingResponse:
        return AsyncDownloadsResourceWithStreamingResponse(self._sessions.downloads)

    @cached_property
    def logs(self) -> AsyncLogsResourceWithStreamingResponse:
        return AsyncLogsResourceWithStreamingResponse(self._sessions.logs)

    @cached_property
    def recording(self) -> AsyncRecordingResourceWithStreamingResponse:
        return AsyncRecordingResourceWithStreamingResponse(self._sessions.recording)

    @cached_property
    def uploads(self) -> AsyncUploadsResourceWithStreamingResponse:
        return AsyncUploadsResourceWithStreamingResponse(self._sessions.uploads)
