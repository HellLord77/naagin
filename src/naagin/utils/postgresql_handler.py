from logging import INFO
from logging import LogRecord

from rich.console import ConsoleRenderable
from rich.logging import RichHandler
from rich.syntax import Syntax
from sqlparse import format

from naagin import settings


class PostgreSQLHandler(RichHandler):
    def emit(self, record: LogRecord):
        if record.levelno == INFO and not record.args:
            record.format = settings.database.echo_lint
            record.syntax = settings.database.echo_color
        return super().emit(record)

    def render_message(self, record: LogRecord, message: str) -> ConsoleRenderable:
        if getattr(record, "format", False):
            message = format(message, reindent=True)

        if getattr(record, "syntax", False):
            return Syntax(message, "postgresql", background_color="default")
        else:
            return super().render_message(record, message)
