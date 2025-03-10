from fastapi import APIRouter

from naagin.models.api import VenusBoardStatusGetResponseModel
from naagin.schemas import VenusBoardStatusSchema
from naagin.types.dependencies import DatabaseDependency
from naagin.types.dependencies import OwnerIdDependency

router = APIRouter(prefix="/status")


@router.get("")
async def get(database: DatabaseDependency, owner_id: OwnerIdDependency) -> VenusBoardStatusGetResponseModel:
    venus_board_status_list = await database.find_all(
        VenusBoardStatusSchema, VenusBoardStatusSchema.owner_id == owner_id
    )
    return VenusBoardStatusGetResponseModel(venus_board_status_list=venus_board_status_list)
