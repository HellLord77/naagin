from naagin.bases import ModelBase
from naagin.models import OwnerRoomModel


class RoomPostResponseModel(ModelBase):
    owner_room: OwnerRoomModel
