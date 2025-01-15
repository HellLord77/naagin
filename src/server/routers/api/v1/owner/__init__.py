from fastapi import APIRouter

from . import countlogin
from . import episode
from .....models.api import OwnerGetResponseModel
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
