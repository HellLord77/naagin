from fastapi import APIRouter

from naagin.models.api import TutorialEventMidPutRequestModel
from naagin.models.api import TutorialEventMidPutResponseModel
from naagin.schemas import TutorialSchema
from naagin.types.dependencies import OwnerIdDependency
from naagin.types.dependencies import SessionDependency

router = APIRouter(prefix="/{event_mid}")


@router.put("")
async def put(
    event_mid: int,
    request: TutorialEventMidPutRequestModel,
    session: SessionDependency,
    owner_id: OwnerIdDependency,
) -> TutorialEventMidPutResponseModel:
    tutorial = await session.get_one(TutorialSchema, (owner_id, event_mid))

    tutorial.flag = request.flag

    await session.flush()
    await session.refresh(tutorial)
    return TutorialEventMidPutResponseModel(tutorial_list=[tutorial])
