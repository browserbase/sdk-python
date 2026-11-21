"""
Type-level contract verification for the Python SDK.

This file never executes as normal Python code. It exists solely to be
type-checked by pyright (in `./scripts/lint`), acting as a tripwire for
breaking changes in the generated Browserbase SDK. If Stainless regenerates
the SDK and a type is renamed, removed, or its shape changes, pyright will
report errors and CI will fail before the change reaches customers. Its
name keeps pytest from collecting it.

The companion file `test_sdk_exports.py` verifies runtime exports; this
file covers the type-level surface:
  1. Imports of client classes and infrastructure, error classes, type
     utilities, resource classes, and response/param types
  2. Shape checks, one function per type
"""

from typing import Dict, Union, Optional
from datetime import datetime

from browserbase import (
    NOT_GIVEN,
    DEFAULT_TIMEOUT,
    DEFAULT_MAX_RETRIES,
    DEFAULT_CONNECTION_LIMITS,
    Omit,
    Client,
    Stream,
    Timeout,
    APIError,
    NoneType,
    NotGiven,
    BaseModel,
    Transport,
    APIResponse,
    AsyncClient,
    AsyncStream,
    Browserbase,
    ProxiesTypes,
    ConflictError,
    NotFoundError,
    APIStatusError,
    RateLimitError,
    RequestOptions,
    APITimeoutError,
    BadRequestError,
    AsyncAPIResponse,
    AsyncBrowserbase,
    BrowserbaseError,
    APIConnectionError,
    DefaultHttpxClient,
    AuthenticationError,
    InternalServerError,
    PermissionDeniedError,
    DefaultAsyncHttpxClient,
    UnprocessableEntityError,
    APIResponseValidationError,
    file_from_path,
)
from browserbase.types import (
    Context,
    Project,
    Session,
    Extension,
    ProjectUsage,
    SessionLiveURLs,
    SessionListParams,
    ContextCreateParams,
    ProjectListResponse,
    SessionCreateParams,
    SessionListResponse,
    SessionUpdateParams,
    FetchAPICreateParams,
    ContextCreateResponse,
    ContextUpdateResponse,
    ExtensionCreateParams,
    SessionCreateResponse,
    FetchAPICreateResponse,
    SessionRetrieveResponse,
    session_create_params,
)
from browserbase.resources import (
    ContextsResource,
    FetchAPIResource,
    ProjectsResource,
    SessionsResource,
    ExtensionsResource,
    AsyncContextsResource,
    AsyncFetchAPIResource,
    AsyncProjectsResource,
    AsyncSessionsResource,
    AsyncExtensionsResource,
)
from browserbase.types.sessions import (
    SessionLog,
    LogListResponse,
    SessionRecording,
    UploadCreateParams,
    UploadCreateResponse,
    RecordingRetrieveResponse,
)
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

# Names imported only to check that they exist; listing them here keeps
# pyright and ruff from reporting them as unused.
__all__ = [
    "AsyncClient",
    "Client",
    "file_from_path",
    "APIResponse",
    "AsyncAPIResponse",
    "BaseModel",
    "DEFAULT_CONNECTION_LIMITS",
    "DEFAULT_MAX_RETRIES",
    "DEFAULT_TIMEOUT",
    "DefaultAsyncHttpxClient",
    "DefaultHttpxClient",
    "RequestOptions",
    "Timeout",
    "AsyncStream",
    "Stream",
    "APIConnectionError",
    "APIError",
    "APIResponseValidationError",
    "APIStatusError",
    "APITimeoutError",
    "AuthenticationError",
    "BadRequestError",
    "BrowserbaseError",
    "ConflictError",
    "InternalServerError",
    "NotFoundError",
    "PermissionDeniedError",
    "RateLimitError",
    "UnprocessableEntityError",
    "NOT_GIVEN",
    "NoneType",
    "NotGiven",
    "Omit",
    "ProxiesTypes",
    "Transport",
    "AsyncContextsResource",
    "AsyncExtensionsResource",
    "AsyncFetchAPIResource",
    "AsyncProjectsResource",
    "AsyncSessionsResource",
    "ContextsResource",
    "ExtensionsResource",
    "FetchAPIResource",
    "ProjectsResource",
    "SessionsResource",
    "AsyncDownloadsResource",
    "AsyncLogsResource",
    "AsyncRecordingResource",
    "AsyncUploadsResource",
    "DownloadsResource",
    "LogsResource",
    "RecordingResource",
    "UploadsResource",
    "SessionListParams",
]

_BrowserSettings = session_create_params.BrowserSettings
_BrowserSettingsContext = session_create_params.BrowserSettingsContext
_BrowserSettingsViewport = session_create_params.BrowserSettingsViewport
_ProxiesUnionMember0 = session_create_params.ProxiesUnionMember0
_ProxiesUnionMember0BrowserbaseProxyConfig = session_create_params.ProxiesUnionMember0BrowserbaseProxyConfig
_ProxiesUnionMember0BrowserbaseProxyConfigGeolocation = (
    session_create_params.ProxiesUnionMember0BrowserbaseProxyConfigGeolocation
)
_ProxiesUnionMember0ExternalProxyConfig = session_create_params.ProxiesUnionMember0ExternalProxyConfig


# ─────────────────────────────────────────────────────────────────────────────
# Shape checks
#
# Each function verifies that a type's fields exist with the expected types.
# These are never called — pyright type-checks them statically.
# Fields are sorted alphabetically within each function.
# ─────────────────────────────────────────────────────────────────────────────


# =============================================================================
# Client resource accessors
# =============================================================================


def check_sync_client_resources(bb: Browserbase) -> None:
    _contexts = bb.contexts
    _extensions = bb.extensions
    _fetch_api = bb.fetch_api
    _projects = bb.projects
    _sessions = bb.sessions


def check_sync_session_subresources(bb: Browserbase) -> None:
    _downloads = bb.sessions.downloads
    _logs = bb.sessions.logs
    _recording = bb.sessions.recording
    _uploads = bb.sessions.uploads


def check_async_client_resources(bb: AsyncBrowserbase) -> None:
    _contexts = bb.contexts
    _extensions = bb.extensions
    _fetch_api = bb.fetch_api
    _projects = bb.projects
    _sessions = bb.sessions


def check_async_session_subresources(bb: AsyncBrowserbase) -> None:
    _downloads = bb.sessions.downloads
    _logs = bb.sessions.logs
    _recording = bb.sessions.recording
    _uploads = bb.sessions.uploads


# =============================================================================
# Context shapes
# =============================================================================


def check_context_shape(ctx: Context) -> None:
    _created_at: datetime = ctx.created_at
    _id: str = ctx.id
    _project_id: str = ctx.project_id
    _updated_at: datetime = ctx.updated_at


def check_context_create_params_shape(params: ContextCreateParams) -> None:
    # project_id is NotRequired in these params. The ignore covers only that,
    # so pyright still reports the key if it is removed.
    _project_id: str = params["project_id"]  # pyright: ignore[reportTypedDictNotRequiredAccess]


def check_context_create_response_shape(resp: ContextCreateResponse) -> None:
    _cipher_algorithm: str = resp.cipher_algorithm
    _id: str = resp.id
    _initialization_vector_size: int = resp.initialization_vector_size
    _public_key: str = resp.public_key
    _upload_url: str = resp.upload_url


def check_context_update_response_shape(resp: ContextUpdateResponse) -> None:
    _cipher_algorithm: str = resp.cipher_algorithm
    _id: str = resp.id
    _initialization_vector_size: int = resp.initialization_vector_size
    _public_key: str = resp.public_key
    _upload_url: str = resp.upload_url


# =============================================================================
# Extension shapes
# =============================================================================


def check_extension_shape(ext: Extension) -> None:
    _created_at: datetime = ext.created_at
    _file_name: str = ext.file_name
    _id: str = ext.id
    _project_id: str = ext.project_id
    _updated_at: datetime = ext.updated_at


def check_extension_create_params_shape(params: ExtensionCreateParams) -> None:
    _file = params["file"]


# =============================================================================
# FetchAPI shapes
# =============================================================================


def check_fetch_api_create_params_shape(params: FetchAPICreateParams) -> None:
    _url: str = params["url"]


def check_fetch_api_create_response_shape(resp: FetchAPICreateResponse) -> None:
    _content: Union[str, Dict[str, object]] = resp.content
    _content_type: str = resp.content_type
    _encoding: str = resp.encoding
    _headers: Dict[str, str] = resp.headers
    _id: str = resp.id
    _status_code: int = resp.status_code


# =============================================================================
# Project shapes
# =============================================================================


def check_project_shape(proj: Project) -> None:
    _concurrency: int = proj.concurrency
    _created_at: datetime = proj.created_at
    _default_timeout: int = proj.default_timeout
    _id: str = proj.id
    _name: str = proj.name
    _owner_id: str = proj.owner_id
    _updated_at: datetime = proj.updated_at


def check_project_list_response_shape(resp: ProjectListResponse) -> None:
    for proj in resp:
        check_project_shape(proj)


def check_project_usage_shape(usage: ProjectUsage) -> None:
    _browser_minutes: int = usage.browser_minutes
    _proxy_bytes: int = usage.proxy_bytes


# =============================================================================
# Session shapes
# =============================================================================


def check_session_shape(session: Session) -> None:
    _context_id: Optional[str] = session.context_id
    _created_at: datetime = session.created_at
    _ended_at: Optional[datetime] = session.ended_at
    _expires_at: datetime = session.expires_at
    _id: str = session.id
    _keep_alive: bool = session.keep_alive
    _project_id: str = session.project_id
    _proxy_bytes: int = session.proxy_bytes
    _region: str = session.region
    _started_at: datetime = session.started_at
    _status: str = session.status
    _updated_at: datetime = session.updated_at
    _user_metadata: Optional[Dict[str, object]] = session.user_metadata


def check_session_create_params_shape(params: SessionCreateParams) -> None:
    _project_id: str = params["project_id"]  # pyright: ignore[reportTypedDictNotRequiredAccess]


def check_session_create_response_shape(resp: SessionCreateResponse) -> None:
    _connect_url: str = resp.connect_url
    _created_at: datetime = resp.created_at
    _expires_at: datetime = resp.expires_at
    _id: str = resp.id
    _keep_alive: bool = resp.keep_alive
    _project_id: str = resp.project_id
    _proxy_bytes: int = resp.proxy_bytes
    _region: str = resp.region
    _selenium_remote_url: str = resp.selenium_remote_url
    _signing_key: str = resp.signing_key
    _started_at: datetime = resp.started_at
    _status: str = resp.status
    _updated_at: datetime = resp.updated_at


def check_session_list_response_shape(resp: SessionListResponse) -> None:
    for session in resp:
        check_session_shape(session)


def check_session_live_urls_shape(urls: SessionLiveURLs) -> None:
    _debugger_fullscreen_url: str = urls.debugger_fullscreen_url
    _debugger_url: str = urls.debugger_url
    _ws_url: str = urls.ws_url


def check_session_retrieve_response_shape(resp: SessionRetrieveResponse) -> None:
    _created_at: datetime = resp.created_at
    _expires_at: datetime = resp.expires_at
    _id: str = resp.id
    _keep_alive: bool = resp.keep_alive
    _project_id: str = resp.project_id
    _proxy_bytes: int = resp.proxy_bytes
    _region: str = resp.region
    _started_at: datetime = resp.started_at
    _status: str = resp.status
    _updated_at: datetime = resp.updated_at


def check_session_update_params_shape(params: SessionUpdateParams) -> None:
    _project_id: str = params["project_id"]  # pyright: ignore[reportTypedDictNotRequiredAccess]
    _status: str = params["status"]


# =============================================================================
# Session sub-resource shapes (logs, recordings, uploads)
# =============================================================================


def check_session_log_shape(log: SessionLog) -> None:
    _method: str = log.method
    _page_id: int = log.page_id
    _session_id: str = log.session_id


def check_log_list_response_shape(resp: LogListResponse) -> None:
    for log in resp:
        check_session_log_shape(log)


def check_session_recording_shape(recording: SessionRecording) -> None:
    _data: Dict[str, object] = recording.data
    _session_id: str = recording.session_id
    _timestamp: int = recording.timestamp
    _type: int = recording.type


def check_recording_retrieve_response_shape(resp: RecordingRetrieveResponse) -> None:
    for recording in resp:
        check_session_recording_shape(recording)


def check_upload_create_params_shape(params: UploadCreateParams) -> None:
    _file = params["file"]


def check_upload_create_response_shape(resp: UploadCreateResponse) -> None:
    _message: str = resp.message


# =============================================================================
# SessionCreateParams nested type shapes (proxy)
# =============================================================================


def check_browserbase_proxy_geolocation_shape(
    geo: _ProxiesUnionMember0BrowserbaseProxyConfigGeolocation,
) -> None:
    _country: str = geo["country"]


def check_browserbase_proxy_config_shape(
    proxy: _ProxiesUnionMember0BrowserbaseProxyConfig,
) -> None:
    _type: str = proxy["type"]


def check_external_proxy_config_shape(
    proxy: _ProxiesUnionMember0ExternalProxyConfig,
) -> None:
    _server: str = proxy["server"]
    _type: str = proxy["type"]


# =============================================================================
# SessionCreateParams nested type shapes (browser settings)
# =============================================================================


def check_browser_settings_shape(settings: _BrowserSettings) -> None:
    _advanced_stealth: Optional[bool] = settings.get("advanced_stealth")
    _block_ads: Optional[bool] = settings.get("block_ads")
    _captcha_image_selector: Optional[str] = settings.get("captcha_image_selector")
    _captcha_input_selector: Optional[str] = settings.get("captcha_input_selector")
    _extension_id: Optional[str] = settings.get("extension_id")
    _log_session: Optional[bool] = settings.get("log_session")
    _record_session: Optional[bool] = settings.get("record_session")
    _solve_captchas: Optional[bool] = settings.get("solve_captchas")
    _verified: Optional[bool] = settings.get("verified")
