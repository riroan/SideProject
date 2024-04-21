from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    model_config = SettingsConfigDict(env_file=(".env",))

    app_name: str
    db_name: str
    db_user: str
    db_password: str
    db_host: str
    db_port: int

    jwt_secret: str
    jwt_algorithm: str


class TestSettings(Settings):
    app_name: str
