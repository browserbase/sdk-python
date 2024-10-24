# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List
from typing_extensions import TypeAlias

from .session_log import SessionLog

__all__ = ["LogListResponse"]

LogListResponse: TypeAlias = List[SessionLog]
