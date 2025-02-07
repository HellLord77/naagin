from datetime import datetime

from naagin.models.base import BaseModel


class ItemConsumeModel(BaseModel):
    item_mid: int
    count: int
    type: int
    created_at: datetime
    updated_at: datetime | None
