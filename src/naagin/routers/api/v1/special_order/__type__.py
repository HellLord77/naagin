from fastapi import APIRouter
from sqlalchemy import select

from naagin.exceptions import InternalServerErrorException
from naagin.models.api import SpecialOrderTypeGetResponseModel
from naagin.schemas import SpecialOrderSchema
from naagin.types.dependencies import OwnerIdDependency
from naagin.types.dependencies import SessionDependency
from naagin.types.enums import SpecialOrderTypeEnum

router = APIRouter(prefix="/{type}")


@router.get("")
async def get(
    type: SpecialOrderTypeEnum, session: SessionDependency, owner_id: OwnerIdDependency
) -> SpecialOrderTypeGetResponseModel:
    if type == SpecialOrderTypeEnum._VALUE_81:
        raise InternalServerErrorException

    if type == SpecialOrderTypeEnum.POSE_CARD_ITEM:
        whereclause = (
            SpecialOrderSchema.type == SpecialOrderTypeEnum.POSE_CARD_ITEM
        ) | (SpecialOrderSchema.type == SpecialOrderTypeEnum._VALUE_81)
    else:
        whereclause = SpecialOrderSchema.type == type
    special_order_list = (
        await session.scalars(
            select(SpecialOrderSchema).where(
                SpecialOrderSchema.owner_id == owner_id, whereclause
            )
        )
    ).all()
    response = SpecialOrderTypeGetResponseModel()
    if type == SpecialOrderTypeEnum.SP_TIMESTOP_ITEM:
        response.sp_timestop_item_list = special_order_list
    elif type == SpecialOrderTypeEnum.ORDER_TICKET:
        response.order_ticket_list = special_order_list
    elif type == SpecialOrderTypeEnum.POSE_CARD_ITEM:
        response.pose_card_item_list = special_order_list
    elif type == SpecialOrderTypeEnum.SP_FAN_ITEM:
        response.sp_fan_item_list = special_order_list
    elif type == SpecialOrderTypeEnum.SP_ORDER_ITEM:
        response.sp_order_item_list = special_order_list
    return response
