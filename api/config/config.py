import os
from dotenv import load_dotenv

load_dotenv(dotenv_path='api\config\.env')

class Config:
    SECRET_KEY=os.getenv('SECRET_KEY')

class DevConfig(Config):
    DEBUG=True

config_dict ={
    'dev': DevConfig
}