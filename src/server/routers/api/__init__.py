from fastapi import APIRouter
from fastapi import Depends

from . import v1
from ...providers import provide_owner_id

router = APIRouter(dependencies=[Depends(provide_owner_id)])

router.include_router(v1.router)
