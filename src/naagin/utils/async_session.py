from collections.abc import Sequence

from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.orm.session import _EntityBindKey
from sqlalchemy.sql._typing import _ColumnExpressionArgument


class AsyncSession(AsyncSession):
    async def get_all[T](self, entity: _EntityBindKey[T], *whereclause: _ColumnExpressionArgument[bool]) -> Sequence[T]:
        return (await self.scalars(select(entity).where(*whereclause))).all()
