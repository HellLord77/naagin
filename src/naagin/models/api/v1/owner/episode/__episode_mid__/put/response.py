from naagin.bases import ModelBase
from naagin.models.common import EpisodeModel


class OwnerEpisodeEpisodeMidPutResponseModel(ModelBase):
    episode_list: list[EpisodeModel]
