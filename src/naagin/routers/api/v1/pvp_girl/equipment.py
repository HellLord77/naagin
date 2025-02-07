from fastapi import APIRouter
from sqlalchemy import select

from naagin.models.api import PvpGirlEquipmentGetResponseModel
from naagin.schemas import PvpGirlEquipmentSchema
from naagin.types.dependencies import OwnerIdDependency
from naagin.types.dependencies import SessionDependency

router = APIRouter(prefix="/equipment")


@router.get("")
async def get(session: SessionDependency, owner_id: OwnerIdDependency) -> PvpGirlEquipmentGetResponseModel:
    pvp_girl_equipment_list = (
        await session.scalars(select(PvpGirlEquipmentSchema).where(PvpGirlEquipmentSchema.owner_id == owner_id))
    ).all()
    return PvpGirlEquipmentGetResponseModel(pvp_girl_equipment_list=pvp_girl_equipment_list)
