from naagin.models.base import CustomBaseModel
from naagin.models.common import EpisodeModel
from naagin.models.common import OwnerOtherModel


class EpisodeResultEpisodeModel(CustomBaseModel):
    episode_mid: int
    count: int


class EpisodeResultOwnerModel(CustomBaseModel):
    experience_before: int
    experience_gain: int
    experience_after: int
    level_before: int
    level_gain: int
    level_after: int


class EpisodeResultModel(CustomBaseModel):
    episode: EpisodeResultEpisodeModel
    owner: EpisodeResultOwnerModel


class OwnerEpisodeEpisodeMidPostResponseModel(CustomBaseModel):
    episode_result: EpisodeResultModel
    owner_list: list[OwnerOtherModel]
    episode_list: list[EpisodeModel]
