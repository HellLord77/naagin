from typing import Optional

from .....base import BaseModel


class OwnerPutRequestModel(BaseModel):
    name: Optional[str] = None
    island_name: Optional[str] = None
    message: Optional[str] = None
