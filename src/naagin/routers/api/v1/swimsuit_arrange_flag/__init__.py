from fastapi import APIRouter

from naagin.models.api import SwimsuitArrangeFlagGetResponseModel
from naagin.schemas import SwimsuitArrangeFlagSchema
from naagin.types.dependencies import OwnerIdDependency
from naagin.types.dependencies import SessionDependency

from . import __owner_id__

router = APIRouter(prefix="/swimsuit_arrange_flag")

router.include_router(__owner_id__.router)


@router.get("")
async def get(session: SessionDependency, owner_id: OwnerIdDependency) -> SwimsuitArrangeFlagGetResponseModel:
    swimsuit_arrage_flag_list = await session.get_all(
        SwimsuitArrangeFlagSchema, SwimsuitArrangeFlagSchema.owner_id == owner_id
    )
    return SwimsuitArrangeFlagGetResponseModel(swimsuit_arrage_flag_list=swimsuit_arrage_flag_list)
