from fastapi import APIRouter

from naagin.models.api import CasinoGameGetResponseModel
from naagin.schemas import CasinoGameSchema
from naagin.types_.dependencies import DatabaseDependency
from naagin.types_.dependencies import OwnerIdDependency

router = APIRouter(prefix="/game")


@router.get("")
async def get(database: DatabaseDependency, owner_id: OwnerIdDependency) -> CasinoGameGetResponseModel:
    casino_game_list = await database.find_all(CasinoGameSchema, CasinoGameSchema.owner_id == owner_id)
    return CasinoGameGetResponseModel(casino_game_list=casino_game_list)
