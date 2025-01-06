import uvicorn
from fastapi import FastAPI
from fastapi import HTTPException
from fastapi import Request
from fastapi import status
from fastapi.middleware.gzip import GZipMiddleware
from fastapi.responses import JSONResponse

from . import apps
from . import routers

app = FastAPI()
# noinspection PyTypeChecker
app.add_middleware(GZipMiddleware)

app.include_router(routers.api.router, prefix="/api")
app.include_router(routers.api01.router, prefix="/api01")
app.mount("", apps.game.app)


@app.exception_handler(status.HTTP_404_NOT_FOUND)
async def not_found(_: Request, __: HTTPException):
    return JSONResponse(
        {"code": status.HTTP_404_NOT_FOUND, "message": "not found"},
        status.HTTP_404_NOT_FOUND,
    )


@app.exception_handler(status.HTTP_405_METHOD_NOT_ALLOWED)
async def method_not_allowed(_: Request, __: HTTPException):
    return JSONResponse(
        {"code": status.HTTP_405_METHOD_NOT_ALLOWED, "message": "method not allowed"},
        status.HTTP_405_METHOD_NOT_ALLOWED,
    )


def main():
    uvicorn.run(app)


if __name__ == "__main__":
    main()
