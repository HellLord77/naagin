from fastapi import APIRouter

from naagin.models.api import TutorialEventMidPutRequestModel
from naagin.models.api import TutorialEventMidPutResponseModel
from naagin.schemas import TutorialSchema
from naagin.types.dependencies import DatabaseDependency
from naagin.types.dependencies import OwnerIdDependency

router = APIRouter(prefix="/{event_mid}")


@router.put("")
async def put(
    event_mid: int, request: TutorialEventMidPutRequestModel, database: DatabaseDependency, owner_id: OwnerIdDependency
) -> TutorialEventMidPutResponseModel:
    tutorial = await database.get(TutorialSchema, (owner_id, event_mid))

    if tutorial is None:
        tutorial = TutorialSchema(owner_id=owner_id, event_mid=event_mid)
        database.add(tutorial)
    tutorial.flag = request.flag

    await database.flush()
    await database.refresh(tutorial)

    return TutorialEventMidPutResponseModel(tutorial_list=[tutorial])
