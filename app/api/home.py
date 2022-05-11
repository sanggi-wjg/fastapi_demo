from fastapi import APIRouter, Depends, HTTPException

from app.api import RouterTags
from app.core.config import Settings, get_config_settings
from app.core.dependency.auth_depend import verify_token, verify_key
from app.core.exceptions import CustomException

router = APIRouter(
    tags = [RouterTags.Home],
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


@router.get("/exception/404")
async def http_exception_404():
    raise HTTPException(404, detail = "not found", headers = { "X-Error": "not found" })


@router.get("/exception/custom")
async def custom_exception():
    raise CustomException("custom")


@router.get("/exception/secret", dependencies = [Depends(verify_token), Depends(verify_key)])
async def exception_verify_token_and_key():
    return { "detail": "must not reach" }
