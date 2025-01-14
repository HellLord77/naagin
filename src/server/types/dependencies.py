from typing import Annotated

from fastapi import Depends
from sqlalchemy.ext.asyncio import AsyncSession

from .. import dependencies

Session = Annotated[AsyncSession, Depends(dependencies.provide_session)]
OwnerId = Annotated[int, Depends(dependencies.provide_owner_id)]
