from fastapi.datastructures import Headers
from starlette._utils import get_route_path
from starlette.types import Scope


def encoding_filter(scope: Scope) -> bool:
    if scope["type"] != "http":
        return False

    route_path = get_route_path(scope)
    return route_path.startswith("/api/") and not route_path.startswith("/api/v1/session")


def gzip_filter(scope: Scope) -> bool:
    headers = Headers(raw=scope.get("headers", []))
    return "Range" not in headers
