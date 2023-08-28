from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    sentry_dsn: str

    model_config = SettingsConfigDict(env_file=".env")
