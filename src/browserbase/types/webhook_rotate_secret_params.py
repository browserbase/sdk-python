# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Annotated, TypedDict

from .._utils import PropertyInfo

__all__ = ["WebhookRotateSecretParams"]


class WebhookRotateSecretParams(TypedDict, total=False):
    revoke_immediately: Annotated[bool, PropertyInfo(alias="revokeImmediately")]
    """Expire the old secret at once instead of honouring it for 24 hours.

    Use when responding to a leak; deliveries signed with the old secret stop
    verifying immediately.
    """
