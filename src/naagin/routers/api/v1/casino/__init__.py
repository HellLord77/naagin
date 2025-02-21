from fastapi import APIRouter

from . import game

router = APIRouter(prefix="/casino")

router.include_router(game.router)
