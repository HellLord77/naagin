from naagin.bases import ModelBase
from naagin.models.common import FriendshipModel


class FriendshipReceivedGetResponseModel(ModelBase):
    friendship_list: list[FriendshipModel]
