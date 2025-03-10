from naagin.bases import ModelBase
from naagin.models import FavoritePrivateItemModel


class GirlGirlMidPrivateFavoriteTypeGetResponseModel(ModelBase):
    favorite_private_item_list: list[FavoritePrivateItemModel]
