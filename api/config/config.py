import os
from os.path import join, dirname
from dotenv import load_dotenv
from datetime import timedelta

dotenv_path = join(dirname(__file__), '.env')
load_dotenv(dotenv_path)
BASE_DIR = os.path.dirname(os.path.realpath(__file__))

class Config:
    SECRET_KEY=os.getenv('SECRET_KEY')
    SQLALCHEMY_TRACK_MODIFICATIONS=False
    JWT_ACCESS_TOKEN_EXPIRES=timedelta(minutes=30)
    JWT_REFRESH_TOKEN_EXPIRES=timedelta(minutes=30)
    JWT_SECRET_KEY=os.getenv('JWT_SECRET_KEY')

class DevConfig(Config):
    DEBUG=True
    SQLALCHEMY_ECHO=True
    SQLALCHEMY_DATABASE_URI=os.getenv('DB_URL')

config_dict ={
    'dev': DevConfig
}