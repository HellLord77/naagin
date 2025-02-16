from re import Pattern
from typing import override

from fastapi import APIRouter
from starlette.middleware.base import BaseHTTPMiddleware
from starlette.middleware.base import DispatchFunction
from starlette.middleware.base import RequestResponseEndpoint
from starlette.requests import Request
from starlette.responses import Response
from starlette.types import ASGIApp

from naagin.utils import match_request


class FilteredMiddleware(BaseHTTPMiddleware):
    @override
    def __init__(
        self,
        app: ASGIApp,
        *,
        dispatch: DispatchFunction,
        prefix: str | None = None,
        suffix: str | None = None,
        pattern: Pattern | None = None,
        router: APIRouter | None = None,
    ) -> None:
        super().__init__(app)
        self.dispatch_func_filter = dispatch

        args = (prefix, suffix, pattern, router)
        if args.count(None) != len(args) - 1:
            raise NotImplementedError

        self.prefix = prefix
        self.suffix = suffix
        self.pattern = pattern
        self.router = router

    @override
    async def dispatch(self, request: Request, call_next: RequestResponseEndpoint) -> Response:
        if await match_request(request, self.prefix, self.suffix, self.pattern, self.router):
            return await self.dispatch_func_filter(request, call_next)
        else:
            return await call_next(request)
