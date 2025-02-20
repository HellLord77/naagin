from fastapi import APIRouter

from naagin.models.api import RoomRequestListGetResponseModel
from naagin.schemas import RequestLogSchema
from naagin.types.dependencies import DatabaseDependency
from naagin.types.dependencies import OwnerIdDependency

router = APIRouter(prefix="/list")


@router.get("")
async def get(database: DatabaseDependency, owner_id: OwnerIdDependency) -> RoomRequestListGetResponseModel:
    custom_room_request_log_list = await database.find_all(RequestLogSchema, RequestLogSchema.owner_id == owner_id)
    return RoomRequestListGetResponseModel(custom_room_request_log_list=custom_room_request_log_list)
