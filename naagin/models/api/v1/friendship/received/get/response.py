from naagin.bases import ModelBase
from naagin.models import FriendshipModel


class FriendshipReceivedGetResponseModel(ModelBase):
    friendship_list: list[FriendshipModel]
