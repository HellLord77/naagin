from fastapi import APIRouter
from fastapi import Depends

from naagin import injectors
from . import v1

router = APIRouter(
    prefix="/api", dependencies=[Depends(injectors.response.inject_doaxvv_headers)]
)

router.include_router(v1.router)
