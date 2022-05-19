from passlib.context import CryptContext
from pydantic import BaseModel

from app.core.auth.auth_util import hash_password
from app.schema.item_schema import Item


class UserBase(BaseModel):
    user_email: str


class UserPassword(BaseModel):
    password: str

    @property
    def user_hashed_password(self):
        return hash_password(self.password)


class UserCreate(UserBase, UserPassword):
    pass


class User(UserBase):
    id: int
    is_active: bool
    items: list[Item] = []

    class Config:
        orm_mode = True
