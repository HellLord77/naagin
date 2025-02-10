from fastapi import APIRouter

from naagin.models.api import GirlPrivateGetResponseModel
from naagin.schemas import PrivateItemSchema
from naagin.types.dependencies import OwnerIdDependency
from naagin.types.dependencies import SessionDependency

from . import favorite

router = APIRouter(prefix="/private")

router.include_router(favorite.router)


@router.get("")
async def get(session: SessionDependency, owner_id: OwnerIdDependency) -> GirlPrivateGetResponseModel:
    private_item_list = await session.find_all(PrivateItemSchema, PrivateItemSchema.owner_id == owner_id)
    return GirlPrivateGetResponseModel(private_item_list=private_item_list)
