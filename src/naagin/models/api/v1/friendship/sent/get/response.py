from naagin.bases import ModelBase
from naagin.models.common import FriendshipModel


class FriendshipSentGetResponseModel(ModelBase):
    friendship_list: list[FriendshipModel]
