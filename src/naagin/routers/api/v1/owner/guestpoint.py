from fastapi import APIRouter

from naagin.models.api import OwnerGuestPointAcceptPostResponseModel
from naagin.models.api.v1.owner.guestpoint.accept.post.response import AcceptedGuestPointModel

router = APIRouter(prefix="/guestpoint")


@router.get("")
async def get() -> OwnerGuestPointAcceptPostResponseModel:
    accepted_guest_point = AcceptedGuestPointModel(guest_count=0, guest_point=0)
    return OwnerGuestPointAcceptPostResponseModel(accepted_guest_point=accepted_guest_point)
