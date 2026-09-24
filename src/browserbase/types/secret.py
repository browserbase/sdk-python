# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from pydantic import Field as FieldInfo

from .._models import BaseModel

__all__ = ["Secret"]


class Secret(BaseModel):
    id: str
    """Unique identifier of the secret."""

    secret_key: str = FieldInfo(alias="secretKey")
    """The name the secret value is stored under."""
