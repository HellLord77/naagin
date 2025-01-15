from fastapi import APIRouter
from sqlalchemy import update

from .....models.api import TutorialEventMidPutRequestModel
from .....models.api import TutorialEventMidPutResponseModel
from .....schemas import TutorialSchema
from .....types.dependencies import OwnerId
from .....types.dependencies import Session

router = APIRouter(prefix="/{event_mid}")


@router.put("")
async def put(
    event_mid: int,
    request: TutorialEventMidPutRequestModel,
    session: Session,
    owner_id: OwnerId,
) -> TutorialEventMidPutResponseModel:
    tutorial = await session.scalar(
        update(TutorialSchema)
        .where(
            TutorialSchema.owner_id == owner_id, TutorialSchema.event_mid == event_mid
        )
        .values(flag=request.flag)
        .returning(TutorialSchema)
    )
    return TutorialEventMidPutResponseModel(tutorial_list=[tutorial])
