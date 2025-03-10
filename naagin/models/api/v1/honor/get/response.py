from naagin.bases import ModelBase
from naagin.models import HonorModel


class HonorGetResponseModel(ModelBase):
    honor_list: list[HonorModel]
