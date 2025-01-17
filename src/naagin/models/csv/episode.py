from datetime import datetime
from typing import Optional

from naagin.models.base import BaseModel


class EpisodeCSVModel(BaseModel):
    _column_1: int
    episode_mid: int
    _column_3: int
    _column_4: int
    experience_gain: int
    _column_6: int
    _column_7: int
    _column_8: int
    _column_9: Optional[datetime]
    _column_10: Optional[int]
    _column_11: Optional[int]
    _column_12: int
