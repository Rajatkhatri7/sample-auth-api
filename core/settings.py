from pydantic_settings import BaseSettings
import os
from dotenv import load_dotenv



load_dotenv(".env")

class DBSettings(BaseSettings):
    POSTGRES_HOST : str = os.getenv('POSTGRES_HOST')
    POSTGRES_PORT : str = os.getenv('POSTGRES_PORT')
    POSTGRES_NAME : str = os.getenv('POSTGRES_NAME')
    POSTGRES_USER : str = os.getenv('POSTGRES_USER')
    POSTGRES_PASSWORD :str = os.getenv('POSTGRES_PASS')


class Settings(BaseSettings):

    db: DBSettings = DBSettings()



settings = Settings()