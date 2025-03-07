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
        last_today = photo_shoot.last_today
        photo_shoot.last_today = func.current_date()

        await database.flush()
        await database.refresh(photo_shoot)

        today = photo_shoot.last_today
        if last_today != today:
            photo_shoot.shoot = False
            photo_shoot.recover = False

            await database.flush()

    return PhotoShootTodayCountGetResponseModel(
        photo_shoot_today_count=int(photo_shoot.shoot), photo_recover_today_count=int(photo_shoot.recover)
    )
