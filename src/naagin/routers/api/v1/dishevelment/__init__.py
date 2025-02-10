from fastapi import APIRouter

from naagin.models.api import DishevelmentGetResponseModel
from naagin.schemas import DishevelmentSwimsuitSchema
from naagin.types.dependencies import OwnerIdDependency
from naagin.types.dependencies import SessionDependency

from . import __owner_id__

router = APIRouter(prefix="/dishevelment")

router.include_router(__owner_id__.router)


@router.get("")
async def get(session: SessionDependency, owner_id: OwnerIdDependency) -> DishevelmentGetResponseModel:
    dishevelment_swimsuit_list = await session.find_all(
        DishevelmentSwimsuitSchema, DishevelmentSwimsuitSchema.owner_id == owner_id
    )
    return DishevelmentGetResponseModel(dishevelment_swimsuit_list=dishevelment_swimsuit_list)
