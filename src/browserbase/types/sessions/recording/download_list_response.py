# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List

from ...._models import BaseModel
from .recording_download import RecordingDownload

__all__ = ["DownloadListResponse"]


class DownloadListResponse(BaseModel):
    downloads: List[RecordingDownload]
