from fastapi import APIRouter

from . import chip
from . import game

router = APIRouter(prefix="/casino")

router.include_router(chip.router)
router.include_router(game.router)
