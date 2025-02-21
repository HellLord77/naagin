from fastapi import APIRouter

from . import bromide
from . import cheat_log
from . import csv
from . import dishevelment
from . import friendship
from . import furniture
from . import girl
from . import honor
from . import information
from . import item
from . import max_combine
from . import option
from . import owner
from . import pvp_fes_deck
from . import pvp_girl
from . import pyon2
from . import quest
from . import room
from . import session
from . import shop
from . import special_order
from . import swimsuit_arrange_flag
from . import tutorial
from . import wallet

router = APIRouter(prefix="/v1")

router.include_router(bromide.router)
router.include_router(cheat_log.router)
router.include_router(csv.router)
router.include_router(dishevelment.router)
router.include_router(friendship.router)
router.include_router(furniture.router)
router.include_router(girl.router)
router.include_router(honor.router)
router.include_router(information.router)
router.include_router(item.router)
router.include_router(max_combine.router)
router.include_router(option.router)
router.include_router(owner.router)
router.include_router(pvp_fes_deck.router)
router.include_router(pvp_girl.router)
router.include_router(pyon2.router)
router.include_router(quest.router)
router.include_router(room.router)
router.include_router(session.router)
router.include_router(shop.router)
router.include_router(special_order.router)
router.include_router(swimsuit_arrange_flag.router)
router.include_router(tutorial.router)
router.include_router(wallet.router)
