from datetime import datetime

from naagin.bases import ModelBase


class EpisodeModel(ModelBase):
    episode_mid: int
    count: int
    created_at: datetime
