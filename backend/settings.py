from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    model_config = SettingsConfigDict(env_file=(".env",))

    app_name: str


class TestSettings(Settings):
    app_name: str
