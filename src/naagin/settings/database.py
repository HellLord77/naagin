from functools import cached_property
from typing import Optional

from pydantic import Field
from pydantic import SecretStr
from pydantic_settings import SettingsConfigDict
from sqlalchemy import URL
from sqlalchemy.ext.asyncio import AsyncEngine
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.ext.asyncio import async_sessionmaker
from sqlalchemy.ext.asyncio import create_async_engine

from .base import BaseSettings


class DatabaseSettings(BaseSettings):
    driver: str = "postgresql"
    user: Optional[str] = None
    pass_: Optional[SecretStr] = Field(None, alias="db_pass")
    host: Optional[str] = None
    port: Optional[str] = None
    name: Optional[str] = None

    echo_sql: bool = False
    echo_pool: bool = False
    echo_args: bool = False
    echo_lint: bool = True
    echo_color: bool = True

    model_config = SettingsConfigDict(env_prefix="db_")

    @cached_property
    def url(self) -> URL:
        if self.driver != "postgresql":
            raise NotImplementedError

        if self.driver == "sqlite":
            driver = "sqlite+aiosqlite"
        elif self.driver == "postgresql":
            driver = "postgresql+asyncpg"
        elif self.driver == "mysql":
            driver = "mysql+aiomysql"
        else:
            driver = self.driver
        password = self.pass_
        if password is not None:
            password = password.get_secret_value()

        return URL.create(driver, self.user, password, self.host, self.port, self.name)

    @cached_property
    def engine(self) -> AsyncEngine:
        return create_async_engine(
            self.url,
            echo=self.echo_sql,
            echo_pool=self.echo_pool,
            hide_parameters=not self.echo_args,
        )

    @cached_property
    def session(self) -> AsyncSession:
        return AsyncSession(self.engine, autoflush=False)

    @cached_property
    def sessionmaker(self) -> async_sessionmaker:
        return async_sessionmaker(self.engine, autoflush=False)
