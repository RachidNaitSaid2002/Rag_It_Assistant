from pydantic_settings import BaseSettings
from dotenv import load_dotenv
load_dotenv()


class Settings(BaseSettings):
    ALG: str = "HS256"
    HF_TOKEN: str

    DB_HOST: str 
    DB_PORT: int 
    DB_NAME: str 
    DB_USER: str 
    DB_PASSWORD: str 

    ACCESS_TOKEN_EXPIRE_MINUTES: int
    SK: str
    ALG: str
    
    DATABASE_URL : str

    model_config = {
        "extra": "ignore",
        "env_file": "./.env",
        "case_sensitive": True
    }

settings = Settings()