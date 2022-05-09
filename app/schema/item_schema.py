from pydantic import BaseModel


class ItemBase(BaseModel):
    item_name: str
    item_description: str | None = None


class ItemCreate(ItemBase):
    pass


class Item(ItemBase):
    id: int
    owner_id: int

    class Config:
        orm_mode = True
