from http import HTTPStatus
from time import time
from typing import Callable

from fastapi import Depends
from fastapi import FastAPI
from fastapi import Request
from fastapi import Response

from naagin import routers
from naagin import settings
from naagin.injectors import inject_session_key
from naagin.middlewares import AESMiddleware
from naagin.middlewares import DeflateMiddleware
from naagin.utils import response_set_doaxvv_header

app = FastAPI(title="Naagin API", dependencies=[Depends(inject_session_key)])


@app.middleware("http")
async def add_doaxvv_headers(request: Request, call_next: Callable) -> Response:
    response = await call_next(request)
    response_set_doaxvv_header(response, "ServerTime", int(time()))
    response_set_doaxvv_header(response, "Status", HTTPStatus.OK)
    response_set_doaxvv_header(
        response, "ApplicationVersion", settings.version.application
    )
    response_set_doaxvv_header(response, "MasterVersion", settings.version.master)
    response_set_doaxvv_header(response, "ResourceVersion", settings.version.resource)
    return response


app.add_middleware(DeflateMiddleware)
app.add_middleware(AESMiddleware)


app.include_router(routers.api.router)
