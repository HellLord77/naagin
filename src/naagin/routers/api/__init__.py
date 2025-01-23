from fastapi import APIRouter
from fastapi import Depends

from naagin.providers import provide_request_body
from . import v1

router = APIRouter(dependencies=[Depends(provide_request_body)])

router.include_router(v1.router)
