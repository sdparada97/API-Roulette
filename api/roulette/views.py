from flask_restx import Namespace, Resource

roulette_namespace = Namespace('Roulettes', description="a namespace for Roulettes")

@roulette_namespace.route('/Roulette')
class RouletteCreate(Resource):
    def post(self):
        pass

@roulette_namespace.route('/Roulette/open/<int:roulette_id>')
class RouletteOpen(Resource):
    def patch(self,roulette_id):
        pass

@roulette_namespace.route('/Roulette/close/<int:roulette_id>')
class RouletteClose(Resource):
    def patch(self,roulette_id):
        pass