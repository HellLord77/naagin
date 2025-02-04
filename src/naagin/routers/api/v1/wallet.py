from fastapi import APIRouter

from naagin.models.api import WalletGetResponseModel
from naagin.schemas import WalletSchema
from naagin.types.dependencies import OwnerIdDependency
from naagin.types.dependencies import SessionDependency

router = APIRouter(prefix="/wallet")


@router.get("")
async def get(
    session: SessionDependency, owner_id: OwnerIdDependency
) -> WalletGetResponseModel:
    wallet = await session.get(WalletSchema, owner_id)

    if wallet is None:
        wallet = WalletSchema(owner_id=owner_id)
        session.add(wallet)

        await session.flush()
        await session.refresh(wallet)

    return WalletGetResponseModel(wallet=wallet)
