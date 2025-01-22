import os
import pathlib
from functools import lru_cache

from dotenv import load_dotenv
from openai import AsyncClient

load_dotenv()

class BaseConfig:
    BASE_DIR: pathlib.Path = pathlib.Path(__file__).parent.parent.parent
    SECRET_KEY = os.getenv('SECRET')
    OPENAI_CLIENT = AsyncClient(api_key=os.getenv('OPENAI_API_KEY'))
    ASSISTANT_ID = os.getenv('ASSISTANT_ID')

class DevelopmentConfig(BaseConfig):
    Issuer = "http://localhost:8000"
    Audience = "http://localhost:3000"


class ProductionConfig(BaseConfig):
    Issuer = ""
    Audience = ""


@lru_cache()
def get_settings() -> DevelopmentConfig | ProductionConfig:
    config_cls_dict = {
        'development': DevelopmentConfig,
        'production': ProductionConfig,
    }
    config_name = os.getenv('FASTAPI_CONFIG', default='development')
    config_cls = config_cls_dict[config_name]
    return config_cls()


settings = get_settings()
