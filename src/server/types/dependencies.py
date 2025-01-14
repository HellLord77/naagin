from typing import Annotated

from fastapi import Depends
from sqlalchemy.ext.asyncio import AsyncSession

from .. import dependencies

Session = Annotated[AsyncSession, Depends(dependencies.get_session)]
OwnerId = Annotated[int, Depends(dependencies.get_owner_id)]
