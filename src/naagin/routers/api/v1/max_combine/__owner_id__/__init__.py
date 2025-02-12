from fastapi import APIRouter

from . import __item_mid__

router = APIRouter(prefix="/{owner_id}")

router.include_router(__item_mid__.router)
