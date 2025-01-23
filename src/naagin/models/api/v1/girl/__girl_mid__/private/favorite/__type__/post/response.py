from naagin.models.base import BaseModel
from naagin.models.common import FavoritePrivateItemModel


class GirlGirlMidPrivateFavoriteTypePostResponseModel(BaseModel):
    favorite_private_item_list: list[FavoritePrivateItemModel]
    favorite_delete_private_item_list: list[FavoritePrivateItemModel]
