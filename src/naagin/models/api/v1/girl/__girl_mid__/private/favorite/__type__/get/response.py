from naagin.models.base import CustomBaseModel
from naagin.models.common import FavoritePrivateItemModel


class GirlGirlMidPrivateFavoriteTypeGetResponseModel(CustomBaseModel):
    favorite_private_item_list: list[FavoritePrivateItemModel]
