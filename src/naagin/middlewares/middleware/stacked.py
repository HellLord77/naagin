from fastapi.middleware import Middleware
from starlette.types import ASGIApp
from starlette.types import Receive
from starlette.types import Scope
from starlette.types import Send


class StackedMiddleware:
    def __init__(self, app: ASGIApp, *middleware: Middleware) -> None:
        for cls, args, kwargs in middleware:
            app = cls(app, *args, **kwargs)
        self.app = app

    async def __call__(self, scope: Scope, receive: Receive, send: Send) -> None:
        await self.app(scope, receive, send)
