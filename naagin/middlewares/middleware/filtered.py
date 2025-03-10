from collections.abc import Callable

from starlette.middleware import Middleware
from starlette.types import ASGIApp
from starlette.types import Receive
from starlette.types import Scope
from starlette.types import Send


class FilteredMiddleware:
    def __init__(self, app: ASGIApp, *, middleware: Middleware, filter: Callable[[Scope], bool] | None = None) -> None:
        self.app = app
        self.middleware = middleware.cls(app, *middleware.args, **middleware.kwargs)
        self.filter_func = self.filter if filter is None else filter

    async def __call__(self, scope: Scope, receive: Receive, send: Send) -> None:
        app = self.app
        if self.filter_func(scope):
            app = self.middleware
        await app(scope, receive, send)

    def filter(self, scope: Scope) -> bool:
        raise NotImplementedError
