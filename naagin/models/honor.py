from datetime import datetime

from naagin.bases import ModelBase


class HonorModel(ModelBase):
    honor_mid: int
    times_received: int
    parent_honor_mid: int
    created_at: datetime
