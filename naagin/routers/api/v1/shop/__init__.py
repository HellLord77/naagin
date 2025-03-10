from fastapi import APIRouter

from . import paymentlog

router = APIRouter(prefix="/shop")

router.include_router(paymentlog.router)
