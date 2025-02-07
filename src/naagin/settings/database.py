from functools import cached_property

from pydantic import Field
from pydantic import SecretStr
from pydantic_settings import SettingsConfigDict
from sqlalchemy import URL
from sqlalchemy.ext.asyncio import AsyncEngine
from sqlalchemy.ext.asyncio import async_sessionmaker
from sqlalchemy.ext.asyncio import create_async_engine

from naagin.classes import AsyncSession
from naagin.enums import DatabaseDriverEnum

from .base import BaseSettings


class DatabaseSettings(BaseSettings):
    driver: DatabaseDriverEnum = DatabaseDriverEnum.POSTGRESQL
    user: str | None = None
    pass_: SecretStr | None = Field(None, alias="db_pass")
    host: str | None = None
    port: str | None = None
    name: str | None = None

    echo_sql: bool = False
    echo_pool: bool = False
    echo_args: bool = False
    echo_lint: bool = True
    echo_color: bool = True

    model_config = SettingsConfigDict(env_prefix="db_")

    @cached_property
    def url(self) -> URL:
        if self.driver != DatabaseDriverEnum.POSTGRESQL:
            raise NotImplementedError

        driver = {
            DatabaseDriverEnum.SQLITE: "sqlite+aiosqlite",
            DatabaseDriverEnum.POSTGRESQL: "postgresql+asyncpg",
            DatabaseDriverEnum.MYSQL: "mysql+aiomysql",
            DatabaseDriverEnum.MARIADB: "mysql+aiomysql",
        }.get(self.driver, self.driver)
        password = self.pass_
        if password is not None:
            password = password.get_secret_value()

        return URL.create(driver, self.user, password, self.host, self.port, self.name)

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
