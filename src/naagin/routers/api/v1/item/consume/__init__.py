from fastapi import APIRouter

from naagin.models.api import ItemConsumeGetResponseModel
from naagin.schemas import ItemConsumeSchema
from naagin.types.dependencies import OwnerIdDependency
from naagin.types.dependencies import SessionDependency

from . import negative

router = APIRouter(prefix="/consume")

router.include_router(negative.router)


@router.get("")
async def get(session: SessionDependency, owner_id: OwnerIdDependency) -> ItemConsumeGetResponseModel:
    item_consume_list = await session.get_all(ItemConsumeSchema, ItemConsumeSchema.owner_id == owner_id)
    return ItemConsumeGetResponseModel(item_consume_list=item_consume_list)
