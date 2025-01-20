from fastapi import APIRouter
from sqlalchemy import select

from naagin.models.api import HonorGetResponseModel
from naagin.schemas import HonorSchema
from naagin.types.dependencies import OwnerIdDependency
from naagin.types.dependencies import SessionDependency

router = APIRouter(prefix="/honor")


@router.get("")
async def get(
    session: SessionDependency, owner_id: OwnerIdDependency
) -> HonorGetResponseModel:
    honors = (
        await session.scalars(
            select(HonorSchema).where(HonorSchema.owner_id == owner_id)
        )
    ).all()
    return HonorGetResponseModel(honor_list=honors)
