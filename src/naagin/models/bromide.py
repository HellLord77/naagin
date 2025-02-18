from datetime import datetime

from naagin.bases import ModelBase


class BromideModel(ModelBase):
    item_mid: int
    variation: int
    is_generate_seal: int
    count: int
    created_at: datetime
