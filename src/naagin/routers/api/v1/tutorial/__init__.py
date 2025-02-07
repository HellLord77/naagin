from fastapi import APIRouter

from naagin.models.api import TutorialGetResponseModel
from naagin.schemas import TutorialSchema
from naagin.types.dependencies import OwnerIdDependency
from naagin.types.dependencies import SessionDependency

from . import __event_mid__

router = APIRouter(prefix="/tutorial")

router.include_router(__event_mid__.router)


@router.get("")
async def get(session: SessionDependency, owner_id: OwnerIdDependency) -> TutorialGetResponseModel:
    tutorial_list = await session.get_all(TutorialSchema, TutorialSchema.owner_id == owner_id)
    return TutorialGetResponseModel(tutorial_list=tutorial_list)
