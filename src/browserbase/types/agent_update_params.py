# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict
from typing_extensions import Annotated, TypedDict

from .._utils import PropertyInfo

__all__ = ["AgentUpdateParams"]


class AgentUpdateParams(TypedDict, total=False):
    name: str
    """Human-readable name for the agent.

    Used to identify the agent in the dashboard and API responses.
    """

    result_schema: Annotated[Dict[str, object], PropertyInfo(alias="resultSchema")]
    """An optional [JSON Schema](https://json-schema.org/specification) object.

    If provided, runs that reference this agent will aim to return a `result` that
    conforms to this schema when they complete. Can be overridden per run by passing
    `resultSchema` on the run request.
    """

    system_prompt: Annotated[str, PropertyInfo(alias="systemPrompt")]
    """
    New system prompt that steers the agent's behavior on every run that uses this
    agent.
    """
