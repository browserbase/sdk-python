# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List
from typing_extensions import Literal, Annotated, TypedDict

from .._utils import PropertyInfo

__all__ = ["WebhookUpdateParams"]


class WebhookUpdateParams(TypedDict, total=False):
    endpoint: str
    """HTTPS URL that event deliveries are POSTed to. Must be publicly reachable."""

    event_types: Annotated[
        List[
            Literal[
                "functions.builds.running",
                "functions.builds.completed",
                "functions.builds.failed",
                "functions.invocations.pending",
                "functions.invocations.running",
                "functions.invocations.completed",
                "functions.invocations.failed",
            ]
        ],
        PropertyInfo(alias="eventTypes"),
    ]
    """Event types this webhook subscribes to. Unknown types are rejected."""
