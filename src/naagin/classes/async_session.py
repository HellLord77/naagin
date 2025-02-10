from collections.abc import Sequence

from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.orm.session import _EntityBindKey
from sqlalchemy.sql._typing import _ColumnExpressionArgument


class AsyncSession(AsyncSession):
    async def find[T](self, entity: _EntityBindKey[type[T]], *whereclause: _ColumnExpressionArgument[bool]) -> T | None:
        return await self.scalar(select(entity).where(*whereclause))

    async def find_all[T](
        self, entity: _EntityBindKey[type[T]], *whereclause: _ColumnExpressionArgument[bool]
    ) -> Sequence[T]:
        return (await self.scalars(select(entity).where(*whereclause))).all()
