from fastapi import APIRouter

from naagin.models.api import CasinoChipGetResponseModel
from naagin.schemas import CasinoChipSchema
from naagin.types_.dependencies import DatabaseDependency
from naagin.types_.dependencies import OwnerIdDependency

router = APIRouter(prefix="/chip")


@router.get("")
async def get(database: DatabaseDependency, owner_id: OwnerIdDependency) -> CasinoChipGetResponseModel:
    casino_chip = await database.get(CasinoChipSchema, owner_id)

    if casino_chip is None:
        casino_chip = CasinoChipSchema(owner_id=owner_id)
        database.add(casino_chip)

        await database.flush()
        await database.refresh(casino_chip)

    return CasinoChipGetResponseModel(casino_chip=casino_chip)
