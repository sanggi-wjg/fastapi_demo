from fastapi import APIRouter, Depends

from app.core.config import Settings, get_config_settings

router = APIRouter(
    tags = ["home"],
)


@router.get("/")
async def index():
    return { "message": "Hello World" }


@router.get("/info")
async def info(conf: Settings = Depends(get_config_settings)):
    return {
        "app_name": conf.app_name,
        "app_desc": conf.app_desc,
    }
