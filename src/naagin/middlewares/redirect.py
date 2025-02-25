from collections.abc import Iterable
from http import HTTPStatus
from typing import override

from starlette.datastructures import URL
from starlette.datastructures import Headers
from starlette.responses import RedirectResponse
from starlette.types import ASGIApp
from starlette.types import Receive
from starlette.types import Scope
from starlette.types import Send
from ua_parser import parse_user_agent


class RedirectMiddleware:
    @override
    def __init__(self, app: ASGIApp, *, families: Iterable[str] = frozenset(("Chrome", "Firefox", "IE"))) -> None:
        self.app = app
        self.families = families

    async def __call__(self, scope: Scope, receive: Receive, send: Send) -> None:
        headers = Headers(raw=scope["headers"])
        user_agent = headers.get("User-Agent")

        if user_agent is not None:
            ua = parse_user_agent(user_agent)
            if ua is not None:
                for family in self.families:
                    if ua.family == family:
                        url = URL(scope=scope)
                        url = url.replace(path=f"/game{url.path}")

                        response = RedirectResponse(url, HTTPStatus.PERMANENT_REDIRECT)
                        await response(scope, receive, send)
                        return

        await self.app(scope, receive, send)
