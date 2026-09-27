# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from .secrets import (
    SecretsResource,
    AsyncSecretsResource,
    SecretsResourceWithRawResponse,
    AsyncSecretsResourceWithRawResponse,
    SecretsResourceWithStreamingResponse,
    AsyncSecretsResourceWithStreamingResponse,
)
from ..._compat import cached_property
from ..._resource import SyncAPIResource, AsyncAPIResource

__all__ = ["FunctionsResource", "AsyncFunctionsResource"]


class FunctionsResource(SyncAPIResource):
    @cached_property
    def secrets(self) -> SecretsResource:
        return SecretsResource(self._client)

    @cached_property
    def with_raw_response(self) -> FunctionsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/browserbase/sdk-python#accessing-raw-response-data-eg-headers
        """
        return FunctionsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> FunctionsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/browserbase/sdk-python#with_streaming_response
        """
        return FunctionsResourceWithStreamingResponse(self)


class AsyncFunctionsResource(AsyncAPIResource):
    @cached_property
    def secrets(self) -> AsyncSecretsResource:
        return AsyncSecretsResource(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncFunctionsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/browserbase/sdk-python#accessing-raw-response-data-eg-headers
        """
        return AsyncFunctionsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncFunctionsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/browserbase/sdk-python#with_streaming_response
        """
        return AsyncFunctionsResourceWithStreamingResponse(self)


class FunctionsResourceWithRawResponse:
    def __init__(self, functions: FunctionsResource) -> None:
        self._functions = functions

    @cached_property
    def secrets(self) -> SecretsResourceWithRawResponse:
        return SecretsResourceWithRawResponse(self._functions.secrets)


class AsyncFunctionsResourceWithRawResponse:
    def __init__(self, functions: AsyncFunctionsResource) -> None:
        self._functions = functions

    @cached_property
    def secrets(self) -> AsyncSecretsResourceWithRawResponse:
        return AsyncSecretsResourceWithRawResponse(self._functions.secrets)


class FunctionsResourceWithStreamingResponse:
    def __init__(self, functions: FunctionsResource) -> None:
        self._functions = functions

    @cached_property
    def secrets(self) -> SecretsResourceWithStreamingResponse:
        return SecretsResourceWithStreamingResponse(self._functions.secrets)


class AsyncFunctionsResourceWithStreamingResponse:
    def __init__(self, functions: AsyncFunctionsResource) -> None:
        self._functions = functions

    @cached_property
    def secrets(self) -> AsyncSecretsResourceWithStreamingResponse:
        return AsyncSecretsResourceWithStreamingResponse(self._functions.secrets)
