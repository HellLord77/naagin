from .....base import BaseModel
from .....utils import FriendshipModel


class FriendshipGetResponseModel(BaseModel):
    friendship_list: list[FriendshipModel]
