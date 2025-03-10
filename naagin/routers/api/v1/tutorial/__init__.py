from fastapi import APIRouter

from naagin.models.api import TutorialGetResponseModel
from naagin.schemas import TutorialSchema
from naagin.types.dependencies import DatabaseDependency
from naagin.types.dependencies import OwnerIdDependency

from . import __event_mid__

router = APIRouter(prefix="/tutorial")

router.include_router(__event_mid__.router)


@router.get("")
async def get(database: DatabaseDependency, owner_id: OwnerIdDependency) -> TutorialGetResponseModel:
    tutorial_list = await database.find_all(TutorialSchema, TutorialSchema.owner_id == owner_id)
    return TutorialGetResponseModel(tutorial_list=tutorial_list)
