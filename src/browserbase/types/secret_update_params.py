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
    """The new secret value encrypted with HPKE.

    In order to seal the secret value before sending, get the project's public key
    from GET /v1/secrets/keypair. Decode the publicKey using base64 into the raw
    32-byte public key. Then, use HPKE Base mode (RFC 9180) with the following
    algorithm suite: DHKEM(X25519, HKDF-SHA256), HKDF-SHA256, and AES-256-GCM. Set
    both info and additional authenticated data (AAD) to an empty byte string. Then,
    create a new sender context using the public key and these settings, and encrypt
    the secret value as one message. Put the 32-byte encapsulated key before the
    ciphertext and keep the authentication tag at the end of the ciphertext. Encode
    the combined bytes with standard base64. Send the result as sealedSecretValue:
    base64(enc || ciphertext)
    """
