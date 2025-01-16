from fastapi import APIRouter
from sqlalchemy import select

from naagin.models.api import GirlGetResponseModel
from naagin.schemas import GirlSchema
from naagin.types.dependencies import OwnerIdDependency
from naagin.types.dependencies import SessionDependency

router = APIRouter(prefix="/girl")


@router.get("")
async def get(
    session: SessionDependency,
    owner_id: OwnerIdDependency,
) -> GirlGetResponseModel:
    girls = (
        await session.scalars(select(GirlSchema).where(GirlSchema.owner_id == owner_id))
    ).all()
    return GirlGetResponseModel(girl_list=girls)
