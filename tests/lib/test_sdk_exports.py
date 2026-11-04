"""
Runtime export verification for the Python SDK.

This file tests that the generated Browserbase Python SDK exports all
expected classes, types, and functions. It serves as a tripwire for
breaking changes: if Stainless regenerates the SDK and an export is
renamed or removed, these tests will fail before the change reaches
customers.

The companion file `sdk_types.py` verifies type-level contracts
via pyright; this file covers runtime imports.

Sections:
  1. Client classes
  2. Client infrastructure (request options, streaming, responses, httpx)
  3. Error classes
  4. Resource classes (sync, async, session sub-resources)
  5. Utilities (functions, constants, version, type sentinels)
"""


# =============================================================================
# Client classes
# =============================================================================


def test_client_classes() -> None:
    """Browserbase, AsyncBrowserbase, and their aliases are importable."""
    from browserbase import Client, AsyncClient, Browserbase, AsyncBrowserbase

    assert callable(AsyncBrowserbase)
    assert callable(AsyncClient)
    assert callable(Browserbase)
    assert callable(Client)
    assert Browserbase.__name__ == "Browserbase"


# =============================================================================
# Client infrastructure
# =============================================================================


def test_request_config() -> None:
    """RequestOptions and Timeout are importable."""
    from browserbase import Timeout, RequestOptions

    assert RequestOptions is not None
    assert Timeout is not None


def test_streaming() -> None:
    """AsyncStream and Stream are importable."""
    from browserbase import Stream, AsyncStream

    assert callable(AsyncStream)
    assert callable(Stream)


def test_response_wrappers() -> None:
    """APIResponse, AsyncAPIResponse, and BaseModel are importable."""
    from browserbase import BaseModel, APIResponse, AsyncAPIResponse

    assert callable(APIResponse)
    assert callable(AsyncAPIResponse)
    assert callable(BaseModel)


def test_httpx_clients() -> None:
    """DefaultAsyncHttpxClient and DefaultHttpxClient are importable."""
    from browserbase import DefaultHttpxClient, DefaultAsyncHttpxClient

    assert callable(DefaultAsyncHttpxClient)
    assert callable(DefaultHttpxClient)


# =============================================================================
# Error classes
# =============================================================================


def test_error_classes() -> None:
    """All error classes are importable."""
    from browserbase import (
        APIError,
        ConflictError,
        NotFoundError,
        APIStatusError,
        RateLimitError,
        APITimeoutError,
        BadRequestError,
        BrowserbaseError,
        APIConnectionError,
        AuthenticationError,
        InternalServerError,
        PermissionDeniedError,
        UnprocessableEntityError,
        APIResponseValidationError,
    )

    for err in [
        APIConnectionError,
        APIError,
        APIResponseValidationError,
        APIStatusError,
        APITimeoutError,
        AuthenticationError,
        BadRequestError,
        BrowserbaseError,
        ConflictError,
        InternalServerError,
        NotFoundError,
        PermissionDeniedError,
        RateLimitError,
        UnprocessableEntityError,
    ]:
        assert callable(err)


# =============================================================================
# Resource classes
# =============================================================================


def test_sync_resources() -> None:
    """Sync resource classes are importable from browserbase.resources."""
    from browserbase.resources import (
        ContextsResource,
        FetchAPIResource,
        ProjectsResource,
        SessionsResource,
        ExtensionsResource,
    )

    for resource in [ContextsResource, ExtensionsResource, FetchAPIResource, ProjectsResource, SessionsResource]:
        assert callable(resource)


def test_async_resources() -> None:
    """Async resource classes are importable from browserbase.resources."""
    from browserbase.resources import (
        AsyncContextsResource,
        AsyncFetchAPIResource,
        AsyncProjectsResource,
        AsyncSessionsResource,
        AsyncExtensionsResource,
    )

    for resource in [
        AsyncContextsResource,
        AsyncExtensionsResource,
        AsyncFetchAPIResource,
        AsyncProjectsResource,
        AsyncSessionsResource,
    ]:
        assert callable(resource)


def test_session_subresources() -> None:
    """Session sub-resource classes (sync + async) are importable."""
    from browserbase.resources.sessions import (
        LogsResource,
        UploadsResource,
        AsyncLogsResource,
        DownloadsResource,
        RecordingResource,
        AsyncUploadsResource,
        AsyncDownloadsResource,
        AsyncRecordingResource,
    )

    for resource in [
        AsyncDownloadsResource,
        AsyncLogsResource,
        AsyncRecordingResource,
        AsyncUploadsResource,
        DownloadsResource,
        LogsResource,
        RecordingResource,
        UploadsResource,
    ]:
        assert callable(resource)


# =============================================================================
# Utilities
# =============================================================================


def test_utility_functions() -> None:
    """Utility functions are importable."""
    from browserbase import file_from_path

    assert callable(file_from_path)


def test_constants() -> None:
    """SDK constants are importable."""
    from browserbase import DEFAULT_TIMEOUT, DEFAULT_MAX_RETRIES, DEFAULT_CONNECTION_LIMITS

    assert DEFAULT_CONNECTION_LIMITS is not None
    assert DEFAULT_TIMEOUT is not None
    assert isinstance(DEFAULT_MAX_RETRIES, int)


def test_version_metadata() -> None:
    """Version metadata is importable."""
    from browserbase import __title__, __version__

    assert isinstance(__title__, str)
    assert isinstance(__version__, str)


def test_type_utilities() -> None:
    """Type utility sentinels and aliases are importable."""
    # The redundant aliases mark names that are only checked for importability.
    from browserbase import (
        NOT_GIVEN,
        Omit as Omit,
        NoneType as NoneType,
        NotGiven,
        Transport as Transport,
        ProxiesTypes as ProxiesTypes,
    )

    assert NOT_GIVEN is not None
    assert NotGiven is not None
