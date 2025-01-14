from fastapi import APIRouter

from .....models.api import OwnerGetResponseModel
from .....schemas import OwnerSchema
from .....types.dependencies import OwnerId
from .....types.dependencies import Session

router = APIRouter(prefix="/owner")


@router.get("")
async def get(session: Session, owner_id: OwnerId) -> OwnerGetResponseModel:
    owner = await session.get(OwnerSchema, owner_id)
    return OwnerGetResponseModel(owner=owner)
