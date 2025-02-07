from collections.abc import Callable

from fastapi import APIRouter


class APIRouter(APIRouter):
    def add_api_route[T, **P](
        self, *args: P.args, _: Callable[P, T] = APIRouter.add_api_route, **kwargs: P.kwargs
    ) -> T:
        kwargs["response_model_exclude_defaults"] = True
        return super().add_api_route(*args, **kwargs)
