from fastapi import APIRouter

from naagin.models.api import InformationPutRequestModel
from naagin.models.api import InformationPutResponseModel
from naagin.schemas import InformationReadSchema
from naagin.types.dependencies import DatabaseDependency
from naagin.types.dependencies import OwnerIdDependency

from . import global_

router = APIRouter(prefix="/information")

router.include_router(global_.router)


@router.put("")
async def put(
    request: InformationPutRequestModel, database: DatabaseDependency, owner_id: OwnerIdDependency
) -> InformationPutResponseModel:
    information_read = await database.get(InformationReadSchema, (owner_id, request.information_id))

    if information_read is None:
        information_read = InformationReadSchema(owner_id=owner_id, information_id=request.information_id)
        database.add(information_read)

        await database.flush()

    return InformationPutResponseModel(information_mark_as_read=information_read)
