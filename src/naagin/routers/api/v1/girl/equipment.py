from fastapi import APIRouter

from naagin.models.api import GirlEquipmentGetResponseModel
from naagin.schemas import GirlEquipmentSchema
from naagin.types.dependencies import OwnerIdDependency
from naagin.types.dependencies import SessionDependency

router = APIRouter(prefix="/equipment")


@router.get("")
async def get(session: SessionDependency, owner_id: OwnerIdDependency) -> GirlEquipmentGetResponseModel:
    girl_equipment_list = await session.get_all(GirlEquipmentSchema, GirlEquipmentSchema.owner_id == owner_id)
    return GirlEquipmentGetResponseModel(girl_equipment_list=girl_equipment_list)
