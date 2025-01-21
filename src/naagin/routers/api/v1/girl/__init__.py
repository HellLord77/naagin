from fastapi import APIRouter
from sqlalchemy import select

from naagin.models.api import GirlGetResponseModel
from naagin.schemas import GirlSchema
from naagin.types.dependencies import OwnerIdDependency
from naagin.types.dependencies import SessionDependency
from . import __girl_mid__
from . import equipment
from . import potential
from . import private

router = APIRouter(prefix="/girl")

router.include_router(__girl_mid__.router)
router.include_router(equipment.router)
router.include_router(potential.router)
router.include_router(private.router)


@router.get("")
async def get(
    session: SessionDependency,
    owner_id: OwnerIdDependency,
) -> GirlGetResponseModel:
    girl_list = (
        await session.scalars(select(GirlSchema).where(GirlSchema.owner_id == owner_id))
    ).all()
    return GirlGetResponseModel(girl_list=girl_list)
