from fastapi import APIRouter
from sqlalchemy import select

from naagin.enums import BooleanEnum
from naagin.enums import PrivateItemTypeEnum
from naagin.exceptions import InternalServerErrorException
from naagin.models.api import GirlGirlMidPrivateFavoriteTypeGetResponseModel
from naagin.models.api import GirlGirlMidPrivateFavoriteTypePostRequestModel
from naagin.models.api import GirlGirlMidPrivateFavoriteTypePostResponseModel
from naagin.schemas import PrivateItemSchema
from naagin.types.dependencies import OwnerIdDependency
from naagin.types.dependencies import SessionDependency

router = APIRouter(prefix="/{type}")


@router.get("")
async def get(
    girl_mid: int,
    type: PrivateItemTypeEnum,
    session: SessionDependency,
    owner_id: OwnerIdDependency,
) -> GirlGirlMidPrivateFavoriteTypeGetResponseModel:
    favorite_private_item_list = (
        await session.scalars(
            select(PrivateItemSchema).where(
                PrivateItemSchema.owner_id == owner_id,
                PrivateItemSchema.girl_mid == girl_mid,
                PrivateItemSchema.type == type,
                PrivateItemSchema.favorite == BooleanEnum.TRUE,
            )
        )
    ).all()
    return GirlGirlMidPrivateFavoriteTypeGetResponseModel(
        favorite_private_item_list=favorite_private_item_list
    )


@router.post("")
async def post(
    girl_mid: int,
    type: PrivateItemTypeEnum,
    request: GirlGirlMidPrivateFavoriteTypePostRequestModel,
    session: SessionDependency,
    owner_id: OwnerIdDependency,
) -> GirlGirlMidPrivateFavoriteTypePostResponseModel:
    if len(request.item_list) > 1:
        raise InternalServerErrorException

    private_item = await session.get_one(
        PrivateItemSchema, owner_id, girl_mid, request.item_list[0].item_mid
    )

    favorite_private_item_list = []
    favorite_delete_private_item_list = []
    private_item.favorite = request.item_list[0].is_favorite
    if private_item.favorite == BooleanEnum.TRUE:
        favorite_private_item_list.append(private_item)
    else:
        favorite_delete_private_item_list.append(private_item)

    await session.flush()
    await session.refresh(private_item)
    return GirlGirlMidPrivateFavoriteTypeGetResponseModel(
        favorite_private_item_list=favorite_private_item_list,
        favorite_delete_private_item_list=favorite_delete_private_item_list,
    )
