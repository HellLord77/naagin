from naagin.models.base import BaseModel
from naagin.models.common import EpisodeModel
from naagin.models.common import OwnerOtherModel


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


class OwnerEpisodeEpisodeMidPostResponseModel(BaseModel):
    episode_result: EpisodeResultModel
    owner_list: list[OwnerOtherModel]
    episode_list: list[EpisodeModel]
