# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import TYPE_CHECKING, Any, Mapping
from typing_extensions import Self, override

import httpx

from . import _exceptions
from ._qs import Querystring
from ._types import (
    Omit,
    Timeout,
    NotGiven,
    Transport,
    ProxiesTypes,
    RequestOptions,
    not_given,
)
from ._utils import is_given, get_async_library
from ._compat import cached_property
from ._version import __version__
from ._streaming import Stream as Stream, AsyncStream as AsyncStream
from ._exceptions import APIStatusError, BrowserbaseError
from ._base_client import (
    DEFAULT_MAX_RETRIES,
    SyncAPIClient,
    AsyncAPIClient,
)

if TYPE_CHECKING:
    from .resources import search, contexts, projects, sessions, fetch_api, extensions
    from .resources.search import SearchResource, AsyncSearchResource
    from .resources.contexts import ContextsResource, AsyncContextsResource
    from .resources.projects import ProjectsResource, AsyncProjectsResource
    from .resources.fetch_api import FetchAPIResource, AsyncFetchAPIResource
    from .resources.extensions import ExtensionsResource, AsyncExtensionsResource
    from .resources.sessions.sessions import SessionsResource, AsyncSessionsResource

__all__ = [
    "Timeout",
    "Transport",
    "ProxiesTypes",
    "RequestOptions",
    "Browserbase",
    "AsyncBrowserbase",
    "Client",
    "AsyncClient",
]


class Browserbase(SyncAPIClient):
    # client options
    api_key: str

    def __init__(
        self,
        *,
        api_key: str | None = None,
        base_url: str | httpx.URL | None = None,
        timeout: float | Timeout | None | NotGiven = not_given,
        max_retries: int = DEFAULT_MAX_RETRIES,
        default_headers: Mapping[str, str] | None = None,
        default_query: Mapping[str, object] | None = None,
        # Configure a custom httpx client.
        # We provide a `DefaultHttpxClient` class that you can pass to retain the default values we use for `limits`, `timeout` & `follow_redirects`.
        # See the [httpx documentation](https://www.python-httpx.org/api/#client) for more details.
        http_client: httpx.Client | None = None,
        # Enable or disable schema validation for data returned by the API.
        # When enabled an error APIResponseValidationError is raised
        # if the API responds with invalid data for the expected schema.
        #
        # This parameter may be removed or changed in the future.
        # If you rely on this feature, please open a GitHub issue
        # outlining your use-case to help us decide if it should be
        # part of our public interface in the future.
        _strict_response_validation: bool = False,
    ) -> None:
        """Construct a new synchronous Browserbase client instance.

        This automatically infers the `api_key` argument from the `BROWSERBASE_API_KEY` environment variable if it is not provided.
        """
        if api_key is None:
            api_key = os.environ.get("BROWSERBASE_API_KEY")
        if api_key is None:
            raise BrowserbaseError(
                "The api_key client option must be set either by passing api_key to the client or by setting the BROWSERBASE_API_KEY environment variable"
            )
        self.api_key = api_key

        if base_url is None:
            base_url = os.environ.get("BROWSERBASE_BASE_URL")
        if base_url is None:
            base_url = f"https://api.browserbase.com"

        super().__init__(
            version=__version__,
            base_url=base_url,
            max_retries=max_retries,
            timeout=timeout,
            http_client=http_client,
            custom_headers=default_headers,
            custom_query=default_query,
            _strict_response_validation=_strict_response_validation,
        )

    @cached_property
    def contexts(self) -> ContextsResource:
        from .resources.contexts import ContextsResource

        return ContextsResource(self)

    @cached_property
    def extensions(self) -> ExtensionsResource:
        from .resources.extensions import ExtensionsResource

        return ExtensionsResource(self)

    @cached_property
    def fetch_api(self) -> FetchAPIResource:
        from .resources.fetch_api import FetchAPIResource

        return FetchAPIResource(self)

    @cached_property
    def projects(self) -> ProjectsResource:
        from .resources.projects import ProjectsResource

        return ProjectsResource(self)

    @cached_property
    def search(self) -> SearchResource:
        from .resources.search import SearchResource

        return SearchResource(self)

    @cached_property
    def sessions(self) -> SessionsResource:
        from .resources.sessions import SessionsResource

        return SessionsResource(self)

    @cached_property
    def with_raw_response(self) -> BrowserbaseWithRawResponse:
        return BrowserbaseWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> BrowserbaseWithStreamedResponse:
        return BrowserbaseWithStreamedResponse(self)

    @property
    @override
    def qs(self) -> Querystring:
        return Querystring(array_format="comma")

    @property
    @override
    def auth_headers(self) -> dict[str, str]:
        api_key = self.api_key
        return {"X-BB-API-Key": api_key}

    @property
    @override
    def default_headers(self) -> dict[str, str | Omit]:
        return {
            **super().default_headers,
            "X-Stainless-Async": "false",
            **self._custom_headers,
        }

    def copy(
        self,
        *,
        api_key: str | None = None,
        base_url: str | httpx.URL | None = None,
        timeout: float | Timeout | None | NotGiven = not_given,
        http_client: httpx.Client | None = None,
        max_retries: int | NotGiven = not_given,
        default_headers: Mapping[str, str] | None = None,
        set_default_headers: Mapping[str, str] | None = None,
        default_query: Mapping[str, object] | None = None,
        set_default_query: Mapping[str, object] | None = None,
        _extra_kwargs: Mapping[str, Any] = {},
    ) -> Self:
        """
        Create a new client instance re-using the same options given to the current client with optional overriding.
        """
        if default_headers is not None and set_default_headers is not None:
            raise ValueError("The `default_headers` and `set_default_headers` arguments are mutually exclusive")

        if default_query is not None and set_default_query is not None:
            raise ValueError("The `default_query` and `set_default_query` arguments are mutually exclusive")

        headers = self._custom_headers
        if default_headers is not None:
            headers = {**headers, **default_headers}
        elif set_default_headers is not None:
            headers = set_default_headers

        params = self._custom_query
        if default_query is not None:
            params = {**params, **default_query}
        elif set_default_query is not None:
            params = set_default_query

        http_client = http_client or self._client
        return self.__class__(
            api_key=api_key or self.api_key,
            base_url=base_url or self.base_url,
            timeout=self.timeout if isinstance(timeout, NotGiven) else timeout,
            http_client=http_client,
            max_retries=max_retries if is_given(max_retries) else self.max_retries,
            default_headers=headers,
            default_query=params,
            **_extra_kwargs,
        )

    # Alias for `copy` for nicer inline usage, e.g.
    # client.with_options(timeout=10).foo.create(...)
    with_options = copy

    @override
    def _make_status_error(
        self,
        err_msg: str,
        *,
        body: object,
        response: httpx.Response,
    ) -> APIStatusError:
        if response.status_code == 400:
            return _exceptions.BadRequestError(err_msg, response=response, body=body)

        if response.status_code == 401:
            return _exceptions.AuthenticationError(err_msg, response=response, body=body)

        if response.status_code == 403:
            return _exceptions.PermissionDeniedError(err_msg, response=response, body=body)

        if response.status_code == 404:
            return _exceptions.NotFoundError(err_msg, response=response, body=body)

        if response.status_code == 409:
            return _exceptions.ConflictError(err_msg, response=response, body=body)

        if response.status_code == 422:
            return _exceptions.UnprocessableEntityError(err_msg, response=response, body=body)

        if response.status_code == 429:
            return _exceptions.RateLimitError(err_msg, response=response, body=body)

        if response.status_code >= 500:
            return _exceptions.InternalServerError(err_msg, response=response, body=body)
        return APIStatusError(err_msg, response=response, body=body)


class AsyncBrowserbase(AsyncAPIClient):
    # client options
    api_key: str

    def __init__(
        self,
        *,
        api_key: str | None = None,
        base_url: str | httpx.URL | None = None,
        timeout: float | Timeout | None | NotGiven = not_given,
        max_retries: int = DEFAULT_MAX_RETRIES,
        default_headers: Mapping[str, str] | None = None,
        default_query: Mapping[str, object] | None = None,
        # Configure a custom httpx client.
        # We provide a `DefaultAsyncHttpxClient` class that you can pass to retain the default values we use for `limits`, `timeout` & `follow_redirects`.
        # See the [httpx documentation](https://www.python-httpx.org/api/#asyncclient) for more details.
        http_client: httpx.AsyncClient | None = None,
        # Enable or disable schema validation for data returned by the API.
        # When enabled an error APIResponseValidationError is raised
        # if the API responds with invalid data for the expected schema.
        #
        # This parameter may be removed or changed in the future.
        # If you rely on this feature, please open a GitHub issue
        # outlining your use-case to help us decide if it should be
        # part of our public interface in the future.
        _strict_response_validation: bool = False,
    ) -> None:
        """Construct a new async AsyncBrowserbase client instance.

        This automatically infers the `api_key` argument from the `BROWSERBASE_API_KEY` environment variable if it is not provided.
        """
        if api_key is None:
            api_key = os.environ.get("BROWSERBASE_API_KEY")
        if api_key is None:
            raise BrowserbaseError(
                "The api_key client option must be set either by passing api_key to the client or by setting the BROWSERBASE_API_KEY environment variable"
            )
        self.api_key = api_key

        if base_url is None:
            base_url = os.environ.get("BROWSERBASE_BASE_URL")
        if base_url is None:
            base_url = f"https://api.browserbase.com"

        super().__init__(
            version=__version__,
            base_url=base_url,
            max_retries=max_retries,
            timeout=timeout,
            http_client=http_client,
            custom_headers=default_headers,
            custom_query=default_query,
            _strict_response_validation=_strict_response_validation,
        )

    @cached_property
    def contexts(self) -> AsyncContextsResource:
        from .resources.contexts import AsyncContextsResource

        return AsyncContextsResource(self)

    @cached_property
    def extensions(self) -> AsyncExtensionsResource:
        from .resources.extensions import AsyncExtensionsResource

        return AsyncExtensionsResource(self)

    @cached_property
    def fetch_api(self) -> AsyncFetchAPIResource:
        from .resources.fetch_api import AsyncFetchAPIResource

        return AsyncFetchAPIResource(self)

    @cached_property
    def projects(self) -> AsyncProjectsResource:
        from .resources.projects import AsyncProjectsResource

        return AsyncProjectsResource(self)

    @cached_property
    def search(self) -> AsyncSearchResource:
        from .resources.search import AsyncSearchResource

        return AsyncSearchResource(self)

    @cached_property
    def sessions(self) -> AsyncSessionsResource:
        from .resources.sessions import AsyncSessionsResource

        return AsyncSessionsResource(self)

    @cached_property
    def with_raw_response(self) -> AsyncBrowserbaseWithRawResponse:
        return AsyncBrowserbaseWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncBrowserbaseWithStreamedResponse:
        return AsyncBrowserbaseWithStreamedResponse(self)

    @property
    @override
    def qs(self) -> Querystring:
        return Querystring(array_format="comma")

    @property
    @override
    def auth_headers(self) -> dict[str, str]:
        api_key = self.api_key
        return {"X-BB-API-Key": api_key}

    @property
    @override
    def default_headers(self) -> dict[str, str | Omit]:
        return {
            **super().default_headers,
            "X-Stainless-Async": f"async:{get_async_library()}",
            **self._custom_headers,
        }

    def copy(
        self,
        *,
        api_key: str | None = None,
        base_url: str | httpx.URL | None = None,
        timeout: float | Timeout | None | NotGiven = not_given,
        http_client: httpx.AsyncClient | None = None,
        max_retries: int | NotGiven = not_given,
        default_headers: Mapping[str, str] | None = None,
        set_default_headers: Mapping[str, str] | None = None,
        default_query: Mapping[str, object] | None = None,
        set_default_query: Mapping[str, object] | None = None,
        _extra_kwargs: Mapping[str, Any] = {},
    ) -> Self:
        """
        Create a new client instance re-using the same options given to the current client with optional overriding.
        """
        if default_headers is not None and set_default_headers is not None:
            raise ValueError("The `default_headers` and `set_default_headers` arguments are mutually exclusive")

        if default_query is not None and set_default_query is not None:
            raise ValueError("The `default_query` and `set_default_query` arguments are mutually exclusive")

        headers = self._custom_headers
        if default_headers is not None:
            headers = {**headers, **default_headers}
        elif set_default_headers is not None:
            headers = set_default_headers

        params = self._custom_query
        if default_query is not None:
            params = {**params, **default_query}
        elif set_default_query is not None:
            params = set_default_query

        http_client = http_client or self._client
        return self.__class__(
            api_key=api_key or self.api_key,
            base_url=base_url or self.base_url,
            timeout=self.timeout if isinstance(timeout, NotGiven) else timeout,
            http_client=http_client,
            max_retries=max_retries if is_given(max_retries) else self.max_retries,
            default_headers=headers,
            default_query=params,
            **_extra_kwargs,
        )

    # Alias for `copy` for nicer inline usage, e.g.
    # client.with_options(timeout=10).foo.create(...)
    with_options = copy

    @override
    def _make_status_error(
        self,
        err_msg: str,
        *,
        body: object,
        response: httpx.Response,
    ) -> APIStatusError:
        if response.status_code == 400:
            return _exceptions.BadRequestError(err_msg, response=response, body=body)

        if response.status_code == 401:
            return _exceptions.AuthenticationError(err_msg, response=response, body=body)

        if response.status_code == 403:
            return _exceptions.PermissionDeniedError(err_msg, response=response, body=body)

        if response.status_code == 404:
            return _exceptions.NotFoundError(err_msg, response=response, body=body)

        if response.status_code == 409:
            return _exceptions.ConflictError(err_msg, response=response, body=body)

        if response.status_code == 422:
            return _exceptions.UnprocessableEntityError(err_msg, response=response, body=body)

        if response.status_code == 429:
            return _exceptions.RateLimitError(err_msg, response=response, body=body)

        if response.status_code >= 500:
            return _exceptions.InternalServerError(err_msg, response=response, body=body)
        return APIStatusError(err_msg, response=response, body=body)


class BrowserbaseWithRawResponse:
    _client: Browserbase

    def __init__(self, client: Browserbase) -> None:
        self._client = client

    @cached_property
    def contexts(self) -> contexts.ContextsResourceWithRawResponse:
        from .resources.contexts import ContextsResourceWithRawResponse

        return ContextsResourceWithRawResponse(self._client.contexts)

    @cached_property
    def extensions(self) -> extensions.ExtensionsResourceWithRawResponse:
        from .resources.extensions import ExtensionsResourceWithRawResponse

        return ExtensionsResourceWithRawResponse(self._client.extensions)

    @cached_property
    def fetch_api(self) -> fetch_api.FetchAPIResourceWithRawResponse:
        from .resources.fetch_api import FetchAPIResourceWithRawResponse

        return FetchAPIResourceWithRawResponse(self._client.fetch_api)

    @cached_property
    def projects(self) -> projects.ProjectsResourceWithRawResponse:
        from .resources.projects import ProjectsResourceWithRawResponse

        return ProjectsResourceWithRawResponse(self._client.projects)

    @cached_property
    def search(self) -> search.SearchResourceWithRawResponse:
        from .resources.search import SearchResourceWithRawResponse

        return SearchResourceWithRawResponse(self._client.search)

    @cached_property
    def sessions(self) -> sessions.SessionsResourceWithRawResponse:
        from .resources.sessions import SessionsResourceWithRawResponse

        return SessionsResourceWithRawResponse(self._client.sessions)


class AsyncBrowserbaseWithRawResponse:
    _client: AsyncBrowserbase

    def __init__(self, client: AsyncBrowserbase) -> None:
        self._client = client

    @cached_property
    def contexts(self) -> contexts.AsyncContextsResourceWithRawResponse:
        from .resources.contexts import AsyncContextsResourceWithRawResponse

        return AsyncContextsResourceWithRawResponse(self._client.contexts)

    @cached_property
    def extensions(self) -> extensions.AsyncExtensionsResourceWithRawResponse:
        from .resources.extensions import AsyncExtensionsResourceWithRawResponse

        return AsyncExtensionsResourceWithRawResponse(self._client.extensions)

    @cached_property
    def fetch_api(self) -> fetch_api.AsyncFetchAPIResourceWithRawResponse:
        from .resources.fetch_api import AsyncFetchAPIResourceWithRawResponse

        return AsyncFetchAPIResourceWithRawResponse(self._client.fetch_api)

    @cached_property
    def projects(self) -> projects.AsyncProjectsResourceWithRawResponse:
        from .resources.projects import AsyncProjectsResourceWithRawResponse

        return AsyncProjectsResourceWithRawResponse(self._client.projects)

    @cached_property
    def search(self) -> search.AsyncSearchResourceWithRawResponse:
        from .resources.search import AsyncSearchResourceWithRawResponse

        return AsyncSearchResourceWithRawResponse(self._client.search)

    @cached_property
    def sessions(self) -> sessions.AsyncSessionsResourceWithRawResponse:
        from .resources.sessions import AsyncSessionsResourceWithRawResponse

        return AsyncSessionsResourceWithRawResponse(self._client.sessions)


class BrowserbaseWithStreamedResponse:
    _client: Browserbase

    def __init__(self, client: Browserbase) -> None:
        self._client = client

    @cached_property
    def contexts(self) -> contexts.ContextsResourceWithStreamingResponse:
        from .resources.contexts import ContextsResourceWithStreamingResponse

        return ContextsResourceWithStreamingResponse(self._client.contexts)

    @cached_property
    def extensions(self) -> extensions.ExtensionsResourceWithStreamingResponse:
        from .resources.extensions import ExtensionsResourceWithStreamingResponse

        return ExtensionsResourceWithStreamingResponse(self._client.extensions)

    @cached_property
    def fetch_api(self) -> fetch_api.FetchAPIResourceWithStreamingResponse:
        from .resources.fetch_api import FetchAPIResourceWithStreamingResponse

        return FetchAPIResourceWithStreamingResponse(self._client.fetch_api)

    @cached_property
    def projects(self) -> projects.ProjectsResourceWithStreamingResponse:
        from .resources.projects import ProjectsResourceWithStreamingResponse

        return ProjectsResourceWithStreamingResponse(self._client.projects)

    @cached_property
    def search(self) -> search.SearchResourceWithStreamingResponse:
        from .resources.search import SearchResourceWithStreamingResponse

        return SearchResourceWithStreamingResponse(self._client.search)

    @cached_property
    def sessions(self) -> sessions.SessionsResourceWithStreamingResponse:
        from .resources.sessions import SessionsResourceWithStreamingResponse

        return SessionsResourceWithStreamingResponse(self._client.sessions)


class AsyncBrowserbaseWithStreamedResponse:
    _client: AsyncBrowserbase

    def __init__(self, client: AsyncBrowserbase) -> None:
        self._client = client

    @cached_property
    def contexts(self) -> contexts.AsyncContextsResourceWithStreamingResponse:
        from .resources.contexts import AsyncContextsResourceWithStreamingResponse

        return AsyncContextsResourceWithStreamingResponse(self._client.contexts)

    @cached_property
    def extensions(self) -> extensions.AsyncExtensionsResourceWithStreamingResponse:
        from .resources.extensions import AsyncExtensionsResourceWithStreamingResponse

        return AsyncExtensionsResourceWithStreamingResponse(self._client.extensions)

    @cached_property
    def fetch_api(self) -> fetch_api.AsyncFetchAPIResourceWithStreamingResponse:
        from .resources.fetch_api import AsyncFetchAPIResourceWithStreamingResponse

        return AsyncFetchAPIResourceWithStreamingResponse(self._client.fetch_api)

    @cached_property
    def projects(self) -> projects.AsyncProjectsResourceWithStreamingResponse:
        from .resources.projects import AsyncProjectsResourceWithStreamingResponse

        return AsyncProjectsResourceWithStreamingResponse(self._client.projects)

    @cached_property
    def search(self) -> search.AsyncSearchResourceWithStreamingResponse:
        from .resources.search import AsyncSearchResourceWithStreamingResponse

        return AsyncSearchResourceWithStreamingResponse(self._client.search)

    @cached_property
    def sessions(self) -> sessions.AsyncSessionsResourceWithStreamingResponse:
        from .resources.sessions import AsyncSessionsResourceWithStreamingResponse

        return AsyncSessionsResourceWithStreamingResponse(self._client.sessions)


Client = Browserbase

AsyncClient = AsyncBrowserbase
