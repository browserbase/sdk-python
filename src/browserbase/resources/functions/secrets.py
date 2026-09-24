# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union
from datetime import datetime

import httpx

from ..._types import Body, Omit, Query, Headers, NoneType, NotGiven, omit, not_given
from ..._utils import path_template, maybe_transform, async_maybe_transform
from ..._compat import cached_property
from ..._resource import SyncAPIResource, AsyncAPIResource
from ..._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ..._base_client import make_request_options
from ...types.functions import secret_list_params, secret_attach_params
from ...types.functions.secret_list_response import SecretListResponse

__all__ = ["SecretsResource", "AsyncSecretsResource"]


class SecretsResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> SecretsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/browserbase/sdk-python#accessing-raw-response-data-eg-headers
        """
        return SecretsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> SecretsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/browserbase/sdk-python#with_streaming_response
        """
        return SecretsResourceWithStreamingResponse(self)

    def list(
        self,
        id: str,
        *,
        cursor: str | Omit = omit,
        end_at: Union[str, datetime] | Omit = omit,
        limit: int | Omit = omit,
        start_at: Union[str, datetime] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SecretListResponse:
        """List secrets attached to a function.

        Supports filtering by secret creation time.
        Returns metadata only.

        Args:
          cursor: Pagination cursor. Pass the nextCursor from the previous response to fetch the
              next page. Keep the same filters across pages. Omit to start from the first
              page.

          end_at: Only return secrets created on or before this timestamp (inclusive). RFC 3339,
              e.g. 2026-01-20T00:00:00Z.

          limit: Maximum number of results to return.

          start_at: Only return secrets created on or after this timestamp (inclusive). RFC 3339,
              e.g. 2026-01-19T00:00:00Z.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return self._get(
            path_template("/v1/functions/{id}/secrets", id=id),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "cursor": cursor,
                        "end_at": end_at,
                        "limit": limit,
                        "start_at": start_at,
                    },
                    secret_list_params.SecretListParams,
                ),
            ),
            cast_to=SecretListResponse,
        )

    def attach(
        self,
        id: str,
        *,
        secret_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> None:
        """
        Attach a secret to a Function, taking effect on the Function's next invocation.
        Note: Attaching a secret that is already attached succeeds to support
        idempotency.

        Args:
          secret_id: The id of the project secret to attach (the `id` returned by POST /v1/secrets).
              Idempotent: re-attaching an already-attached secret succeeds.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return self._post(
            path_template("/v1/functions/{id}/secrets", id=id),
            body=maybe_transform({"secret_id": secret_id}, secret_attach_params.SecretAttachParams),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )

    def detach(
        self,
        secret_id: str,
        *,
        id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> None:
        """Detach a secret from a Function, taking effect on the Function's next
        invocation.

        Note: Detaching a secret that is not attached succeeds to support
        idempotency.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        if not secret_id:
            raise ValueError(f"Expected a non-empty value for `secret_id` but received {secret_id!r}")
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return self._delete(
            path_template("/v1/functions/{id}/secrets/{secret_id}", id=id, secret_id=secret_id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )


class AsyncSecretsResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncSecretsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/browserbase/sdk-python#accessing-raw-response-data-eg-headers
        """
        return AsyncSecretsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncSecretsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/browserbase/sdk-python#with_streaming_response
        """
        return AsyncSecretsResourceWithStreamingResponse(self)

    async def list(
        self,
        id: str,
        *,
        cursor: str | Omit = omit,
        end_at: Union[str, datetime] | Omit = omit,
        limit: int | Omit = omit,
        start_at: Union[str, datetime] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SecretListResponse:
        """List secrets attached to a function.

        Supports filtering by secret creation time.
        Returns metadata only.

        Args:
          cursor: Pagination cursor. Pass the nextCursor from the previous response to fetch the
              next page. Keep the same filters across pages. Omit to start from the first
              page.

          end_at: Only return secrets created on or before this timestamp (inclusive). RFC 3339,
              e.g. 2026-01-20T00:00:00Z.

          limit: Maximum number of results to return.

          start_at: Only return secrets created on or after this timestamp (inclusive). RFC 3339,
              e.g. 2026-01-19T00:00:00Z.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return await self._get(
            path_template("/v1/functions/{id}/secrets", id=id),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "cursor": cursor,
                        "end_at": end_at,
                        "limit": limit,
                        "start_at": start_at,
                    },
                    secret_list_params.SecretListParams,
                ),
            ),
            cast_to=SecretListResponse,
        )

    async def attach(
        self,
        id: str,
        *,
        secret_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> None:
        """
        Attach a secret to a Function, taking effect on the Function's next invocation.
        Note: Attaching a secret that is already attached succeeds to support
        idempotency.

        Args:
          secret_id: The id of the project secret to attach (the `id` returned by POST /v1/secrets).
              Idempotent: re-attaching an already-attached secret succeeds.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return await self._post(
            path_template("/v1/functions/{id}/secrets", id=id),
            body=await async_maybe_transform({"secret_id": secret_id}, secret_attach_params.SecretAttachParams),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )

    async def detach(
        self,
        secret_id: str,
        *,
        id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> None:
        """Detach a secret from a Function, taking effect on the Function's next
        invocation.

        Note: Detaching a secret that is not attached succeeds to support
        idempotency.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        if not secret_id:
            raise ValueError(f"Expected a non-empty value for `secret_id` but received {secret_id!r}")
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return await self._delete(
            path_template("/v1/functions/{id}/secrets/{secret_id}", id=id, secret_id=secret_id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )


class SecretsResourceWithRawResponse:
    def __init__(self, secrets: SecretsResource) -> None:
        self._secrets = secrets

        self.list = to_raw_response_wrapper(
            secrets.list,
        )
        self.attach = to_raw_response_wrapper(
            secrets.attach,
        )
        self.detach = to_raw_response_wrapper(
            secrets.detach,
        )


class AsyncSecretsResourceWithRawResponse:
    def __init__(self, secrets: AsyncSecretsResource) -> None:
        self._secrets = secrets

        self.list = async_to_raw_response_wrapper(
            secrets.list,
        )
        self.attach = async_to_raw_response_wrapper(
            secrets.attach,
        )
        self.detach = async_to_raw_response_wrapper(
            secrets.detach,
        )


class SecretsResourceWithStreamingResponse:
    def __init__(self, secrets: SecretsResource) -> None:
        self._secrets = secrets

        self.list = to_streamed_response_wrapper(
            secrets.list,
        )
        self.attach = to_streamed_response_wrapper(
            secrets.attach,
        )
        self.detach = to_streamed_response_wrapper(
            secrets.detach,
        )


class AsyncSecretsResourceWithStreamingResponse:
    def __init__(self, secrets: AsyncSecretsResource) -> None:
        self._secrets = secrets

        self.list = async_to_streamed_response_wrapper(
            secrets.list,
        )
        self.attach = async_to_streamed_response_wrapper(
            secrets.attach,
        )
        self.detach = async_to_streamed_response_wrapper(
            secrets.detach,
        )
