from naagin.bases import ModelBase
from naagin.models.common import FavoritePrivateItemModel


class GirlGirlMidPrivateFavoriteTypeGetResponseModel(ModelBase):
    favorite_private_item_list: list[FavoritePrivateItemModel]
