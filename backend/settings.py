from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    model_config = SettingsConfigDict(env_file=(".env",))

    app_name: str
    db_name: str
    db_user: str
    db_password: str
    db_host: str
    db_port: int


class TestSettings(Settings):
    app_name: str
