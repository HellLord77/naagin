from naagin.bases import ModelBase
from naagin.models import GiftBoxModel


class GiftBoxGetResponseModel(ModelBase):
    giftbox_list: list[GiftBoxModel]
