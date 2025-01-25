from fastapi import APIRouter
from fastapi import Depends

from naagin import settings
from naagin.injectors import inject_session_key
from naagin.providers import provide_request_body
from . import v1

dependencies = [Depends(provide_request_body)]
if settings.api.encrypt:
    dependencies.append(Depends(inject_session_key))

router = APIRouter(dependencies=dependencies)

router.include_router(v1.router)
