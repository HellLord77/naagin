from fastapi import Depends

from naagin import injectors
from naagin.utils import ResponseModelExcludeDefaultsAPIRouter
from . import v1

router = ResponseModelExcludeDefaultsAPIRouter(
    prefix="/api", dependencies=[Depends(injectors.response.add_doaxvv_headers)]
)

router.include_router(v1.router)
