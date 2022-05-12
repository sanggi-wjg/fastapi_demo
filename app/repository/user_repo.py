from typing import List

from sqlalchemy.exc import NoResultFound
from sqlalchemy.orm import Session

from app.core.exceptions import UserNotFoundException, DuplicateUserEmailException
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


def find_user_by_credentials(db: Session, user_email: str, user_password: str):
    try:
        user = db.query(models.UserEntity).filter(
            models.UserEntity.user_email == user_email,
            models.UserEntity.user_hashed_password == user_password
        ).one()
        return user
    except NoResultFound:
        raise UserNotFoundException()


def find_users(db: Session, offset: int = 0, limit: int = 100) -> List[models.UserEntity]:
    users = db.query(models.UserEntity).offset(offset).limit(limit).all()
    return users


def create_user(db: Session, user: user_schema.UserCreate) -> models.UserEntity:
    try:
        _ = find_user_by_email(db, user.user_email)
        raise DuplicateUserEmailException(user.user_email)

    except UserNotFoundException:
        new_user = models.UserEntity(
            user_email = user.user_email,
            user_hashed_password = user.user_hashed_password
        )
        db.add(new_user)
        db.commit()
        db.refresh(new_user)
        return new_user


def change_password(db: Session, user_id: int, user: user_schema.UserPassword) -> models.UserEntity:
    find_user = find_user_by_id(db, user_id)
    find_user.user_hashed_password = user.user_hashed_password

    db.commit()
    db.refresh(find_user)
    return find_user


def delete_user_by_id(db: Session, user_id: int) -> bool:
    remove_user = find_user_by_id(db, user_id)
    db.delete(remove_user)
    db.commit()
    return True
