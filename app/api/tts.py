from fastapi import APIRouter, Depends
from redis.client import Redis
from sqlalchemy.orm import Session
from fastapi.responses import FileResponse

from app.api import RouterTags
from app.core.cache import get_redis
from app.core.lib.tts_util import create_tts_file, get_tts_save_path
from app.db.database import get_db
from app.repository import tts_record_repo

router = APIRouter(
    tags = [RouterTags.TTS],
    responses = { 404: { "detail": "not found" } }
)


# [GET]
@router.get("/tts/{text}", response_class = FileResponse)
async def get_tts_mp3(text: str, db: Session = Depends(get_db)):
    """
    FileResponse 사용으로
    path - The filepath to the file to stream.
    headers - Any custom headers to include, as a dictionary.
    media_type - A string giving the media type. If unset, the filename or path will be used to infer a media type.
    filename - If set, this will be included in the response Content-Disposition

    Header
    content-type: audio/mpeg
    etag: 8605e7cb703e23450b8d6baea38b95c3
    """
    if not tts_record_repo.is_exist_tts_record(db, text):
        tts_record_repo.create_tts_record(db, text)
        create_tts_file(text)

    return get_tts_save_path(text)


@router.get("/tts-redis/{text}", response_class = FileResponse)
async def get_tts_mp3_with_redis(text: str, redis: Redis = Depends(get_redis)):
    add_result = redis.sadd("tts", text)
    if add_result == 1:  # 0: set에 있음  /  1: set에 없음
        create_tts_file(text)
    return get_tts_save_path(text)
