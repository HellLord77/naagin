from fastapi import Depends

from naagin.classes import APIRouter
from naagin.dependencies import add_custom_headers
from naagin.dependencies import check_maintenance

from . import v1

router = APIRouter(prefix="/api", dependencies=[Depends(check_maintenance), Depends(add_custom_headers)])

router.include_router(v1.router)
