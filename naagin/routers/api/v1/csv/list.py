from fastapi import APIRouter

from naagin.models.json import CSVListModel
from naagin.types_.dependencies.json import CSVListDependency

router = APIRouter(prefix="/list")


@router.get("")
async def get(csv_list: CSVListDependency) -> CSVListModel:
    return csv_list
