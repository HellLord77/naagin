from naagin.bases import ModelBase
from naagin.models.common import ItemConsumeModel


class SpecialOrderTypeGetResponseModel(ModelBase):
    sp_timestop_item_list: list[ItemConsumeModel] | None = None
    order_ticket_list: list[ItemConsumeModel] | None = None
    pose_card_item_list: list[ItemConsumeModel] | None = None
    sp_fan_item_list: list[ItemConsumeModel] | None = None
    sp_order_item_list: list[ItemConsumeModel] | None = None
