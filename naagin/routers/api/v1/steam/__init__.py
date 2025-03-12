from fastapi import APIRouter

from . import currencyinfo
from . import timeoutcheck

router = APIRouter(prefix="/steam")

router.include_router(currencyinfo.router)
router.include_router(timeoutcheck.router)
