# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List

from .._models import BaseModel
from .navigation_policy import NavigationPolicy

__all__ = ["NavigationPolicyListResponse"]


class NavigationPolicyListResponse(BaseModel):
    """The project's navigation policies."""

    data: List[NavigationPolicy]
    """The project's navigation policies, ordered by name."""
