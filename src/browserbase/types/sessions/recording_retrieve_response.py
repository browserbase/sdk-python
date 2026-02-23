# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, List
from typing_extensions import TypeAlias

from pydantic import Field as FieldInfo

from ..._models import BaseModel

__all__ = ["RecordingRetrieveResponse", "RecordingRetrieveResponseItem"]


class RecordingRetrieveResponseItem(BaseModel):
    data: Dict[str, object]
    """
    See
    [rrweb documentation](https://github.com/rrweb-io/rrweb/blob/master/docs/recipes/dive-into-event.md).
    """

    session_id: str = FieldInfo(alias="sessionId")

    timestamp: int
    """milliseconds that have elapsed since the UNIX epoch"""

    type: int


RecordingRetrieveResponse: TypeAlias = List[RecordingRetrieveResponseItem]
