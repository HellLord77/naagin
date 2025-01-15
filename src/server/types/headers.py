from typing import Annotated

from fastapi import Header

AccessTokenHeader = Annotated[str, Header(alias="X-DOAXVV-Access-Token")]
ApplicationVersionHeader = Annotated[int, Header(alias="X-DOAXVV-ApplicationVersion")]
ClientTypeHeader = Annotated[int, Header(alias="X-DOAXVV-ClientType")]
MasterVersionHeader = Annotated[int, Header(alias="X-DOAXVV-MasterVersion")]
