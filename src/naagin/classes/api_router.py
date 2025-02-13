from typing import override

from fastapi import APIRouter


class CustomAPIRouter(APIRouter):
    @override
    def add_api_route(
        self,
        *args,  # noqa:ANN002
        **kwargs,  # noqa:ANN003
    ) -> None:
        kwargs["response_model_exclude_defaults"] = True
        super().add_api_route(*args, **kwargs)
