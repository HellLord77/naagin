from naagin.bases import ModelBase
from naagin.models.common import FriendshipModel
from naagin.models.common import OwnerOtherModel


class FriendshipFriendIdDeleteResponseModel(ModelBase):
    friendship_list: list[FriendshipModel]
    owner_list: list[OwnerOtherModel] | None = None
