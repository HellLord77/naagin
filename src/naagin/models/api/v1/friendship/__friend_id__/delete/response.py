from naagin.models.base import CustomBaseModel
from naagin.models.common import FriendshipModel
from naagin.models.common import OwnerOtherModel


class FriendshipFriendIdDeleteResponseModel(CustomBaseModel):
    friendship_list: list[FriendshipModel]
    owner_list: list[OwnerOtherModel] | None = None
