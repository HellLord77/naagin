from fastapi import APIRouter

from naagin.models.api import DynamicGameParameterGetResponseModel

router = APIRouter(prefix="/dynamic_game_parameter")


@router.get("")
async def get() -> DynamicGameParameterGetResponseModel:
    return DynamicGameParameterGetResponseModel(dynamic_game_parameter_list=[])
