from naagin.bases import ModelBase
from naagin.models import FriendshipModel
from naagin.models import OwnerOtherModel


class FriendshipFriendIdDeleteResponseModel(ModelBase):
    friendship_list: list[FriendshipModel]
    owner_list: list[OwnerOtherModel] | None = None
