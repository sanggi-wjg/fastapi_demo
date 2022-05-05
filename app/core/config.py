from functools import lru_cache
from os import environ

from pydantic import BaseSettings


class Config(BaseSettings):
    title = "Fast API Demo"

    app_name: str
    admin_email: str
    items_per_user: int

    database_engine: str
    database_user: str
    database_password: str
    database_host: str
    database_port: str
    database_name: str

    class Config:
        env_file = '../../.env'


class LocalConfig(Config):
    reload: bool = True


class ProductionConfig(Config):
    reload: bool = False


@lru_cache()
def get_config():
    env = environ.get("API_ENV", "local")
    return dict(
        production = ProductionConfig(),
        local = LocalConfig,
    ).get(env)
