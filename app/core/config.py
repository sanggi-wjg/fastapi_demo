import os.path
from functools import lru_cache
from os import environ, path

from pydantic import BaseSettings

base_path = path.dirname(path.dirname(path.dirname(path.abspath(__file__))))


def get_env_filepath() -> str:
    filepath = f"{base_path}/{environ.get('ENV_FILE', '.env.local')}"

    if not os.path.exists(filepath):
        raise Exception("not exist file : .env")

    return filepath


class Settings(BaseSettings):
    base_dir: str = base_path

    debug: bool
    reload: bool
    host: str
    port: int = 8090

    app_name: str
    app_desc: str
    admin_email: str
    items_per_user: int

    database_engine: str
    database_user: str
    database_password: str
    database_host: str
    database_port: str
    database_name: str

    class Config:
        env_file = get_env_filepath()


@lru_cache()
def get_config_settings():
    return Settings()
