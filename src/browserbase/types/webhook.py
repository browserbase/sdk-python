# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List
from datetime import datetime
from typing_extensions import Literal

from pydantic import Field as FieldInfo

from .._models import BaseModel

__all__ = ["Webhook"]


class Webhook(BaseModel):
    """A delivery endpoint for a project.

    Browserbase POSTs a signed event to it whenever one of its subscribed event types occurs. The signing secret is returned only when it is created or rotated.
    """

    id: str
    """Unique identifier for the webhook."""

    created_at: datetime = FieldInfo(alias="createdAt")

    endpoint: str
    """HTTPS URL that event deliveries are POSTed to. Must be publicly reachable."""

    event_types: List[
        Literal[
            "functions.builds.running",
            "functions.builds.completed",
            "functions.builds.failed",
            "functions.invocations.pending",
            "functions.invocations.running",
            "functions.invocations.completed",
            "functions.invocations.failed",
        ]
    ] = FieldInfo(alias="eventTypes")
    """Event types this webhook subscribes to. Unknown types are rejected."""

    project_id: str = FieldInfo(alias="projectId")
    """The project the webhook belongs to."""

    updated_at: datetime = FieldInfo(alias="updatedAt")
