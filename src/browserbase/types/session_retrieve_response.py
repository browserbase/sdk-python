# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from pydantic import Field as FieldInfo

from .session import Session
from .._models import BaseModel

__all__ = ["SessionRetrieveResponse", "SessionRetrieveResponseLabel"]


class SessionRetrieveResponseLabel(BaseModel):
    """A project-owned session label."""

    id: str
    """Stable identifier of the label."""

    name: str
    """Display name, unique ignoring case within the project."""


class SessionRetrieveResponse(Session):
    connect_url: Optional[str] = FieldInfo(alias="connectUrl", default=None)
    """WebSocket URL to connect to the Session."""

    labels: Optional[List[SessionRetrieveResponseLabel]] = None
    """Browserbase returns label IDs and current names only when includeLabels is true.

    An empty array means the session has no labels.
    """

    selenium_remote_url: Optional[str] = FieldInfo(alias="seleniumRemoteUrl", default=None)
    """HTTP URL to connect to the Session."""

    signing_key: Optional[str] = FieldInfo(alias="signingKey", default=None)
    """Signing key to use when connecting to the Session via HTTP."""
