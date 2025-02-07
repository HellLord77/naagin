from fastapi import APIRouter

from naagin.models.api import GirlPotentialGetResponseModel
from naagin.schemas import GirlPotentialSchema
from naagin.types.dependencies import OwnerIdDependency
from naagin.types.dependencies import SessionDependency

router = APIRouter(prefix="/potential")


@router.get("")
async def get(session: SessionDependency, owner_id: OwnerIdDependency) -> GirlPotentialGetResponseModel:
    girl_potential_list = await session.get_all(GirlPotentialSchema, GirlPotentialSchema.owner_id == owner_id)
    return GirlPotentialGetResponseModel(girl_potential_list=girl_potential_list)
