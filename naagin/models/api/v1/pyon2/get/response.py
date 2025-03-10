from naagin.bases import ModelBase


class Pyon2RunModel(ModelBase):
    owner_id: int
    girl_mid: int
    stage_mid: int
    lane_id: int
    pos_id: int


class Pyon2GetResponseModel(ModelBase):
    pyon2_run_list: list[Pyon2RunModel]
