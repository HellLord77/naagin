from naagin.bases import ModelBase
from naagin.models import HonorModel
from naagin.models import OwnerCheckedAtModel


class HonorPostResponseModel(ModelBase):
    honor_list: list[HonorModel]
    owner_checked_at_list: list[OwnerCheckedAtModel]
