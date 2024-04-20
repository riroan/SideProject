from pydantic_settings import SettingsConfigDict, BaseSettings


class Settings(BaseSettings):
    model_config = SettingsConfigDict(env_file=(".env", ))

    app_name: str


class TestSettings(Settings):
    app_name: str
