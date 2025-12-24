from naagin.imports import AsyncPath


async def get_bytes(directory: AsyncPath, application_version: int | None) -> bytes:
    path = (
        directory.with_suffix(".json") if application_version is None else (directory / f"{application_version}.json")
    )
    return await path.read_bytes()
