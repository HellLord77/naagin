from fastapi import Request
from starlette.routing import Match

from naagin import routers


def should_endec(request: Request) -> bool:
    return any(route.matches(request)[0] == Match.FULL for route in routers.api.router.routes)
