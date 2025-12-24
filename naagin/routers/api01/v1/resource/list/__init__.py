from fastapi import APIRouter

from naagin.models.json import ResourceFileListModel
from naagin.types_.dependencies.json import ResourceListDependency

from . import encrypt

router = APIRouter(prefix="/list")

router.include_router(encrypt.router)


@router.get("")
async def get(resource_list: ResourceListDependency) -> ResourceFileListModel:
    return resource_list
