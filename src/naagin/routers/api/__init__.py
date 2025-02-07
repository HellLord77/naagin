from collections.abc import Callable
from functools import partial

from fastapi import APIRouter
from fastapi import Depends

from naagin import injectors

from . import v1


def add_api_route[T, **P](api_router_add_api_route: Callable[P, T], *args: P.args, **kwargs: P.kwargs) -> None:
    kwargs["response_model_exclude_defaults"] = True
    api_router_add_api_route(*args, **kwargs)


router = APIRouter(prefix="/api", dependencies=[Depends(injectors.response.add_doaxvv_headers)])
router.add_api_route = partial(add_api_route, router.add_api_route)

router.include_router(v1.router)
