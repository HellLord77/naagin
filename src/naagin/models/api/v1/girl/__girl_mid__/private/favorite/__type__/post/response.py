from naagin.bases import ModelBase
from naagin.models.common import FavoritePrivateItemModel


class GirlGirlMidPrivateFavoriteTypePostResponseModel(ModelBase):
    favorite_private_item_list: list[FavoritePrivateItemModel]
    favorite_delete_private_item_list: list[FavoritePrivateItemModel]
