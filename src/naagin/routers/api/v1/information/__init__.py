from fastapi import APIRouter

from naagin.models.api import InformationPutRequestModel
from naagin.models.api import InformationPutResponseModel
from naagin.schemas import InformationReadSchema
from naagin.types.dependencies import OwnerIdDependency
from naagin.types.dependencies import SessionDependency

from . import global_

router = APIRouter(prefix="/information")

router.include_router(global_.router)


@router.put("")
async def put(
    request: InformationPutRequestModel, session: SessionDependency, owner_id: OwnerIdDependency
) -> InformationPutResponseModel:
    information_read = await session.get(InformationReadSchema, (owner_id, request.information_id))

    if information_read is None:
        information_read = InformationReadSchema(owner_id=owner_id, information_id=request.information_id)

        session.add(information_read)
        await session.flush()

    return InformationPutResponseModel(information_mark_as_read=information_read)
