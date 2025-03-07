from fastapi import APIRouter

from naagin.models.api import PhotoShootShootPostResponseModel
from naagin.schemas import PhotoShootSchema
from naagin.types.dependencies import DatabaseDependency
from naagin.types.dependencies import OwnerIdDependency

router = APIRouter(prefix="/shoot")


@router.post("")
async def post(database: DatabaseDependency, owner_id: OwnerIdDependency) -> PhotoShootShootPostResponseModel:
    photo_shoot = await database.get_one(PhotoShootSchema, owner_id)

    photo_shoot.shoot = True

    await database.flush()

    return PhotoShootShootPostResponseModel(photo_shoot_today_count=1)
