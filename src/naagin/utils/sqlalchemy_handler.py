from logging import INFO
from logging import LogRecord

from rich.console import ConsoleRenderable
from rich.logging import RichHandler
from rich.syntax import Syntax
from sqlparse import format

from naagin import settings
from naagin.enums import DatabaseDriverEnum

SYNTAX = Syntax(
    "",
    {
        DatabaseDriverEnum.POSTGRESQL: "postgresql",
        DatabaseDriverEnum.MYSQL: "mysql",
        DatabaseDriverEnum.MARIADB: "mysql",
    }.get(settings.database.driver, "sql"),
    background_color="default",
)


class SQLAlchemyHandler(RichHandler):
    def emit(self, record: LogRecord) -> None:
        if record.levelno == INFO and record.msg != "[%s] %r":
            record.format = settings.database.echo_lint
            record.syntax = settings.database.echo_color
        super().emit(record)

    def render_message(self, record: LogRecord, message: str) -> ConsoleRenderable:
        if getattr(record, "format", False):
            message = format(message, reindent=True, keyword_case="upper")

        if getattr(record, "syntax", False):
            return SYNTAX.highlight(message)
        else:
            return super().render_message(record, message)
