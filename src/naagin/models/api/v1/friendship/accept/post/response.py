from naagin.bases import ModelBase
from naagin.models import FriendshipModel
from naagin.models import OwnerOtherModel


class FriendshipAcceptPostResponseModel(ModelBase):
    friendship_list: list[FriendshipModel]
    owner_list: list[OwnerOtherModel]
