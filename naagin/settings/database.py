from functools import cached_property
from typing import Annotated
from typing import Literal

from pydantic import AliasChoices
from pydantic import Field
from pydantic import PostgresDsn
from pydantic import SecretStr
from pydantic import computed_field
from sqlalchemy.ext.asyncio import AsyncEngine
from sqlalchemy.ext.asyncio import async_sessionmaker
from sqlalchemy.ext.asyncio import create_async_engine

from naagin.bases import SettingsBase
from naagin.classes import AsyncSession
from naagin.enums import DatabaseDriverEnum
from naagin.types_.fields import PortField


class DatabaseSettings(SettingsBase):
    drivername: Annotated[
        Literal[DatabaseDriverEnum.POSTGRESQL],
        Field(validation_alias=AliasChoices("drivername", "driver"), exclude=True),
    ] = DatabaseDriverEnum.POSTGRESQL
    username: Annotated[str | None, Field(validation_alias=AliasChoices("username", "user"), exclude=True)] = None
    password: Annotated[SecretStr | None, Field(validation_alias=AliasChoices("password", "pass"), exclude=True)] = None
    host: Annotated[str, Field(validation_alias=AliasChoices("host", "hostname"), exclude=True)] = "localhost"
    port: Annotated[PortField | None, Field(exclude=True)] = None
    database: Annotated[str | None, Field(validation_alias=AliasChoices("database", "name"), exclude=True)] = None
    full_url: Annotated[PostgresDsn | None, Field(validation_alias=AliasChoices("full_url", "url"), exclude=True)] = (
        None
    )

    echo_sql: bool = False
    echo_pool: bool = False
    echo_args: bool = False
    echo_lint: bool = True
    echo_color: bool = True

    @computed_field
    @cached_property
    def url(self) -> PostgresDsn:
        if self.full_url is None:
            scheme = {
                DatabaseDriverEnum.SQLITE: "sqlite+aiosqlite",
                DatabaseDriverEnum.POSTGRESQL: "postgresql+asyncpg",
                DatabaseDriverEnum.MYSQL: "mysql+aiomysql",
                DatabaseDriverEnum.MARIADB: "mysql+aiomysql",
            }.get(self.drivername, self.drivername)
            password = None
            if self.password is not None:
                password = self.password.get_secret_value()
            return PostgresDsn.build(
                scheme=scheme,
                username=self.username,
                password=password,
                host=self.host,
                port=self.port,
                path=self.database,
            )

        return self.full_url

    @cached_property
    def engine(self) -> AsyncEngine:
        return create_async_engine(
            str(self.url), echo=self.echo_sql, echo_pool=self.echo_pool, hide_parameters=not self.echo_args
        )

    @cached_property
    def session(self) -> AsyncSession:
        return AsyncSession(self.engine, autoflush=False)

    @cached_property
    def sessionmaker(self) -> async_sessionmaker:
        return async_sessionmaker(self.engine, class_=AsyncSession, autoflush=False)
