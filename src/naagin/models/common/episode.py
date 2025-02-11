from datetime import datetime

from naagin.models.base import BaseModel


class EpisodeModel(BaseModel):
    episode_mid: int
    count: int
    created_at: datetime
