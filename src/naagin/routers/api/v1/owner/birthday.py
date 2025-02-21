from fastapi import APIRouter

from naagin.models.api import OwnerBirthdayPostRequestModel
from naagin.models.api import OwnerBirthdayPostResponseModel
from naagin.schemas import OwnerSchema
from naagin.types.dependencies import DatabaseDependency
from naagin.types.dependencies import OwnerIdDependency

router = APIRouter(prefix="/birthday")


@router.post("")
async def post(
    request: OwnerBirthdayPostRequestModel, database: DatabaseDependency, owner_id: OwnerIdDependency
) -> OwnerBirthdayPostResponseModel:
    owner = await database.get_one(OwnerSchema, owner_id)

    if owner.birthday is None:
        owner.birthday = request.birthday

        await database.flush()

    return OwnerBirthdayPostResponseModel(owner=owner, owner_list=[owner])
