from fastapi import APIRouter

from naagin.enums import ItemEquipmentTypeEnum
from naagin.exceptions import InternalServerErrorException
from naagin.models.api import ItemEquipmentTypeTypeGetResponseModel
from naagin.schemas import ItemEquipmentSchema
from naagin.types.dependencies import DatabaseDependency
from naagin.types.dependencies import OwnerIdDependency

router = APIRouter(prefix="/{type}")


@router.get("")
async def get(
    type: ItemEquipmentTypeEnum, database: DatabaseDependency, owner_id: OwnerIdDependency
) -> ItemEquipmentTypeTypeGetResponseModel:
    if type in {ItemEquipmentTypeEnum.HAIRSTYLE, ItemEquipmentTypeEnum.EXPRESSION}:
        raise InternalServerErrorException

    if type == ItemEquipmentTypeEnum.HAIRSTYLE_OR_EXPRESSION:
        whereclause = (ItemEquipmentSchema.type == ItemEquipmentTypeEnum.HAIRSTYLE) | (
            ItemEquipmentSchema.type == ItemEquipmentTypeEnum.EXPRESSION
        )
    else:
        whereclause = ItemEquipmentSchema.type == type
    item_equipment_list = await database.find_all(
        ItemEquipmentSchema, ItemEquipmentSchema.owner_id == owner_id, whereclause
    )
    return ItemEquipmentTypeTypeGetResponseModel(item_equipment_list=item_equipment_list)
