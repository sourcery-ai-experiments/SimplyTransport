from typing import Literal

from pydantic_settings import BaseSettings


class BaseEnvSettings(BaseSettings):
    """Base settings class for environment variables."""

    class Config:
        env_file = ".env"
        env_file_encoding = "utf-8"


class AppSettings(BaseEnvSettings):
    """Settings class for environment variables."""

    class Config:
        case_sensitive = True

    DEBUG: bool = False
    ENVIRONMENT: Literal["DEV", "PROD", "TEST", "CI_TEST"] = "DEV"
    if ENVIRONMENT != "PROD":
        NAME: str = f"SimplyTransport {ENVIRONMENT}"
    else:
        NAME: str = "SimplyTransport"

    if ENVIRONMENT == "DEV":
        LOG_LEVEL: str = "DEBUG"
    else:
        LOG_LEVEL: str = "INFO"

    VERSION: str = "0.1.0"
    SECRET_KEY: str = "secret"
    LITESTAR_APP: str = "SimplyTransport.app:create_app"

    # Database
    DB_URL: str = "postgresql+asyncpg://user:password@localhost:5432/st_database"
    DB_URL_SYNC: str = "postgresql+psycopg2://user:password@localhost:5432/st_database"
    DB_ECHO: bool = False

    POSTGRES_DB: str = "example"
    POSTGRES_USER: str = "example"
    POSTGRES_PASSWORD: str = "example"

    # Loki
    LOKI_URL: str = "http://localhost:3100/loki/api/v1/push"


app = AppSettings.model_validate({})
