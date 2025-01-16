from enum import IntEnum

from sqlalchemy import Enum

from .checked_license_level import CheckedLicenseLevelEnum
from .license_level import LicenseLevelEnum
from .option_lock import OptionLockEnum
from .owner_status import OwnerStatusEnum


def values_callable(enum: type[IntEnum]):
    return list(map(str, enum))


CheckedLicenseLevelEnumSchema = Enum(
    CheckedLicenseLevelEnum, values_callable=values_callable
)
LicenseLevelEnumSchema = Enum(LicenseLevelEnum, values_callable=values_callable)
OptionLockEnumSchema = Enum(OptionLockEnum, values_callable=values_callable)
OwnerStatusEnumSchema = Enum(OwnerStatusEnum, values_callable=values_callable)
