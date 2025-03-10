from fastapi import APIRouter

from . import private

router = APIRouter(prefix="/{girl_mid}")

router.include_router(private.router)
