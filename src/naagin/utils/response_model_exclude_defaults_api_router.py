from fastapi.routing import APIRouter


class ResponseModelExcludeDefaultsAPIRouter(APIRouter):
    def add_api_route(self, *args, **kwargs):
        kwargs["response_model_exclude_defaults"] = True
        super().add_api_route(*args, **kwargs)
