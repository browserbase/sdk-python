# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, TypedDict

__all__ = ["LabelUpdateParams"]


class LabelUpdateParams(TypedDict, total=False):
    name: Required[str]
    """Label name.

    Browserbase trims surrounding Unicode whitespace and preserves display
    capitalization. The trimmed name must contain 1–128 Unicode characters and no
    NUL characters. Names are unique ignoring case within the project.
    """
