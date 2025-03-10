from fastapi import APIRouter
from sqlalchemy import func

from naagin.models.api import PhotoShootTodayCountGetResponseModel
from naagin.schemas import PhotoShootSchema
from naagin.types.dependencies import DatabaseDependency
from naagin.types.dependencies import OwnerIdDependency

router = APIRouter(prefix="/today_count")


@router.get("")
async def get(database: DatabaseDependency, owner_id: OwnerIdDependency) -> PhotoShootTodayCountGetResponseModel:
    photo_shoot = await database.get(PhotoShootSchema, owner_id)

    if photo_shoot is None:
        photo_shoot = PhotoShootSchema(owner_id=owner_id)
        database.add(photo_shoot)

        await database.flush()
    else:
        today = photo_shoot.today
        photo_shoot.today = func.current_datetime()

        await database.flush()
        await database.refresh(photo_shoot)

        if today != photo_shoot.today:
            photo_shoot.shoot_count = 0
            photo_shoot.recover_count = 0

            await database.flush()

    return PhotoShootTodayCountGetResponseModel(
        photo_shoot_today_count=int(photo_shoot.shoot_count), photo_recover_today_count=int(photo_shoot.recover_count)
    )
