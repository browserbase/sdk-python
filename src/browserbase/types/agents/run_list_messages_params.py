# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import TypedDict

__all__ = ["RunListMessagesParams"]


class RunListMessagesParams(TypedDict, total=False):
    all: bool
    """Return every message after `since` in one response, ignoring `limit`."""

    limit: int
    """Maximum number of messages to return."""

    since: str
    """The `id` of the last message you've already received.

    The response will contain messages produced after that one, in chronological
    order. Omit on the first call. Pass the previous response's `nextSince` value to
    continue paging or to poll for new messages.
    """
