from fastapi import APIRouter
from fastapi import Depends

from . import v1
from ...dependencies import get_owner_id

router = APIRouter(dependencies=[Depends(get_owner_id)])

router.include_router(v1.router)
