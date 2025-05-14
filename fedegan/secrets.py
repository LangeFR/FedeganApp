from pydantic_settings import BaseSettings


class Secrets(BaseSettings):
    DEBUG: bool = False

    SECRET_KEY: str = "secret_key"

    DATABASE_USER: str = "postgres"
    DATABASE_PASSWORD: str = "postgres"
    DATABASE_HOST: str = "db"
    DATABASE_PORT: str = "5432"
    DATABASE_NAME: str = "fedegan-app"
