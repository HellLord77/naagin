from naagin.bases import ModelBase
from naagin.models import SwimsuitArrangeFlagModel


class SwimsuitArrangeFlagOwnerIdGetResponseModel(ModelBase):
    swimsuit_arrage_flag_other_list: list[SwimsuitArrangeFlagModel]
