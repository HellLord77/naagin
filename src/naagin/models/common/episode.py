from datetime import datetime

from naagin.models.base import CustomBaseModel


class EpisodeModel(CustomBaseModel):
    episode_mid: int
    count: int
    created_at: datetime
