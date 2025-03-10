from datetime import datetime

from naagin.bases import ModelBase


class CustomRoomRequestModel(ModelBase):
    owner_id: int
    request_mid: int
    girl_mid1: int
    girl_mid2: int
    trend_status: int
    created_at: datetime
    updated_at: datetime | None
    started_at: datetime | None
    end_at: datetime | None


class RoomRequestGetResponseModel(ModelBase):
    custom_room_request_list: list[CustomRoomRequestModel]
