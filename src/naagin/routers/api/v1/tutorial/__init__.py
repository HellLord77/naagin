from fastapi import APIRouter
from sqlalchemy import select

from naagin.models.api import TutorialGetResponseModel
from naagin.schemas import TutorialSchema
from naagin.types.dependencies import OwnerIdDependency
from naagin.types.dependencies import SessionDependency
from . import __event_mid__

router = APIRouter(prefix="/tutorial")

router.include_router(__event_mid__.router)


@router.get("")
async def get(
    session: SessionDependency, owner_id: OwnerIdDependency
) -> TutorialGetResponseModel:
    tutorials = (
        await session.scalars(
            select(TutorialSchema).where(TutorialSchema.owner_id == owner_id)
        )
    ).all()
    return TutorialGetResponseModel(tutorial_list=tutorials)
