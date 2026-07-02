# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union
from datetime import datetime
from typing_extensions import Literal, Annotated, TypedDict

from ..._utils import PropertyInfo

__all__ = ["RunListParams"]


class RunListParams(TypedDict, total=False):
    agent_id: Annotated[str, PropertyInfo(alias="agentId")]
    """Only return runs that reference this agent ID."""

    cursor: str
    """Pagination cursor.

    Pass the nextCursor from the previous response to fetch the next page. Omit to
    start from the first page.
    """

    end_at: Annotated[Union[str, datetime], PropertyInfo(alias="endAt", format="iso8601")]
    """Only return runs created on or before this timestamp (inclusive).

    ISO 8601 / RFC 3339, e.g. 2026-01-20T00:00:00Z.
    """

    limit: int
    """Maximum number of results to return."""

    start_at: Annotated[Union[str, datetime], PropertyInfo(alias="startAt", format="iso8601")]
    """Only return runs created on or after this timestamp (inclusive).

    ISO 8601 / RFC 3339, e.g. 2026-01-19T00:00:00Z.
    """

    status: Literal["PENDING", "RUNNING", "COMPLETED", "FAILED", "STOPPED", "TIMED_OUT"]
    """Current status of the run.

    - `PENDING` - agent will run soon
    - `RUNNING` - agent is currently running
    - `COMPLETED` - agent has finished running
    - `FAILED` - agent has failed the run
    - `STOPPED` - run was stopped by the user
    - `TIMED_OUT` - run exceeded maximum time
    """
