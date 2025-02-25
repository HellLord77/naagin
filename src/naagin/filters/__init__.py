from http import HTTPMethod

from fastapi.datastructures import Headers
from starlette._utils import get_route_path
from starlette.types import Scope

from naagin import settings


def gzip_filter(scope: Scope) -> bool:
    headers = Headers(raw=scope.get("headers", []))
    return "Range" not in headers


def redirect_filter(scope: Scope) -> bool:
    if scope["type"] != "http":
        return False

    if scope["method"] not in {HTTPMethod.GET, HTTPMethod.HEAD}:
        return False

    headers = Headers(raw=scope["headers"])
    if headers.get("User-Agent") == settings.app.user_agent:
        return False

    route_path = get_route_path(scope)
    return not route_path.startswith("/game/")


def encoding_filter(scope: Scope) -> bool:
    if scope["type"] != "http":
        return False

    route_path = get_route_path(scope)
    return route_path.startswith("/api/") and not route_path.startswith("/api/v1/session")
