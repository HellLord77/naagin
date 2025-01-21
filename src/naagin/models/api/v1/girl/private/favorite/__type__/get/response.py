from naagin.models.base import BaseModel


class FavoritePrivateItemModel(BaseModel):
    girl_mid: int
    type: int
    item_mid: int


class GirlPrivateFavoriteTypeGetResponseModel(BaseModel):
    favorite_private_item_list: list[FavoritePrivateItemModel]
