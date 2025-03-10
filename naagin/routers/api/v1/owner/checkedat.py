from fastapi import APIRouter

from naagin.models.api import OwnerCheckedAtGetResponseModel
from naagin.schemas import OwnerCheckedAtSchema
from naagin.types.dependencies import DatabaseDependency
from naagin.types.dependencies import OwnerIdDependency

router = APIRouter(prefix="/checkedat")


@router.get("")
async def get(database: DatabaseDependency, owner_id: OwnerIdDependency) -> OwnerCheckedAtGetResponseModel:
    owner_checked_at = await database.get(OwnerCheckedAtSchema, owner_id)

    if owner_checked_at is None:
        owner_checked_at = OwnerCheckedAtSchema(owner_id=owner_id)
        database.add(owner_checked_at)

        await database.flush()
        await database.refresh(owner_checked_at)

    return OwnerCheckedAtGetResponseModel(owner_checked_at=owner_checked_at)
