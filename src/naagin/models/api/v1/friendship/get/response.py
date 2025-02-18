from naagin.bases import ModelBase
from naagin.models import FriendshipModel


class FriendshipGetResponseModel(ModelBase):
    friendship_list: list[FriendshipModel]
