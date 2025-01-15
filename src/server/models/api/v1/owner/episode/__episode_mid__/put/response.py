from datetime import datetime

from .......base import NaaginBaseModel


class EpisodeModel(NaaginBaseModel):
    episode_mid: int
    count: int
    created_at: datetime


class OwnerEpisodeEpisodeMidPutResponseModel(NaaginBaseModel):
    episode_list: list[EpisodeModel]
