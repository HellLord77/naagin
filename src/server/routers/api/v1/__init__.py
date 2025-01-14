from fastapi import APIRouter

from . import csv
from . import owner
from . import shop
from . import tutorial

router = APIRouter(prefix="/v1")

router.include_router(csv.router)
router.include_router(owner.router)
router.include_router(shop.router)
router.include_router(tutorial.router)
