from fastapi import APIRouter

from . import incomplete

router = APIRouter(prefix="/paymentlog")

router.include_router(incomplete.router)
