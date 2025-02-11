from naagin.models.base import BaseModel
from naagin.models.common import EpisodeModel


class OwnerEpisodeGetResponseModel(BaseModel):
    episode_list: list[EpisodeModel]
