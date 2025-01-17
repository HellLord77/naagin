from naagin.models.base import BaseModel
from naagin.models.utils import FriendshipModel


class FriendshipReceivedGetResponseModel(BaseModel):
    friendship_list: list[FriendshipModel]
