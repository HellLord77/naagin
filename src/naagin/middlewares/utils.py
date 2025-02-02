from fastapi import Request
from starlette.routing import Match

from naagin import routers


def should_endec(request: Request) -> bool:
    for route in routers.api.router.routes:
        if route.matches(request)[0] == Match.FULL:
            return True
    return False
