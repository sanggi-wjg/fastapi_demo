from enum import Enum
from typing import Optional

from fastapi import APIRouter
from fastapi.params import Query, Depends
from pydantic import BaseModel
from sqlalchemy.orm import Session

from app.db.database import get_db
from app.repository import item_repo
from app.schema import item_schema

router = APIRouter(
    tags = ["items"],
    responses = { 404: { "detail": "not found" } }
)


####################################
# Tag, Model 예제
####################################
# class TagName(str, Enum):
#     CREATE_ITEM = "CreateItem"
#
#
# class Item(BaseModel):
#     name: str
#     description: Optional[str] = None
#     price: float
#     tax: Optional[float] = None
#
#
# @router.get("/items")
# async def get_items(q: Optional[str] = Query(None, max_length = 50, title = "query")):
#     item = Item(name = "Guitar", price = 123.45)
#     item2 = Item(name = "Computer", price = 12345.67)
#     results = { "items": [item.dict(), item2.dict()], "request": q }
#     return results
#
#
# @router.post("/items", status_code = 201, tags = [TagName.CREATE_ITEM])
# async def create_item(item: Item):
#     new_item = item.dict()
#     if item.tax:
#         new_item.setdefault("total_price", item.price + item.tax)
#     return new_item


# [GET] find user items
@router.get("/items", response_model = list[item_schema.Item])
async def get_items(offset: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    find_items = item_repo.find_items(db, offset, limit)
    return find_items


# [POST] create new item by user
@router.post('/users/{user_id}/items', response_model = item_schema.Item)
async def create_user_item(user_id: int, item: item_schema.ItemCreate, db: Session = Depends(get_db)):
    new_item = item_repo.create_user_item(db, item, user_id)
    return new_item
