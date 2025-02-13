from datetime import datetime

from naagin.bases import ModelBase


class ItemConsumeModel(ModelBase):
    item_mid: int
    count: int
    type: int
    created_at: datetime
    updated_at: datetime | None
