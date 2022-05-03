from pydantic import BaseSettings


class Settings(BaseSettings):
    app_name: str
    admin_email: str
    items_per_user: int

    class Config:
        env_file = '../.env'


def get_settings():
    return Settings()
