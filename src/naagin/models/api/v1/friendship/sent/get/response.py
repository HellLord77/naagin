from ......base import BaseModel
from ......utils import FriendshipModel


class FriendshipSentGetResponseModel(BaseModel):
    friendship_list: list[FriendshipModel]
