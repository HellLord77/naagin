from naagin.bases import ModelBase
from naagin.models import FriendshipModel


class FriendshipSentGetResponseModel(ModelBase):
    friendship_list: list[FriendshipModel]
