from fastapi import APIRouter

router = APIRouter(prefix="/maintenance")


@router.get("")
async def get():
    return {"maintenance": False}


@router.get("/privilege/check/{steam_id}")
async def get_privilege_check(_: int):
    return {"result": "NG"}
