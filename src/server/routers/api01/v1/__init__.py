import contextlib
import json
import os

from fastapi import APIRouter
from fastapi import FastAPI

from . import maintenance
from .... import config

resource_list = {}


@contextlib.asynccontextmanager
async def lifespan(_: FastAPI):
    with open(
        os.path.join(config.DATA_DIR, "api01", "v1", "resource", "list.json")
    ) as file:
        resource_list.update(json.load(file))
    yield
    resource_list.clear()


router = APIRouter(prefix="/v1", lifespan=lifespan)

router.include_router(maintenance.router)


@router.get("/gamestart")
async def get_gamestart():
    return {"gamestart": True}


@router.get("/resource/list")
async def get_resource_list():
    return resource_list
