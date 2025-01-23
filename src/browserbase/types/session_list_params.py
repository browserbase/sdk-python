# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, TypedDict

__all__ = ["SessionListParams"]


class SessionListParams(TypedDict, total=False):
    q: str
    """Query sessions by user metadata.

    See
    [Querying Sessions by User Metadata](/features/sessions#querying-sessions-by-user-metadata)
    for the schema of this query.
    """

    status: Literal["RUNNING", "ERROR", "TIMED_OUT", "COMPLETED"]
