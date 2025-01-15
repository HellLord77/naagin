from typing import Annotated

from fastapi import Header

AccessTokenHeader = Annotated[str, Header(alias="X-DOAXVV-Access-Token")]
MasterVersionHeader = Annotated[int, Header(alias="X-DOAXVV-MasterVersion")]
