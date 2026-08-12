# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from datetime import datetime

from pydantic import Field as FieldInfo

from .._models import BaseModel

__all__ = ["Context"]


class Context(BaseModel):
    id: str

    created_at: datetime = FieldInfo(alias="createdAt")

    project_id: str = FieldInfo(alias="projectId")
    """The Project ID linked to the uploaded Context."""

    updated_at: datetime = FieldInfo(alias="updatedAt")

    name: Optional[str] = None
    """Optional user-defined name for the Context.

    Leading and trailing whitespace is trimmed before storage. Names are unique
    within the project among active Contexts, compared case-insensitively.
    """
