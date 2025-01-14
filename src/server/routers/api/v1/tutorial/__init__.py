from fastapi import APIRouter
from sqlalchemy import select

from .....models.api import TutorialGetResponseModel
from .....schemas import TutorialSchema
from .....types.dependencies import OwnerId
from .....types.dependencies import Session

router = APIRouter(prefix="/tutorial")


@router.get("")
async def get(session: Session, owner_id: OwnerId) -> TutorialGetResponseModel:
    tutorials = (
        await session.scalars(
            select(TutorialSchema).where(TutorialSchema.owner_id == owner_id)
        )
    ).all()
    return TutorialGetResponseModel(tutorial_list=tutorials)
