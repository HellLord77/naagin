from naagin.models.base import BaseModel


class PrivateItemModel(BaseModel):
    girl_mid: int
    item_mid: int


class GirlPrivateGetResponseModel(BaseModel):
    private_item_list: list[PrivateItemModel]
