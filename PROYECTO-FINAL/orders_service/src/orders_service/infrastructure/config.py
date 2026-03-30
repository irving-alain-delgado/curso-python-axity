from pydantic_settings import BaseSettings, SettingsConfigDict
from pydantic import Field


class Settings(BaseSettings):
    model_config = SettingsConfigDict(
        env_file=".env",
        env_file_encoding="utf-8"
    )

    app_name: str = "Orders Service"
    debug: bool = False
    database_url: str = Field(..., alias="DATABASE_URL")


settings = Settings()  # type: ignore[call-arg]