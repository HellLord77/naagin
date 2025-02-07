from fastapi import APIRouter

from naagin.models.api import OwnerGetResponseModel
from naagin.models.api import OwnerPutRequestModel
from naagin.models.api import OwnerPutResponseModel
from naagin.schemas import OwnerSchema
from naagin.types.dependencies import OwnerIdDependency
from naagin.types.dependencies import SessionDependency

from . import birthday
from . import checkedat
from . import countlogin
from . import episode

router = APIRouter(prefix="/owner")

router.include_router(birthday.router)
router.include_router(checkedat.router)
router.include_router(countlogin.router)
router.include_router(episode.router)


@router.get("")
async def get(session: SessionDependency, owner_id: OwnerIdDependency) -> OwnerGetResponseModel:
    owner = await session.get_one(OwnerSchema, owner_id)
    return OwnerGetResponseModel(owner=owner)


@router.post("")
async def post(
    request: OwnerPutRequestModel, session: SessionDependency, owner_id: OwnerIdDependency
) -> OwnerPutResponseModel:
    owner = await session.get_one(OwnerSchema, owner_id)

    success = True
    if request.name is not None:
        owner.name = request.name
    elif request.island_name is not None:
        owner.island_name = request.island_name
    elif request.message is not None:
        owner.message = request.message
    else:
        success = False

    await session.flush()
    await session.refresh(owner)
    return OwnerPutResponseModel(success=success, owner_list=[owner])
