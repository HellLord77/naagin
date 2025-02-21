from fastapi import APIRouter

from . import chip
from . import game
from . import roulette

router = APIRouter(prefix="/casino")

router.include_router(chip.router)
router.include_router(game.router)
router.include_router(roulette.router)
