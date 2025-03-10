from naagin.bases import ModelBase


class ItemModel(ModelBase):
    is_favorite: int
    item_mid: int


class GirlGirlMidPrivateFavoriteTypePostRequestModel(ModelBase):
    item_list: list[ItemModel]
