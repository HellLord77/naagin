from fastapi import APIRouter

from naagin.models.api import GirlGetResponseModel
from naagin.schemas import GirlSchema
from naagin.types_.dependencies import DatabaseDependency
from naagin.types_.dependencies import OwnerIdDependency

from . import __girl_mid__
from . import equipment
from . import head
from . import potential
from . import private
from . import ywrk_skill

router = APIRouter(prefix="/girl")

router.include_router(__girl_mid__.router)
router.include_router(equipment.router)
router.include_router(head.router)
router.include_router(potential.router)
router.include_router(private.router)
router.include_router(ywrk_skill.router)


@router.get("")
async def get(database: DatabaseDependency, owner_id: OwnerIdDependency) -> GirlGetResponseModel:
    girl_list = await database.find_all(GirlSchema, GirlSchema.owner_id == owner_id)
    return GirlGetResponseModel(girl_list=girl_list)
