from datetime import datetime

from naagin.models.base import CustomBaseModel


class ItemConsumeModel(CustomBaseModel):
    item_mid: int
    count: int
    type: int
    created_at: datetime
    updated_at: datetime | None
