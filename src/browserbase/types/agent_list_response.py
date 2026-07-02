# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, List, Optional
from datetime import datetime

from pydantic import Field as FieldInfo

from .._models import BaseModel

__all__ = ["AgentListResponse", "Data"]


class Data(BaseModel):
    """A reusable agent.

    Referenced by `agentId` to apply a system prompt to every run that uses the agent.
    """

    agent_id: str = FieldInfo(alias="agentId")
    """Unique identifier for the agent.

    Use this value as `agentId` when creating an agent run.
    """

    created_at: datetime = FieldInfo(alias="createdAt")

    name: str
    """Human-readable name for the agent.

    Used to identify the agent in the dashboard and API responses.
    """

    updated_at: datetime = FieldInfo(alias="updatedAt")

    result_schema: Optional[Dict[str, object]] = FieldInfo(alias="resultSchema", default=None)
    """
    [JSON Schema](https://json-schema.org/specification) that runs referencing this
    agent will aim to conform their `result` to. Can be overridden per run by
    passing `resultSchema` on the run request.
    """

    system_prompt: Optional[str] = FieldInfo(alias="systemPrompt", default=None)
    """System prompt applied to every run that uses this agent."""


class AgentListResponse(BaseModel):
    """A page of agents."""

    data: List[Data]
    """The page of matching agents."""

    limit: int
    """The maximum number of results returned in this page."""

    next_cursor: Optional[str] = FieldInfo(alias="nextCursor", default=None)
    """Cursor for the next page.

    Pass it back as `cursor` on the next request to continue paging. null when there
    are no more results.
    """
