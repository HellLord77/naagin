from sqlalchemy import Enum

from naagin.types.enums import AppealUpEnum
from naagin.types.enums import BooleanEnum
from naagin.types.enums import CheckedLicenseLevelEnum
from naagin.types.enums import FriendshipStateEnum
from naagin.types.enums import ItemConsumeTypeEnum
from naagin.types.enums import ItemEquipmentTypeEnum
from naagin.types.enums import LicenseLevelEnum
from naagin.types.enums import OwnerStatusEnum
from .utils import values_callable
from .utils import values_callable

AppealUpEnumSchema = Enum(AppealUpEnum, values_callable=values_callable)
BooleanEnumSchema = Enum(BooleanEnum, values_callable=values_callable)
CheckedLicenseLevelEnumSchema = Enum(
    CheckedLicenseLevelEnum, values_callable=values_callable
)
FriendshipStateEnumSchema = Enum(FriendshipStateEnum, values_callable=values_callable)
ItemConsumeTypeEnumSchema = Enum(ItemConsumeTypeEnum, values_callable=values_callable)
ItemEquipmentTypeEnumSchema = Enum(
    ItemEquipmentTypeEnum, values_callable=values_callable
)
LicenseLevelEnumSchema = Enum(LicenseLevelEnum, values_callable=values_callable)
OwnerStatusEnumSchema = Enum(OwnerStatusEnum, values_callable=values_callable)
