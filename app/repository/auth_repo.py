from typing import Optional

from fastapi.security import OAuth2PasswordRequestForm
from sqlalchemy.orm import Session

from app.core.auth.auth_util import verify_password
from app.core.exceptions import UserNotFoundException, NotExistUserEmail, BadCredentials
from app.db.models import UserEntity
from app.repository import user_repo
from app.schema import user_schema


def is_valid_user(db: Session, user: user_schema.UserCreate) -> bool:
    try:
        find_user = user_repo.find_user_by_email(db, user.user_email)
    except UserNotFoundException:
        raise NotExistUserEmail(user.user_email)

    if not verify_password(user.password, find_user.user_hashed_password):
        raise BadCredentials(user.user_email)

    return True


def authenticate_user(db: Session, form_data: OAuth2PasswordRequestForm) -> UserEntity:
    try:
        find_user = user_repo.find_user_by_email(db, form_data.username)
    except UserNotFoundException:
        raise NotExistUserEmail(form_data.username)

    if not verify_password(form_data.password, find_user.user_hashed_password):
        raise BadCredentials(form_data.username)

    return find_user
