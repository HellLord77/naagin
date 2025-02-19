from fastapi import APIRouter

from naagin.models.api import GirlEquipmentGetResponseModel
from naagin.schemas import GirlEquipmentSchema
from naagin.types.dependencies import DatabaseDependency
from naagin.types.dependencies import OwnerIdDependency

router = APIRouter(prefix="/equipment")


@router.get("")
async def get(database: DatabaseDependency, owner_id: OwnerIdDependency) -> GirlEquipmentGetResponseModel:
    girl_equipment_list = await database.find_all(GirlEquipmentSchema, GirlEquipmentSchema.owner_id == owner_id)
    return GirlEquipmentGetResponseModel(girl_equipment_list=girl_equipment_list)
