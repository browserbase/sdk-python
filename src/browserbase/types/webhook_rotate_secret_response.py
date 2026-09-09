# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from .._models import BaseModel

__all__ = ["WebhookRotateSecretResponse"]


class WebhookRotateSecretResponse(BaseModel):
    """The new signing secret. Shown once; store it now."""

    secret: str
    """The new signing secret, prefixed `whsec_`."""
