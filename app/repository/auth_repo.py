from sqlalchemy.orm import Session

from app.core.exceptions import UserNotFoundException, NotExistUserEmail, BadCredentials
from app.repository import user_repo
from app.schema import user_schema


def is_valid_user(db: Session, user: user_schema.UserCreate) -> bool:
    try:
        _ = user_repo.find_user_by_email(db, user.user_email)
    except UserNotFoundException:
        raise NotExistUserEmail(user.user_email)

    try:
        _ = user_repo.find_user_by_credentials(db, user.user_email, user.user_hashed_password)
    except UserNotFoundException:
        raise BadCredentials(user.user_email)

    return True
