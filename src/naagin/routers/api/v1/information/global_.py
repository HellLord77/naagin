from functools import cache

from fastapi import APIRouter
from sqlalchemy import func

from naagin.enums import InformationCategoryEnum
from naagin.enums import LanguageEnum
from naagin.exceptions import InternalServerErrorException
from naagin.models.api import InformationGlobalPostRequestModel
from naagin.models.api import InformationGlobalPostResponseModel
from naagin.schemas import InformationReadSchema
from naagin.schemas import InformationSchema
from naagin.types.dependencies import OwnerIdDependency
from naagin.types.dependencies import SessionDependency

router = APIRouter(prefix="/global")


@cache
def get_categories(
    language: LanguageEnum,
) -> tuple[InformationCategoryEnum, InformationCategoryEnum, InformationCategoryEnum, InformationCategoryEnum]:
    match language:
        case LanguageEnum.JPN:
            return (
                InformationCategoryEnum.IMPORTANT_JPN,
                InformationCategoryEnum.NOTICE_JPN,
                InformationCategoryEnum.EVENT_JPN,
                InformationCategoryEnum.GACHA_JPN,
            )
        case LanguageEnum.ENG:
            return (
                InformationCategoryEnum.IMPORTANT_ENG,
                InformationCategoryEnum.NOTICE_ENG,
                InformationCategoryEnum.EVENT_ENG,
                InformationCategoryEnum.GACHA_ENG,
            )
        case LanguageEnum.CHN:
            return (
                InformationCategoryEnum.IMPORTANT_CHN,
                InformationCategoryEnum.NOTICE_CHN,
                InformationCategoryEnum.EVENT_CHN,
                InformationCategoryEnum.GACHA_CHN,
            )
        case LanguageEnum.ZHN:
            return (
                InformationCategoryEnum.IMPORTANT_ZHN,
                InformationCategoryEnum.NOTICE_ZHN,
                InformationCategoryEnum.EVENT_ZHN,
                InformationCategoryEnum.GACHA_ZHN,
            )
        case LanguageEnum.KOR:
            return (
                InformationCategoryEnum.IMPORTANT_KOR,
                InformationCategoryEnum.NOTICE_KOR,
                InformationCategoryEnum.EVENT_KOR,
                InformationCategoryEnum.GACHA_KOR,
            )
        case _:
            raise InternalServerErrorException


@router.post("")
async def post(
    request: InformationGlobalPostRequestModel, session: SessionDependency, owner_id: OwnerIdDependency
) -> InformationGlobalPostResponseModel:
    information_list = await session.find_all(
        InformationSchema,
        InformationSchema.category.in_(get_categories(request.language)),
        InformationSchema.close_at >= func.current_timestamp(),
    )

    information_read_list = await session.find_all(
        InformationReadSchema,
        InformationReadSchema.owner_id == owner_id,
        InformationReadSchema.information_id.in_([information.information_id for information in information_list]),
    )
    information_read_id_set = {information_read.information_id for information_read in information_read_list}
    for information in information_list:
        information.read = information.information_id in information_read_id_set

    return InformationGlobalPostResponseModel(information_list=information_list)
