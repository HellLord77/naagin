from fastapi import APIRouter

from naagin.models.api import WalletGetResponseModel
from naagin.schemas import WalletSchema
from naagin.types_.dependencies import DatabaseDependency
from naagin.types_.dependencies import OwnerIdDependency

router = APIRouter(prefix="/wallet")


@router.get("")
async def get(database: DatabaseDependency, owner_id: OwnerIdDependency) -> WalletGetResponseModel:
    wallet = await database.get(WalletSchema, owner_id)

    if wallet is None:
        wallet = WalletSchema(owner_id=owner_id)
        database.add(wallet)

        await database.flush()

    return WalletGetResponseModel(wallet=wallet)
