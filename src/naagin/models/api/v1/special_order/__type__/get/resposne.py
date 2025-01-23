from typing import Optional

from naagin.models.base import BaseModel
from naagin.models.common import ItemConsumeModel


class SpecialOrderTypeGetResponseModel(BaseModel):
    sp_timestop_item_list: Optional[list[ItemConsumeModel]] = None
    order_ticket_list: Optional[list[ItemConsumeModel]] = None
    pose_card_item_list: Optional[list[ItemConsumeModel]] = None
    sp_fan_item_list: Optional[list[ItemConsumeModel]] = None
    sp_order_item_list: Optional[list[ItemConsumeModel]] = None
