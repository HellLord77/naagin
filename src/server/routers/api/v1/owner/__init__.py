from fastapi import APIRouter

from . import countlogin
from . import episode
from .....models.api import OwnerGetResponseModel
from .....models.api import OwnerPutRequestModel
from .....models.api import OwnerPutResponseModel
from .....schemas import OwnerSchema
from .....types.dependencies import OwnerIdDependency
from .....types.dependencies import SessionDependency

router = APIRouter(prefix="/owner")

router.include_router(countlogin.router)
router.include_router(episode.router)


@router.get("")
async def get(
    session: SessionDependency, owner_id: OwnerIdDependency
) -> OwnerGetResponseModel:
    owner = await session.get_one(OwnerSchema, owner_id)
    return OwnerGetResponseModel(owner=owner)


@router.post("")
async def post(
    request: OwnerPutRequestModel,
    session: SessionDependency,
    owner_id: OwnerIdDependency,
) -> OwnerPutResponseModel:
    owner = await session.get_one(OwnerSchema, owner_id)
    if request.name is not None:
        owner.name = request.name
    if request.island_name is not None:
        owner.island_name = request.island_name
    if request.message is not None:
        owner.message = request.message
    success = owner in session.dirty
    await session.flush()
    await session.refresh(owner)
    return OwnerPutResponseModel(success=success, owner_list=[owner])
