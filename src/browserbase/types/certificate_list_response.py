# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List
from typing_extensions import TypeAlias

from .certificate import Certificate

__all__ = ["CertificateListResponse"]

CertificateListResponse: TypeAlias = List[Certificate]
