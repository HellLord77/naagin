from fastapi import APIRouter


class CustomAPIRouter(APIRouter):
    def add_api_route(self, *args, **kwargs) -> None:
        kwargs["response_model_exclude_defaults"] = True
        super().add_api_route(*args, **kwargs)
