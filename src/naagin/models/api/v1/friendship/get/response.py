from naagin.bases import ModelBase
from naagin.models.common import FriendshipModel


class FriendshipGetResponseModel(ModelBase):
    friendship_list: list[FriendshipModel]
