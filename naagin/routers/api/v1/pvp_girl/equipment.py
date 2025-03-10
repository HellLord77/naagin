from fastapi import APIRouter

from naagin.models.api import PvpGirlEquipmentGetResponseModel
from naagin.schemas import PvpGirlEquipmentSchema
from naagin.types.dependencies import DatabaseDependency
from naagin.types.dependencies import OwnerIdDependency

router = APIRouter(prefix="/equipment")


@router.get("")
async def get(database: DatabaseDependency, owner_id: OwnerIdDependency) -> PvpGirlEquipmentGetResponseModel:
    pvp_girl_equipment_list = await database.find_all(
        PvpGirlEquipmentSchema, PvpGirlEquipmentSchema.owner_id == owner_id
    )
    return PvpGirlEquipmentGetResponseModel(pvp_girl_equipment_list=pvp_girl_equipment_list)
