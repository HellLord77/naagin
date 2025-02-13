from naagin.bases import ModelBase


class PrivateItemModel(ModelBase):
    girl_mid: int
    item_mid: int


class GirlPrivateGetResponseModel(ModelBase):
    private_item_list: list[PrivateItemModel]
