from base64 import b64encode
from http import HTTPStatus

from aiopath import AsyncPath
from filelock import AsyncFileLock
from httpx import HTTPStatusError
from starlette.exceptions import HTTPException  # noqa: TID251
from starlette.responses import FileResponse
from starlette.responses import Response  # noqa: TID251
from starlette.staticfiles import PathLike
from starlette.types import Scope

from naagin import loggers
from naagin import settings
from naagin.classes import StaticFiles


async def not_found_handler(path: PathLike, scope: Scope) -> Response:
    full_path = await AsyncPath(settings.data.game_dir / path).resolve()
    try:
        relative_path = full_path.relative_to(settings.data.game_dir)
    except ValueError:
        raise HTTPException(status_code=HTTPStatus.NOT_FOUND) from None

    url = relative_path.as_posix()
    name = b64encode(url.encode()).decode()
    lock_path = (settings.data.temp_dir / name).with_suffix(".lock")

    async with AsyncFileLock(lock_path):
        if not await full_path.is_file():
            loggers.game.info("GET: %s", url)
            try:
                response = await settings.game.client.get(url)
                response.raise_for_status()
            except HTTPStatusError as exception:
                if exception.response.status_code == HTTPStatus.NOT_FOUND:
                    loggers.game.warning("Not Found: %s", url)
                    if full_path.name != "index.html" and scope["path"].endswith("/"):
                        return await not_found_handler(full_path / "index.html", scope)

                    raise HTTPException(status_code=HTTPStatus.NOT_FOUND) from None
                raise
            else:
                await full_path.parent.mkdir(parents=True, exist_ok=True)
                temp_path = (settings.data.temp_dir / name).with_suffix(".temp")

                await temp_path.write_bytes(response.content)
                await temp_path.rename(full_path)
    return FileResponse(full_path)


kwargs = {}
if not settings.game.offline_mode:
    kwargs["not_found_handler"] = not_found_handler

app = StaticFiles(directory=settings.data.game_dir, html=True, autoindex=settings.game.list_dir, **kwargs)
