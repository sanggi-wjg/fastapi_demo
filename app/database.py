from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base, sessionmaker

from app.main import get_config_settings

settings = get_config_settings()


def create_database_engine():
    match settings.database_engine:
        case "mysql":
            database_dsn = f"mysql+pymysql://{settings.database_user}:{settings.database_password}@{settings.database_host}:{settings.database_port}/{settings.database_name}"
            return create_engine(database_dsn, isolation_level = 'REPEATABLE READ', echo = False)
        case "sqlite":
            database_dsn = "sqlite:///:memory:"
            return create_engine(database_dsn)
        case _:
            raise Exception(f"check database dsn:{settings.database_engine}")


Engine = create_database_engine()
SessionLocal = sessionmaker(autocommit = False, autoflush = False, bind = Engine)
Base = declarative_base()
