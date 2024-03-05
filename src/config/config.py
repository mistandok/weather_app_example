from pydantic_settings import BaseSettings, SettingsConfigDict


class PGSettings(BaseSettings):
    model_config = SettingsConfigDict(extra="ignore")
    pg_host: str
    pg_port: str
    postgres_user: str
    postgres_password: str
    postgres_db: str


class OpenWeatherSettings(BaseSettings):
    model_config = SettingsConfigDict(extra="ignore")
    api_key: str
