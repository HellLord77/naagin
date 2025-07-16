from fastapi import APIRouter

from naagin.models.api import RoomRequestCancelPostResponseModel
from naagin.schemas import RequestSchema
from naagin.types_.dependencies import DatabaseDependency
from naagin.types_.dependencies import OwnerIdDependency

router = APIRouter(prefix="/cancel")


@router.post("")
async def post(database: DatabaseDependency, owner_id: OwnerIdDependency) -> RoomRequestCancelPostResponseModel:
    request = await database.get_one(RequestSchema, owner_id)

    request.request_mid = 0
    request.girl_mid1 = 0
    request.girl_mid2 = 0
    request.trend_status = False
    request.started_at = None
    request.end_at = None

    await database.flush()
    await database.refresh(request)

    return RoomRequestCancelPostResponseModel(custom_room_request_list=[request])
