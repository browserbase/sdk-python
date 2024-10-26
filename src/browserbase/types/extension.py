# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from datetime import datetime

from pydantic import Field as FieldInfo

from .._models import BaseModel

__all__ = ["Extension"]


class Extension(BaseModel):
    id: str

    created_at: datetime

    file_name: str = FieldInfo(alias="fileName")

    project_id: str = FieldInfo(alias="projectId")
    """The Project ID linked to the uploaded Extension."""

    updated_at: datetime
