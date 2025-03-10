from starlette.middleware import Middleware
from starlette.types import ASGIApp
from starlette.types import Receive
from starlette.types import Scope
from starlette.types import Send


class RenewedMiddleware:
    def __init__(self, app: ASGIApp, *, middleware: Middleware) -> None:
        self.app = app
        self.middleware = middleware

    async def __call__(self, scope: Scope, receive: Receive, send: Send) -> None:
        app = self.middleware.cls(self.app, *self.middleware.args, **self.middleware.kwargs)
        await app(scope, receive, send)
