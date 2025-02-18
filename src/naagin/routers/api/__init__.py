from fastapi import Depends

from naagin import injectors
from naagin.classes import APIRouter

from . import v1

router = APIRouter(prefix="/api", dependencies=[Depends(injectors.response.add_custom_headers)])

router.include_router(v1.router)
