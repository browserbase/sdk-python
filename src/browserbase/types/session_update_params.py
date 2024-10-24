# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, Required, Annotated, TypedDict

from .._utils import PropertyInfo

__all__ = ["SessionUpdateParams"]


class SessionUpdateParams(TypedDict, total=False):
    project_id: Required[Annotated[str, PropertyInfo(alias="projectId")]]
    """The Project ID.

    Can be found in [Settings](https://www.browserbase.com/settings).
    """

    status: Required[Literal["REQUEST_RELEASE"]]
    """Set to `REQUEST_RELEASE` to request that the session complete.

    Use before session's timeout to avoid additional charges.
    """
