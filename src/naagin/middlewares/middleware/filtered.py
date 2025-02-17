from re import Pattern

from fastapi import APIRouter
from fastapi.middleware import Middleware
from starlette._utils import get_route_path
from starlette.routing import Match
from starlette.types import ASGIApp
from starlette.types import Receive
from starlette.types import Scope
from starlette.types import Send

from naagin.utils import router_matches


class FilteredMiddleware:
    def __init__(
        self,
        app: ASGIApp,
        *,
        middleware: Middleware,
        prefix: str | None = None,
        pattern: Pattern | None = None,
        router: APIRouter | None = None,
    ) -> None:
        self.app = app
        self.middleware = middleware.cls(app, *middleware.args, **middleware.kwargs)

        args = (prefix, pattern, router)
        if args.count(None) != len(args) - 1:
            raise NotImplementedError

        self.prefix = prefix
        self.pattern = pattern
        self.router = router

    async def __call__(self, scope: Scope, receive: Receive, send: Send) -> None:
        app = self.app
        if scope["type"] == "http":
            if self.router is None:
                route_path = get_route_path(scope)
                if self.prefix is not None:
                    match = route_path.startswith(self.prefix)
                elif self.pattern is not None:
                    match = self.pattern.match(route_path) is not None
                else:
                    raise NotImplementedError
            else:
                match = router_matches(self.router, scope)[0] == Match.FULL

            if match:
                app = self.middleware
        await app(scope, receive, send)
