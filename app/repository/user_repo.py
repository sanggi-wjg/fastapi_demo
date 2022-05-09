from typing import List

from sqlalchemy.exc import NoResultFound
from sqlalchemy.orm import Session

from app.core.exceptions import UserNotFoundException
from app.db import models
from app.schema import user_schema

"""
repository 이지만
service 도 일단 같이
"""


def find_user_by_id(db: Session, user_id: int) -> models.UserEntity:
    try:
        user = db.query(models.UserEntity).filter(models.UserEntity.id == user_id).one()
        return user
    except NoResultFound:
        raise UserNotFoundException()


def find_user_by_email(db: Session, user_email: str) -> models.UserEntity:
    try:
        user = db.query(models.UserEntity).filter(models.UserEntity.user_email == user_email).one()
        return user
    except NoResultFound:
        raise UserNotFoundException()


def find_users(db: Session, offset: int = 0, limit: int = 100) -> List[models.UserEntity]:
    users = db.query(models.UserEntity).offset(offset).limit(limit).all()
    return users


def create_user(db: Session, user: user_schema.UserCreate):
    user.hash_password()

    new_user = models.UserEntity(
        user_email = user.user_email,
        user_hashed_password = user.user_hashed_password
    )
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user
