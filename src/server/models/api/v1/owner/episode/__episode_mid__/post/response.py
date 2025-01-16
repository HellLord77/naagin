from datetime import datetime

from ......utils import OtherOwnerModel
from .......base import NaaginBaseModel


class EpisodeResultEpisodeModel(NaaginBaseModel):
    episode_mid: int
    count: int


class EpisodeResultOwnerModel(NaaginBaseModel):
    experience_before: int
    experience_gain: int
    experience_after: int
    level_before: int
    level_gain: int
    level_after: int


class EpisodeResultModel(NaaginBaseModel):
    episode: EpisodeResultEpisodeModel
    owner: EpisodeResultOwnerModel


class EpisodeModel(NaaginBaseModel):
    episode_mid: int
    count: int
    created_at: datetime


class OwnerEpisodeEpisodeMidPostResponseModel(NaaginBaseModel):
    episode_result: EpisodeResultModel
    owner_list: list[OtherOwnerModel]
    episode_list: list[EpisodeModel]
