from starlette.requests import Request
from starlette.types import ASGIApp
from starlette.types import Receive
from starlette.types import Scope
from starlette.types import Send

from naagin.classes import AsyncSession
from naagin.exceptions import UnderMaintenanceNowException
from naagin.providers import provide_maintenance


class MaintenanceMiddleware:
    def __init__(self, app: ASGIApp, *, database: AsyncSession) -> None:
        self.app = app
        self.database = database

    async def __call__(self, scope: Scope, receive: Receive, send: Send) -> None:
        request = Request(scope)
        maintenance = await provide_maintenance(request, self.database)
        if maintenance is not None:
            raise UnderMaintenanceNowException

        await self.app(scope, receive, send)
