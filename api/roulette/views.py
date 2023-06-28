from flask_restx import Namespace, Resource

roulette_namespace = Namespace('Roulettes', description="a namespace for Roulettes")

@roulette_namespace.route('/')
class HelloRoulette(Resource):
    def get(self):
        return { "message": "Hello roulette" }