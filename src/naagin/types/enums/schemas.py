from enum import IntEnum

from sqlalchemy import Enum

from .appeal_up import AppealUpEnum
from .boolean import BooleanEnum
from .checked_license_level import CheckedLicenseLevelEnum
from .friendship_state import FriendshipStateEnum
from .license_level import LicenseLevelEnum
from .owner_status import OwnerStatusEnum


def values_callable(enum: type[IntEnum]) -> tuple[str, ...]:
    return tuple(map(str, enum))


AppealUpEnumSchema = Enum(AppealUpEnum, values_callable=values_callable)
BooleanEnumSchema = Enum(BooleanEnum, values_callable=values_callable)
CheckedLicenseLevelEnumSchema = Enum(
    CheckedLicenseLevelEnum, values_callable=values_callable
)
FriendshipStateEnumSchema = Enum(FriendshipStateEnum, values_callable=values_callable)
LicenseLevelEnumSchema = Enum(LicenseLevelEnum, values_callable=values_callable)
OwnerStatusEnumSchema = Enum(OwnerStatusEnum, values_callable=values_callable)
