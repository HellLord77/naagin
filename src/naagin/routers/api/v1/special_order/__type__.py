from fastapi import APIRouter

from naagin.enums import SpecialOrderTypeEnum
from naagin.exceptions import InternalServerErrorException
from naagin.models.api import SpecialOrderTypeGetResponseModel
from naagin.schemas import SpecialOrderSchema
from naagin.types.dependencies import DatabaseDependency
from naagin.types.dependencies import OwnerIdDependency

router = APIRouter(prefix="/{type}")


@router.get("")
async def get(
    type: SpecialOrderTypeEnum, database: DatabaseDependency, owner_id: OwnerIdDependency
) -> SpecialOrderTypeGetResponseModel:
    if type == SpecialOrderTypeEnum._VALUE_81:  # noqa: SLF001
        raise InternalServerErrorException

    if type == SpecialOrderTypeEnum.POSE_CARD_ITEM:
        whereclause = (SpecialOrderSchema.type == SpecialOrderTypeEnum.POSE_CARD_ITEM) | (
            SpecialOrderSchema.type == SpecialOrderTypeEnum._VALUE_81  # noqa: SLF001
        )
    else:
        whereclause = SpecialOrderSchema.type == type
    special_order_list = await database.find_all(
        SpecialOrderSchema, SpecialOrderSchema.owner_id == owner_id, whereclause
    )
    match type:
        case SpecialOrderTypeEnum.SP_TIMESTOP_ITEM:
            return SpecialOrderTypeGetResponseModel(sp_timestop_item_list=special_order_list)
        case SpecialOrderTypeEnum.ORDER_TICKET:
            return SpecialOrderTypeGetResponseModel(order_ticket_list=special_order_list)
        case SpecialOrderTypeEnum.POSE_CARD_ITEM:
            return SpecialOrderTypeGetResponseModel(pose_card_item_list=special_order_list)
        case SpecialOrderTypeEnum.SP_FAN_ITEM:
            return SpecialOrderTypeGetResponseModel(sp_fan_item_list=special_order_list)
        case SpecialOrderTypeEnum.SP_ORDER_ITEM:
            return SpecialOrderTypeGetResponseModel(sp_order_item_list=special_order_list)
        case _:
            raise NotImplementedError
