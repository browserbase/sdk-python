# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from pydantic import Field as FieldInfo

from .._models import BaseModel

__all__ = ["ContextCreateResponse"]


class ContextCreateResponse(BaseModel):
    id: str

    cipher_algorithm: Optional[str] = FieldInfo(alias="cipherAlgorithm", default=None)
    """The cipher algorithm used to encrypt the user-data-directory.

    AES-256-CBC is currently the only supported algorithm.
    """

    initialization_vector_size: Optional[int] = FieldInfo(alias="initializationVectorSize", default=None)
    """The initialization vector size used to encrypt the user-data-directory.

    [Read more about how to use it](/features/contexts).
    """

    public_key: Optional[str] = FieldInfo(alias="publicKey", default=None)
    """The public key to encrypt the user-data-directory."""

    upload_url: Optional[str] = FieldInfo(alias="uploadUrl", default=None)
    """An upload URL to upload a custom user-data-directory."""
