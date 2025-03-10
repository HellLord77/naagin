from fastapi import APIRouter
from sqlalchemy import func

from naagin.models.api import GiftBoxGetResponseModel
from naagin.schemas import GiftBoxSchema
from naagin.types.dependencies import DatabaseDependency
from naagin.types.dependencies import OwnerIdDependency

from . import count
from . import fetch
from . import history

router = APIRouter(prefix="/giftbox")

router.include_router(count.router)
router.include_router(fetch.router)
router.include_router(history.router)


@router.get("")
async def get(database: DatabaseDependency, owner_id: OwnerIdDependency) -> GiftBoxGetResponseModel:
    giftbox_list = await database.find_all(
        GiftBoxSchema,
        GiftBoxSchema.sender_id.in_((1, owner_id)),
        GiftBoxSchema.expired_at >= func.current_timestamp(),
        GiftBoxSchema.accepted_at == None,  # noqa: E711
    )
    return GiftBoxGetResponseModel(giftbox_list=giftbox_list)
