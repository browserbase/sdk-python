# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from datetime import datetime

from pydantic import Field as FieldInfo

from .._models import BaseModel

__all__ = ["Label"]


class Label(BaseModel):
    """A project-owned session label."""

    id: str
    """Stable identifier of the label."""

    created_at: datetime = FieldInfo(alias="createdAt")
    """UTC timestamp when the label was created."""

    name: str
    """Display name, unique ignoring case within the project."""

    project_id: str = FieldInfo(alias="projectId")
    """The project that owns the label."""

    updated_at: datetime = FieldInfo(alias="updatedAt")
    """UTC timestamp when the label was last renamed."""
