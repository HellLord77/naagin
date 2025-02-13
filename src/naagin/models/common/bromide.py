from datetime import datetime

from naagin.models.base import CustomBaseModel


class BromideModel(CustomBaseModel):
    item_mid: int
    variation: int
    is_generate_seal: int
    count: int
    created_at: datetime
