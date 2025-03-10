from fastapi import APIRouter

from . import affection_reward
from . import bromide
from . import casino
from . import cheat_log
from . import csv
from . import dishevelment
from . import dynamic_game_parameter
from . import friendship
from . import furniture
from . import giftbox
from . import girl
from . import honor
from . import information
from . import item
from . import login_bonus
from . import max_combine
from . import ngword
from . import onsen
from . import option
from . import owner
from . import photo_shoot
from . import pvp_fes_deck
from . import pvp_girl
from . import pyon2
from . import quest
from . import radio_station
from . import room
from . import seal
from . import session
from . import shop
from . import special_order
from . import subscription
from . import swimsuit_arrange_flag
from . import tutorial
from . import venus_board
from . import wallet

router = APIRouter(prefix="/v1")

router.include_router(affection_reward.router)
router.include_router(bromide.router)
router.include_router(casino.router)
router.include_router(cheat_log.router)
router.include_router(csv.router)
router.include_router(dishevelment.router)
router.include_router(dynamic_game_parameter.router)
router.include_router(friendship.router)
router.include_router(furniture.router)
router.include_router(giftbox.router)
router.include_router(girl.router)
router.include_router(honor.router)
router.include_router(information.router)
router.include_router(item.router)
router.include_router(login_bonus.router)
router.include_router(max_combine.router)
router.include_router(ngword.router)
router.include_router(onsen.router)
router.include_router(option.router)
router.include_router(owner.router)
router.include_router(photo_shoot.router)
router.include_router(pvp_fes_deck.router)
router.include_router(pvp_girl.router)
router.include_router(pyon2.router)
router.include_router(quest.router)
router.include_router(radio_station.router)
router.include_router(room.router)
router.include_router(seal.router)
router.include_router(session.router)
router.include_router(shop.router)
router.include_router(special_order.router)
router.include_router(subscription.router)
router.include_router(swimsuit_arrange_flag.router)
router.include_router(tutorial.router)
router.include_router(venus_board.router)
router.include_router(wallet.router)
