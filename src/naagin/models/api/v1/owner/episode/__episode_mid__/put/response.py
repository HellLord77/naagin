from datetime import datetime

from .......base import BaseModel


class EpisodeModel(BaseModel):
    episode_mid: int
    count: int
    created_at: datetime


class OwnerEpisodeEpisodeMidPutResponseModel(BaseModel):
    episode_list: list[EpisodeModel]
