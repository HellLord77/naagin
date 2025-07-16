from fastapi import APIRouter

from naagin.models.api import OptionItemAutoLockPostRequestModel
from naagin.models.api import OptionItemAutoLockPostResponseModel
from naagin.schemas import OptionItemAutoLockSchema
from naagin.types_.dependencies import DatabaseDependency
from naagin.types_.dependencies import OwnerIdDependency

router = APIRouter(prefix="/item_auto_lock")


@router.post("")
async def post(
    request: OptionItemAutoLockPostRequestModel, database: DatabaseDependency, owner_id: OwnerIdDependency
) -> OptionItemAutoLockPostResponseModel:
    option_item_auto_lock = await database.get(OptionItemAutoLockSchema, owner_id)

    if option_item_auto_lock is None:
        option_item_auto_lock = OptionItemAutoLockSchema(owner_id=owner_id)
        database.add(option_item_auto_lock)
    option_item_auto_lock.option_lock_only = bool(request.option_lock_only)
    option_item_auto_lock.option_lock_sr = bool(request.option_lock_sr)
    option_item_auto_lock.option_lock_ssr = bool(request.option_lock_ssr)

    await database.flush()

    return OptionItemAutoLockPostResponseModel(root=[])
