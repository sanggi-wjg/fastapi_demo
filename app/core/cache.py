import redis

from app.core.config import get_config_settings


def get_redis():
    settings = get_config_settings()
    redis_instance = redis.Redis(
        host = settings.redis_host,
        port = settings.redis_port,
        charset = "utf-8",
        decode_responses = True
    )
    try:
        yield redis_instance
    finally:
        redis_instance.close()
