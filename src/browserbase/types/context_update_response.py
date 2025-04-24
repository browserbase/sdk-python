# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from pydantic import Field as FieldInfo

from .._models import BaseModel

__all__ = ["ContextUpdateResponse"]


class ContextUpdateResponse(BaseModel):
    id: str

    cipher_algorithm: str = FieldInfo(alias="cipherAlgorithm")
    """The cipher algorithm used to encrypt the user-data-directory.

    AES-256-CBC is currently the only supported algorithm.
    """

    initialization_vector_size: int = FieldInfo(alias="initializationVectorSize")
    """The initialization vector size used to encrypt the user-data-directory.

    [Read more about how to use it](/features/contexts).
    """

    public_key: str = FieldInfo(alias="publicKey")
    """The public key to encrypt the user-data-directory."""

    upload_url: str = FieldInfo(alias="uploadUrl")
    """An upload URL to upload a custom user-data-directory."""
