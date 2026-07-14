# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from datetime import datetime
from typing_extensions import Literal

from pydantic import Field as FieldInfo

from ...._models import BaseModel

__all__ = ["RecordingDownload"]


class RecordingDownload(BaseModel):
    page_id: str = FieldInfo(alias="pageId")
    """Recorded page (tab) within the session, e.g. "0", "1"."""

    status: Literal["NOT_REQUESTED", "PENDING", "COMPLETED", "FAILED"]
    """Per-page MP4 assembly state.

    `NOT_REQUESTED`: no download has been requested for the session yet. `PENDING`:
    assembly is enqueued or in progress. `COMPLETED`: the MP4 is ready. `FAILED`:
    assembly failed; POST again to retry.
    """

    completed_at: Optional[datetime] = FieldInfo(alias="completedAt", default=None)
    """When the MP4 was created.

    Present only when COMPLETED on a standard (non-BYOS) project.
    """

    download_url: Optional[str] = FieldInfo(alias="downloadUrl", default=None)
    """Short-lived signed CDN URL, re-minted each GET.

    Present only when COMPLETED on a standard (non-BYOS) project.
    """
