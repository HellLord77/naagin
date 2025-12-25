from base64 import b64decode

from anyio.functools import lru_cache
from cryptography.hazmat.primitives.asymmetric.padding import PKCS1v15
from cryptography.hazmat.primitives.asymmetric.rsa import RSAPrivateKey
from cryptography.hazmat.primitives.serialization import Encoding
from cryptography.hazmat.primitives.serialization import PublicFormat
from cryptography.hazmat.primitives.serialization import load_pem_private_key
from fastapi import APIRouter

from naagin import settings
from naagin.models.api import SessionKeyGetResponseModel
from naagin.models.api import SessionKeyPutRequestModel
from naagin.models.api import SessionKeyPutResponseModel
from naagin.schemas import SessionSchema
from naagin.types_.dependencies import DatabaseDependency
from naagin.types_.dependencies import OwnerIdDependency

router = APIRouter(prefix="/key")


@lru_cache
async def get_private_key() -> RSAPrivateKey:
    path = settings.data.api_dir / "v1" / "session" / "key.pem"
    data = await path.read_bytes()
    return load_pem_private_key(data, None)


@router.get("")
@lru_cache
async def get() -> SessionKeyGetResponseModel:
    private_key = await get_private_key()

    public_key = private_key.public_key()
    encrypt_key = public_key.public_bytes(Encoding.PEM, PublicFormat.SubjectPublicKeyInfo).decode()
    return SessionKeyGetResponseModel(encrypt_key=encrypt_key)


@router.put("")
async def put(
    request: SessionKeyPutRequestModel, database: DatabaseDependency, owner_id: OwnerIdDependency
) -> SessionKeyPutResponseModel:
    session = await database.get_one(SessionSchema, owner_id)

    private_key = await get_private_key()
    session_key = private_key.decrypt(b64decode(request.encrypt_key), PKCS1v15())
    session.key = session_key

    await database.flush()

    return SessionKeyPutResponseModel(session="encrypt key saved")
