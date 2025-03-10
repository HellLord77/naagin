from naagin.bases import ModelBase


class CustomRoomRequestLogModel(ModelBase):
    request_mid: int
    clear_rank: int


class RoomRequestListGetResponseModel(ModelBase):
    custom_room_request_log_list: list[CustomRoomRequestLogModel]
