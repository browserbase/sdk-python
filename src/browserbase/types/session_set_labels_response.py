# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List

from .label import Label
from .._models import BaseModel

__all__ = ["SessionSetLabelsResponse"]


class SessionSetLabelsResponse(BaseModel):
    labels: List[Label]
