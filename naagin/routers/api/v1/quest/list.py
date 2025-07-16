from fastapi import APIRouter

from naagin.models.api import QuestListGetResponseModel
from naagin.schemas import QuestSchema
from naagin.types_.dependencies import DatabaseDependency
from naagin.types_.dependencies import OwnerIdDependency

router = APIRouter(prefix="/list")


@router.get("")
async def get(database: DatabaseDependency, owner_id: OwnerIdDependency) -> QuestListGetResponseModel:
    quest_list = await database.find_all(QuestSchema, QuestSchema.owner_id == owner_id)
    return QuestListGetResponseModel(quest_list=quest_list, auto_fes_attempts=0)
