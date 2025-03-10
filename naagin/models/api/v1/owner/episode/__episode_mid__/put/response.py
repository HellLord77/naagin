from naagin.bases import ModelBase
from naagin.models import EpisodeModel


class OwnerEpisodeEpisodeMidPutResponseModel(ModelBase):
    episode_list: list[EpisodeModel]
