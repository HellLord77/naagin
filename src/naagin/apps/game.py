from base64 import b64encode
from http import HTTPStatus

from aiopath import AsyncPath
from filelock import AsyncFileLock
from httpx import HTTPStatusError
from starlette.exceptions import HTTPException  # noqa: TID251
from starlette.responses import FileResponse
from starlette.responses import Response  # noqa: TID251

from naagin import loggers
from naagin import settings
from naagin.classes import StaticFiles


async def not_found_handler(path: AsyncPath) -> Response:
    relative_path = path.relative_to(settings.data.game_dir)
    url = relative_path.as_posix()
    name = b64encode(url.encode()).decode()

    lock_path = (settings.data.temp_dir / name).with_suffix(".lock")
    async with AsyncFileLock(lock_path):
        if not await path.is_file():
            loggers.game.info("Downloading: %s", url)
            try:
                response = await settings.game.client.get(url)
                response.raise_for_status()
            except HTTPStatusError as exception:
                if exception.response.status_code == HTTPStatus.NOT_FOUND:
                    raise HTTPException(status_code=HTTPStatus.NOT_FOUND) from exception
                raise
            else:
                await path.parent.mkdir(parents=True, exist_ok=True)
                temp_path = (settings.data.temp_dir / name).with_suffix(".temp")

                await temp_path.write_bytes(response.content)
                await temp_path.rename(path)
    return FileResponse(path)


kwargs = {}
if not settings.game.offline_mode:
    kwargs["not_found_handler"] = not_found_handler

app = StaticFiles(directory=settings.data.game_dir, autoindex=settings.game.list_dir, **kwargs)
