from fastapi import APIRouter

router = APIRouter(
    tags = ["home"],
)


@router.get("/")
async def index():
    return { "message": "Hello World" }
