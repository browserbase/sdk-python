# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, Annotated, TypedDict

from .._utils import PropertyInfo

__all__ = ["SecretUpdateParams"]


class SecretUpdateParams(TypedDict, total=False):
    keypair_id: Required[Annotated[str, PropertyInfo(alias="keypairId")]]
    """
    The `id` returned by GET /v1/secrets/keypair, identifying the keypair whose
    public key encrypted the value. Recorded with the secret so decryption stays
    correct across keypair rotation.
    """

    sealed_secret_value: Required[Annotated[str, PropertyInfo(alias="sealedSecretValue")]]
    """
    The new secret value, HPKE-sealed with the project's public key (see GET
    /v1/secrets/keypair) and base64-encoded.
    """
