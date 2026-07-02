# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, List, Optional
from datetime import datetime
from typing_extensions import Literal

from pydantic import Field as FieldInfo

from ..._models import BaseModel

__all__ = ["RunListResponse", "Data", "DataCause"]


class DataCause(BaseModel):
    code: str
    """Structured failure code (e.g., RUNNER_HEARTBEAT_LOST)."""

    message: Optional[str] = None
    """Human-readable failure detail."""


class Data(BaseModel):
    """One execution of an agent against a task.

    Created in `pending` and transitioned through `running` → `completed`/`failed` by the runner.
    """

    created_at: datetime = FieldInfo(alias="createdAt")

    run_id: str = FieldInfo(alias="runId")
    """Unique identifier for the run."""

    status: Literal["PENDING", "RUNNING", "COMPLETED", "FAILED", "STOPPED", "TIMED_OUT"]
    """Current status of the run.

    - `PENDING` - agent will run soon
    - `RUNNING` - agent is currently running
    - `COMPLETED` - agent has finished running
    - `FAILED` - agent has failed the run
    - `STOPPED` - run was stopped by the user
    - `TIMED_OUT` - run exceeded maximum time
    """

    task: str
    """The original task description."""

    updated_at: datetime = FieldInfo(alias="updatedAt")

    agent_id: Optional[str] = FieldInfo(alias="agentId", default=None)
    """The ID of the agent applied to this run, if any. Omitted for ad-hoc runs."""

    cause: Optional[DataCause] = None

    ended_at: Optional[datetime] = FieldInfo(alias="endedAt", default=None)

    result: Optional[Dict[str, object]] = None
    """The agent's structured result for the run.

    Only present when the run has finished and output is available. The result
    conforms to the provided [JSON Schema](https://json-schema.org/specification)
    when one is set.
    """

    result_schema: Optional[Dict[str, object]] = FieldInfo(alias="resultSchema", default=None)
    """
    Per-run [JSON Schema](https://json-schema.org/specification) override for the
    result shape. When unset, the agent's default `resultSchema` applies.
    """

    sandbox_id: Optional[str] = FieldInfo(alias="sandboxId", default=None)
    """External sandbox identifier assigned by the runner. Optional."""

    session_id: Optional[str] = FieldInfo(alias="sessionId", default=None)
    """The Browserbase session ID powering this run."""

    started_at: Optional[datetime] = FieldInfo(alias="startedAt", default=None)


class RunListResponse(BaseModel):
    """A page of agent runs."""

    data: List[Data]
    """The page of matching agent runs."""

    limit: int
    """The maximum number of results returned in this page."""

    next_cursor: Optional[str] = FieldInfo(alias="nextCursor", default=None)
    """Cursor for the next page.

    Pass it back as `cursor` on the next request to continue paging. null when there
    are no more results.
    """
