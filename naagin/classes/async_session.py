from collections.abc import Sequence

from sqlalchemy import func
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession  # noqa: TID251
from sqlalchemy.sql._typing import _ColumnExpressionArgument

from naagin.bases import SchemaBase


class CustomAsyncSession(AsyncSession):
    async def find[T: SchemaBase](self, entity: type[T], *whereclause: _ColumnExpressionArgument[bool]) -> T | None:
        return await self.scalar(select(entity).where(*whereclause))

    async def find_all[T: SchemaBase](
        self, entity: type[T], *whereclause: _ColumnExpressionArgument[bool]
    ) -> Sequence[T]:
        return (await self.scalars(select(entity).where(*whereclause))).all()

    async def count(self, entity: type[SchemaBase], *whereclause: _ColumnExpressionArgument[bool]) -> int:
        return await self.scalar(select(func.count()).select_from(entity).where(*whereclause))
