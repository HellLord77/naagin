from fastapi import APIRouter

from naagin.models.api import GirlPotentialGetResponseModel
from naagin.schemas import GirlPotentialSchema
from naagin.types.dependencies import DatabaseDependency
from naagin.types.dependencies import OwnerIdDependency

router = APIRouter(prefix="/potential")


@router.get("")
async def get(database: DatabaseDependency, owner_id: OwnerIdDependency) -> GirlPotentialGetResponseModel:
    girl_potential_list = await database.find_all(GirlPotentialSchema, GirlPotentialSchema.owner_id == owner_id)
    return GirlPotentialGetResponseModel(girl_potential_list=girl_potential_list)
