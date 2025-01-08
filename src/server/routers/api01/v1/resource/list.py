import contextlib
import json

from fastapi import APIRouter
from fastapi import FastAPI

from ..... import config
from .....models.api01.v1.resource.list import ResourceListGetResponseModel

resource_list = {}


@contextlib.asynccontextmanager
async def lifespan(_: FastAPI):
    resource_list.update(
        json.loads(
            (config.DATA_DIR / "api01" / "v1" / "resource" / "list.json").read_text()
        )
    )
    yield
    resource_list.clear()


router = APIRouter(prefix="/list", lifespan=lifespan)


@router.get("")
async def get() -> ResourceListGetResponseModel:
    # noinspection PyTypeChecker
    return resource_list
