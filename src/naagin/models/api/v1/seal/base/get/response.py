from naagin.bases import ModelBase


class SealBaseModel(ModelBase):
    girl_mid: int
    main_base_mid: int
    sub_base_mid: int


class SealBaseGetResponseModel(ModelBase):
    seal_base_list: list[SealBaseModel]
