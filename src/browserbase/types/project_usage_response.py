# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from pydantic import Field as FieldInfo

from .._models import BaseModel

__all__ = ["ProjectUsageResponse"]


class ProjectUsageResponse(BaseModel):
    browser_minutes: int = FieldInfo(alias="browserMinutes")

    proxy_bytes: int = FieldInfo(alias="proxyBytes")
