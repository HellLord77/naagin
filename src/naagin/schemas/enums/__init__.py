from sqlalchemy import Enum

from naagin.enums import CasinoGameEnum
from naagin.enums import CheckedLicenseLevelEnum
from naagin.enums import FriendshipStateEnum
from naagin.enums import GiftBoxMessageTypeTypeEnum
from naagin.enums import InformationCategoryEnum
from naagin.enums import ItemConsumeTypeEnum
from naagin.enums import ItemEquipmentTypeEnum
from naagin.enums import LicenseLevelEnum
from naagin.enums import OwnerStatusEnum
from naagin.enums import PrivateItemTypeEnum
from naagin.enums import RequestClearRankEnum
from naagin.enums import SealRarityEnum
from naagin.enums import SpecialOrderTypeEnum

from .utils import values_callable

CasinoGameEnumSchema = Enum(CasinoGameEnum, values_callable=values_callable)
CheckedLicenseLevelEnumSchema = Enum(CheckedLicenseLevelEnum, values_callable=values_callable)
FriendshipStateEnumSchema = Enum(FriendshipStateEnum, values_callable=values_callable)
GiftBoxMessageTypeTypeEnumSchema = Enum(GiftBoxMessageTypeTypeEnum, values_callable=values_callable)
InformationCategoryEnumSchema = Enum(InformationCategoryEnum, values_callable=values_callable)
ItemConsumeTypeEnumSchema = Enum(ItemConsumeTypeEnum, values_callable=values_callable)
ItemEquipmentTypeEnumSchema = Enum(ItemEquipmentTypeEnum, values_callable=values_callable)
LicenseLevelEnumSchema = Enum(LicenseLevelEnum, values_callable=values_callable)
OwnerStatusEnumSchema = Enum(OwnerStatusEnum, values_callable=values_callable)
PrivateItemTypeEnumSchema = Enum(PrivateItemTypeEnum, values_callable=values_callable)
RequestClearRankEnumSchema = Enum(RequestClearRankEnum, values_callable=values_callable)
SealRarityEnumSchema = Enum(SealRarityEnum, values_callable=values_callable)
SpecialOrderTypeEnumSchema = Enum(SpecialOrderTypeEnum, values_callable=values_callable)
