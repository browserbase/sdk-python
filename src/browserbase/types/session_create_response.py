# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from pydantic import Field as FieldInfo

from .session import Session

__all__ = ["SessionCreateResponse"]


class SessionCreateResponse(Session):
    connect_url: str = FieldInfo(alias="connectUrl")
    """WebSocket URL to connect to the Session."""

    selenium_remote_url: str = FieldInfo(alias="seleniumRemoteUrl")
    """HTTP URL to connect to the Session."""

    signing_key: str = FieldInfo(alias="signingKey")
    """Signing key to use when connecting to the Session via HTTP."""
