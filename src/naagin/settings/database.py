from functools import cached_property
from typing import Optional

from pydantic import SecretStr
from pydantic_settings import SettingsConfigDict
from sqlalchemy import URL
from sqlalchemy.ext.asyncio import AsyncEngine
from sqlalchemy.ext.asyncio import async_sessionmaker
from sqlalchemy.ext.asyncio import create_async_engine

from .base import BaseSettings


class DatabaseSettings(BaseSettings):
    driver: str = "sqlite"
    user: Optional[str] = None
    passwd: Optional[SecretStr] = None
    host: Optional[str] = None
    port: Optional[str] = None
    name: Optional[str] = None

    echo: bool = False

    model_config = SettingsConfigDict(env_prefix="db_")

    @cached_property
    def url(self) -> URL:
        if self.driver == "sqlite":
            self.driver = "sqlite+aiosqlite"
        elif self.driver == "postgresql":
            self.driver = "postgresql+asyncpg"
        elif self.driver == "mysql":
            self.driver = "mysql+aiomysql"
        if self.passwd is None:
            self.passwd = SecretStr("")
        return URL.create(
            self.driver,
            self.user,
            self.passwd.get_secret_value(),
            self.host,
            self.port,
            self.name,
        )

    @cached_property
    def engine(self) -> AsyncEngine:
        return create_async_engine(self.url, echo=self.echo)

    @cached_property
    def sessionmaker(self) -> async_sessionmaker:
        return async_sessionmaker(self.engine, autoflush=False)
