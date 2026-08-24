# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Annotated, TypedDict

from .._utils import PropertyInfo

__all__ = ["SessionDebugParams"]


class SessionDebugParams(TypedDict, total=False):
    expires_in: Annotated[int, PropertyInfo(alias="expiresIn")]
    """Time-to-live of the generated live view URLs, in seconds.

    If omitted, the URLs expire with the session, up to a maximum of 21600 seconds
    (6 hours).
    """
