from fastapi import APIRouter

from naagin.models.api import BromideGetResponseModel
from naagin.schemas import BromideSchema
from naagin.types.dependencies import OwnerIdDependency
from naagin.types.dependencies import SessionDependency

router = APIRouter(prefix="/bromide")


@router.get("")
async def get(session: SessionDependency, owner_id: OwnerIdDependency) -> BromideGetResponseModel:
    bromide_list = await session.find_all(BromideSchema, BromideSchema.owner_id == owner_id)
    return BromideGetResponseModel(bromide_list=bromide_list)
