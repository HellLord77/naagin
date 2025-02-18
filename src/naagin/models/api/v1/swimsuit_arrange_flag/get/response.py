from naagin.bases import ModelBase
from naagin.models import SwimsuitArrangeFlagModel


class SwimsuitArrangeFlagGetResponseModel(ModelBase):
    swimsuit_arrage_flag_list: list[SwimsuitArrangeFlagModel]
