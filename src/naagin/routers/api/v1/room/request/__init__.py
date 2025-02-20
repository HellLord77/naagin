from fastapi import APIRouter

from naagin.models.api import RoomRequestGetResponseModel
from naagin.schemas import RequestSchema
from naagin.types.dependencies import DatabaseDependency
from naagin.types.dependencies import OwnerIdDependency

from . import list

router = APIRouter(prefix="/request")

router.include_router(list.router)


@router.get("")
async def get(database: DatabaseDependency, owner_id: OwnerIdDependency) -> RoomRequestGetResponseModel:
    request = await database.get(RequestSchema, owner_id)

    if request is None:
        request = RequestSchema(owner_id=owner_id)
        database.add(request)

        await database.flush()
        await database.refresh(request)

    return RoomRequestGetResponseModel(custom_room_request_list=[request])
