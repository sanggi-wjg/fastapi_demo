from typing import List

from sqlalchemy.orm import Session

from app.db import models


def find_user(db: Session, user_id: int) -> models.UserEntity:
    return db.query(models.UserEntity).filter(models.UserEntity.id == user_id)


def find_users(db: Session, offset: int = 0, limit: int = 100) -> List[models.UserEntity]:
    return db.query(models.UserEntity).offset(offset).limit(limit).all()
