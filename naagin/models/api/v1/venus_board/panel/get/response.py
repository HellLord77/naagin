from naagin.bases import ModelBase


class VenusBoardGirlPanelModel(ModelBase):
    content_mid: int
    girl_mid: int
    panel_id: int


class VenusBoardPanelGetResponseModel(ModelBase):
    venus_board_girl_panel_list: list[VenusBoardGirlPanelModel]
