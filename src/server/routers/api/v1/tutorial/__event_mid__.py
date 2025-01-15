from fastapi import APIRouter
from sqlalchemy import select
from sqlalchemy import update

from .....models.api import TutorialEventMidPutRequestModel
from .....models.api import TutorialEventMidPutResponseModel
from .....schemas import TutorialSchema
from .....types.dependencies import OwnerId
from .....types.dependencies import Session

router = APIRouter()


@router.put("/{event_mid}")
async def put(
    event_mid: int,
    tutorial_event_mid: TutorialEventMidPutRequestModel,
    session: Session,
    owner_id: OwnerId,
) -> TutorialEventMidPutResponseModel:
    await session.execute(
        update(TutorialSchema)
        .where(
            TutorialSchema.owner_id == owner_id, TutorialSchema.event_mid == event_mid
        )
        .values(flag=tutorial_event_mid.flag)
    )
    tutorial = await session.scalar(
        select(TutorialSchema).where(
            TutorialSchema.owner_id == owner_id, TutorialSchema.event_mid == event_mid
        )
    )
    return TutorialEventMidPutResponseModel(tutorial_list=[tutorial])
