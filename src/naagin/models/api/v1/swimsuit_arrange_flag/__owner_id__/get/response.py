from naagin.models.base import CustomBaseModel
from naagin.models.common import SwimsuitArrangeFlagModel


class SwimsuitArrangeFlagOwnerIdGetResponseModel(CustomBaseModel):
    swimsuit_arrage_flag_other_list: list[SwimsuitArrangeFlagModel]
