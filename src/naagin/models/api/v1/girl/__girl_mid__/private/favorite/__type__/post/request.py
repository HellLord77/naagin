from naagin.models.base import BaseModel


class ItemModel(BaseModel):
    is_favorite: int
    item_mid: int


class GirlGirlMidPrivateFavoriteTypePostRequestModel(BaseModel):
    item_list: list[ItemModel]
