from fastapi import APIRouter

from naagin.enums import SpecialOrderTypeEnum
from naagin.exceptions import InternalServerErrorException
from naagin.models.api import SpecialOrderTypeGetResponseModel
from naagin.schemas import SpecialOrderSchema
from naagin.types.dependencies import OwnerIdDependency
from naagin.types.dependencies import SessionDependency

router = APIRouter(prefix="/{type}")


@router.get("")
async def get(
    type: SpecialOrderTypeEnum, session: SessionDependency, owner_id: OwnerIdDependency
) -> SpecialOrderTypeGetResponseModel:
    if type == SpecialOrderTypeEnum._VALUE_81:  # noqa: SLF001
        raise InternalServerErrorException

    if type == SpecialOrderTypeEnum.POSE_CARD_ITEM:
        whereclause = (SpecialOrderSchema.type == SpecialOrderTypeEnum.POSE_CARD_ITEM) | (
            SpecialOrderSchema.type == SpecialOrderTypeEnum._VALUE_81  # noqa: SLF001
        )
    else:
        whereclause = SpecialOrderSchema.type == type
    special_order_list = await session.find_all(
        SpecialOrderSchema, SpecialOrderSchema.owner_id == owner_id, whereclause
    )
    if type == SpecialOrderTypeEnum.SP_TIMESTOP_ITEM:
        return SpecialOrderTypeGetResponseModel(sp_timestop_item_list=special_order_list)
    elif type == SpecialOrderTypeEnum.ORDER_TICKET:
        return SpecialOrderTypeGetResponseModel(order_ticket_list=special_order_list)
    elif type == SpecialOrderTypeEnum.POSE_CARD_ITEM:
        return SpecialOrderTypeGetResponseModel(pose_card_item_list=special_order_list)
    elif type == SpecialOrderTypeEnum.SP_FAN_ITEM:
        return SpecialOrderTypeGetResponseModel(sp_fan_item_list=special_order_list)
    elif type == SpecialOrderTypeEnum.SP_ORDER_ITEM:
        return SpecialOrderTypeGetResponseModel(sp_order_item_list=special_order_list)
    else:
        raise NotImplementedError
