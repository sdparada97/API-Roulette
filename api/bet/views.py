from flask_restx import Namespace, Resource

bet_namespace = Namespace('Bets', description="a namespace for Bets")

@bet_namespace.route('/bet')
class BetCreate(Resource):
    def post(self):
        pass