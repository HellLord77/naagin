import contextlib
import json

from fastapi import APIRouter
from fastapi import FastAPI

from ..... import config
from .....models.api01.v1.resource.list.get.response import ResourceListGetResponseModel

resource_list = {}


@contextlib.asynccontextmanager
async def lifespan(_: FastAPI):
    with (config.DATA_DIR / "api01" / "v1" / "resource" / "list.json").open() as file:
        resource_list.update(json.load(file))
    yield
    resource_list.clear()


router = APIRouter(prefix="/list", lifespan=lifespan)


@router.get("")
async def get() -> ResourceListGetResponseModel:
    # noinspection PyTypeChecker
    return resource_list
