from typing import Annotated
from typing import Optional

from fastapi import Header

from naagin.enums import ClientTypeEnum
from naagin.enums import EncodingEnum
from .utils import default_factory

ContentTypeHeader = Annotated[str, Header(alias="Content-Type")]
ContentLengthHeader = Annotated[
    Optional[int], Header(default_factory=default_factory, alias="Content-Length")
]

AccessTokenHeader = Annotated[str, Header(alias="X-DOAXVV-Access-Token")]
NonceHeader = Annotated[str, Header(alias="X-DOAXVV-Nonce")]
ApplicationVersionHeader = Annotated[int, Header(alias="X-DOAXVV-ApplicationVersion")]
ClientTypeHeader = Annotated[ClientTypeEnum, Header(alias="X-DOAXVV-ClientType")]
EncodingHeader = Annotated[
    Optional[EncodingEnum],
    Header(default_factory=default_factory, alias="X-DOAXVV-Encoding"),
]
EncryptedHeader = Annotated[
    Optional[str], Header(default_factory=default_factory, alias="X-DOAXVV-Encrypted")
]
MasterVersionHeader = Annotated[int, Header(alias="X-DOAXVV-MasterVersion")]
