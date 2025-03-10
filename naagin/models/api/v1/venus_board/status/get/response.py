from naagin.bases import ModelBase


class VenusBoardStatusModel(ModelBase):
    girl_mid: int


class VenusBoardStatusGetResponseModel(ModelBase):
    venus_board_status_list: list[VenusBoardStatusModel]
