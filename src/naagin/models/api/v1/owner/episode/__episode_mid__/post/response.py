from datetime import datetime

from naagin.models.base import BaseModel
from naagin.models.common import OtherOwnerModel


class EpisodeResultEpisodeModel(BaseModel):
    episode_mid: int
    count: int


class EpisodeResultOwnerModel(BaseModel):
    experience_before: int
    experience_gain: int
    experience_after: int
    level_before: int
    level_gain: int
    level_after: int


class EpisodeResultModel(BaseModel):
    episode: EpisodeResultEpisodeModel
    owner: EpisodeResultOwnerModel


class EpisodeModel(BaseModel):
    episode_mid: int
    count: int
    created_at: datetime


class OwnerEpisodeEpisodeMidPostResponseModel(BaseModel):
    episode_result: EpisodeResultModel
    owner_list: list[OtherOwnerModel]
    episode_list: list[EpisodeModel]
