from fastapi import APIRouter
from sqlalchemy import select

from . import __event_mid__
from .....models.api import TutorialGetResponseModel
from .....schemas import TutorialSchema
from .....types.dependencies import OwnerIdDependency
from .....types.dependencies import SessionDependency

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
