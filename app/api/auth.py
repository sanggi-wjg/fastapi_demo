from fastapi import APIRouter, Depends, HTTPException
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from jose import JWTError
from sqlalchemy.orm import Session
from starlette import status

from app.api import RouterTags
from app.core.auth.auth_util import create_jwt_token, get_delta_access_token_expire, decode_jwt_token
from app.db.database import get_db
from app.repository import auth_repo, user_repo
from app.repository.auth_repo import authenticate_user
from app.schema import auth_schema, user_schema
from app.schema.auth_schema import LoginSNSType, TokenData
from app.schema.user_schema import UserCreate, User

router = APIRouter(
    tags = [RouterTags.Auth],
    responses = { 404: { "detail": "not found" } }
)


@router.post("/login/{sns_type}", response_model = auth_schema.TokenData, summary = "Login")
async def login(sns_type: LoginSNSType, user: UserCreate, db: Session = Depends(get_db)):
    # Email
    if sns_type == LoginSNSType.Email:
        if auth_repo.is_valid_user(db, user):
            return True

    else:
        return HTTPException(status_code = 400, detail = f"{sns_type} is not implemented")


@router.post("/token", response_model = auth_schema.TokenData, summary = "Create JWT Token")
async def login_for_access_token(form_data: OAuth2PasswordRequestForm = Depends(), db: Session = Depends(get_db)):
    auth_user = authenticate_user(db, form_data)
    access_token = create_jwt_token({ "sub": auth_user.user_email }, get_delta_access_token_expire())
    return TokenData(token_type = "bearer", access_token = access_token, username = auth_user.user_email)


oauth2_scheme = OAuth2PasswordBearer(tokenUrl = "token")


async def get_current_user(token: str = Depends(oauth2_scheme), db: Session = Depends(get_db)):
    credentials_exception = HTTPException(
        status_code = status.HTTP_401_UNAUTHORIZED,
        detail = "Could not validate credentials",
        headers = { "WWW-Authenticate": "Bearer" },
    )
    try:
        payload = decode_jwt_token(token)
        find_user = user_repo.find_user_by_email(db, payload.get("sub"))
    except JWTError:
        raise credentials_exception

    return find_user


async def get_current_active_user(current_user: User = Depends(get_current_user)):
    if not current_user.is_active:
        raise HTTPException(status_code = 400, detail = "Inactive user")
    return current_user


@router.get("/token/me", response_model = user_schema.User, summary = "Get current user")
async def get_current_user_me(current_user: User = Depends(get_current_active_user)):
    return current_user


async def logout():
    pass
