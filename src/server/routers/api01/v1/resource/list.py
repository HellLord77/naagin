import contextlib
import json
import os

from fastapi import APIRouter
from fastapi import FastAPI

from ..... import config
from .....models.api01.v1.resource.list import ResourceListGetResponseModel

resource_list = {}


@contextlib.asynccontextmanager
async def lifespan(_: FastAPI):
    with open(
        os.path.join(config.DATA_DIR, "api01", "v1", "resource", "list.json")
    ) as file:
        resource_list.update(json.load(file))
    yield
    resource_list.clear()


router = APIRouter(prefix="/list", lifespan=lifespan)


@router.get("")
async def get() -> ResourceListGetResponseModel:
    # noinspection PyTypeChecker
    return resource_list
