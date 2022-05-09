from pydantic import BaseModel

from app.schema.item_schema import Item


class UserBase(BaseModel):
    user_email: str


class UserCreate(UserBase):
    user_hashed_password: str


class User(UserBase):
    id: int
    is_active: bool
    items: list[Item] = []

    class Config:
        orm_mode = True
