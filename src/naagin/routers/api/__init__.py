from functools import partial

from fastapi import APIRouter
from fastapi import Depends

from naagin import injectors
from . import v1


def add_api_route(self: APIRouter, *args, **kwargs):
    kwargs["response_model_exclude_defaults"] = True
    APIRouter.add_api_route(self, *args, **kwargs)


router = APIRouter(
    prefix="/api", dependencies=[Depends(injectors.response.add_doaxvv_headers)]
)
router.add_api_route = partial(add_api_route, router)

router.include_router(v1.router)
