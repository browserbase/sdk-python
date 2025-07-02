# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from datetime import datetime

from pydantic import Field as FieldInfo

from .._models import BaseModel

__all__ = ["ExtensionCreateResponse"]


class ExtensionCreateResponse(BaseModel):
    id: str

    created_at: datetime = FieldInfo(alias="createdAt")

    file_name: str = FieldInfo(alias="fileName")

    project_id: str = FieldInfo(alias="projectId")
    """The Project ID linked to the uploaded Extension."""

    updated_at: datetime = FieldInfo(alias="updatedAt")
