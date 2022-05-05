from enum import Enum
from typing import Optional

from fastapi import APIRouter
from fastapi.params import Query
from pydantic import BaseModel

router = APIRouter(
    tags = ["items"],
    responses = { 404: { "detail": "not found" } }
)


####################################
# Tag, Model 예제
####################################
class TagName(str, Enum):
    CREATE_ITEM = "CreateItem"


class Item(BaseModel):
    name: str
    description: Optional[str] = None
    price: float
    tax: Optional[float] = None


@router.get("/items")
async def get_items(q: Optional[str] = Query(None, max_length = 50, title = "query")):
    item = Item(name = "Guitar", price = 123.45)
    item2 = Item(name = "Computer", price = 12345.67)
    results = { "items": [item.dict(), item2.dict()], "request": q }
    return results


@router.post("/items", status_code = 201, tags = [TagName.CREATE_ITEM])
async def create_item(item: Item):
    new_item = item.dict()
    if item.tax:
        new_item.setdefault("total_price", item.price + item.tax)
    return new_item
