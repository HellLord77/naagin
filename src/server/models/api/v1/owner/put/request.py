from typing import Optional

from .....base import NaaginBaseModel


class OwnerPutRequestModel(NaaginBaseModel):
    name: Optional[str] = None
    island_name: Optional[str] = None
    message: Optional[str] = None
