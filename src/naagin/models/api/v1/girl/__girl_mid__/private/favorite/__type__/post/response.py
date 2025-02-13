from naagin.models.base import CustomBaseModel
from naagin.models.common import FavoritePrivateItemModel


class GirlGirlMidPrivateFavoriteTypePostResponseModel(CustomBaseModel):
    favorite_private_item_list: list[FavoritePrivateItemModel]
    favorite_delete_private_item_list: list[FavoritePrivateItemModel]
