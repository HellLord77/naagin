from fastapi import APIRouter
from sqlalchemy import func

from naagin.models.api import GiftBoxHistoryGetResponseModel
from naagin.schemas import GiftBoxSchema
from naagin.types_.dependencies import DatabaseDependency
from naagin.types_.dependencies import OwnerIdDependency

router = APIRouter(prefix="/history")


@router.get("")
async def get(database: DatabaseDependency, owner_id: OwnerIdDependency) -> GiftBoxHistoryGetResponseModel:
    giftbox_history_list = await database.find_all(
        GiftBoxSchema,
        GiftBoxSchema.sender_id.in_((1, owner_id)),
        GiftBoxSchema.expired_at >= func.current_timestamp(),
        GiftBoxSchema.accepted_at != None,  # noqa: E711
    )
    return GiftBoxHistoryGetResponseModel(giftbox_history_list=giftbox_history_list)
