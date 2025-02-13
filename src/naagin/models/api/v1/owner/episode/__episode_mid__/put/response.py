from naagin.models.base import CustomBaseModel
from naagin.models.common import EpisodeModel


class OwnerEpisodeEpisodeMidPutResponseModel(CustomBaseModel):
    episode_list: list[EpisodeModel]
