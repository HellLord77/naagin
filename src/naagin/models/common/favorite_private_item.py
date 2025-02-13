from naagin.models.base import CustomBaseModel


class FavoritePrivateItemModel(CustomBaseModel):
    girl_mid: int
    type: int
    item_mid: int
