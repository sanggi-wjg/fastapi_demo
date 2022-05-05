from fastapi import APIRouter

router = APIRouter(
    tags = ["files"],
    responses = { 404: { "detail": "not found" } }
)


####################################
# file serve request
# /home/foo/var.txt -> /files//home/foo/var.txt
####################################
@router.get("/files/{filepath:path}")
async def serve_file(filepath: str):
    return { filepath: filepath }
