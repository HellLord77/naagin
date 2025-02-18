from naagin.bases import ModelBase
from naagin.models import ItemConsumeModel


class ItemConsumeGetResponseModel(ModelBase):
    item_consume_list: list[ItemConsumeModel]
