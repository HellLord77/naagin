from naagin.models.base import CustomBaseModel
from naagin.models.common import EpisodeModel


class OwnerEpisodeGetResponseModel(CustomBaseModel):
    episode_list: list[EpisodeModel]
