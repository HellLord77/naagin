from collections.abc import Sequence

from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.sql._typing import _ColumnExpressionArgument

from naagin.bases import SchemaBase


class CustomAsyncSession(AsyncSession):
    async def find[T: SchemaBase](self, entity: type[T], *whereclause: _ColumnExpressionArgument[bool]) -> T | None:
        return await self.scalar(select(entity).where(*whereclause))

    async def find_all[T: SchemaBase](
        self, entity: type[T], *whereclause: _ColumnExpressionArgument[bool]
    ) -> Sequence[T]:
        return (await self.scalars(select(entity).where(*whereclause))).all()
