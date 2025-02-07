from fastapi import APIRouter
from sqlalchemy import select

from naagin.models.api import BromideGetResponseModel
from naagin.schemas import BromideSchema
from naagin.types.dependencies import OwnerIdDependency
from naagin.types.dependencies import SessionDependency

router = APIRouter(prefix="/bromide")


@router.get("")
async def get(session: SessionDependency, owner_id: OwnerIdDependency) -> BromideGetResponseModel:
    bromide_list = (await session.scalars(select(BromideSchema).where(BromideSchema.owner_id == owner_id))).all()
    return BromideGetResponseModel(bromide_list=bromide_list)
