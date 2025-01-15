from typing import Annotated

from fastapi import Depends
from sqlalchemy.ext.asyncio import AsyncSession

from ... import providers

SessionDependency = Annotated[AsyncSession, Depends(providers.provide_session)]
OwnerIdDependency = Annotated[int, Depends(providers.provide_owner_id)]
