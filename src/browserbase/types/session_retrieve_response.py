# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from pydantic import Field as FieldInfo

from .session import Session

__all__ = ["SessionRetrieveResponse"]


class SessionRetrieveResponse(Session):
    connect_url: Optional[str] = FieldInfo(alias="connectUrl", default=None)
    """WebSocket URL to connect to the Session."""

    selenium_remote_url: Optional[str] = FieldInfo(alias="seleniumRemoteUrl", default=None)
    """HTTP URL to connect to the Session."""

    signing_key: Optional[str] = FieldInfo(alias="signingKey", default=None)
    """Signing key to use when connecting to the Session via HTTP."""
