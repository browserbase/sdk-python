# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from datetime import datetime
from typing_extensions import Literal

from pydantic import Field as FieldInfo

from .._models import BaseModel

__all__ = ["Session"]


class Session(BaseModel):
    id: str

    created_at: datetime = FieldInfo(alias="createdAt")

    expires_at: datetime = FieldInfo(alias="expiresAt")

    keep_alive: bool = FieldInfo(alias="keepAlive")
    """Indicates if the Session was created to be kept alive upon disconnections"""

    project_id: str = FieldInfo(alias="projectId")
    """The Project ID linked to the Session."""

    proxy_bytes: int = FieldInfo(alias="proxyBytes")
    """Bytes used via the [Proxy](/features/stealth-mode#proxies-and-residential-ips)"""

    started_at: datetime = FieldInfo(alias="startedAt")

    status: Literal["RUNNING", "ERROR", "TIMED_OUT", "COMPLETED"]

    updated_at: datetime = FieldInfo(alias="updatedAt")

    avg_cpu_usage: Optional[int] = FieldInfo(alias="avgCpuUsage", default=None)
    """CPU used by the Session"""

    context_id: Optional[str] = FieldInfo(alias="contextId", default=None)
    """Optional. The Context linked to the Session."""

    ended_at: Optional[datetime] = FieldInfo(alias="endedAt", default=None)

    memory_usage: Optional[int] = FieldInfo(alias="memoryUsage", default=None)
    """Memory used by the Session"""
