# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from datetime import datetime

from pydantic import Field as FieldInfo

from .._models import BaseModel

__all__ = ["Secret"]


class Secret(BaseModel):
    id: str
    """Unique identifier of the secret."""

    secret_key: str = FieldInfo(alias="secretKey")
    """The name the secret value is stored under."""

    created_at: Optional[datetime] = FieldInfo(alias="createdAt", default=None)
    """Time at which the secret was created, in UTC, using RFC 3339 format, e.g.

    2026-01-19T00:00:00.000Z.
    """

    updated_at: Optional[datetime] = FieldInfo(alias="updatedAt", default=None)
    """
    Time at which the secret's value was last set, in UTC, using RFC 3339 format,
    e.g. 2026-01-20T00:00:00.000Z.
    """
