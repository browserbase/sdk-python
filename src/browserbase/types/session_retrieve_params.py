# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Annotated, TypedDict

from .._utils import PropertyInfo

__all__ = ["SessionRetrieveParams"]


class SessionRetrieveParams(TypedDict, total=False):
    include_labels: Annotated[bool, PropertyInfo(alias="includeLabels")]
    """Include the session's label IDs and current names."""
