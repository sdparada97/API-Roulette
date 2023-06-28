from flask_restx import Namespace, Resource

bet_namespace = Namespace('Bets', description="a namespace for Bets")

@bet_namespace.route('/')
class HelloBet(Resource):
    def get(self):
        return { "message": "Hello bet" }