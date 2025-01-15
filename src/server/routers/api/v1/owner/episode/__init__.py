from fastapi import APIRouter

from . import __episode_mid__

router = APIRouter(prefix="/episode")

router.include_router(__episode_mid__.router)
