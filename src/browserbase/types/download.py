# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from datetime import datetime

from pydantic import Field as FieldInfo

from .._models import BaseModel

__all__ = ["Download"]


class Download(BaseModel):
    id: str
    """Unique identifier for the download."""

    checksum: str
    """SHA256 checksum of the file."""

    created_at: datetime = FieldInfo(alias="createdAt")
    """Timestamp when the file was downloaded."""

    filename: str
    """The filename of the downloaded file."""

    mime_type: str = FieldInfo(alias="mimeType")
    """The MIME type of the file."""

    session_id: str = FieldInfo(alias="sessionId")
    """The Session ID this download belongs to."""

    size: float
    """File size in bytes."""
