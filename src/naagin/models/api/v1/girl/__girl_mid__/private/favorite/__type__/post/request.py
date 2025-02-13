from naagin.models.base import CustomBaseModel


class ItemModel(CustomBaseModel):
    is_favorite: int
    item_mid: int


class GirlGirlMidPrivateFavoriteTypePostRequestModel(CustomBaseModel):
    item_list: list[ItemModel]
