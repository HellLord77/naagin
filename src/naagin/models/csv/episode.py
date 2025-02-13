from datetime import datetime

from naagin.models.base import CustomBaseModel


class EpisodeCSVModel(CustomBaseModel):
    _column_1: int
    episode_mid: int
    _column_3: int
    _column_4: int
    experience_gain: int
    _column_6: int
    _column_7: int
    _column_8: int
    _column_9: datetime | None
    _column_10: int | None
    _column_11: int | None
    _column_12: int
