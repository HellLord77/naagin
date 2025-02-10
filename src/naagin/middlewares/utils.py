from fastapi import Request
from starlette.routing import Match

from naagin import routers
from naagin.utils import api_router_matches


def should_endec(request: Request) -> bool:
    return api_router_matches(routers.api.router, request.scope)[0] == Match.FULL
