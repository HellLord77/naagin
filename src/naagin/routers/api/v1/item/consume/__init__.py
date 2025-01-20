from fastapi import APIRouter
from sqlalchemy import select

from naagin.models.api import ItemConsumeGetResponseModel
from naagin.schemas import ItemConsumeSchema
from naagin.types.dependencies import OwnerIdDependency
from naagin.types.dependencies import SessionDependency

router = APIRouter(prefix="/consume")


@router.get("")
async def get(
    session: SessionDependency, owner_id: OwnerIdDependency
) -> ItemConsumeGetResponseModel:
    consume_items = (
        await session.scalars(
            select(ItemConsumeSchema).where(ItemConsumeSchema.owner_id == owner_id)
        )
    ).all()
    return ItemConsumeGetResponseModel(item_consume_list=consume_items)
