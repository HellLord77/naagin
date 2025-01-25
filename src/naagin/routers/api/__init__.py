from fastapi import APIRouter
from fastapi import Depends

from naagin import injectors
from naagin import settings
from . import v1

dependencies = [
    Depends(injectors.request.inject_decoded_body),
    Depends(injectors.response.inject_doaxvv_headers),
]
if settings.api.encrypt:
    dependencies.append(Depends(injectors.request.inject_session_key))

router = APIRouter(dependencies=dependencies)

router.include_router(v1.router)
