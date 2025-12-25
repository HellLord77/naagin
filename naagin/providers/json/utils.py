from naagin import settings


async def get_resource_list_data(application_version: int | None, *, encrypt: bool) -> bytes:
    directory = settings.data.api01_dir / "v1" / "resource" / "list"
    if encrypt:
        directory = directory / "encrypt"

    path = (
        directory.with_suffix(".json") if application_version is None else (directory / f"{application_version}.json")
    )
    return await path.read_bytes()
