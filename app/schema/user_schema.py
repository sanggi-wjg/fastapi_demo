from pydantic import BaseModel

from app.schema.item_schema import Item


class UserBase(BaseModel):
    user_email: str


class UserPassword(BaseModel):
    password: str

    @property
    def user_hashed_password(self):
        return f"ha{self.password}sh"


class UserCreate(UserBase):
    password: str

    @property
    def user_hashed_password(self):
        return f"ha{self.password}sh"


class User(UserBase):
    id: int
    is_active: bool
    items: list[Item] = []

    class Config:
        orm_mode = True
