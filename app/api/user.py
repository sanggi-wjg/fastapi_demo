from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.core.exceptions import UserNotFoundException
from app.db.database import get_db
from app.repository import user_repo
from app.schema import user_schema

router = APIRouter(
    tags = ["users"],
    responses = { 404: { "detail": "not found" } }
)


@router.get("/users/{user_id}")
async def get_user(user_id: int):  # data 형 지정으로 pydantic 에서 검증하여 관리
    users = [{ 'user_name': 'John', 'age': 10 }, { 'user_name': 'Snow', 'age': 20 }]
    if user_id >= 2:
        raise UserNotFoundException()
    return users[user_id]


@router.get('/users/', response_model = list[user_schema.User])
async def get_users(offset: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    find_users = user_repo.find_users(db, offset, limit)
    return find_users
