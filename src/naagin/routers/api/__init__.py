from fastapi import APIRouter
from fastapi import Depends

from naagin.providers import provide_owner_id
from . import v1

router = APIRouter(dependencies=[Depends(provide_owner_id)])

router.include_router(v1.router)
