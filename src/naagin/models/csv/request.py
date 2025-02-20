from datetime import datetime
from typing import Optional

from naagin.bases import ModelBase


class RequestCSVModel(ModelBase):
    request_mid: int
    _column_2: int
    _column_3: int
    category: int
    _column_5: int
    _column_6: int
    time_required: int
    friendly_level: int
    publish_at: datetime
    close_at: Optional[datetime]
    _column_11: int
    rank_1_rate: int
    _column_13: int
    rank_2_rate: int
    _column_15: int
    rank_3_rate: int
    _column_17: Optional[int]
