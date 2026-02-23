# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from datetime import datetime

from pydantic import Field as FieldInfo

from .._models import BaseModel

__all__ = ["ContextRetrieveResponse"]


class ContextRetrieveResponse(BaseModel):
    id: str

    created_at: datetime = FieldInfo(alias="createdAt")

    project_id: str = FieldInfo(alias="projectId")
    """The Project ID linked to the uploaded Context."""

    updated_at: datetime = FieldInfo(alias="updatedAt")
