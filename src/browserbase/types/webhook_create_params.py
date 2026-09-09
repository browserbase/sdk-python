# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List
from typing_extensions import Literal, Required, Annotated, TypedDict

from .._utils import PropertyInfo

__all__ = ["WebhookCreateParams"]


class WebhookCreateParams(TypedDict, total=False):
    endpoint: Required[str]
    """HTTPS URL that event deliveries are POSTed to. Must be publicly reachable."""

    event_types: Required[
        Annotated[
            List[Literal["agents.runs.running", "agents.runs.completed", "agents.runs.stopped", "agents.runs.failed"]],
            PropertyInfo(alias="eventTypes"),
        ]
    ]
    """Event types this webhook subscribes to. Unknown types are rejected."""
