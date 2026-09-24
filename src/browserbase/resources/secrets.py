# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union
from datetime import datetime

import httpx

from ..types import secret_list_params, secret_create_params, secret_update_params
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
from .._base_client import make_request_options
from ..types.secret import Secret
from ..types.secrets_keypair import SecretsKeypair
from ..types.secret_list_response import SecretListResponse

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

    def create(
        self,
        *,
        keypair_id: str,
        sealed_secret_value: str,
        secret_key: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Secret:
        """
        Create Secret

        Args:
          keypair_id: The `id` returned by GET /v1/secrets/keypair, identifying the keypair whose
              public key encrypted the value. Recorded with the secret so decryption stays
              correct across keypair rotation.

          sealed_secret_value: The secret value encrypted with HPKE. In order to seal the secret value before
              sending, get the project's public key from GET /v1/secrets/keypair. Decode the
              publicKey using base64 into the raw 32-byte public key. Then, use HPKE Base mode
              (RFC 9180) with the following algorithm suite: DHKEM(X25519, HKDF-SHA256),
              HKDF-SHA256, and AES-256-GCM. Set both info and additional authenticated data
              (AAD) to an empty byte string. Then, create a new sender context using the
              public key and these settings, and encrypt the secret value as one message. Put
              the 32-byte encapsulated key before the ciphertext and keep the authentication
              tag at the end of the ciphertext. Encode the combined bytes with standard
              base64. Send the result as sealedSecretValue: base64(enc || ciphertext)

          secret_key: The name to store the secret value under.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/v1/secrets",
            body=maybe_transform(
                {
                    "keypair_id": keypair_id,
                    "sealed_secret_value": sealed_secret_value,
                    "secret_key": secret_key,
                },
                secret_create_params.SecretCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=Secret,
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
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Secret:
        """
        Get Secret

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return self._get(
            path_template("/v1/secrets/{id}", id=id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=Secret,
        )

    def update(
        self,
        id: str,
        *,
        keypair_id: str,
        sealed_secret_value: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Secret:
        """Replace a secret's value.

        The name cannot be changed; to rename, create a new
        secret and delete the old one.

        Args:
          keypair_id: The `id` returned by GET /v1/secrets/keypair, identifying the keypair whose
              public key encrypted the value. Recorded with the secret so decryption stays
              correct across keypair rotation.

          sealed_secret_value: The new secret value encrypted with HPKE. In order to seal the secret value
              before sending, get the project's public key from GET /v1/secrets/keypair.
              Decode the publicKey using base64 into the raw 32-byte public key. Then, use
              HPKE Base mode (RFC 9180) with the following algorithm suite: DHKEM(X25519,
              HKDF-SHA256), HKDF-SHA256, and AES-256-GCM. Set both info and additional
              authenticated data (AAD) to an empty byte string. Then, create a new sender
              context using the public key and these settings, and encrypt the secret value as
              one message. Put the 32-byte encapsulated key before the ciphertext and keep the
              authentication tag at the end of the ciphertext. Encode the combined bytes with
              standard base64. Send the result as sealedSecretValue: base64(enc || ciphertext)

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return self._patch(
            path_template("/v1/secrets/{id}", id=id),
            body=maybe_transform(
                {
                    "keypair_id": keypair_id,
                    "sealed_secret_value": sealed_secret_value,
                },
                secret_update_params.SecretUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=Secret,
        )

    def list(
        self,
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
        """List project secrets.

        Supports filtering by creation time.

        Args:
          cursor: Pagination cursor. Pass the nextCursor from the previous response to fetch the
              next page. Omit to start from the first page.

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
        return self._get(
            "/v1/secrets",
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

    def delete(
        self,
        id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> None:
        """
        Delete Secret

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return self._delete(
            path_template("/v1/secrets/{id}", id=id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )

    def get_public_key(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SecretsKeypair:
        """Get Secrets Keypair"""
        return self._get(
            "/v1/secrets/keypair",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=SecretsKeypair,
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

    async def create(
        self,
        *,
        keypair_id: str,
        sealed_secret_value: str,
        secret_key: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Secret:
        """
        Create Secret

        Args:
          keypair_id: The `id` returned by GET /v1/secrets/keypair, identifying the keypair whose
              public key encrypted the value. Recorded with the secret so decryption stays
              correct across keypair rotation.

          sealed_secret_value: The secret value encrypted with HPKE. In order to seal the secret value before
              sending, get the project's public key from GET /v1/secrets/keypair. Decode the
              publicKey using base64 into the raw 32-byte public key. Then, use HPKE Base mode
              (RFC 9180) with the following algorithm suite: DHKEM(X25519, HKDF-SHA256),
              HKDF-SHA256, and AES-256-GCM. Set both info and additional authenticated data
              (AAD) to an empty byte string. Then, create a new sender context using the
              public key and these settings, and encrypt the secret value as one message. Put
              the 32-byte encapsulated key before the ciphertext and keep the authentication
              tag at the end of the ciphertext. Encode the combined bytes with standard
              base64. Send the result as sealedSecretValue: base64(enc || ciphertext)

          secret_key: The name to store the secret value under.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/v1/secrets",
            body=await async_maybe_transform(
                {
                    "keypair_id": keypair_id,
                    "sealed_secret_value": sealed_secret_value,
                    "secret_key": secret_key,
                },
                secret_create_params.SecretCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=Secret,
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
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Secret:
        """
        Get Secret

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return await self._get(
            path_template("/v1/secrets/{id}", id=id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=Secret,
        )

    async def update(
        self,
        id: str,
        *,
        keypair_id: str,
        sealed_secret_value: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Secret:
        """Replace a secret's value.

        The name cannot be changed; to rename, create a new
        secret and delete the old one.

        Args:
          keypair_id: The `id` returned by GET /v1/secrets/keypair, identifying the keypair whose
              public key encrypted the value. Recorded with the secret so decryption stays
              correct across keypair rotation.

          sealed_secret_value: The new secret value encrypted with HPKE. In order to seal the secret value
              before sending, get the project's public key from GET /v1/secrets/keypair.
              Decode the publicKey using base64 into the raw 32-byte public key. Then, use
              HPKE Base mode (RFC 9180) with the following algorithm suite: DHKEM(X25519,
              HKDF-SHA256), HKDF-SHA256, and AES-256-GCM. Set both info and additional
              authenticated data (AAD) to an empty byte string. Then, create a new sender
              context using the public key and these settings, and encrypt the secret value as
              one message. Put the 32-byte encapsulated key before the ciphertext and keep the
              authentication tag at the end of the ciphertext. Encode the combined bytes with
              standard base64. Send the result as sealedSecretValue: base64(enc || ciphertext)

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return await self._patch(
            path_template("/v1/secrets/{id}", id=id),
            body=await async_maybe_transform(
                {
                    "keypair_id": keypair_id,
                    "sealed_secret_value": sealed_secret_value,
                },
                secret_update_params.SecretUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=Secret,
        )

    async def list(
        self,
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
        """List project secrets.

        Supports filtering by creation time.

        Args:
          cursor: Pagination cursor. Pass the nextCursor from the previous response to fetch the
              next page. Omit to start from the first page.

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
        return await self._get(
            "/v1/secrets",
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

    async def delete(
        self,
        id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> None:
        """
        Delete Secret

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return await self._delete(
            path_template("/v1/secrets/{id}", id=id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )

    async def get_public_key(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SecretsKeypair:
        """Get Secrets Keypair"""
        return await self._get(
            "/v1/secrets/keypair",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=SecretsKeypair,
        )


class SecretsResourceWithRawResponse:
    def __init__(self, secrets: SecretsResource) -> None:
        self._secrets = secrets

        self.create = to_raw_response_wrapper(
            secrets.create,
        )
        self.retrieve = to_raw_response_wrapper(
            secrets.retrieve,
        )
        self.update = to_raw_response_wrapper(
            secrets.update,
        )
        self.list = to_raw_response_wrapper(
            secrets.list,
        )
        self.delete = to_raw_response_wrapper(
            secrets.delete,
        )
        self.get_public_key = to_raw_response_wrapper(
            secrets.get_public_key,
        )


class AsyncSecretsResourceWithRawResponse:
    def __init__(self, secrets: AsyncSecretsResource) -> None:
        self._secrets = secrets

        self.create = async_to_raw_response_wrapper(
            secrets.create,
        )
        self.retrieve = async_to_raw_response_wrapper(
            secrets.retrieve,
        )
        self.update = async_to_raw_response_wrapper(
            secrets.update,
        )
        self.list = async_to_raw_response_wrapper(
            secrets.list,
        )
        self.delete = async_to_raw_response_wrapper(
            secrets.delete,
        )
        self.get_public_key = async_to_raw_response_wrapper(
            secrets.get_public_key,
        )


class SecretsResourceWithStreamingResponse:
    def __init__(self, secrets: SecretsResource) -> None:
        self._secrets = secrets

        self.create = to_streamed_response_wrapper(
            secrets.create,
        )
        self.retrieve = to_streamed_response_wrapper(
            secrets.retrieve,
        )
        self.update = to_streamed_response_wrapper(
            secrets.update,
        )
        self.list = to_streamed_response_wrapper(
            secrets.list,
        )
        self.delete = to_streamed_response_wrapper(
            secrets.delete,
        )
        self.get_public_key = to_streamed_response_wrapper(
            secrets.get_public_key,
        )


class AsyncSecretsResourceWithStreamingResponse:
    def __init__(self, secrets: AsyncSecretsResource) -> None:
        self._secrets = secrets

        self.create = async_to_streamed_response_wrapper(
            secrets.create,
        )
        self.retrieve = async_to_streamed_response_wrapper(
            secrets.retrieve,
        )
        self.update = async_to_streamed_response_wrapper(
            secrets.update,
        )
        self.list = async_to_streamed_response_wrapper(
            secrets.list,
        )
        self.delete = async_to_streamed_response_wrapper(
            secrets.delete,
        )
        self.get_public_key = async_to_streamed_response_wrapper(
            secrets.get_public_key,
        )
