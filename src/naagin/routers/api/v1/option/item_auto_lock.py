from fastapi import APIRouter

from .....models.api import OptionItemAutoLockPostRequestModel
from .....models.api import OptionItemAutoLockPostResponseModel
from .....schemas import OptionItemAutoLockSchema
from .....types.dependencies import OwnerIdDependency
from .....types.dependencies import SessionDependency

router = APIRouter(prefix="/item_auto_lock")


@router.post("")
async def post(
    request: OptionItemAutoLockPostRequestModel,
    session: SessionDependency,
    owner_id: OwnerIdDependency,
) -> OptionItemAutoLockPostResponseModel:
    option_item_auto_lock = await session.get_one(OptionItemAutoLockSchema, owner_id)
    option_item_auto_lock.option_lock_only = request.option_lock_only
    option_item_auto_lock.option_lock_sr = request.option_lock_sr
    option_item_auto_lock.option_lock_ssr = request.option_lock_ssr
    await session.flush()
    return OptionItemAutoLockPostResponseModel(root=[])
