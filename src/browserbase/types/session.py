# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from datetime import datetime
from typing_extensions import Literal

from pydantic import Field as FieldInfo

from .._models import BaseModel

__all__ = ["Session"]


class Session(BaseModel):
    id: str

    created_at: datetime

    expires_at: datetime

    keep_alive: bool
    """Indicates if the Session was created to be kept alive upon disconnections"""

    project_id: str
    """The Project ID linked to the Session."""

    region: str

    started_at: datetime

    status: Literal["RUNNING", "ERROR", "TIMED_OUT", "COMPLETED"]

    updated_at: datetime

    avg_cpu_usage: Optional[int] = None
    """CPU used by the Session"""

    connect_url: Optional[str] = FieldInfo(alias="connectUrl", default=None)

    context_id: Optional[str] = None
    """Optional. The Context linked to the Session."""

    ended_at: Optional[datetime] = None

    is_idle: Optional[bool] = None

    memory_usage: Optional[int] = None
    """Memory used by the Session"""

    proxy_bytes: Optional[int] = None
    """Bytes used via the [Proxy](/features/stealth-mode#proxies-and-residential-ips)"""

    selenium_remote_url: Optional[str] = FieldInfo(alias="seleniumRemoteUrl", default=None)

    signing_key: Optional[str] = FieldInfo(alias="signingKey", default=None)

    viewport_height: Optional[int] = None

    viewport_width: Optional[int] = None
