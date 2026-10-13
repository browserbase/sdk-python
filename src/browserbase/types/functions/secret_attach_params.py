# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, Annotated, TypedDict

from ..._utils import PropertyInfo

__all__ = ["SecretAttachParams"]


class SecretAttachParams(TypedDict, total=False):
    secret_id: Required[Annotated[str, PropertyInfo(alias="secretId")]]
    """The id of the project secret to attach (the `id` returned by POST /v1/secrets).

    Idempotent: re-attaching an already-attached secret succeeds.
    """
