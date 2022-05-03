from fastapi import APIRouter

router = APIRouter(
    tags = ["users"],
    responses = { 404: { "detail": "not found" } }
)


@router.get("/users/{user_id}")
async def get_user(user_id: int):  # data 형 지정으로 pydantic 에서 검증하여 관리
    users = [{ 'user_name': 'John', 'age': 10 }, { 'user_name': 'Snow', 'age': 20 }]
    if user_id >= 2:
        from app.main import UserNotFoundException
        raise UserNotFoundException()
    return users[user_id]
