from fastapi import APIRouter
from sqlalchemy import select

from naagin.models.api import GirlEquipmentGetResponseModel
from naagin.schemas import GirlEquipmentSchema
from naagin.types.dependencies import OwnerIdDependency
from naagin.types.dependencies import SessionDependency

router = APIRouter(prefix="/equipment")


@router.get("")
async def get(
    session: SessionDependency,
    owner_id: OwnerIdDependency,
) -> GirlEquipmentGetResponseModel:
    girl_equipment_list = (
        await session.scalars(
            select(GirlEquipmentSchema).where(GirlEquipmentSchema.owner_id == owner_id)
        )
    ).all()
    return GirlEquipmentGetResponseModel(girl_equipment_list=girl_equipment_list)
