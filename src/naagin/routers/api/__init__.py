from fastapi import Depends

from naagin import injectors
from naagin.classes import CustomAPIRouter

from . import v1

router = CustomAPIRouter(prefix="/api", dependencies=[Depends(injectors.response.add_doaxvv_headers)])

router.include_router(v1.router)
