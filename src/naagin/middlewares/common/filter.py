from re import Pattern

from fastapi import APIRouter
from starlette._utils import get_route_path
from starlette.middleware.base import BaseHTTPMiddleware
from starlette.middleware.base import DispatchFunction
from starlette.middleware.base import RequestResponseEndpoint
from starlette.requests import Request
from starlette.responses import Response
from starlette.types import ASGIApp

from naagin.utils import match_request


class FilterMiddleware(BaseHTTPMiddleware):
    def __init__(
        self,
        app: ASGIApp,
        dispatch: DispatchFunction,
        *,
        prefix: str | None = None,
        pattern: Pattern | None = None,
        router: APIRouter | None = None,
    ) -> None:
        super().__init__(app)
        self.dispatch_func_filter = dispatch

        args = (prefix, pattern, router)
        if args.count(None) != len(args) - 1:
            raise NotImplementedError

        self.prefix = prefix
        self.pattern = pattern
        self.router = router

    async def dispatch(self, request: Request, call_next: RequestResponseEndpoint) -> Response:
        if self.router is None:
            route_path = get_route_path(request.scope)
            if self.prefix is not None:
                matches = self.prefix.startswith(route_path)
            elif self.pattern is not None:
                matches = self.pattern.match(route_path) is not None
            else:
                raise NotImplementedError
        else:
            matches = await match_request(request, self.router)

        if matches:
            response = await self.dispatch_func_filter(request, call_next)
        else:
            response = await call_next(request)
        return response
