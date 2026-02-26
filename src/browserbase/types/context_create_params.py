# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Annotated, TypedDict

from .._utils import PropertyInfo

__all__ = ["ContextCreateParams"]


class ContextCreateParams(TypedDict, total=False):
    project_id: Annotated[str, PropertyInfo(alias="projectId")]
    """The Project ID.

    Can be found in [Settings](https://www.browserbase.com/settings). Optional - if
    not provided, the project will be inferred from the API key.
    """
