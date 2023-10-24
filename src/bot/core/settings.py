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
    smtp_server: str = 'smtp.yandex.ru'
    port: int = 465
    sender_email: str
    receiver_email: str
    password_email: str

    class Config:
        env_file = '.env'
        env_file_encoding = 'utf-8'


settings = Settings()
