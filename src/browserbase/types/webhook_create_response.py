# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from .webhook import Webhook

__all__ = ["WebhookCreateResponse"]


class WebhookCreateResponse(Webhook):
    """The created webhook, including its signing secret."""

    secret: str
    """HMAC-SHA256 signing secret, prefixed `whsec_`.

    Shown once here; store it now. Use it to verify the signature on every delivery.
    """
