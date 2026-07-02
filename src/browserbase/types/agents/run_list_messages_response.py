# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import TYPE_CHECKING, Dict, List, Union, Optional
from datetime import datetime
from typing_extensions import Literal

from pydantic import Field as FieldInfo

from ..._models import BaseModel

__all__ = ["RunListMessagesResponse", "Data", "DataMessage", "DataMessageContentUnionMember1"]


class DataMessageContentUnionMember1(BaseModel):
    type: str
    """text | reasoning | file | tool-call | tool-result"""

    data: Optional[str] = None

    input: Optional[object] = None

    media_type: Optional[str] = FieldInfo(alias="mediaType", default=None)

    output: Optional[object] = None

    text: Optional[str] = None

    tool_call_id: Optional[str] = FieldInfo(alias="toolCallId", default=None)

    tool_name: Optional[str] = FieldInfo(alias="toolName", default=None)

    if TYPE_CHECKING:
        # Some versions of Pydantic <2.8.0 have a bug and don’t allow assigning a
        # value to this field, so for compatibility we avoid doing it at runtime.
        __pydantic_extra__: Dict[str, object] = FieldInfo(init=False)  # pyright: ignore[reportIncompatibleVariableOverride]

        # Stub to indicate that arbitrary properties are accepted.
        # To access properties that are not valid identifiers you can use `getattr`, e.g.
        # `getattr(obj, '$type')`
        def __getattr__(self, attr: str) -> object: ...
    else:
        __pydantic_extra__: Dict[str, object]


class DataMessage(BaseModel):
    """An AI SDK response message (assistant or tool)."""

    content: Union[str, List[DataMessageContentUnionMember1]]
    """Plain string (assistant text) or an array of typed parts."""

    role: Literal["assistant", "tool"]

    if TYPE_CHECKING:
        # Some versions of Pydantic <2.8.0 have a bug and don’t allow assigning a
        # value to this field, so for compatibility we avoid doing it at runtime.
        __pydantic_extra__: Dict[str, object] = FieldInfo(init=False)  # pyright: ignore[reportIncompatibleVariableOverride]

        # Stub to indicate that arbitrary properties are accepted.
        # To access properties that are not valid identifiers you can use `getattr`, e.g.
        # `getattr(obj, '$type')`
        def __getattr__(self, attr: str) -> object: ...
    else:
        __pydantic_extra__: Dict[str, object]


class Data(BaseModel):
    id: str

    created_at: datetime = FieldInfo(alias="createdAt")

    message: DataMessage
    """An AI SDK response message (assistant or tool)."""


class RunListMessagesResponse(BaseModel):
    data: List[Data]
    """The page of messages, in chronological order, with the oldest messages first."""

    next_since: Optional[str] = FieldInfo(alias="nextSince", default=None)
    """The `id` of the last message in `data`.

    Pass it back as `since` on the next request to continue paging, or to poll for
    new messages. `null` only when the run has no messages yet; in that case, omit
    `since` and retry.
    """
