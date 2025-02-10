from functools import cache

from fastapi import APIRouter
from sqlalchemy import func

from naagin.enums import InformationCategoryEnum
from naagin.enums import LanguageEnum
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
    return {
        LanguageEnum.JPN: (
            InformationCategoryEnum.IMPORTANT_JPN,
            InformationCategoryEnum.NOTICE_JPN,
            InformationCategoryEnum.EVENT_JPN,
            InformationCategoryEnum.GACHA_JPN,
        ),
        LanguageEnum.ENG: (
            InformationCategoryEnum.IMPORTANT_ENG,
            InformationCategoryEnum.NOTICE_ENG,
            InformationCategoryEnum.EVENT_ENG,
            InformationCategoryEnum.GACHA_ENG,
        ),
        LanguageEnum.CHN: (
            InformationCategoryEnum.IMPORTANT_CHN,
            InformationCategoryEnum.NOTICE_CHN,
            InformationCategoryEnum.EVENT_CHN,
            InformationCategoryEnum.GACHA_CHN,
        ),
        LanguageEnum.ZHN: (
            InformationCategoryEnum.IMPORTANT_ZHN,
            InformationCategoryEnum.NOTICE_ZHN,
            InformationCategoryEnum.EVENT_ZHN,
            InformationCategoryEnum.GACHA_ZHN,
        ),
        LanguageEnum.KOR: (
            InformationCategoryEnum.IMPORTANT_KOR,
            InformationCategoryEnum.NOTICE_KOR,
            InformationCategoryEnum.EVENT_KOR,
            InformationCategoryEnum.GACHA_KOR,
        ),
    }[language]


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
