from datetime import datetime
from typing import Optional

from naagin.models.base import BaseModel


class ItemConsumeModel(BaseModel):
    item_mid: int
    count: int
    type: int
    updated_at: Optional[datetime]
    created_at: datetime


class ItemConsumeGetResponseModel(BaseModel):
    item_consume_list: list[ItemConsumeModel]
