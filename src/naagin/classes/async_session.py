from collections.abc import Sequence

from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.sql._typing import _ColumnExpressionArgument

from naagin.schemas.base import CustomBaseSchema


class CustomAsyncSession(AsyncSession):
    async def find[T: CustomBaseSchema](
        self, entity: type[T], *whereclause: _ColumnExpressionArgument[bool]
    ) -> T | None:
        return await self.scalar(select(entity).where(*whereclause))

    async def find_all[T: CustomBaseSchema](
        self, entity: type[T], *whereclause: _ColumnExpressionArgument[bool]
    ) -> Sequence[T]:
        return (await self.scalars(select(entity).where(*whereclause))).all()
