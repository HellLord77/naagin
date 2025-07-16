from fastapi import APIRouter
from sqlalchemy import func

from naagin.models.api import GiftBoxCountGetResponseModel
from naagin.schemas import GiftBoxSchema
from naagin.types_.dependencies import DatabaseDependency
from naagin.types_.dependencies import OwnerIdDependency

router = APIRouter(prefix="/count")


@router.get("")
async def get(database: DatabaseDependency, owner_id: OwnerIdDependency) -> GiftBoxCountGetResponseModel:
    giftbox_received_count = await database.count(
        GiftBoxSchema,
        GiftBoxSchema.sender_id.in_((1, owner_id)),
        GiftBoxSchema.expired_at >= func.current_timestamp(),
        GiftBoxSchema.accepted_at == None,  # noqa: E711
    )
    return GiftBoxCountGetResponseModel(giftbox_received_count=giftbox_received_count)
