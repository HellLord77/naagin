from fastapi import APIRouter

from naagin.models.api import Pyon2GetResponseModel
from naagin.schemas import Pyon2RunSchema
from naagin.types.dependencies import DatabaseDependency
from naagin.types.dependencies import OwnerIdDependency

router = APIRouter(prefix="/pyon2")


@router.get("")
async def get(database: DatabaseDependency, owner_id: OwnerIdDependency) -> Pyon2GetResponseModel:
    pyon2_run = await database.get(Pyon2RunSchema, owner_id)

    if pyon2_run is None:
        pyon2_run = Pyon2RunSchema(owner_id=owner_id)
        database.add(pyon2_run)

        await database.flush()

    return Pyon2GetResponseModel(pyon2_run_list=[pyon2_run])
