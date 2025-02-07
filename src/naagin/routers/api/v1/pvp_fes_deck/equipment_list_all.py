from fastapi import APIRouter

from naagin.models.api import PvpFesDeckEquipmentListAllGetResponseModel

router = APIRouter(prefix="/equipment_list_all")


@router.get("")
async def get() -> PvpFesDeckEquipmentListAllGetResponseModel:
    return PvpFesDeckEquipmentListAllGetResponseModel(pvp_fes_deck_girl_equipment_full_list=[])
