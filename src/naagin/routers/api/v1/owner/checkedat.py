from fastapi import APIRouter

from naagin.models.api import OwnerCheckedAtGetResponseModel
from naagin.schemas import OwnerCheckedAtSchema
from naagin.types.dependencies import OwnerIdDependency
from naagin.types.dependencies import SessionDependency

router = APIRouter(prefix="/checkedat")


@router.get("")
async def get(session: SessionDependency, owner_id: OwnerIdDependency) -> OwnerCheckedAtGetResponseModel:
    owner_checked_at = await session.get(OwnerCheckedAtSchema, owner_id)

    if owner_checked_at is None:
        owner_checked_at = OwnerCheckedAtSchema(owner_id=owner_id)
        session.add(owner_checked_at)

        await session.commit()
        await session.refresh(owner_checked_at)

    return OwnerCheckedAtGetResponseModel(owner_checked_at=owner_checked_at)
