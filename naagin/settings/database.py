from functools import cached_property
from typing import Annotated
from typing import Literal

from pydantic import Field
from pydantic import SecretStr
from pydantic_settings import SettingsConfigDict
from sqlalchemy import URL
from sqlalchemy.ext.asyncio import AsyncEngine
from sqlalchemy.ext.asyncio import async_sessionmaker
from sqlalchemy.ext.asyncio import create_async_engine

from naagin.bases import SettingsBase
from naagin.classes import AsyncSession
from naagin.enums import DatabaseDriverEnum
from naagin.types.fields import PortField


class DatabaseSettings(SettingsBase):
    driver: Literal[DatabaseDriverEnum.POSTGRESQL] = DatabaseDriverEnum.POSTGRESQL
    user: str | None = None
    pass_: Annotated[SecretStr | None, Field(alias="db_pass")] = None
    host: str | None = None
    port: PortField | None = None
    name: str | None = None

    echo_sql: bool = False
    echo_pool: bool = False
    echo_args: bool = False
    echo_lint: bool = True
    echo_color: bool = True

    model_config = SettingsConfigDict(env_prefix="db_")

    @cached_property
    def url(self) -> URL:
        drivername = {
            DatabaseDriverEnum.SQLITE: "sqlite+aiosqlite",
            DatabaseDriverEnum.POSTGRESQL: "postgresql+asyncpg",
            DatabaseDriverEnum.MYSQL: "mysql+aiomysql",
            DatabaseDriverEnum.MARIADB: "mysql+aiomysql",
        }.get(self.driver, self.driver)
        password = None
        if self.pass_ is not None:
            password = self.pass_.get_secret_value()

        return URL.create(drivername, self.user, password, self.host, self.port, self.name)

    @cached_property
    def engine(self) -> AsyncEngine:
        return create_async_engine(
            self.url, echo=self.echo_sql, echo_pool=self.echo_pool, hide_parameters=not self.echo_args
        )

    @cached_property
    def session(self) -> AsyncSession:
        return AsyncSession(self.engine, autoflush=False)

    @cached_property
    def sessionmaker(self) -> async_sessionmaker:
        return async_sessionmaker(self.engine, class_=AsyncSession, autoflush=False)
