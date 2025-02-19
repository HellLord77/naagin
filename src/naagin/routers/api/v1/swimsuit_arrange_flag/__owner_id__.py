from fastapi import APIRouter

from naagin.models.api import SwimsuitArrangeFlagOwnerIdGetResponseModel
from naagin.schemas import SwimsuitArrangeFlagSchema
from naagin.types.dependencies import DatabaseDependency

router = APIRouter(prefix="/{owner_id}")


@router.get("")
async def get(owner_id: int, database: DatabaseDependency) -> SwimsuitArrangeFlagOwnerIdGetResponseModel:
    swimsuit_arrage_flag_list = await database.find_all(
        SwimsuitArrangeFlagSchema, SwimsuitArrangeFlagSchema.owner_id == owner_id
    )
    return SwimsuitArrangeFlagOwnerIdGetResponseModel(swimsuit_arrage_flag_list=swimsuit_arrage_flag_list)
