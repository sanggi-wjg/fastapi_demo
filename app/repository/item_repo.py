from typing import List

from sqlalchemy.orm import Session

from app.db import models
from app.repository import user_repo
from app.schema import item_schema


def create_user_item(db: Session, item: item_schema.ItemCreate, user_id: int) -> models.ItemEntity:
    _ = user_repo.find_user_by_id(db, user_id)

    new_item = models.ItemEntity(
        item_name = item.item_name,
        item_description = item.item_description,
        owner_id = user_id,
    )

    db.add(new_item)
    db.commit()
    db.refresh(new_item)
    return new_item


def find_items(db: Session, offset: int = 0, limit: int = 100) -> List[models.ItemEntity]:
    items = db.query(models.ItemEntity).offset(offset).limit(limit).all()
    return items
