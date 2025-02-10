from fastapi import APIRouter

from naagin.models.api import SwimsuitArrangeFlagOwnerIdGetResponseModel
from naagin.schemas import SwimsuitArrangeFlagSchema
from naagin.types.dependencies import SessionDependency

router = APIRouter(prefix="/{owner_id}")


@router.get("")
async def get(owner_id: int, session: SessionDependency) -> SwimsuitArrangeFlagOwnerIdGetResponseModel:
    swimsuit_arrage_flag_list = await session.find_all(
        SwimsuitArrangeFlagSchema, SwimsuitArrangeFlagSchema.owner_id == owner_id
    )
    return SwimsuitArrangeFlagOwnerIdGetResponseModel(swimsuit_arrage_flag_list=swimsuit_arrage_flag_list)
