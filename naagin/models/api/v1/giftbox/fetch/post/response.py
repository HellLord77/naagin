from naagin.bases import ModelBase
from naagin.models import GiftBoxModel
from naagin.models import OwnerCheckedAtModel


class GiftBoxFetchPostResponseModel(ModelBase):
    giftbox_fetch_list: list[GiftBoxModel]
    owner_checked_at_list: list[OwnerCheckedAtModel] | None = None
