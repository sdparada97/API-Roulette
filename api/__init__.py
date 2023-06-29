from flask import Flask
from flask_restx import Api
from flask_migrate import Migrate
from flask_jwt_extended import JWTManager

from api.config.config import config_dict

from api.database import db
from .models.users import User
from .models.bets import Bet
from .models.roulettes import Roulette

from .auth.views import auth_namespace
from .bet.views import bet_namespace
from .roulette.views import roulette_namespace


def create_app(config=config_dict["dev"]):
    app = Flask(__name__)
    app.config.from_object(config)

    db.init_app(app)
    migrate = Migrate(app, db)
    migrate.init_app(app, db)

    jwt=JWTManager(app)

    api = Api(
        app=app,
        title="Roulette-API",
        version="1.0",
        description="API about bets in Roulettes",
    )

    api.add_namespace(auth_namespace, path="/auth")
    api.add_namespace(bet_namespace, path="/bets")
    api.add_namespace(roulette_namespace, path="/roulettes")

    @app.shell_context_processor
    def make_shell_context():
        return {
            "db": db,
            "User": User,
            "Bet": Bet,
            "Roulette": Roulette,
        }

    return app
