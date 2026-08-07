import os

from dotenv import find_dotenv, load_dotenv
from pydantic_settings import BaseSettings, SettingsConfigDict

env_path = find_dotenv()
load_dotenv(env_path)

DATABASE_URL = (
    f"mysql+pymysql://"
    f"{os.getenv('MYSQL_USER')}:"
    f"{os.getenv('MYSQL_PASSWORD')}@"
    f"{os.getenv('MYSQL_HOST')}:"
    f"{os.getenv('MYSQL_PORT')}/"
    f"{os.getenv('MYSQL_DATABASE')}"
)


class Settings(BaseSettings):
    OPENAI_API_KEY: str
    openai_model: str = "gpt-5-mini"
    environment: str = "development"

    # MySQL settings
    mysql_host: str = "localhost"
    mysql_port: int = 3306
    mysql_user: str
    mysql_password: str
    mysql_database: str

    model_config = SettingsConfigDict(env_file=env_path)


settings = Settings()
