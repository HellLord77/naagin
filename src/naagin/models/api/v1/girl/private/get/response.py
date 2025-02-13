from naagin.models.base import CustomBaseModel


class PrivateItemModel(CustomBaseModel):
    girl_mid: int
    item_mid: int


class GirlPrivateGetResponseModel(CustomBaseModel):
    private_item_list: list[PrivateItemModel]
