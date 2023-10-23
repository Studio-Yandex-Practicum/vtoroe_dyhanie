from dotenv import load_dotenv
from pydantic_settings import BaseSettings


load_dotenv()


class Settings(BaseSettings):
    telegram_token: str
    debug: bool = False
    secret_word: str = 'Бруня'
    smtp_server: str = 'smtp.yandex.ru'
    port: int = 465
    sender_email: str
    receiver_email: str
    password_email: str

    class Config:
        env_file = '.env'
        env_file_encoding = 'utf-8'


settings = Settings()
