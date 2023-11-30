import logging

from dotenv import load_dotenv
from pydantic_settings import BaseSettings


load_dotenv()


class Settings(BaseSettings):
    telegram_token: str
    debug: bool = False
    secret_word: str = 'Бруня'
    logging_level: int = logging.INFO
    logging_format: str = '%(asctime)s, %(name)s, %(levelname)s, %(message)s'
    logging_dir: str = './src/bot/data/logs'
    smtp_server: str
    port: int
    sender_email: str
    receiver_email: str
    password_email: str
    admin_api_host: str = 'localhost'
    admin_api_port: str = '8000'
    database_url: str
    max_contacts_to_show_in_sesarch: int = 5

    class Config:
        env_file = '.env'
        env_file_encoding = 'utf-8'
        extra = 'ignore'


settings = Settings()

api_root = f'http://{settings.admin_api_host}:{settings.admin_api_port}/'

# database_url = f'postgresql+asyncpg://'
