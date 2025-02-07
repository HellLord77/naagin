from fastapi import APIRouter

from naagin.models.api import DishevelmentGetResponseModel
from naagin.schemas import DishevelmentSchema
from naagin.types.dependencies import OwnerIdDependency
from naagin.types.dependencies import SessionDependency

from . import __owner_id__

router = APIRouter(prefix="/dishevelment")

router.include_router(__owner_id__.router)


@router.get("")
async def get(session: SessionDependency, owner_id: OwnerIdDependency) -> DishevelmentGetResponseModel:
    dishevelment_swimsuit_list = await session.get_all(DishevelmentSchema, DishevelmentSchema.owner_id == owner_id)
    return DishevelmentGetResponseModel(dishevelment_swimsuit_list=dishevelment_swimsuit_list)
