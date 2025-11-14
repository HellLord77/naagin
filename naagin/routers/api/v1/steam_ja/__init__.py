from fastapi import APIRouter

from . import currencyinfo
from . import session
from . import timeoutcheck

router = APIRouter(prefix="/steam_ja")

router.include_router(currencyinfo.router)
router.include_router(session.router)
router.include_router(timeoutcheck.router)
