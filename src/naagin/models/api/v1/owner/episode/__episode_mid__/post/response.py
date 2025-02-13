from naagin.bases import ModelBase
from naagin.models.common import EpisodeModel
from naagin.models.common import OwnerOtherModel


class EpisodeResultEpisodeModel(ModelBase):
    episode_mid: int
    count: int


class EpisodeResultOwnerModel(ModelBase):
    experience_before: int
    experience_gain: int
    experience_after: int
    level_before: int
    level_gain: int
    level_after: int


class EpisodeResultModel(ModelBase):
    episode: EpisodeResultEpisodeModel
    owner: EpisodeResultOwnerModel


class OwnerEpisodeEpisodeMidPostResponseModel(ModelBase):
    episode_result: EpisodeResultModel
    owner_list: list[OwnerOtherModel]
    episode_list: list[EpisodeModel]
