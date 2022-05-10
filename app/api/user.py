from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.db.database import get_db
from app.repository import user_repo
from app.schema import user_schema

router = APIRouter(
    tags = ["users"],
    responses = { 404: { "detail": "not found" } }
)


# [GET] find user by user id
@router.get("/users/{user_id}", response_model = user_schema.User)
async def get_user(user_id: int, db: Session = Depends(get_db)):
    find_user = user_repo.find_user_by_id(db, user_id)
    return find_user


# [GET] find user by user email
@router.get("/users/{user_email}", response_model = user_schema.User)
async def get_user(user_email: str, db: Session = Depends(get_db)):
    find_user = user_repo.find_user_by_email(db, user_email)
    return find_user


# [GET] find all user by paginated
@router.get('/users/', response_model = list[user_schema.User])
async def get_users(offset: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    find_users = user_repo.find_users(db, offset, limit)
    return find_users


# [POST] create new user
@router.post('/users', response_model = user_schema.User)
async def create_new_user(user: user_schema.UserCreate, db: Session = Depends(get_db)):
    new_user = user_repo.create_user(db, user)
    return new_user


# [PATCH] update user password
@router.patch("/users/{user_id}", response_model = user_schema.User)
async def change_password(user_id: int, user: user_schema.UserPassword, db: Session = Depends(get_db)):
    update_user = user_repo.change_password(db, user_id, user)
    return update_user


# [DELETE] remove user
@router.delete("/users/{user_id}")
async def remove_user(user_id: int, db: Session = Depends(get_db)):
    user_repo.delete_user_by_id(db, user_id)
    return { "detail": "remove success" }
