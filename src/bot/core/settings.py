from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    telegram_token: str
    debug: bool = False
    secret_word: str = 'Бруня'

    class Config:
        env_file = '.env'
        env_file_encoding = 'utf-8'


settings = Settings()
