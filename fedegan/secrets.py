from pydantic_settings import BaseSettings
from pydantic import Field

class Secrets(BaseSettings):
    DEBUG: bool = Field(default=False)
    SECRET_KEY: str = Field(default="secret_key")

    DATABASE_USER: str = Field(default="postgres")
    DATABASE_PASSWORD: str = Field(default="postgres")
    DATABASE_HOST: str = Field(default="db")
    DATABASE_PORT: str = Field(default="5432")
    DATABASE_NAME: str = Field(default="fedegan-app")

    class Config:
        env_file = ".env"
        env_file_encoding = "utf-8"
