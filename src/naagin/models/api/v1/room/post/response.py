from naagin.bases import ModelBase
from naagin.models.common import OwnerRoomModel


class RoomPostResponseModel(ModelBase):
    owner_room: OwnerRoomModel
