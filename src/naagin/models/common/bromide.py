from datetime import datetime

from naagin.models.base import BaseModel


class BromideModel(BaseModel):
    item_mid: int
    variation: int
    is_generate_seal: int
    count: int
    created_at: datetime
