from re import compile

from starlette._utils import get_route_path
from starlette.types import Scope

encoding_pattern = compile(r"^/api/v1/(?!session(?:/|$))")


def encoding_filter(scope: Scope) -> bool:
    if scope["type"] != "http":
        return False

    route_path = get_route_path(scope)
    return encoding_pattern.match(route_path) is not None
