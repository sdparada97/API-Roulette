from flask import Flask
from flask_restx import Api

from api.config.config import config_dict

from .auth.views import auth_namespace
from .bet.views import bet_namespace
from .roulette.views import roulette_namespace



def create_app(config=config_dict['dev']):
    app=Flask(__name__)
    app.config.from_object(config)
    
    api=Api(app)
    
    api.add_namespace(auth_namespace,path='/auth')
    api.add_namespace(bet_namespace,path='/bet')
    api.add_namespace(roulette_namespace,path='/roulette')
    
    
    return app