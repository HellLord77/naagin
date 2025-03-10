from fastapi import APIRouter

from naagin.enums import PrivateItemTypeEnum
from naagin.exceptions import InternalServerErrorException
from naagin.models.api import GirlPrivateFavoriteTypeGetResponseModel
from naagin.schemas import PrivateItemSchema
from naagin.types.dependencies import DatabaseDependency
from naagin.types.dependencies import OwnerIdDependency

router = APIRouter(prefix="/{type}")


@router.get("")
async def get(
    type: PrivateItemTypeEnum, database: DatabaseDependency, owner_id: OwnerIdDependency
) -> GirlPrivateFavoriteTypeGetResponseModel:
    if type == PrivateItemTypeEnum._VALUE_80:  # noqa: SLF001
        raise InternalServerErrorException

    favorite_private_item_list = await database.find_all(
        PrivateItemSchema, PrivateItemSchema.owner_id == owner_id, PrivateItemSchema.type == type
    )
    return GirlPrivateFavoriteTypeGetResponseModel(favorite_private_item_list=favorite_private_item_list)
