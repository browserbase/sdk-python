# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from pydantic import Field as FieldInfo

from .._models import BaseModel

__all__ = ["SecretsKeypair"]


class SecretsKeypair(BaseModel):
    id: str
    """Identifier of the keypair the public key was minted from.

    Pass this back when creating a secret so the ciphertext records which keypair
    sealed it, which keeps decryption correct across keypair rotation.
    """

    public_key: str = FieldInfo(alias="publicKey")
    """The project's HPKE public encryption key, base64-encoded.

    Encrypt secret values with this key before creating a secret.
    """
