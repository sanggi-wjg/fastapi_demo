from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from starlette.responses import JSONResponse

from app.api import RouterTags
from app.db.database import get_db
from app.repository import auth_repo
from app.schema.auth_schema import LoginSNSType
from app.schema.user_schema import UserCreate

router = APIRouter(
    tags = [RouterTags.Auth],
    responses = { 404: { "detail": "not found" } }
)


@router.post("/login/{sns_type}", summary = "Login")
async def login(sns_type: LoginSNSType, user: UserCreate, db: Session = Depends(get_db)):
    # Email
    if sns_type == LoginSNSType.Email:
        if auth_repo.is_valid_user(db, user):
            return JSONResponse({ "detail": "login success" })

    else:
        return HTTPException(status_code = 400, detail = f"{sns_type} is not implemented")
