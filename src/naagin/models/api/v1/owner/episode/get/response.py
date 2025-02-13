from naagin.bases import ModelBase
from naagin.models.common import EpisodeModel


class OwnerEpisodeGetResponseModel(ModelBase):
    episode_list: list[EpisodeModel]
