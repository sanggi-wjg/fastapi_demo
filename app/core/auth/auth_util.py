from datetime import timedelta, datetime
from typing import Optional, Dict

from jose import jwt, JWTError
from passlib.context import CryptContext

from app.core.config import get_config_settings
from app.core.exceptions import JWTBadCredentials

crypt = CryptContext(schemes = ["bcrypt"], deprecated = "auto")

settings = get_config_settings()


def verify_password(plain_password: str, hashed_password: str) -> bool:
    return crypt.verify(plain_password, hashed_password)


def hash_password(plain_password: str) -> str:
    return crypt.hash(plain_password)


def create_jwt_token(data: dict, expires_delta: Optional[timedelta] = None) -> str:
    to_encode = data.copy()
    expire = datetime.utcnow() + timedelta(minutes = 15)
    if expires_delta:
        expire = datetime.utcnow() + expires_delta

    to_encode.update(dict(exp = expire))
    return jwt.encode(to_encode, settings.secret_key, algorithm = settings.algorithm)


def decode_jwt_token(token: str) -> Dict:
    try:
        return jwt.decode(token, settings.secret_key, algorithms = settings.algorithm)
    except JWTError:
        raise JWTBadCredentials()


def get_jwt_token_username(token: str):
    payload = decode_jwt_token(token)
    username = payload.get("sub")
    if not username:
        raise JWTBadCredentials()


def get_delta_access_token_expire() -> timedelta:
    return timedelta(minutes = settings.access_token_expire_minutes)
