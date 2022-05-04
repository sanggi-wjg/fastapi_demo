from pydantic import BaseSettings


class Settings(BaseSettings):
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
        env_file = '../.env'
