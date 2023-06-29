from flask_restx import Namespace, Resource, fields
from flask_jwt_extended import jwt_required

from ..models.roulettes import Roulette

from http import HTTPStatus

roulette_namespace = Namespace('Roulettes', description="a namespace for Roulettes")

roulette_model = roulette_namespace.model(
        'Roulette',{
            'id':fields.Integer()
    }
)

@roulette_namespace.route('/Roulette')
class RouletteCreate(Resource):
    @roulette_namespace.marshal_with(roulette_model)
    @jwt_required()
    def post(self):
        """
            Create a roulette
        """
        new_roulette = Roulette()
        new_roulette.save()
        return {'id':new_roulette.id},HTTPStatus.CREATED

@roulette_namespace.route('/Roulette/open/<int:roulette_id>')
class RouletteOpen(Resource):
    def patch(self,roulette_id):
        pass

@roulette_namespace.route('/Roulette/close/<int:roulette_id>')
class RouletteClose(Resource):
    def patch(self,roulette_id):
        pass