from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.api import RouterTags
from app.core.dependency.query_depend import page_parameter, PageQueryParameter
from app.db.database import get_db
from app.repository import user_repo
from app.schema import user_schema

router = APIRouter(
    tags = [RouterTags.User],
    responses = { 404: { "detail": "not found" } }
)


@router.get("/users/{user_id}", response_model = user_schema.User, summary = "Find user by user id")
async def get_user(user_id: int, db: Session = Depends(get_db)):
    """
    Get id, is_active, items, email
    - **id** : user id
    - **email** : user email
    - **is_active** : user is active?
    - **items** : items
    """
    find_user = user_repo.find_user_by_id(db, user_id)
    return find_user


# [GET] find user by user email
@router.get("/users/{user_email}", response_model = user_schema.User)
async def get_user(user_email: str, db: Session = Depends(get_db)):
    find_user = user_repo.find_user_by_email(db, user_email)
    return find_user


# [GET] find all user by paginated
@router.get('/users/', response_model = list[user_schema.User])
async def get_users(page_param: PageQueryParameter = Depends(page_parameter), db: Session = Depends(get_db)):
    find_users = user_repo.find_users(db, page_param.offset, page_param.limit)
    return find_users


# [POST] create new user
@router.post('/users', response_model = user_schema.User, status_code = 201)
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
