from datetime import datetime

from fastapi import APIRouter

from .....models.api import OwnerBirthdayPostRequestModel
from .....models.api import OwnerBirthdayPostResponseModel
from .....schemas import OwnerSchema
from .....types.dependencies import OwnerIdDependency
from .....types.dependencies import SessionDependency

router = APIRouter(prefix="/birthday")


@router.post("")
async def post(
    request: OwnerBirthdayPostRequestModel,
    session: SessionDependency,
    owner_id: OwnerIdDependency,
) -> OwnerBirthdayPostResponseModel:
    owner = await session.get_one(OwnerSchema, owner_id)
    birthday = datetime.strptime(request.birthday, "%Y%m%d").date()
    if owner.birthday is None:
        owner.birthday = birthday
    await session.flush()
    await session.refresh(owner)
    return OwnerBirthdayPostResponseModel(owner=owner, owner_list=[owner])
