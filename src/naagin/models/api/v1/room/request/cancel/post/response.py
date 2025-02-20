from datetime import datetime

from naagin.bases import ModelBase


class CustomRoomRequestModel(ModelBase):
    owner_id: int
    request_mid: int
    girl_mid1: int
    girl_mid2: int
    trend_status: int
    created_at: datetime
    updated_at: datetime
    started_at: None
    end_at: None


class RoomRequestCancelPostResponseModel(ModelBase):
    custom_room_request_list: list[CustomRoomRequestModel]
