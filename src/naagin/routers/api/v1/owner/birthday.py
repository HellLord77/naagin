from datetime import UTC
from datetime import datetime

from fastapi import APIRouter

from naagin.models.api import OwnerBirthdayPostRequestModel
from naagin.models.api import OwnerBirthdayPostResponseModel
from naagin.schemas import OwnerSchema
from naagin.types.dependencies import OwnerIdDependency
from naagin.types.dependencies import SessionDependency

router = APIRouter(prefix="/birthday")


@router.post("")
async def post(
    request: OwnerBirthdayPostRequestModel, session: SessionDependency, owner_id: OwnerIdDependency
) -> OwnerBirthdayPostResponseModel:
    owner = await session.get_one(OwnerSchema, owner_id)

    if owner.birthday is None:
        owner.birthday = datetime.strptime(request.birthday, "%Y%m%d").replace(tzinfo=UTC).date()

    await session.flush()
    await session.refresh(owner)
    return OwnerBirthdayPostResponseModel(owner=owner, owner_list=[owner])
