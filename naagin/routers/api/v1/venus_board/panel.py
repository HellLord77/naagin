from fastapi import APIRouter

from naagin.models.api import VenusBoardPanelGetResponseModel
from naagin.schemas import VenusBoardGirlPanelSchema
from naagin.types_.dependencies import DatabaseDependency
from naagin.types_.dependencies import OwnerIdDependency

router = APIRouter(prefix="/panel")


@router.get("")
async def get(database: DatabaseDependency, owner_id: OwnerIdDependency) -> VenusBoardPanelGetResponseModel:
    venus_board_girl_panel_list = await database.find_all(
        VenusBoardGirlPanelSchema, VenusBoardGirlPanelSchema.owner_id == owner_id
    )
    return VenusBoardPanelGetResponseModel(venus_board_girl_panel_list=venus_board_girl_panel_list)
