from fastapi import APIRouter

from app.api import RouterTags

router = APIRouter(
    tags = [RouterTags.File],
    responses = { 404: { "detail": "not found" } }
)


####################################
# file serve request
# /home/foo/var.txt -> /files//home/foo/var.txt
####################################
@router.get("/files/{filepath:path}")
async def serve_file(filepath: str):
    return { filepath: filepath }
