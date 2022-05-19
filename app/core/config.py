import os.path
from functools import lru_cache
from os import environ, path

from pydantic import BaseSettings

base_path = path.dirname(path.dirname(path.dirname(path.abspath(__file__))))


def get_env_filepath() -> str:
    filepath = f"{base_path}/{environ.get('ENV_FILE', '.env.local')}"

    if not os.path.exists(filepath):
        raise Exception("Not exist file: .env")

    return filepath


class Settings(BaseSettings):
    base_dir: str = base_path

    app_name: str
    app_desc: str
    app_version: str
    app_admin_name: str
    app_admin_email: str

    debug: bool
    reload: bool
    host: str
    port: int = 8090

    cors_origins: list
    trust_host: list
    gzip_minimum_size: int

    database_engine: str
    database_user: str
    database_password: str
    database_host: str
    database_port: str
    database_name: str

    # secret key, to get a string like this run: openssl rand -hex 32
    secret_key: str
    algorithm: str
    access_token_expire_minutes: int

    class Config:
        env_file = get_env_filepath()


@lru_cache()
def get_config_settings():
    return Settings()
