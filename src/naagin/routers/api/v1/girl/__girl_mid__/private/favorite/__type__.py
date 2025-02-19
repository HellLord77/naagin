from fastapi import APIRouter

from naagin.enums import PrivateItemTypeEnum
from naagin.exceptions import InternalServerErrorException
from naagin.models.api import GirlGirlMidPrivateFavoriteTypeGetResponseModel
from naagin.models.api import GirlGirlMidPrivateFavoriteTypePostRequestModel
from naagin.models.api import GirlGirlMidPrivateFavoriteTypePostResponseModel
from naagin.schemas import PrivateItemSchema
from naagin.types.dependencies import DatabaseDependency
from naagin.types.dependencies import OwnerIdDependency

router = APIRouter(prefix="/{type}")


@router.get("")
async def get(
    girl_mid: int, type: PrivateItemTypeEnum, database: DatabaseDependency, owner_id: OwnerIdDependency
) -> GirlGirlMidPrivateFavoriteTypeGetResponseModel:
    favorite_private_item_list = await database.find_all(
        PrivateItemSchema,
        PrivateItemSchema.owner_id == owner_id,
        PrivateItemSchema.girl_mid == girl_mid,
        PrivateItemSchema.type == type,
        PrivateItemSchema.favorite,
    )
    return GirlGirlMidPrivateFavoriteTypeGetResponseModel(favorite_private_item_list=favorite_private_item_list)


@router.post("")
async def post(
    girl_mid: int,
    type: PrivateItemTypeEnum,  # noqa: ARG001
    request: GirlGirlMidPrivateFavoriteTypePostRequestModel,
    database: DatabaseDependency,
    owner_id: OwnerIdDependency,
) -> GirlGirlMidPrivateFavoriteTypePostResponseModel:
    if len(request.item_list) > 1:
        raise InternalServerErrorException

    private_item = await database.get_one(PrivateItemSchema, (owner_id, girl_mid, request.item_list[0].item_mid))

    private_item.favorite = request.item_list[0].is_favorite
    if private_item.favorite:
        favorite_private_item_list = [private_item]
        favorite_delete_private_item_list = []
    else:
        favorite_private_item_list = []
        favorite_delete_private_item_list = [private_item]

    await database.flush()
    await database.refresh(private_item)

    return GirlGirlMidPrivateFavoriteTypePostResponseModel(
        favorite_private_item_list=favorite_private_item_list,
        favorite_delete_private_item_list=favorite_delete_private_item_list,
    )
