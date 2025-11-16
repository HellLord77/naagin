from fastapi import APIRouter
from fastapi import Response
from sqlalchemy import func

from naagin import factories
from naagin.models.api import SteamJaSessionPostRequestModel
from naagin.models.api import SteamJaSessionPostResponseModel
from naagin.schemas import OwnerCountLoginSchema
from naagin.schemas import OwnerSchema
from naagin.schemas import SessionSchema
from naagin.types_.dependencies import DatabaseDependency
from naagin.utils import CustomHeader

router = APIRouter(prefix="/session")


@router.post("")
async def post(
    _: SteamJaSessionPostRequestModel, database: DatabaseDependency, response: Response
) -> SteamJaSessionPostResponseModel:
    owner_id = 6957694
    owner = await database.get(OwnerSchema, owner_id)
    if owner is None:
        owner = OwnerSchema(owner_id=owner_id)
        database.add(owner)

        await database.flush()

    owner = await database.get_one(OwnerSchema, owner_id)
    stamina_checked_at = owner.stamina_checked_at  # noqa: F841
    last_logged_at = owner.last_logged_at.date()
    owner.stamina_checked_at = func.current_timestamp()
    owner.last_logged_at = func.current_timestamp()

    await database.flush()
    await database.refresh(owner)

    owner_count_login = await database.get(OwnerCountLoginSchema, owner_id)
    if owner_count_login is None:
        owner_count_login = OwnerCountLoginSchema(owner_id=owner_id)
        database.add(owner_count_login)
    else:
        today = owner.last_logged_at.date()
        if last_logged_at == today:
            owner_count_login.value += 1
        else:
            owner_count_login.value = 1

    session = await database.get(SessionSchema, owner_id)
    if session is None:
        session = SessionSchema(owner_id=owner_id)
        database.add(session)
    else:
        session.access_token = factories.schema.access_token_factory()
        session.pinksid = factories.schema.pinksid_factory()

    await database.flush()

    CustomHeader.set(response, "Access-Token", session.access_token)
    response.set_cookie("PINKSID", session.pinksid, samesite=None)
    return SteamJaSessionPostResponseModel(auth=True, owner_id=owner.owner_id, owner_status=owner.status)
