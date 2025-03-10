from typing import Annotated
from typing import Literal

from fastapi import Header

from naagin import factories
from naagin.enums import ClientTypeEnum
from naagin.enums import EncodingEnum

UserAgentHeader = Annotated[str | None, Header(default_factory=factories.null_factory, alias="User-Agent")]
ContentTypeHeader = Annotated[str, Header(alias="Content-Type")]
ContentLengthHeader = Annotated[int | None, Header(default_factory=factories.null_factory, alias="Content-Length")]

AccessTokenHeader = Annotated[str, Header(alias="X-DOAXVV-Access-Token")]
NonceHeader = Annotated[str, Header(alias="X-DOAXVV-Nonce")]
ApplicationVersionHeader = Annotated[int, Header(alias="X-DOAXVV-ApplicationVersion")]
ClientTypeHeader = Annotated[ClientTypeEnum, Header(alias="X-DOAXVV-ClientType")]
EncodingHeader = Annotated[
    Literal[EncodingEnum.DEFLATE] | None, Header(default_factory=factories.null_factory, alias="X-DOAXVV-Encoding")
]
EncryptedHeader = Annotated[str | None, Header(default_factory=factories.null_factory, alias="X-DOAXVV-Encrypted")]
MasterVersionHeader = Annotated[int, Header(alias="X-DOAXVV-MasterVersion")]
