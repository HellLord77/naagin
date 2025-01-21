from naagin.models.base import BaseModel
from naagin.models.utils import FavoritePrivateItemModel


class GirlGirlMidPrivateFavoriteTypeGetResponseModel(BaseModel):
    favorite_private_item_list: list[FavoritePrivateItemModel]
