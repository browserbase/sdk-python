# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List
from typing_extensions import TypeAlias

from .session_recording import SessionRecording

__all__ = ["RecordingRetrieveResponse"]

RecordingRetrieveResponse: TypeAlias = List[SessionRecording]
